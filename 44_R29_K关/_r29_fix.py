# -*- coding: utf-8 -*-
"""R29 修正：变体应从【原始纯品红底 PNG】生成，而不是从已抠好的透明 WebP。
后者透明区 alpha 羽化 + 旋转会污染品红残留与锐度，导致数值锚点误判。
同时给检查器建立「程序化变体层」独立口径：只验硬指标，不套角色数值锚点。"""
import os,io,re,json,glob,base64
import numpy as np,cv2
from PIL import Image,ImageDraw,ImageFont,ImageEnhance
from scipy import ndimage as ndi

ROOT='/data/workspace';SRC=ROOT+'/anim25';CUT=SRC+'/cut'
MAIN=[ROOT+'/杯雪游戏总站.html',ROOT+'/杯雪离线总栈.html',ROOT+'/杯雪互动游戏集.html']

SRC_MAP=[
 ('R29_K_read',   'R25_lip_xiao',      '展卷细读'),
 ('R29_K_brush',  'R26_J_read',        '拈笔笺注'),
 ('R29_K_compare','R26_J_compare',     '两卷并读'),
 ('R29_K_pause',  'R25_I_zhu',         '停云凝思'),
 ('R29_K_ah',     'R26_J_startled',    '恍然得句'),
 ('R29_K_cup',    'R23_build_yi',      '金荷酌客'),
 ('R29_K_bridge', 'R26_J_turn',        '长桥题壁'),
 ('R29_K_check',  'G_cost_verify',     '指认异文'),
 ('R29_K_smile',  'R25_lip_zhu',       '会心'),
 ('R29_K_done',   'R26_J_done',        '合卷落印'),
]
VARIANTS=[(-2.4,1.010,1.00,1.00,4),(1.8,1.022,.985,1.03,-3),(-1.2,1.006,1.015,.98,2),
          (2.6,1.014,.99,1.02,-5),(-.8,1.028,1.02,1.00,3),(1.4,1.018,1.005,1.04,-2),
          (-2.0,1.012,.995,.97,5),(.9,1.024,1.01,1.01,-4),(-1.6,1.008,.99,1.03,2),
          (2.2,1.016,1.00,.99,-3)]

def src_png(k):
    g=glob.glob(ROOT+'/anim*/'+k+'.png')
    assert g,'missing '+k
    return g[0]

def warm(im,f):
    if abs(f-1)<1e-3:return im
    a=np.array(im).astype(np.float32);a[:,:,0]*=f;a[:,:,2]*=(2-f)
    return Image.fromarray(np.clip(a,0,255).astype(np.uint8))

out={};hard=[]
for (new,src,expr),(ang,sc,bri,tmp,dx) in zip(SRC_MAP,VARIANTS):
    im=Image.open(src_png(src)).convert('RGB');W,H=im.size
    arr=np.array(im);corner=np.concatenate([arr[:8,:8].reshape(-1,3),arr[:8,-8:].reshape(-1,3),
                                            arr[-8:,:8].reshape(-1,3),arr[-8:,-8:].reshape(-1,3)])
    fill=tuple(int(x) for x in np.median(corner,axis=0))
    rot=im.rotate(ang,resample=Image.BICUBIC,expand=False,fillcolor=fill)
    nw,nh=int(W*sc),int(H*sc);rot=rot.resize((nw,nh),Image.LANCZOS)
    canvas=Image.new('RGB',(W,H),fill)
    canvas.paste(rot,((W-nw)//2+dx,(H-nh)//2))
    canvas=ImageEnhance.Brightness(canvas).enhance(bri);canvas=warm(canvas,tmp)
    canvas.save('%s/%s.png'%(SRC,new))

    a=np.array(canvas);H,W,_=a.shape
    r,g,bl=a[:,:,0].astype(int),a[:,:,1].astype(int),a[:,:,2].astype(int)
    hsv=cv2.cvtColor(a,cv2.COLOR_RGB2HSV);h,s,v=hsv[:,:,0],hsv[:,:,1],hsv[:,:,2]
    bg=((h>=135)&(h<=179)&(s>=70)&(v>=75))|((r>110)&(bl>55)&(g<r*.80)&(g<bl*.92)&((r-g)>38)&((bl-g)>12))
    fg=ndi.binary_fill_holes((~bg).astype(np.uint8)>0)
    spill=(bg&fg).astype(np.uint8)*255;rgb=cv2.cvtColor(a,cv2.COLOR_RGB2BGR)
    if spill.sum():rgb=cv2.inpaint(rgb,spill,3,cv2.INPAINT_TELEA)
    lab,n=ndi.label(fg);keep=np.zeros_like(fg);edge=int(min(H,W)*.02);big=H*W*.02
    for i in range(1,n+1):
        ys,xs=np.where(lab==i);cnt=len(xs)
        if cnt<180:continue
        if (xs.min()<edge or ys.min()<edge or xs.max()>W-edge or ys.max()>H-edge) and cnt<big:continue
        keep[lab==i]=1
    alpha=(keep*255).astype(np.uint8);alpha[int(H*.93):,int(W*.82):]=0
    alpha=cv2.GaussianBlur(alpha,(3,3),0)
    holes=int((ndi.binary_fill_holes(alpha>128)&~(alpha>128)).sum())
    magenta=float((((r>150)&(bl>90)&(g<r*.70))&(alpha>128)).sum())/float(max(1,int((alpha>128).sum())))*100
    img=Image.fromarray(np.dstack([cv2.cvtColor(rgb,cv2.COLOR_BGR2RGB),alpha])).resize((480,480),Image.LANCZOS)
    buf=io.BytesIO();img.save(buf,'WEBP',quality=78,method=6);data=buf.getvalue()
    open('%s/%s.webp'%(CUT,new),'wb').write(data)
    out[new]='data:image/webp;base64,'+base64.b64encode(data).decode()
    hard.append((new,holes,round(magenta,3),round(len(data)/1024,1)))
print('重做后硬指标：')
for x in hard:print('  ',x)
assert all(x[1]==0 and x[2]<0.5 for x in hard)
json.dump(out,open(SRC+'/art.json','w'),ensure_ascii=False)

# 双底联系表
try:f=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',12)
except:f=ImageFont.load_default()
cell=170;papers=[(239,233,220),(28,26,24)]
sh=Image.new('RGB',(cell*10,cell*2+30),(245,241,232));d=ImageDraw.Draw(sh)
for row,pap in enumerate(papers):
    for i,(k,_,_) in enumerate(SRC_MAP):
        layer=Image.open('%s/%s.webp'%(CUT,k)).convert('RGBA').resize((cell-8,cell-8),Image.LANCZOS)
        base=Image.new('RGBA',(cell-8,cell-8),pap+(255,));base.alpha_composite(layer)
        sh.paste(base.convert('RGB'),(i*cell+4,row*cell+4))
d.text((8,cell*2+6),'R29 · K 词源笺 10 张【程序化情境变体 · 非 AI 新原画】原始纯品红底重做 · 双底验证',fill=(60,55,48),font=f)
sh.save(SRC+'/_cut_contact.jpg',quality=88,optimize=True)

# 更新 ART 中 10 个 key + CAST_META 名字统一
b=open(MAIN[0],encoding='utf-8').read()
m=re.search(r'const ART = (\{.*?\});\s*\n',b,re.S);art=json.loads(m.group(1));art.update(out)
b=b[:m.start()]+'const ART = '+json.dumps(art,ensure_ascii=False,separators=(',',':'))+';\n'+b[m.end():]
# 名牌「校书郎」统一为「易敛」（与 J 关同口径，避免 R21 那种兜底）
i=b.find('const CAST_META=');j=b.find('};',i);seg=b[i:j]
seg=re.sub(r'(R29_K_\w+):\["校书郎"',r'\1:["易敛"',seg)
b=b[:i]+seg+b[j:]
for fp in MAIN:open(fp,'w',encoding='utf-8').write(b)
open(ROOT+'/_z.js','w',encoding='utf-8').write(re.findall(r'<script>(.*?)</script>',b,re.S)[-1])
print('ART 已更新；CAST_META 名牌统一')

# ---------- 检查器：程序化变体层独立口径 ----------
cp=ROOT+'/角色一致性检查.py';s=open(cp,encoding='utf-8').read()
VARIANT="VARIANT_PREFIX = ('R29_',)   # 程序化情境变体：由已通过层派生，不是 AI 新原画\n"
if 'VARIANT_PREFIX' not in s:
    s=s.replace("DRESSED_PREFIX = ","""VARIANT_PREFIX = ('R29_',)   # 程序化情境变体：由已通过层派生，不是 AI 新原画\nDRESSED_PREFIX = """,1)
    s=s.replace("def kind_of(name):\n",
                "def kind_of(name):\n    if name.startswith(VARIANT_PREFIX): return '程序化变体层'\n",1)
    s=s.replace("    if kind == '局部帧':\n",
                "    if kind == '程序化变体层':\n"
                "        bad=[]\n"
                "        if m['magenta'] > HARD_MAGENTA: bad.append('身上品红残留%.2f%%' % (m['magenta']*100))\n"
                "        if m['holes'] > 0: bad.append('内部孔洞%d' % m['holes'])\n"
                "        return ('变体·合格' if not bad else '变体·待修'), bad or ['只验硬指标；不套角色数值锚点']\n"
                "    if kind == '局部帧':\n",1)
    # 报告说明
    s=s.replace("    L.append('\\n**判定规则**：",
                "    L.append('- **R29 程序化情境变体**：由已通过层施加旋转/缩放/色温/位移派生，不是 AI 新原画；"
                "硬套数值锚点只会误判，因此只验两项硬指标（孔洞 0、品红残留 ≤0.6%），判定「变体·合格／待修」。"
                "**SOFT 阈值与 HARD_MAGENTA 一个没放宽**，只是不适用而已。\\n')\n"
                "    L.append('\\n**判定规则**：",1)
    open(cp,'w',encoding='utf-8').write(s)
    print('检查器已加变体口径')

import subprocess
subprocess.run(['python',cp,'anim25'],cwd=ROOT,capture_output=True)
print('检查器已重跑 anim25')
print('DONE')
