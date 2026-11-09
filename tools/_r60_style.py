# -*- coding: utf-8 -*-
"""R60 全量画风一致性检查：直接对主站里实际内嵌的图层像素做统计。
维度：尺寸 / 色温(warm=R-B 均值) / 勾线墨色(暗像素占比) / 灰调占比 / 鲜色占比 / 平均饱和度 / 亮度。
分角色聚合，输出离群层（角色内 median±3*MAD 或全局阈值）。"""
import re,io,json,base64,numpy as np
from PIL import Image
h=open('/data/workspace/杯雪游戏总站.html',encoding='utf-8').read()
# ART 表： "key": {"...src":"data:image/webp;base64,XXXX"...}
pat=re.compile(r'"([A-Za-z0-9_]+)"\s*:\s*"data:image/(\w+);base64,([^"]+)"')
rows=[];seen=set()
for m in pat.finditer(h):
    k,fmt,b64=m.groups()
    if k in seen: continue
    seen.add(k)
    try:
        raw=base64.b64decode(b64)
        im=Image.open(io.BytesIO(raw)).convert('RGBA')
    except Exception as e:
        rows.append({'key':k,'err':str(e)[:40]});continue
    a=np.asarray(im).astype(int)
    op=a[:,:,3]>32
    n=int(op.sum())
    if n<500:
        rows.append({'key':k,'err':'too_small','px':n});continue
    rgb=a[:,:,:3][op]
    mx=rgb.max(1);mn=rgb.min(1)
    sat=np.where(mx>0,(mx-mn)/np.maximum(mx,1),0)
    lum=0.299*rgb[:,0]+0.587*rgb[:,1]+0.114*rgb[:,2]
    rows.append({'key':k,'size':list(im.size),'px':n,
        'warm':round(float((rgb[:,0]-rgb[:,2]).mean()),1),
        'dark':round(float((lum<70).mean()*100),2),
        'gray':round(float((sat<0.12).mean()*100),1),
        'vivid':round(float((sat>0.45).mean()*100),2),
        'sat':round(float(sat.mean()),3),'lum':round(float(lum.mean()),1)})
print('图层总数',len(rows),'解码失败',sum(1 for r in rows if 'err' in r))
ok=[r for r in rows if 'err' not in r]
# 角色归类：键前缀 -> 角色
def cast_of(k):
    if k.startswith('fx_'): return '@特效层'
    if k.startswith('bg_'): return '@背景层'
    if k.startswith('cover'): return '@封面'
    m=re.match(r'(cos_[a-z]+?)(_|$)',k)
    if m: return m.group(1)
    if k.startswith('R59_base'): return 'cos_base'
    if k.startswith(('A_','B_','C_','D_','G_','H_','HR_')): return '@舞台构图'
    return '@其他'
for r in ok: r['cast']=cast_of(r['key'])
from collections import defaultdict
g=defaultdict(list)
for r in ok: g[r['cast']].append(r)
print('角色/分组数',len(g))
sizes=sorted(set(tuple(r['size']) for r in ok))
print('尺寸档位',sizes)
allv=np.array([r['warm'] for r in ok])
print('全局色温 min/med/max',round(allv.min(),1),round(float(np.median(allv)),1),round(allv.max(),1))
# 离群：角色内 MAD
out=[]
for c,rs in g.items():
    if c.startswith('@') or len(rs)<3: continue
    w=np.array([r['warm'] for r in rs])
    med=np.median(w); mad=np.median(np.abs(w-med)) or 1.0
    for r in rs:
        z=abs(r['warm']-med)/(1.4826*mad)
        if z>3.5: out.append((round(z,1),r['key'],c,r['warm'],round(float(med),1),len(rs)))
print('角色内色温离群层',len(out))
for o in sorted(out,reverse=True)[:15]: print('  z=%s %s 角色=%s warm=%s 角色中位=%s (n=%s)'%o)
# 全局鲜色离群
vv=np.array([r['vivid'] for r in ok]); med=np.median(vv); mad=np.median(np.abs(vv-med)) or 1
vo=[(r['key'],r['vivid'],r['cast']) for r in ok if abs(r['vivid']-med)/(1.4826*mad)>3.5]
print('全局鲜色离群',len(vo),'中位',round(float(med),2))
for x in sorted(vo,key=lambda t:-t[1])[:12]: print('  ',x)
json.dump({'total':len(rows),'ok':len(ok),'sizes':[list(s) for s in sizes],
           'warm_global':[round(float(allv.min()),1),round(float(np.median(allv)),1),round(float(allv.max()),1)],
           'outliers_warm':out,'outliers_vivid':vo,'rows':rows},
          open('/data/workspace/R60_画风一致性.json','w'),ensure_ascii=False,indent=1)
# CSV
import csv
with open('/data/workspace/R60_画风一致性检查.csv','w',newline='',encoding='utf-8-sig') as f:
    wtr=csv.DictWriter(f,fieldnames=['key','cast','size','px','warm','dark','gray','vivid','sat','lum','err'])
    wtr.writeheader()
    for r in sorted(ok,key=lambda r:(r['cast'],r['key'])): wtr.writerow({k:r.get(k,'') for k in wtr.fieldnames})
print('CSV 写出')
