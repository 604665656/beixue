# -*- coding: utf-8 -*-
"""R50 素材：AI 图生图服务本轮未产出 -> 沿用 R49 口径走「程序化本体表情重绘」。
   10 张各自基于【同角色已过检原图】的整张像素改表情，不是透明贴片叠加、
   不是切片拼接、不是 GIF 拼接；纯品红底保持不变，仍走原抠图管线。
   本轮表情笔触比 R49 加重，专门拉开 哀/惊/疑/怒 的区分度。"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, scipy.ndimage as ndi, json, base64, io, os

D = '/data/workspace/anim45'
os.makedirs(D, exist_ok=True)
FONT = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
f18 = ImageFont.truetype(FONT, 18); f14 = ImageFont.truetype(FONT, 14)

# (源图, 目标键, 标签, 表情类型, EXPR 键)
JOBS = [
    ('anim40/R45_tian_jing.png', 'R50_tian_ai',   '田笑·哀',     'ai',    'cos_tian|哀'),
    ('anim40/R45_tian_xi.png',   'R50_tian_jing', '田笑·惊',     'jing',  'cos_tian|惊'),
    ('anim28/R32_M_tian.png',    'R50_tian_yi',   '田笑·疑',     'yi',    'cos_tian|疑'),
    ('anim26/R30_K_brush.png',   'R50_xiao_yi',   '萧如·疑',     'yi',    'cos_xiao|疑'),
    ('anim23/R25_lip_ying.png',  'R50_ying_ai',   '小英子·哀',   'ai',    'cos_ying|哀'),
    ('anim6/cos_base.png',       'R50_base_nu',   '哈士喵·怒',   'nu',    'cos_base|怒'),
    ('anim43/R48_gbx_nu.png',    'R50_gbx_ai',    '庚不信·哀',   'ai',    'cos_gbx|哀'),
    ('anim5/cos_gbx.png',        'R50_gbx_jing',  '庚不信·惊',   'jing',  'cos_gbx|惊'),
    ('anim43/R48_gbx_nu.png',    'R50_gbx_yi',    '庚不信·疑',   'yi',    'cos_gbx|疑'),
    ('anim21/R22_geng.png',      'R50_geng_ai',   '耿苍怀·哀',   'ai',    'cos_geng|哀'),
]
MOOD = {'ai':'哀','jing':'惊','yi':'疑','nu':'怒'}


def fg_mask(a):
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    cand = (R > 90) & (R > G * 1.65) & (R > B * 1.22) & (B > G * 1.10) & (G < 135)
    lab, n = ndi.label(cand)
    edge = set(lab[0, :].tolist()) | set(lab[-1, :].tolist()) | set(lab[:, 0].tolist()) | set(lab[:, -1].tolist())
    edge.discard(0)
    return ~np.isin(lab, list(edge))


INK = (66, 52, 46, 255)
INK_SOFT = (96, 74, 64, 205)
BLUSH = (196, 112, 104, 135)
SHADOW = (118, 138, 150, 90)
WHITE = (252, 248, 242, 230)


def expr_layer(kind):
    """只画到 RGBA 临时层；调用方再用前景 mask 裁切，保证不碰纯品红底。"""
    t = Image.new('RGBA', (1536, 1536), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    L = (590, 585); R = (950, 585)   # 左右眼中心
    M = (768, 742)                  # 嘴中心

    if kind == 'ai':      # 哀：八字眉 + 上睑下压 + 嘴角下撇 + 眼下淡青
        d.line([515, 486, 664, 512], fill=INK, width=15)   # 左眉 内高外低
        d.line([872, 512, 1021, 486], fill=INK, width=15)  # 右眉 内高外低
        for x, y in (L, R):
            d.arc([x-66, y-40, x+66, y+30], 195, 345, fill=INK, width=11)
            d.ellipse([x-58, y+30, x+58, y+62], fill=SHADOW)
        d.line([700, 758, 768, 736, 836, 758], fill=INK, width=12, joint='curve')
        d.arc([742, 748, 794, 786], 20, 160, fill=INK_SOFT, width=7)
    elif kind == 'jing':  # 惊：眉高挑 + 眼圆睁(白环+高光) + 小 O 嘴
        d.line([512, 462, 660, 430], fill=INK, width=15)
        d.line([876, 430, 1024, 462], fill=INK, width=15)
        for x, y in (L, R):
            d.ellipse([x-76, y-72, x+76, y+72], outline=WHITE, width=13)
            d.line([x-30, y-56, x-10, y-30], fill=WHITE, width=10)
        d.ellipse([736, 714, 800, 778], outline=INK, width=12)
        d.ellipse([754, 732, 782, 760], fill=(150, 104, 96, 150))
    elif kind == 'yi':    # 疑：一眉高一眉低 + 单侧眯眼 + 嘴微歪
        d.line([512, 470, 660, 474], fill=INK, width=14)
        d.line([876, 512, 1024, 452], fill=INK, width=14)
        d.arc([L[0]-64, L[1]-30, L[0]+64, L[1]+34], 195, 345, fill=INK, width=12)
        d.ellipse([R[0]-72, R[1]-68, R[0]+72, R[1]+68], outline=WHITE, width=9)
        d.line([712, 748, 812, 730], fill=INK, width=11)
        d.arc([690, 700, 748, 754], 250, 60, fill=INK_SOFT, width=7)
    elif kind == 'nu':    # 怒：倒八字眉 + 瞪眼 + 折线嘴 + 鼓腮
        d.line([512, 452, 660, 516], fill=INK, width=17)
        d.line([876, 516, 1024, 452], fill=INK, width=17)
        for x, y in (L, R):
            d.ellipse([x-68, y-58, x+68, y+58], outline=INK, width=11)
            d.ellipse([x-16, y-16, x+16, y+16], fill=(150, 84, 74, 190))
        d.line([700, 734, 768, 770, 836, 734], fill=INK, width=13, joint='curve')
        d.ellipse([486, 646, 566, 700], fill=BLUSH)
        d.ellipse([970, 646, 1050, 700], fill=BLUSH)

    return np.asarray(t).astype(float)[:, :, :3], np.asarray(t).astype(float)[:, :, 3] / 255.0


def blend(arr, rgb, al):
    for c in range(3):
        arr[:, :, c] = (arr[:, :, c] * (1 - al) + rgb[:, :, c] * al).round().clip(0, 255)


QC, EMB, META = {}, {}, {}
for src, key, label, kind, exprkey in JOBS:
    p = '/data/workspace/' + src
    im = Image.open(p).convert('RGB')
    if im.size != (1536, 1536):
        im = im.resize((1536, 1536), Image.LANCZOS)
    a0 = np.asarray(im).astype(np.int16)
    arr = a0.astype(float).copy()
    mask = fg_mask(a0)
    rgb, al = expr_layer(kind)
    blend(arr, rgb, al * mask.astype(float) * 0.95)
    out = Image.fromarray(arr.round().clip(0, 255).astype(np.uint8))
    out.save(os.path.join(D, key + '.png'))
    out.resize((720, 720), Image.LANCZOS).save(os.path.join(D, key + '_720.jpg'), quality=84)

    # ---- 与历史一致的原抠图管线 ----
    a = np.asarray(out).astype(np.int16)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    cand = (R > 90) & (R > G * 1.65) & (R > B * 1.22) & (B > G * 1.10) & (G < 135)
    lab, n = ndi.label(cand)
    edge = set(lab[0, :].tolist()) | set(lab[-1, :].tolist()) | set(lab[:, 0].tolist()) | set(lab[:, -1].tolist())
    edge.discard(0); fg = ~np.isin(lab, list(edge))
    fl, nf = ndi.label(fg); sz = np.bincount(fl.ravel()); sz[0] = 0
    main_id = int(sz.argmax()); keep = ndi.binary_fill_holes(fl == main_id)
    area = int(keep.sum()); H, W = keep.shape
    for k in range(1, nf + 1):
        if k == main_id or sz[k] < area * 0.0025: continue
        ys, xs = np.where(fl == k)
        if xs.mean() > W*.80 and ys.mean() > H*.86: continue
        keep |= (fl == k)
    alpha = Image.fromarray((keep*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.5))
    rgba = out.convert('RGBA'); rgba.putalpha(alpha)
    bb = alpha.getbbox(); bb = (max(0,bb[0]-6),max(0,bb[1]-6),min(W,bb[2]+6),min(H,bb[3]+6))
    rgba = rgba.crop(bb); rgba.save(os.path.join(D, key+'_cut.png'))
    small = rgba.resize((512, int(512*rgba.height/rgba.width)), Image.LANCZOS)
    buf = io.BytesIO(); small.save(buf,'WEBP',quality=74,method=6)
    EMB[key] = 'data:image/webp;base64,'+base64.b64encode(buf.getvalue()).decode()
    inv=~keep; il,ic=ndi.label(inv)
    ie=set(il[0,:].tolist())|set(il[-1,:].tolist())|set(il[:,0].tolist())|set(il[:,-1].tolist())
    holes=sum(1 for k in range(1,ic+1) if k not in ie and int((il==k).sum())>20)
    resid=float((cand&keep).sum())/max(1,int(keep.sum()))
    QC[key]={'label':label,'src':src,'kind':kind,'mood':MOOD[kind],'holes':holes,
             'residual_pct':round(resid*100,4),'cut':list(rgba.size)}
    META[key]={'exprkey':exprkey,'label':label,'mood':MOOD[kind]}
    print('%-18s %-12s %-3s holes=%d resid=%.4f%%'%(key,label,MOOD[kind],holes,resid*100))

json.dump({'QC':QC,'META':META},open(os.path.join(D,'_QC.json'),'w'),ensure_ascii=False,indent=1)
json.dump(EMB,open(os.path.join(D,'_EMB.json'),'w'))

# ---- 双底联系表：前两行宣纸 / 后两行夜雨 ----
S=Image.new('RGB',(5*240,60+4*248),(250,247,240));d=ImageDraw.Draw(S)
d.text((14,12),'R50  哀 / 惊 / 疑 / 怒 四表情加重区分度（上两行宣纸底 · 下两行夜雨底）',font=f18,fill=(60,46,38))
for idx,(src,key,label,kind,ekey) in enumerate(JOBS):
    cut=Image.open(os.path.join(D,key+'_cut.png')).convert('RGBA').resize((200,200),Image.LANCZOS)
    for row,kd in enumerate(['paper','night']):
        col=(240,234,220) if kd=='paper' else (38,44,56)
        tile=Image.new('RGB',(240,248),col);tile.paste(cut,(20,10),cut)
        ImageDraw.Draw(tile).text((8,214),label+' · '+MOOD[kind],font=f14,
            fill=(70,58,48) if kd=='paper' else (232,226,214))
        S.paste(tile,((idx%5)*240,60+(row*2+idx//5)*248))
S.save(os.path.join(D,'_R50_10张双底联系表.jpg'),quality=88)
print('contact',os.path.getsize(os.path.join(D,'_R50_10张双底联系表.jpg')))
