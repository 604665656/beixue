import base64,io,json,os,sys
from PIL import Image
SRC='anim62/cut'
# layer key -> (cell, source png, cropbox or None)
PLAN=[
 ('R62_luo_ai','cos_luo|哀','luo_ai.png'),
 ('R62_luo_jue','cos_luo|决','luo_jue.png'),
 ('R62_qinwen_nu','cos_qinwen|怒','qinwen_nu2.png'),
 ('R62_qinwen_jing','cos_qinwen|惊','qinwen_jing2.png'),
 ('R62_qinwen_zui','cos_qinwen|醉','qinwen_zui2.png'),
 ('R62_du_xi','cos_du|喜','du_xi.png'),
 ('R62_du_yi','cos_du|疑','du_yi.png'),
 ('R62_du_jue','cos_du|决','du_jue2.png'),
 ('R62_du_jing','cos_du|惊','du_jing.png'),
 ('R62_jinhe_xi','cos_jinhe|喜','jinhe_xi.png'),
]
SIZE=480
def webp_b64(im):
    buf=io.BytesIO(); im.save(buf,'WEBP',quality=82,method=4)
    return base64.b64encode(buf.getvalue()).decode()
h=open('杯雪游戏总站.html',encoding='utf-8').read()
if 'R62_luo_ai' in h:
    print('ALREADY PATCHED'); sys.exit(0)
entries=[]
data_add=[]
for key,cell,png in PLAN:
    im=Image.open(os.path.join(SRC,png)).convert('RGBA')
    # trim to content bbox, keep aspect, fit into SIZE
    bb=im.getbbox()
    im=im.crop(bb)
    w,hh=im.size
    s=min(SIZE/w,SIZE/hh)
    im=im.resize((max(1,int(w*s)),max(1,int(hh*s))),Image.LANCZOS)
    b64=webp_b64(im)
    data_add.append('"%s":"data:image/webp;base64,%s"'%(key,b64))
    entries.append('"%s": "%s"'%(cell,key))
# 1) insert ART entries right after the opening of ART object
i=h.index('const ART = {')
j=i+len('const ART = {')
h=h[:j]+''.join(','+x for x in data_add)+h[j:]
# 2) insert EXPR_SPECIAL entries at the start of its object body
k=h.index('const EXPR_SPECIAL=')
l=h.index('{',k)+1
h=h[:l]+''.join(','+x for x in entries)+h[l:]
# 3) bump version labels R55 -> R62 (panel footnote + csv filename)
h=h.replace("return '<div class=\"exprfoot\">R55：","return '<div class=\"exprfoot\">R62：")
h=h.replace("a.download='杯雪表情谱系_R55_","a.download='杯雪表情谱系_R62_")
open('杯雪游戏总站.html','w',encoding='utf-8').write(h)
print('patched: added',len(data_add),'layers; html bytes',len(h))
