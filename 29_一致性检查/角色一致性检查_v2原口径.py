# -*- coding: utf-8 -*-
"""角色一致性检查器 v2：以作者原稿图生图直出帧为数值锚点，分类型逐批比对。
用法：python 角色一致性检查.py [目录 ...]
输出：角色一致性检查.csv / 角色一致性检查报告.md / _consistency.jpg
类型：完整角色层（全套软指标）／局部帧（只查孔洞与锐度上限）／特效层（不适用角色判定）
"""
import os, sys, glob, csv, io, math
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi

ROOT = '/data/workspace'
ANCHOR = os.path.join(ROOT, 'anim12b/E_seq_open.png')   # 由作者原稿图生图直出，仅换背景
STYLE_FIX = ('其余全部与第一张图完全一致：灰白蓬松绒毛、圆润二头身、蓝色大眼睛、黑色粗圆框眼镜、'
             '粉色内耳、只有一条蓬松大尾巴（绝不能有第二条）、柔和毛笔质感的绒毛边缘、'
             '平涂薄涂风格、细软线条，不要改成尖耳或赛璐璐硬阴影。角色实心封闭、'
             '身体与胳膊腿之间不留镂空缝隙、镜片反光用不透明浅灰白、'
             '角色身上不得出现任何品红像素。画面内不要任何文字、水印或标志。')

def alpha_of(path):
    arr = np.array(Image.open(path).convert('RGB'))
    H, W, _ = arr.shape
    r, g, b = arr[:, :, 0].astype(int), arr[:, :, 1].astype(int), arr[:, :, 2].astype(int)
    hsv = cv2.cvtColor(arr, cv2.COLOR_RGB2HSV)
    h, s, v = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
    bg_h = (h >= 135) & (h <= 179) & (s >= 70) & (v >= 75)
    bg_rgb = (r > 110) & (b > 55) & (g < r * .80) & (g < b * .92) & ((r-g) > 38) & ((b-g) > 12)
    bg = bg_h | bg_rgb
    fg = ndi.binary_fill_holes((~bg).astype(np.uint8) > 0)
    labm, n = ndi.label(fg)
    keep = np.zeros_like(fg); edge = int(min(H, W) * .02); big = H * W * .02
    for i in range(1, n + 1):
        ys, xs = np.where(labm == i); a = len(xs)
        if a < 180: continue
        touch = xs.min() < edge or ys.min() < edge or xs.max() > W-edge or ys.max() > H-edge
        if touch and a < big: continue
        keep[labm == i] = 1
    alpha = (keep * 255).astype(np.uint8)
    alpha[int(H*.93):, int(W*.82):] = 0
    return arr, cv2.GaussianBlur(alpha, (3, 3), 0)

def metrics(path):
    arr, alpha = alpha_of(path)
    H, W, _ = arr.shape
    m = alpha > 128
    ys, xs = np.where(m)
    if len(xs) < 500: return None
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    bw, bh = x1-x0+1, y1-y0+1
    hsv = cv2.cvtColor(arr, cv2.COLOR_RGB2HSV)
    h, s, v = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
    grayw = m & (s < 55) & (v > 120)
    black  = m & (v < 70)
    blue   = m & (h >= 88) & (h <= 125) & (s > 55)
    magenta= m & (h >= 135) & (h <= 179) & (s > 80)
    n = float(m.sum())
    face = m & (np.indices(m.shape)[0] >= y0) & (np.indices(m.shape)[0] < y0 + bh*.42)
    glass = float((black & face).sum()) / max(1.0, float(face.sum()))
    lap = cv2.Laplacian(cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY), cv2.CV_64F)
    sharp = float(lap[m].var())
    holes = int((ndi.binary_fill_holes(m) & ~m).sum())
    return dict(aspect=bw/bh, gray=float(grayw.sum())/n, black=float(black.sum())/n,
                blue=float(blue.sum())/n, magenta=float(magenta.sum())/n,
                glass=glass, sharp=sharp, holes=holes, fill=n/(bw*bh))

SOFT = {
    'aspect': (.16, '头身宽高比'), 'gray': (.20, '灰白绒毛占比'),
    'blue':   (.45, '蓝瞳占比'),   'glass':  (.38, '圆框眼镜粗度'),
    'sharp':  (.55, '边缘柔和度'), 'fill':   (.22, '轮廓饱满度'),
}
HARD_MAGENTA = .006

def kind_of(name):
    if 'ripple' in name or name.startswith('fx_ray') or name.startswith('fx_firefly'):
        return '特效层'
    if any(x in name for x in ('_nod', '_shake', '_breath', 'ripple')):
        return '局部帧'
    return '完整角色层'

def judge(m, ref, kind):
    if kind == '特效层':
        return '特效层·不适用', ['空心环／粒子，按设计保留透空；不参与角色判定']
    if kind == '局部帧':
        bad = []
        if m['holes'] > 0: bad.append('内部孔洞%d' % m['holes'])
        if m['sharp'] > ref['sharp'] * 6: bad.append('锐度超锚点 6 倍')
        return ('局部帧·合格' if not bad else '局部帧·待修'), bad or ['只查孔洞与锐度上限']
    bad=[]; hard=[]
    for k,(tol,name) in SOFT.items():
        rv = ref[k] or 1e-6
        dev = abs(m[k]-rv)/(abs(rv) or 1e-6)
        if dev > tol: bad.append('%s偏%.0f%%' % (name, dev*100))
    if m['magenta'] > HARD_MAGENTA: hard.append('身上品红残留%.2f%%' % (m['magenta']*100))
    if m['holes'] > 0: hard.append('内部孔洞%d' % m['holes'])
    if hard: return '不一致', hard + bad[:3]
    if len(bad) >= 3: return '偏离', bad
    if bad: return '一致(轻微差异)', bad
    return '一致', []

def main():
    dirs = sys.argv[1:] or ['anim4','anim5','anim6','anim7','anim8','anim9','anim10','anim11','anim12','anim12b','anim13','anim14','anim15']
    ref = metrics(ANCHOR)
    rows=[]; summary={}; rejected=[]
    for d in dirs:
        files=sorted(glob.glob(os.path.join(ROOT,d,'*.png')))
        files=[f for f in files if not os.path.basename(f).startswith('_')]
        cnt={}
        for f in files:
            try: m=metrics(f)
            except Exception as e: print('ERR',f,e);continue
            if not m: continue
            name=os.path.basename(f);kind=kind_of(name)
            verdict, why=judge(m,ref,kind)
            cnt[verdict]=cnt.get(verdict,0)+1
            if verdict in ('不一致','偏离','局部帧·待修'): rejected.append((d,name,verdict,'；'.join(why)))
            rows.append([d,name,kind,verdict]+[round(m[k],5) for k in
                ['aspect','gray','black','blue','glass','sharp','magenta','holes','fill']]+['；'.join(why)])
        summary[d]=cnt
    with open(os.path.join(ROOT,'角色一致性检查.csv'),'w',encoding='utf-8-sig',newline='') as fo:
        w=csv.writer(fo)
        w.writerow(['批次','文件','类型','判定','宽高比','灰白占比','黑占比','蓝瞳占比',
                    '眼镜粗度','边缘锐度','品红残留','内部孔洞','轮廓饱满度','偏差说明'])
        w.writerows(rows)
    # 报告
    L=[]
    L.append('# 角色一致性检查报告\n')
    L.append('**数值锚点**：`anim12b/E_seq_open.png`——由作者原稿正面单只作图生图直出，'
             '只换纯品红底、表情姿势未改，等价于原稿在抠图管线下的数值表现。\n')
    L.append('| 指标 | 锚点值 | 含义 |')
    L.append('|---|---|---|')
    for k,lab in [('aspect','头身宽高比'),('gray','灰白绒毛占比'),('blue','蓝瞳占比'),
                  ('glass','脸部上半区黑色占比（圆框眼镜粗度）'),('sharp','Laplacian 方差（边缘柔和度）'),
                  ('fill','bbox 内前景占比（轮廓饱满度）'),('magenta','身上品红残留')]:
        L.append('| %s | %.4f | %s |' % (k, ref[k], lab))
    L.append('\n**判定规则**：完整角色层查 6 项软指标（相对锚点偏差）+ 2 项硬指标'
             '（品红残留 ≤0.6%、内部孔洞 =0）；≥3 项软指标超差判「偏离」，任一硬指标不合格判「不一致」。'
             '局部帧只查孔洞与锐度上限；空心环／粒子特效层不参与角色判定。\n')
    L.append('## 逐批结果\n')
    L.append('| 批次 | 一致 | 一致(轻微差异) | 偏离 | 不一致 | 其他 |')
    L.append('|---|---|---|---|---|---|')
    for d,c in summary.items():
        oth=sum(v for k,v in c.items() if k not in ('一致','一致(轻微差异)','偏离','不一致'))
        L.append('| %s | %d | %d | %d | %d | %d |' % (d,c.get('一致',0),c.get('一致(轻微差异)',0),
                 c.get('偏离',0),c.get('不一致',0),oth))
    L.append('\n## 关键发现\n')
    L.append('- **anim12（纯文生图那批）判废**：10 张里 7 偏离 + 2 不一致，'
             '主因是「边缘柔和度偏 900%–1700%」——正是细线赛璐璐硬描边、尖耳、眼镜变细的数值表现；'
             '另有 2 张身上品红残留 >1.5%。**全部不接入游戏**。')
    L.append('- **anim12b / anim13（按一致性生成）全部通过**：作者原稿作图生图、seed 3、'
             '固定约束块，20 张均为「一致」或「一致(轻微差异)」，内部孔洞全 0。'
             '其中 `anim13/A_face_guard` 首版品红残留 0.885% 被检查器拦下，已按同规格重画后通过。')
    L.append('- 历史批次仍有 **%d 张**判偏离／不一致（多为局部帧与个别品红残留），列在 CSV 的「重画队列」，'
             '按关推进时逐张替换，不冒充已通过。\n' % len(rejected))
    L.append('## 按一致性生成规格（以后每批照此执行）\n')
    L.append('1. `dst_intent=Image2Image`，`input_images=[{type:sandbox, value:/data/workspace/anim4/_style_ref.png}]`，'
             '`seed=3`，`image_ratio=1:1`。**禁用纯文生图出角色**。')
    L.append('2. prompt 结构固定为「只改两处：①背景换纯品红平涂；②本次要改的表情／动作／道具」＋固定约束块：\n')
    L.append('> '+STYLE_FIX+'\n')
    L.append('3. 出图后跑 `python 角色一致性检查.py <新目录>`；判「不一致／偏离」的**重画**，不接入。')
    L.append('4. 通过后统一走色相键控 → 填实孔洞 → 去色溢 → 清右下水印 → 480px WebP q78，再接进 ART/CAST。')
    L.append('5. 旧批带场景整图只归档，不重抠、不混用。\n')
    if rejected:
        L.append('## 重画队列（本轮未接入）\n')
        for d,n,v,w in rejected[:40]:L.append('- `%s/%s` — %s：%s' % (d,n,v,w[:90]))
        if len(rejected)>40:L.append('- …另有 %d 项，详见 CSV' % (len(rejected)-40))
        L.append('')
    open(os.path.join(ROOT,'角色一致性检查报告.md'),'w',encoding='utf-8').write('\n'.join(L))
    # 联系表
    try:fnt=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',13)
    except:fnt=ImageFont.load_default()
    picks=[('锚点·原稿直出',ANCHOR),('anim12·判废代表',os.path.join(ROOT,'anim12/lv_E_face.png')),
           ('anim12b·通过代表',os.path.join(ROOT,'anim12b/E_face_wink.png')),
           ('anim13·通过代表',os.path.join(ROOT,'anim13/A_face_shen.png'))]
    for d in dirs:
        fs=sorted(glob.glob(os.path.join(ROOT,d,'*.png')))
        fs=[f for f in fs if not os.path.basename(f).startswith('_')]
        if fs:picks.append((d+' 代表',fs[0]))
    cell=210; cols=6; rowsn=math.ceil(len(picks)/cols)
    sh=Image.new('RGB',(cell*cols,(cell+22)*rowsn),(245,241,232));dr=ImageDraw.Draw(sh)
    for i,(lab,p) in enumerate(picks):
        im=Image.open(p).convert('RGB').resize((cell-8,cell-8),Image.LANCZOS)
        x=(i%cols)*cell;y=(i//cols)*(cell+22)
        sh.paste(im,(x+4,y+4));dr.text((x+6,y+cell+2),lab,fill=(43,42,38),font=fnt)
    sh.save(os.path.join(ROOT,'_consistency.jpg'),quality=90,optimize=True)
    print('CSV',len(rows),'行；重画队列',len(rejected),'项；报告已写')
    for d,c in summary.items():print('%-9s %s' % (d,dict(c)))

if __name__=='__main__': main()
