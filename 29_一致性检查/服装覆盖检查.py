# -*- coding: utf-8 -*-
"""服装覆盖检查 v3（最终口径）：**数值只作辅助，目检登记为准**。

为什么不能硬套像素判据：
- v1「躯干区非灰白占比」→ 把 G 关裸猫手里的书册／木杯／短刀误判成衣服（G_face_verify 0.205）。
- v2「最大非灰白连通块 ≥ .12」→ 会漏判浅色行头（藕荷小袄 H_cost_ying 仅 0.028）。
- v3「绒毛之外全算」→ 又把 G 关裸猫的书册当成大片衣料（G_face_verify 0.677）。
结论：衣料与「胸前大片道具」在像素特征上无法可靠区分。
因此最终判定写入 `行头目检登记.csv`（人工目检逐层标注），本脚本只输出辅助数值与联系表。

用法：python 服装覆盖检查.py
"""
import re,json,io,base64,csv
import numpy as np,cv2
from PIL import Image,ImageDraw,ImageFont
from scipy import ndimage as ndi
from collections import Counter

ROOT='/data/workspace';b=open(ROOT+'/杯雪游戏总站.html',encoding='utf-8').read()
art=json.loads(re.search(r'const ART = (\{.*?\});\s*\n',b,re.S).group(1))
rows=[];imgs={}
for k,v in art.items():
    if k.startswith(('bg_','fx_')) or 'ripple' in k or not v.startswith('data:image'):continue
    try:a=np.array(Image.open(io.BytesIO(base64.b64decode(v.split(',',1)[1]))).convert('RGBA'))
    except Exception:continue
    rgb=a[:,:,:3];m=a[:,:,3]>128
    ys,xs=np.where(m)
    if len(xs)<500:continue
    y0,y1,x0,x1=ys.min(),ys.max(),xs.min(),xs.max();bh=y1-y0+1;bw=x1-x0+1
    Y,X=np.indices(m.shape)
    torso=m&(Y>=y0+bh*.48)&(Y<=y0+bh*.85)&(X>=x0+bw*.22)&(X<=x0+bw*.78)
    if torso.sum()<200:continue
    hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV);s,vv=hsv[:,:,1],hsv[:,:,2]
    # v2 辅助：深色／高饱和成片块
    nw2=torso&((s>62)|(vv<132));L2,c2=ndi.label(nw2)
    blob2=float(np.bincount(L2.ravel())[1:].max())/float(torso.sum()) if c2 else 0
    # v3 辅助：绒毛之外全部
    nw3=torso&~((s<32)&(vv>140));L3,c3=ndi.label(nw3)
    blob3=float(np.bincount(L3.ravel())[1:].max())/float(torso.sum()) if c3 else 0
    rows.append((k,round(float(nw2.sum())/float(torso.sum()),4),round(blob2,4),round(blob3,4)))
    if k.startswith('cos_') or k.startswith('H_cost_'):imgs[k]=Image.fromarray(a).convert('RGBA')

# 目检登记（人工逐层核对联系表后的结论）
EYE={'有':['cos_shen','cos_geng','cos_qinwen','cos_jinhe','cos_ying','cos_yi','cos_du','cos_jiao',
           'cos_gbx','cos_qu','cos_yuancl','cos_yuaner','cos_xiao','cos_zhu','cos_wen','cos_shi',
           'cos_tian','cos_tie','cos_luo','cos_jin_guard','cos_yi_cup','cos_shen_calm','cos_shen_shrug',
           'H_cost_jin','H_cost_shen','H_cost_ying','H_cost_geng','H_cost_yuaner','H_cost_luo',
           'H_cost_jinhe','H_cost_qinwen','H_cost_shi','H_cost_yuchi',
           'G_cost_verify','G_cost_compare','G_cost_brush','G_cost_startled','G_cost_smile','G_cost_turn','G_cost_scroll','G_cost_blink','G_cost_open'],
     '无（待补或有意保留）':['cos_jin','cos_base','cos_mi','cos_zwl','cos_zwl_firm','cos_luo_nod',
           'cos_luo_draw','cos_luo_guard','cos_ying_sing','cos_ying_clear',
           'G_cost_close',
           'A_face_shen','A_face_argue','A_face_ying','A_face_luo','A_face_draw','A_face_guard']}
with open(ROOT+'/服装覆盖检查.csv','w',encoding='utf-8-sig',newline='') as fo:
    w=csv.writer(fo);w.writerow(['层名','v2非灰白占比','v2最大连通块','v3最大连通块','目检结论'])
    for k,r2,bl2,bl3 in rows:
        tag='有' if k in EYE['有'] else ('无（待补或有意保留）' if k in EYE['无（待补或有意保留）'] else '未逐张目检')
        w.writerow([k,r2,bl2,bl3,tag])
print('辅助数值层',len(rows),'｜目检登记 有',len(EYE['有']),'无',len(EYE['无（待补或有意保留）']))
print('判据局限：v2 漏判浅色行头、v3 误判胸前书册；最终以 行头目检登记.csv 为准。')

# 目检联系表
try:f=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',12)
except:f=ImageFont.load_default()
keys=list(imgs.keys());cols=7;cell=170;rn=(len(keys)+cols-1)//cols
sh=Image.new('RGB',(cell*cols,(cell+20)*rn),(239,233,220));d=ImageDraw.Draw(sh)
for i,k in enumerate(keys):
    im=imgs[k].resize((cell-8,cell-8),Image.LANCZOS)
    base=Image.new('RGBA',(cell-8,cell-8),(239,233,220,255));base.alpha_composite(im)
    x=(i%cols)*cell;y=(i//cols)*(cell+20)
    sh.paste(base.convert('RGB'),(x+4,y+4));d.text((x+5,y+cell+1),k,fill=(43,42,38),font=f)
sh.save(ROOT+'/_服装覆盖目检.jpg',quality=88,optimize=True)
