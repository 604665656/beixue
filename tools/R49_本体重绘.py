# -*- coding: utf-8 -*-
"""R49 素材：AI 图生图服务本轮未产出 -> 走「程序化本体表情重绘」。
   直接在已过检原图的整张像素上改（不是透明贴片叠加、不是切片拼接），
   只改角色 alpha 区域内的像素，纯品红底保持不变，故仍可走原抠图管线。
   金和尚两张按用户建议做「戒疤 + 剃净光头 / 一体僧帽」本体改造。"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, scipy.ndimage as ndi, json, base64, io, os

D = '/data/workspace/anim44'
os.makedirs(D, exist_ok=True)
FONT = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
f18 = ImageFont.truetype(FONT, 18)
f14 = ImageFont.truetype(FONT, 14)

# 源图 -> 目标键 / 标签 / 表情重绘类型
JOBS = [
    ('anim43/R48_jinhe_jing.png', 'R49_jinhe_scar', '金和尚·静息 戒疤+剃净光头', 'bald_scar'),
    ('anim43/R48_jinhe_jing.png', 'R49_jinhe_hat', '金和尚·喜 一体僧帽', 'hat_scar'),
    ('anim43/R48_gbx_nu.png',    'R49_tie_jing',  '铁萼英·静息', 'calm'),
    ('anim40/R45_tian_xi.png',   'R49_tian_jue',  '田笑·决', 'resolve'),
    ('anim40/R45_tian_jing.png', 'R49_tian_zui',  '田笑·醉', 'drunk'),
    ('anim40/R45_ying_xi.png',   'R49_ying_nu',   '小英子·怒', 'angry'),
    ('anim42/R47_jin_ai.png',    'R49_jin_jue',   '荆三娘·决', 'resolve'),
    ('anim42/R47_jin_yi.png',    'R49_jin_zui',   '荆三娘·醉', 'drunk'),
    ('anim39/R44_qin_jing.png',  'R49_qinwen_yi', '秦稳·疑', 'doubt'),
    ('anim40/R45_tian_xi.png',   'R49_tian_nu',   '田笑·怒', 'angry'),
]


def fg_mask(a):
    """角色前景 = 非纯品红背景（与历史抠图管线同口径）"""
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    cand = (R > 90) & (R > G * 1.65) & (R > B * 1.22) & (B > G * 1.10) & (G < 135)
    lab, n = ndi.label(cand)
    edge = set(lab[0, :].tolist()) | set(lab[-1, :].tolist()) | set(lab[:, 0].tolist()) | set(lab[:, -1].tolist())
    edge.discard(0)
    return ~np.isin(lab, list(edge))


def soft_blend(arr, mask, shape, color, alpha=0.85, feather=14):
    """在 mask∩shape 内把像素向 color 混合，边缘羽化；shape 是 bool 图"""
    m = Image.fromarray((shape * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(feather))
    w = np.asarray(m).astype(float) / 255.0
    w *= mask.astype(float) * alpha
    for c in range(3):
        arr[:, :, c] = (arr[:, :, c] * (1 - w) + color[c] * w).round().clip(0, 255)


def draw_in(dr, fn, mask):
    """只在前景内落笔：先画到临时层，再用 mask 裁"""
    tmp = Image.new('RGBA', (1536, 1536), (0, 0, 0, 0))
    fn(ImageDraw.Draw(tmp))
    t = np.asarray(tmp).astype(float)
    al = t[:, :, 3] / 255.0 * mask.astype(float)
    return t[:, :, :3], al


def expr_layer(kind, mask):
    """表情本体重绘：眼睑 / 眉 / 嘴 / 脸颊，全部按 1536 画布比例定位"""
    tmp = Image.new('RGBA', (1536, 1536), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    INK = (72, 58, 50, 255)
    BLUSH = (196, 122, 112, 120)
    # 双眼中心（按基准构图）
    eyes = [(590, 585), (950, 585)]
    if kind == 'calm':
        for x, y in eyes:
            d.arc([x - 62, y - 34, x + 62, y + 34], 195, 345, fill=INK, width=9)
    elif kind in ('angry', 'resolve'):
        for x, y in eyes:
            d.line([x - 66, y - 74 - (10 if kind == 'angry' else 0),
                    x + 66, y - 56 + (14 if kind == 'angry' else 0)], fill=INK, width=13)
        d.arc([710, 690, 830, 760], 190, 350, fill=INK, width=9) if kind == 'angry' else \
            d.line([712, 736, 824, 736], fill=INK, width=10)
    elif kind == 'doubt':
        d.line([520, 505, 655, 525], fill=INK, width=12)
        d.line([890, 490, 1020, 480], fill=INK, width=12)
        d.arc([726, 700, 812, 758], 200, 340, fill=INK, width=8)
    elif kind == 'drunk':
        for x, y in eyes:
            d.arc([x - 60, y - 28, x + 60, y + 30], 200, 340, fill=INK, width=10)
        d.ellipse([500, 650, 585, 700], fill=BLUSH)
        d.ellipse([955, 650, 1040, 700], fill=BLUSH)
        d.arc([716, 700, 820, 762], 20, 160, fill=INK, width=9)
    if kind == 'angry':
        d.ellipse([500, 650, 580, 692], fill=BLUSH)
        d.ellipse([960, 650, 1040, 692], fill=BLUSH)
    t = np.asarray(tmp).astype(float)
    return t[:, :, :3], (t[:, :, 3] / 255.0) * mask.astype(float)


def blend_layer(arr, rgb, al):
    for c in range(3):
        arr[:, :, c] = (arr[:, :, c] * (1 - al) + rgb[:, :, c] * al).round().clip(0, 255)


def bald_scar(arr, mask):
    """头顶绒毛剃净：只改中间头顶，圆耳保留；羽化过渡，与脸颊绒毛连续"""
    yy, xx = np.mgrid[0:1536, 0:1536]
    dome = ((xx - 768) / 340) ** 2 + ((yy - 300) / 230) ** 2 < 1
    dome &= (yy < 430) & (yy > 120)
    soft_blend(arr, mask, dome, (238, 218, 208), alpha=0.92, feather=26)
    # 3 点深赭戒疤，本体小圆点，不是贴片
    tmp = Image.new('RGBA', (1536, 1536), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    for x, y in [(700, 268), (768, 246), (836, 268)]:
        d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=(122, 76, 58, 255))
        d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=(88, 54, 42, 255))
    t = np.asarray(tmp).astype(float)
    blend_layer(arr, t[:, :, :3], (t[:, :, 3] / 255.0) * mask.astype(float))


def hat_scar(arr, mask):
    """一体僧帽：沿头顶弧线填充深褐布帽，与头部轮廓连续，不描硬边、不做悬浮盖片"""
    yy, xx = np.mgrid[0:1536, 0:1536]
    dome = ((xx - 768) / 372) ** 2 + ((yy - 322) / 268) ** 2 < 1
    dome &= (yy < 430) & (yy > 105)
    soft_blend(arr, mask, dome, (86, 68, 62), alpha=0.95, feather=22)
    # 帽檐布褶（同一笔触的暗线，不是独立配件）
    yy2, xx2 = np.mgrid[0:1536, 0:1536]
    fold = dome & (np.abs(yy2 - (382 + 26 * np.sin((xx2 - 768) / 90.0))) < 9)
    soft_blend(arr, mask, fold, (58, 44, 40), alpha=0.75, feather=6)
    # 帽下露出的光头 + 3 点戒疤
    bald = ((xx - 768) / 250) ** 2 + ((yy - 452) / 72) ** 2 < 1
    bald &= (yy > 400) & (yy < 500)
    soft_blend(arr, mask, bald, (236, 214, 204), alpha=0.88, feather=12)
    tmp = Image.new('RGBA', (1536, 1536), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    for x, y in [(724, 452), (768, 440), (812, 452)]:
        d.ellipse([x - 10, y - 10, x + 10, y + 10], fill=(122, 76, 58, 255))
    t = np.asarray(tmp).astype(float)
    blend_layer(arr, t[:, :, :3], (t[:, :, 3] / 255.0) * mask.astype(float))


QC, EMB = {}, {}
for src, key, label, kind in JOBS:
    im = Image.open('/data/workspace/' + src).convert('RGB')
    if im.size != (1536, 1536):
        im = im.resize((1536, 1536), Image.LANCZOS)
    arr = np.asarray(im).astype(float)
    mask = fg_mask(np.asarray(im).astype(np.int16))
    if kind == 'bald_scar':
        bald_scar(arr, mask)
        expr_layer('calm', mask)  # 静息眼睑
        rgb, al = expr_layer('calm', mask)
        blend_layer(arr, rgb, al * 0.55)
    elif kind == 'hat_scar':
        hat_scar(arr, mask)
        rgb, al = expr_layer('drunk', mask)  # 喜色：弯眼 + 淡赭脸颊
        blend_layer(arr, rgb, al * 0.6)
    else:
        rgb, al = expr_layer(kind, mask)
        blend_layer(arr, rgb, al * 0.85)
    out = Image.fromarray(arr.round().clip(0, 255).astype(np.uint8))
    out.save(os.path.join(D, key + '.png'))
    out.resize((720, 720), Image.LANCZOS).save(os.path.join(D, key + '_720.jpg'), quality=84)

    # ---- 历史抠图管线 ----
    a = np.asarray(out).astype(np.int16)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    cand = (R > 90) & (R > G * 1.65) & (R > B * 1.22) & (B > G * 1.10) & (G < 135)
    lab, n = ndi.label(cand)
    edge = set(lab[0, :].tolist()) | set(lab[-1, :].tolist()) | set(lab[:, 0].tolist()) | set(lab[:, -1].tolist())
    edge.discard(0)
    fg = ~np.isin(lab, list(edge))
    fl, nf = ndi.label(fg)
    sz = np.bincount(fl.ravel()); sz[0] = 0
    main_id = int(sz.argmax()); keep = ndi.binary_fill_holes(fl == main_id)
    area = int(keep.sum())
    H, W = keep.shape
    for k in range(1, nf + 1):
        if k == main_id: continue
        c = int(sz[k])
        if c < area * 0.0025: continue
        ys, xs = np.where(fl == k)
        if xs.mean() > W * .80 and ys.mean() > H * .86: continue
        keep |= (fl == k)
    al = Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.5))
    rgba = out.convert('RGBA'); rgba.putalpha(al)
    bb = al.getbbox(); bb = (max(0, bb[0] - 6), max(0, bb[1] - 6), min(W, bb[2] + 6), min(H, bb[3] + 6))
    rgba = rgba.crop(bb); rgba.save(os.path.join(D, key + '_cut.png'))
    small = rgba.resize((512, int(512 * rgba.height / rgba.width)), Image.LANCZOS)
    buf = io.BytesIO(); small.save(buf, 'WEBP', quality=74, method=6)
    EMB[key] = 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()
    inv = ~keep; il, ic = ndi.label(inv)
    ie = set(il[0, :].tolist()) | set(il[-1, :].tolist()) | set(il[:, 0].tolist()) | set(il[:,-1].tolist())
    holes = sum(1 for k in range(1, ic + 1) if k not in ie and int((il == k).sum()) > 20)
    resid = float((cand & keep).sum()) / max(1, int(keep.sum()))
    QC[key] = {'label': label, 'src': src, 'kind': kind, 'holes': holes,
               'residual_pct': round(resid * 100, 4), 'cut': list(rgba.size)}
    print('%-20s %-28s holes=%d resid=%.4f%%' % (key, label, holes, resid * 100))

json.dump({'QC': QC}, open(os.path.join(D, '_QC.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(EMB, open(os.path.join(D, '_EMB.json'), 'w'))

# ---- 双底联系表 ----
S = Image.new('RGB', (5 * 240, 60 + 4 * 248), (250, 247, 240))
d = ImageDraw.Draw(S)
d.text((14, 12), 'R49  金和尚戒疤/一体僧帽 + 铁萼英 + 高频格（前两行宣纸底／后两行夜雨底）', font=f18, fill=(60, 46, 38))
for idx, (src, key, label, kind) in enumerate(JOBS):
    cut = Image.open(os.path.join(D, key + '_cut.png')).convert('RGBA').resize((200, 200), Image.LANCZOS)
    for row, kd in enumerate(['paper', 'night']):
        col = (240, 234, 220) if kd == 'paper' else (38, 44, 56)
        tile = Image.new('RGB', (240, 248), col); tile.paste(cut, (20, 10), cut)
        ImageDraw.Draw(tile).text((8, 214), label, font=f14,
                                  fill=(70, 58, 48) if kd == 'paper' else (232, 226, 214))
        S.paste(tile, ((idx % 5) * 240, 60 + (row * 2 + idx // 5) * 248))
S.save(os.path.join(D, '_R49_10张双底联系表.jpg'), quality=88)
print('contact', os.path.getsize(os.path.join(D, '_R49_10张双底联系表.jpg')))
