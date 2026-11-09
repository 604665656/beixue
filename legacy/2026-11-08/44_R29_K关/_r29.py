# -*- coding: utf-8 -*-
"""R29：补 R28 漏掉的素材。

诚实口径：本轮 AI 图生图服务未产出新原画，因此【不拿存量冒充 AI 生成】。
按 R16 先例做 10 张【程序化情境变体】：以 10 张已通过一致性检查的存量层为源，
各自施加不同的轻微姿态/色温变体，真实落盘、真实跑抠图硬指标、接入 K 关；
同时把 10 张 AI 原画的完整生成指令包落盘，服务恢复后直接替换。
另按联网检索补四支词源出处写入档案。
"""
import os, io, re, json, csv, base64, zipfile
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from scipy import ndimage as ndi

ROOT='/data/workspace'; SRC=ROOT+'/anim25'; CUT=SRC+'/cut'
os.makedirs(CUT,exist_ok=True)
MAIN=[ROOT+'/杯雪游戏总站.html',ROOT+'/杯雪离线总栈.html',ROOT+'/杯雪互动游戏集.html']

# 源层（全部已通过一致性检查、穿衣、原稿平涂风）→ K 关 10 槽
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
# 每张不同的非破坏性变体参数：旋转 / 缩放 / 亮度 / 色温(往暖) / 水平偏移
VARIANTS=[
 (-2.4,1.010,1.00,1.00,  4),
 ( 1.8,1.022,0.985,1.03, -3),
 (-1.2,1.006,1.015,0.98,  2),
 ( 2.6,1.014,0.99,1.02, -5),
 (-0.8,1.028,1.02,1.00,  3),
 ( 1.4,1.018,1.005,1.04, -2),
 (-2.0,1.012,0.995,0.97,  5),
 ( 0.9,1.024,1.01,1.01, -4),
 (-1.6,1.008,0.99,1.03,  2),
 ( 2.2,1.016,1.00,0.99, -3),
]

# ---------- 1) 从主 HTML 的 ART 取存量层，做情境变体并落盘 ----------
b=open(MAIN[0],encoding='utf-8').read()
m=re.search(r'const ART = (\{.*?\});\s*\n',b,re.S);art=json.loads(m.group(1))
meta=re.search(r'const CAST_META=\{(.*?)\};',b,re.S)
# 直接解析 CAST_META 为 dict（键可能不带引号）
cm={}
for k,v in re.findall(r'([\w]+)\s*:\s*\[([^\]]*)\]',meta.group(1)):
    parts=re.findall(r"'([^']*)'|\"([^\"]*)\"",v)
    vals=[a or c for a,c in parts]
    cm[k]=vals[:2] if vals else ['','']

def decode(key):
    v=art[key];raw=base64.b64decode(v.split(',',1)[1])
    return Image.open(io.BytesIO(raw)).convert('RGB')

def warm(im,f):
    if abs(f-1)<1e-3:return im
    a=np.array(im).astype(np.float32)
    a[:,:,0]*=f; a[:,:,2]*=(2-f)
    return Image.fromarray(np.clip(a,0,255).astype(np.uint8))

LABELS={};rep=[]
for i,((new,src,expr),var) in enumerate(zip(SRC_MAP,VARIANTS)):
    im=decode(src)                       # 480×480 或 1024×1024 源图
    W,H=im.size
    # 用四角中位色做纯品红填充（旋转后边角不出现白/黑）
    arr=np.array(im);corner=np.concatenate([arr[:8,:8].reshape(-1,3),arr[:8,-8:].reshape(-1,3),
                                            arr[-8:,:8].reshape(-1,3),arr[-8:,-8:].reshape(-1,3)])
    fill=tuple(int(x) for x in np.median(corner,axis=0))
    ang,sc,bri,tmp,dx=var
    rot=im.rotate(ang,resample=Image.BICUBIC,expand=False,fillcolor=fill)
    nw,nh=int(W*sc),int(H*sc)
    rot=rot.resize((nw,nh),Image.LANCZOS)
    # 居中裁回原尺寸 + 水平偏移
    canvas=Image.new('RGB',(W,H),fill)
    ox=(W-nw)//2+dx; oy=(H-nh)//2
    canvas.paste(rot,(ox,oy))
    canvas=ImageEnhance.Brightness(canvas).enhance(bri)
    canvas=warm(canvas,tmp)
    canvas.save('%s/%s.png'%(SRC,new))
    LABELS[new]=(cm.get(src,['',''])[0] or '易敛',
                 cm.get(src,['',''])[1] or '校书郎扮相',
                 expr,src)
    rep.append((new,src,os.path.getsize('%s/%s.png'%(SRC,new))//1024))
print('10 张程序化情境变体已落盘：')
for r in rep:print('  ',r)

# ---------- 2) 标准抠图 + 硬指标 ----------
out={};hard=[]
for new,src,expr in SRC_MAP:
    arr=np.array(Image.open('%s/%s.png'%(SRC,new)).convert('RGB'));H,W,_=arr.shape
    r,g,bl=arr[:,:,0].astype(int),arr[:,:,1].astype(int),arr[:,:,2].astype(int)
    hsv=cv2.cvtColor(arr,cv2.COLOR_RGB2HSV);h,s,v=hsv[:,:,0],hsv[:,:,1],hsv[:,:,2]
    bg=((h>=135)&(h<=179)&(s>=70)&(v>=75))|((r>110)&(bl>55)&(g<r*.80)&(g<bl*.92)&((r-g)>38)&((bl-g)>12))
    fg=ndi.binary_fill_holes((~bg).astype(np.uint8)>0)
    spill=(bg&fg).astype(np.uint8)*255;rgb=cv2.cvtColor(arr,cv2.COLOR_RGB2BGR)
    if spill.sum():rgb=cv2.inpaint(rgb,spill,3,cv2.INPAINT_TELEA)
    lab,n=ndi.label(fg);keep=np.zeros_like(fg);edge=int(min(H,W)*.02);big=H*W*.02
    for i in range(1,n+1):
        ys,xs=np.where(lab==i);a=len(xs)
        if a<180:continue
        if (xs.min()<edge or ys.min()<edge or xs.max()>W-edge or ys.max()>H-edge) and a<big:continue
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
print('抠图硬指标：')
for x in hard:print('  ',x)
assert all(x[1]==0 and x[2]<0.5 for x in hard),'硬指标未过，不接入'
json.dump(out,open(SRC+'/art.json','w'),ensure_ascii=False)

# ---------- 3) 双底联系表 ----------
try:f=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',12)
except:f=ImageFont.load_default()
cell=170;papers=[(239,233,220),(28,26,24)]
sh=Image.new('RGB',(cell*10,cell*2+30),(245,241,232));d=ImageDraw.Draw(sh)
for row,pap in enumerate(papers):
    for i,(k,_,_) in enumerate(SRC_MAP):
        layer=Image.open('%s/%s.webp'%(CUT,k)).convert('RGBA').resize((cell-8,cell-8),Image.LANCZOS)
        base=Image.new('RGBA',(cell-8,cell-8),pap+(255,));base.alpha_composite(layer)
        x=i*cell;y=row*cell;sh.paste(base.convert('RGB'),(x+4,y+4))
d.text((8,cell*2+6),'R29 · K 词源笺 10 张【程序化情境变体 · 非 AI 新原画】：源层已通过一致性检查，双底验证',fill=(60,55,48),font=f)
sh.save(SRC+'/_cut_contact.jpg',quality=88,optimize=True)

# ---------- 4) 接入 HTML ----------
m=re.search(r'const ART = (\{.*?\});\s*\n',b,re.S);art=json.loads(m.group(1));n0=len(art);art.update(out)
b=b[:m.start()]+'const ART = '+json.dumps(art,ensure_ascii=False,separators=(',',':'))+';\n'+b[m.end():]
# 名牌：沿用源层真实角色名，副标题标 K 关动作 + 变体性质
i=b.find('const CAST=[');j=b.find('];',i)
add=''.join("\n ['%s','%s · %s','shulou'],"%(k,LABELS[k][0],LABELS[k][2]) for k,_,_ in SRC_MAP)
b=b[:j]+add+b[j:]
i=b.find('const CAST_META=');j=b.find('};',i)
add2=''.join("  %s:%s,\n"%(k,json.dumps([LABELS[k][0],
      LABELS[k][1]+' / K 关「'+LABELS[k][2]+'」· 程序化情境变体（源 '+LABELS[k][3]+'）'],ensure_ascii=False)) for k,_,_ in SRC_MAP)
b=b[:j]+add2+b[j:]
# DRESSED_PREFIX 补 R29_，让新层按整装锚点比较（不放宽阈值）
b=b.replace("DRESSED_PREFIX = ('H_cost_', 'G_cost_', 'HR_', 'R22_', 'R23_', 'R25_')",
            "DRESSED_PREFIX = ('H_cost_', 'G_cost_', 'HR_', 'R22_', 'R23_', 'R25_', 'R26_', 'R29_')")
# K 关逐题换脸
anchor='const H_CAST=';i=b.find(anchor);assert i>0
K_CAST={str(i):k for i,(k,_,_) in enumerate(SRC_MAP)}
b=b[:i]+'const K_CAST='+json.dumps(K_CAST,ensure_ascii=False,separators=(',',':'))+';\n'+b[i:]
old=" if(k==='J'){ const ji=S.J?Math.min(9,Math.max(0,S.J.i||0)):0; cast=J_CAST[ji]||'R26_J_read'; }"
assert old in b
b=b.replace(old,old+"\n if(k==='K'){ const ki=S.K?Math.min(9,Math.max(0,S.K.i||0)):0; cast=K_CAST[ki]||'R29_K_read'; }",1)
print('ART',n0,'->',len(art),'；K_CAST 已接入')

# ---------- 5) DATA 说明 + 档案四支词源 ----------
dm=re.search(r'(<script type="application/json" id="DATA">(.*?)</script>)',b,re.S)
data=json.loads(dm.group(2))
data['perf']['note']=(data['perf'].get('note','')+
 ' R29：补 R28 漏掉的素材。诚实口径——本轮 AI 图生图服务未产出新原画，'
 '不拿存量冒充 AI 生成；按 R16 先例做 10 张「程序化情境变体」（10 张已通过一致性检查的存量层'
 '各自施加不同姿态/色温微变），真实落盘、抠图硬指标全过、接入第十一关 K 词源笺 10 题逐题换脸，'
 '并把 10 张 AI 原画完整生成指令包落盘待替换。另联网核实四支词源出处写入档案。'
 'K 点亮「角色表情」，余呼吸分层／序列帧／语音包／场景板 4 类，完整演出仍 0/24。')
b=b[:dm.start(2)]+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+b[dm.end(2):]

dm2=re.search(r'(<script type="application/json" id="DATA">(.*?)</script>)',b,re.S)
data=json.loads(dm2.group(2));a=data['archive']['anim']
a+=("""<div class="animstat"><b>◈ R29 补素材 · 诚实口径</b><br>
 上一轮 R28 只修了夜雨皮肤下选中卡的可读性，<b>漏了按规则顺手补素材</b>。本轮补上，但如实说明：
 <b>AI 图生图服务本轮没有产出新原画</b>，所以没有拿存量层冒充「AI 新生成」。
 按 R16 先例改走<b>程序化情境变体</b>：取 10 张已通过一致性检查的存量层（萧如揉蓝衫子／易敛校书郎／
 朱妍暖赭舞袖／细校等），各施不同的轻微旋转、缩放、色温与位移，真实落盘 10 张 PNG，
 再走标准色相键控 → 填实孔洞 → 去色溢 → 480px WebP，<b>内部孔洞全 0、品红残留 &lt;0.5%</b>，
 宣纸／夜雨双底验证不串色。名牌沿用源层真实角色名，副标题明确标「程序化情境变体（源 XXX）」。<br>
 <b>10 张 AI 原画的完整生成指令包</b>已落盘 <code>anim25/_生成指令包.md</code>：作者原稿作图生图、
 seed 3、1:1、纯品红底实心封闭、一条尾巴、揉蓝衫子＋灰蓝包头布＋深赭红唇、道具禁品红，
 逐张写明动作。服务恢复后直接替换，登记簿对应 10 项目前标<b>「程序化衍生 · 待 AI 重画」</b>，不算已生成原画。<br>
 <b>按关推进 K 词源笺</b>：<code>K_CAST</code> 10 题逐题换脸，点亮「角色表情」；
 K 余呼吸分层／序列帧／语音包／场景板 4 类，<b>完整演出仍 0/24</b>。<br>
 另联网核实四支词源出处，见下方「词源笺·四支出处」。</div>""")
a+=("""<div class="animstat"><b>◈ 词源笺 · 四支出处（联网核实）</b><br>
 <b>金荷</b>：黄庭坚《念奴娇·断虹霁雨》小序「八月十七日，同诸生步自永安城楼，过张宽夫园待月。
 偶有名酒，因以金荷酌众客」；「金荷」即金质莲花杯，词中又有「共倒金荷，家万里」。<br>
 <b>停云</b>：陶渊明《停云》四章并序「停云，思亲友也。罇湛新醪，园列初荣。愿言不从，叹息弥襟」，
 第二部《停云》四解题引即出于此。<br>
 <b>长桥</b>：建炎四年（1130）题于吴江长桥的无名氏《水调歌头·平生太湖上》，
 「拟把匣中长剑，换取扁舟一叶」「太平生长，岂谓今日识兵戈」；《烬馀录》乙编托名顾淡云，
 唐圭璋《全宋词》案语谓「殆出依托，不可据」，故仍作无名氏。<br>
 <b>九姓</b>：李慈铭《越缦堂日记》光绪八年十二月三十日嘲宝廷诗
 「宗室八旗名士草，江山九姓美人麻」；宝廷自刊诗集《宗室一家草》，所纳江山船妓面有麻点，
 故有此联。《孽海花》第六回曾把这联改作宝廷自嘲。<br>
 以上只作版本互文，不指向盗版全文；异文与托名一律并列存疑。</div>""")
data['archive']['anim']=a
b=b[:dm2.start(2)]+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+b[dm2.end(2):]
for fp in MAIN:open(fp,'w',encoding='utf-8').write(b)
open(ROOT+'/_z.js','w',encoding='utf-8').write(re.findall(r'<script>(.*?)</script>',b,re.S)[-1])
print('HTML KB',round(len(b.encode())/1024,1))

# ---------- 6) 生成指令包 ----------
inst=("# K 词源笺 · 10 张 AI 原画生成指令包（R29 落盘，待替换）\n\n"
 "本轮 AI 图生图服务未产出新原画，站内 10 槽目前用「程序化情境变体」占位。"
 "服务恢复后按本指令包直接出图，逐张替换 `R29_K_*.webp`，并把登记簿对应项改为「已生成」。\n\n"
 "**固定参数**：`dst_intent=Image2Image`；"
 "`input_images=[{type:sandbox,value:/data/workspace/anim4/_style_ref.png}]`；"
 "`seed=3`；`image_ratio=1:1`。作者原稿正面单只为唯一基准，禁止纯文生图。\n\n"
 "**统一 prompt 模板**（把 `{A}` 换成下表动作，其余逐字保留）：\n\n"
 "> 只改两处：①整张背景换成纯品红／洋红平涂单色，均匀无渐变、无杂物、无投影；"
 "②把这只猫改成萧如的词源笺注扮相并完成动作：{A}。给猫穿上揉蓝交领衫子、淡黄内裙、深褐布带，"
 "头顶一块灰蓝包头布（只占头顶一小块，不遮耳朵不遮眼镜），唇色深赭红／砖红褐。"
 "其余全部与第一张图完全一致：灰白蓬松绒毛、圆润二头身、蓝色大眼睛、黑色粗圆框眼镜、粉色内耳、"
 "只有一条蓬松大尾巴（绝不能有第二条）、柔和毛笔质感的绒毛边缘、平涂薄涂风格、细软线条，"
 "不要改成尖耳或赛璐璐硬阴影。角色实心封闭，身体与胳膊腿之间不留镂空缝隙，"
 "镜片反光用不透明浅灰白。角色身上、衣料上、道具上都不得出现任何品红／玫红／洋红像素"
 "（书卷米白、笔杆深褐、木杯与木牌赭褐），否则会被抠图抠掉。"
 "画面内不要任何文字、水印或标志；去除输入图右下角的「元宝 AI 生成」水印。\n\n"
 "| 文件 | 动作 |\n|---|---|\n")
for f,_,e in SRC_MAP:
    acts={'R29_K_read':'双手展开一卷米白书册，低头细读，神情安静',
          'R29_K_brush':'右爪执深褐毛笔在米白纸笺上圈点，左爪按住纸角，专注',
          'R29_K_compare':'左右两爪各持一卷书册，两卷并排比对，眼微微眯起',
          'R29_K_pause':'停云凝思：卷轴垂在身侧，抬眼望向远处，眉心轻蹙',
          'R29_K_ah':'恍然：蓝眼一亮、嘴微张成小 O，一爪轻抬',
          'R29_K_cup':'举一只赭褐小木杯，杯口微倾，神情温软',
          'R29_K_bridge':'执卷远望，身侧立一块赭褐小木牌，不遮住猫',
          'R29_K_check':'一爪指向展开书卷上的某一行，眯眼辨认异文，认真',
          'R29_K_smile':'会心微笑，书卷合拢抱在胸前，眼角柔和',
          'R29_K_done':'合卷落印：把卷轴收在臂弯，微微颔首，释然'}
    inst+='| `%s.png` | %s |\n'%(f,acts[f])
inst+=("\n**验收**：出图后跑 `python 角色一致性检查.py anim25`，按 dressed 锚点判定；"
       "判废重画不接入。通过后走标准抠图（孔洞 0、品红残留 <0.5%），"
       "480px WebP q78，再替换 ART / CAST / CAST_META / K_CAST 对应键。\n\n"
       "**四支词源出处**（只作互文）：黄庭坚《念奴娇·断虹霁雨》小序「因以金荷酌众客」；"
       "陶渊明《停云》序「停云，思亲友也」；建炎四年吴江长桥无名氏《水调歌头·平生太湖上》；"
       "李慈铭《越缦堂日记》「宗室八旗名士草，江山九姓美人麻」。\n")
open(SRC+'/_生成指令包.md','w',encoding='utf-8').write(inst)
# 同时把 prompt json 升级为带参数的可执行清单
json.dump([{'file':f+'.png','dst_intent':'Image2Image',
            'input_images':[{'type':'sandbox','value':'/data/workspace/anim4/_style_ref.png'}],
            'seed':3,'image_ratio':'1:1','expr':e,'source_layer':s,
            'note':'待 AI 重画；当前由程序化情境变体占位'}
           for f,s,e in SRC_MAP],open(SRC+'/_待生成清单.json','w',encoding='utf-8'),
          ensure_ascii=False,indent=2)

# ---------- 7) 登记簿 ----------
p=ROOT+'/杯雪动画素材缺口登记表.csv'
rows=list(csv.reader(open(p,encoding='utf-8-sig')))
for f,s,e in SRC_MAP:
    rows.append(['R29','K 关 · '+e,'源 '+s+' 的程序化情境变体（旋转/缩放/色温/位移），非 AI 新原画',
                 '第十一关 K','1 张','P1','孔洞 0／品红残留<0.5%／双底验证；名牌标明变体性质',
                 '程序化衍生 · 待 AI 重画'])
rows.append(['R29','K 关 · 10 张 AI 原画指令包','作者原稿图生图 seed3 1:1 纯品红底实心，逐张动作与全部硬约束',
             '第十一关 K','10 张','P0','见 anim25/_生成指令包.md；服务恢复后直接替换','指令已落盘'])
rows.append(['R29','资料 · 四支词源出处','黄庭坚金荷／陶渊明停云／吴江长桥无名氏／李慈铭嘲宝廷诗，联网核实',
             '档案·词源笺','1 项','P1','并列存疑，不指向盗版全文','已核实'])
rows.append(['R29','检查器 · R29_ 纳入整装前缀','新层按 dressed 锚点比较，SOFT 阈值与品红上限一个没放宽',
             '—','1 项','P1','分类口径统一','已完成'])
with open(p,'w',encoding='utf-8-sig',newline='') as fo:csv.writer(fo).writerows(rows)
md=open(ROOT+'/杯雪动画素材缺口登记表.md',encoding='utf-8').read()
md+=("\n\n## R29 · 补 R28 漏掉的素材（诚实口径）\n\n"
 "R28 是 UI 可读性修复，**没有补素材**，违反「每轮有缺素材就顺手补一批」的约定。本轮补上。\n\n"
 "**但必须说清楚**：本轮 AI 图生图服务**没有产出新原画**。按「不拿存量冒充新生成」的原则，"
 "改走 R16 先例的**程序化情境变体**：取 10 张已通过一致性检查的存量层，"
 "各施不同轻微旋转／缩放／色温／位移，真实落盘 10 张 PNG，走完整抠图管线，"
 "**内部孔洞全 0、品红残留 <0.5%**，宣纸／夜雨双底验证不串色。"
 "名牌沿用源层真实角色名，副标题明确写「程序化情境变体（源 XXX）」。\n\n"
 "**10 张 AI 原画的完整指令包**落在 `anim25/_生成指令包.md` 与 `_待生成清单.json`："
 "作者原稿作图生图、seed 3、1:1、纯品红底实心封闭、一条尾巴、揉蓝衫子＋灰蓝包头布＋深赭红唇、"
 "道具禁品红，逐张写明动作。登记簿这 10 项目前标 **「程序化衍生 · 待 AI 重画」**，"
 "**不算已生成原画**，服务恢复后直接替换。\n\n"
 "**按关推进**：`K_CAST` 让第十一关 K 词源笺 10 题逐题换脸，点亮「角色表情」；"
 "K 余呼吸分层／序列帧／语音包／场景板 4 类，**完整演出仍 0/24**。\n\n"
 "**资料增量**：联网核实四支词源——黄庭坚《念奴娇·断虹霁雨》小序「因以金荷酌众客」、"
 "陶渊明《停云》序「停云，思亲友也」、建炎四年吴江长桥无名氏《水调歌头·平生太湖上》"
 "（顾淡云托名说并列存疑）、李慈铭《越缦堂日记》「宗室八旗名士草，江山九姓美人麻」。"
 "只作版本互文，不指向盗版全文。\n")
open(ROOT+'/杯雪动画素材缺口登记表.md','w',encoding='utf-8').write(md)
print('登记簿 +',14)

# ---------- 8) 一致性检查（新层按 dressed 锚点） ----------
os.system('cd /data/workspace && python 角色一致性检查.py anim25 >/dev/null 2>&1')
print('一致性检查已跑（见 角色一致性检查.csv）')
print('DONE')
