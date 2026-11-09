# -*- coding: utf-8 -*-
"""R51 v2：修 R51 v1 的水印 bug。
   v1 沿用 anim28/cut_pipe.py：填洞后才清「右下角非主域小岛」。
   本批 AI 图的水印笔画被 fill_holes 与右侧尾巴桥接进主域 → 清不掉。
   v2 改为【源头预清】：先在原始 RGB 上按连通域找出水印小岛，
   把对应像素刷成四角采样的品红背景色，再重新走完整色键抠图。
   这样水印根本不进入前景，且不依赖成品后处理的连通域判定。"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, cv2, scipy.ndimage as ndi, json, base64, io, os

D='/data/workspace/anim46'; os.makedirs(D+'/cut',exist_ok=True)
FP='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
f18=ImageFont.truetype(FP,18); f14=ImageFont.truetype(FP,14)

JOBS=[
 ('R51_jiao_nu',    '焦泗隐·怒',  'cos_jiao|怒'),
 ('R51_jiao_ai',    '焦泗隐·哀',  'cos_jiao|哀'),
 ('R51_jiao_jing',  '焦泗隐·惊',  'cos_jiao|惊'),
 ('R51_jiao_yi',    '焦泗隐·疑',  'cos_jiao|疑'),
 ('R51_luo_xi',     '骆寒·喜',    'cos_luo|喜'),
 ('R51_luo_jing',   '骆寒·惊',    'cos_luo|惊'),
 ('R51_luo_jue',    '骆寒·决',    'cos_luo|决'),
 ('R51_luo_zui',    '骆寒·醉',    'cos_luo|醉'),
 ('R51_qinwen_jing','秦稳·静息',  'cos_qinwen|静息'),
 ('R51_qinwen_ai',  '秦稳·哀',    'cos_qinwen|哀'),
]

def outer_of(a):
    r,g,b=[a[:,:,i].astype(np.float32) for i in range(3)]
    bg=(r>g*1.35)&(b>g*1.08)&(r>85)&(g<150)&(r>b*0.95)
    bg=cv2.morphologyEx(bg.astype(np.uint8),cv2.MORPH_CLOSE,np.ones((3,3),np.uint8))>0
    lab,n=ndi.label(bg);sz=np.bincount(lab.ravel());sz[0]=0
    corners={lab[0,0],lab[0,-1],lab[-1,0],lab[-1,-1]}
    cand=[c for c in corners if c>0]
    seed=max(cand,key=lambda c:sz[c]) if cand else int(sz.argmax())
    outer=(lab==seed)
    near=cv2.dilate(outer.astype(np.uint8),np.ones((9,9),np.uint8))>0
    return outer|(bg&near), bg

def cut_one(key,label):
    im=Image.open(D+'/'+key+'.png').convert('RGB')
    a0=np.array(im); H,W=a0.shape[:2]
    # 四角采样背景色（纯品红）
    corners=np.concatenate([a0[:20,:20].reshape(-1,3),a0[:20,-20:].reshape(-1,3),
                            a0[-20:,:20].reshape(-1,3),a0[-20:,-20:].reshape(-1,3)])
    bgc=np.median(corners,axis=0).astype(np.uint8)
    # ---- 源头预清水印 ----
    outer0,_=outer_of(a0)
    fg0=(~outer0).astype(np.uint8)
    l0,n0=ndi.label(fg0); s0=np.bincount(l0.ravel()); s0[0]=0
    yy,xx=np.indices((H,W))
    a=a0.copy(); removed=0
    for k in range(1,n0+1):
        if s0[k]>=2000: continue           # 主体与大面积部件一律保留
        ys,xs=np.where(l0==k)
        if len(xs)==0: continue
        cx,cy=xs.mean(),ys.mean()          # 保持像素坐标，与 W*.72 同量纲
        if cx>W*.72 and cy>H*.78:          # 仅右下角水印区
            a[l0==k]=bgc; removed+=int(s0[k])
    # ---- 重新走完整色键抠图 ----
    outer,bg=outer_of(a)
    alpha=(~outer).astype(np.uint8)*255
    alpha=ndi.binary_fill_holes(alpha>128).astype(np.uint8)*255
    fg=(alpha>128).astype(np.uint8)
    l2,n2=ndi.label(fg); s2=np.bincount(l2.ravel()); s2[0]=0
    main=(l2==int(s2.argmax())); dropped=(fg>0)&(~main)
    roi=(xx>W*.72)&(yy>H*.78)
    alpha[(dropped&roi)]=0
    fg=(alpha>128).astype(np.uint8)
    resid=fg&bg
    if resid.sum():
        mask=(resid.astype(np.uint8)*255)
        a=cv2.cvtColor(cv2.inpaint(cv2.cvtColor(a,cv2.COLOR_RGB2BGR),mask,5,cv2.INPAINT_TELEA),cv2.COLOR_BGR2RGB)
    alpha=cv2.GaussianBlur(alpha,(3,3),0.55)
    rgba=np.dstack([a,alpha]).astype(np.uint8)
    ys,xs=np.where(alpha>128)
    x0,x1,y0,y1=int(xs.min()),int(xs.max()),int(ys.min()),int(ys.max())
    m=int(max(x1-x0,y1-y0)*.06)
    x0=max(0,x0-m);y0=max(0,y0-m);x1=min(W,x1+m);y1=min(H,y1+m)
    crop=Image.fromarray(rgba,'RGBA').crop((x0,y0,x1,y1))
    S=max(crop.size); sq=Image.new('RGBA',(S,S),(0,0,0,0))
    sq.paste(crop,((S-crop.width)//2,(S-crop.height)//2))
    sq.save(D+'/cut/'+key+'.png')
    small=sq.resize((512,512),Image.LANCZOS)
    buf=io.BytesIO(); small.save(buf,'WEBP',quality=74,method=6)
    emb='data:image/webp;base64,'+base64.b64encode(buf.getvalue()).decode()
    im.resize((720,720),Image.LANCZOS).save(D+'/'+key+'_720.jpg',quality=84)
    # ---- 质检 ----
    aa=np.array(sq)[:,:,3]; keep=aa>128
    holes=int((ndi.binary_fill_holes(keep)&(~keep)).sum())
    inv=~keep; il,ic=ndi.label(inv)
    ie=set(il[0,:].tolist())|set(il[-1,:].tolist())|set(il[:,0].tolist())|set(il[:,-1].tolist())
    holes=max(holes,sum(1 for k in range(1,ic+1) if k not in ie and int((il==k).sum())>20))
    ca=np.array(sq.convert('RGB')); cr,cg,cb=[ca[:,:,i].astype(np.float32) for i in range(3)]
    cbg=(cr>cg*1.35)&(cb>cg*1.08)&(cr>85)&(cg<150)&(cr>cb*0.95)
    resid_pct=float((cbg&keep).sum())/max(1,int(keep.sum()))*100
    # 成品连通域：主域=角色（含右下白脚），独立小岛=残留水印
    fl,fn=ndi.label(keep); fs=np.bincount(fl.ravel());fs[0]=0
    main=int(fs.argmax()); islands=int(((fs>20)&(fs<2000)).sum())
    hh,ww=keep.shape; ry,rx=np.indices((hh,ww))
    rroi=(rx>ww*.72)&(ry>hh*.78)
    lum=ca.mean(axis=2); neutral=(ca.max(axis=2)-ca.min(axis=2))<70
    # 只统计【非主域小岛】里的浅色像素，排除角色白脚造成的假警报
    wm_left=int(((lum>190)&neutral&keep&rroi&(fl!=main)&(fl>0)).sum())
    foot=int(((lum>190)&neutral&keep&rroi&(fl==main)).sum())
    return {'label':label,'holes':holes,'residual_pct':round(resid_pct,4),
            'fg_pct':round(float(keep.mean())*100,2),'cut':list(sq.size),
            'wm_pixels_removed':removed,'wm_left':wm_left,'islands':islands,
            'foot_pixels':foot},emb

QC,EMB,META={},{},{}
for key,label,ekey in JOBS:
    q,emb=cut_one(key,label)
    QC[key]=q; EMB[key]=emb; META[key]={'exprkey':ekey,'label':label}
    print('%-18s %-10s holes=%d resid=%.4f%% fg=%.1f%% | 预清=%d 右下残留=%d 小岛=%d'%(
        key,label,q['holes'],q['residual_pct'],q['fg_pct'],
        q['wm_pixels_removed'],q['wm_left'],q['islands']))

json.dump({'QC':QC,'META':META},open(D+'/_QC.json','w'),ensure_ascii=False,indent=1)
json.dump(EMB,open(D+'/_EMB.json','w'))

S=Image.new('RGB',(5*240,60+4*248),(250,247,240));d=ImageDraw.Draw(S)
d.text((14,12),'R51 v2  10 张真 AI 图生图 · 水印已源头清除（上两行宣纸底 · 下两行夜雨底）',font=f18,fill=(60,46,38))
for idx,(key,label,ekey) in enumerate(JOBS):
    cut=Image.open(D+'/cut/'+key+'.png').convert('RGBA').resize((200,200),Image.LANCZOS)
    for row,kd in enumerate(['paper','night']):
        col=(240,234,220) if kd=='paper' else (38,44,56)
        tile=Image.new('RGB',(240,248),col);tile.paste(cut,(20,10),cut)
        ImageDraw.Draw(tile).text((8,214),label,font=f14,
            fill=(70,58,48) if kd=='paper' else (232,226,214))
        S.paste(tile,((idx%5)*240,60+(row*2+idx//5)*248))
S.save(D+'/_R51_10张双底联系表.jpg',quality=88)
print('contact',os.path.getsize(D+'/_R51_10张双底联系表.jpg'))
