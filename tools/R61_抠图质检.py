# -*- coding: utf-8 -*-
"""R61：沿用 R54 的「源头预清 → 完整色键抠图 → 碎块清理」管线。
   本轮 AI 图底色仍为纯品红，故 v2 管线直接可用；无新增特例。"""
import numpy as np, cv2, scipy.ndimage as ndi, json, base64, io, os, sys
from PIL import Image, ImageDraw, ImageFont

D='/data/workspace/anim61'
FP='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
f18=ImageFont.truetype(FP,18); f14=ImageFont.truetype(FP,14)

JOBS=[
 ('R61_base_ai',    '哈士喵·哀',   'cos_base|哀'),
 ('R61_base_jing',  '哈士喵·惊',   'cos_base|惊'),
 ('R61_base_yi',    '哈士喵·疑',   'cos_base|疑'),
 ('R61_base_zui',   '哈士喵·醉',   'cos_base|醉'),
 ('R61_geng_jing',  '耿苍怀·惊',   'cos_geng|惊'),
 ('R61_geng_zui',   '耿苍怀·醉',   'cos_geng|醉'),
 ('R61_jinhe_ai',   '金和尚·哀',   'cos_jinhe|哀'),
 ('R61_jinhe_jing', '金和尚·惊',   'cos_jinhe|惊'),
 ('R61_qinwen_nu',  '秦稳·怒',     'cos_qinwen|怒'),
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
    im=Image.open(D+'/raw/'+key+'.png').convert('RGB')
    a0=np.array(im); H,W=a0.shape[:2]
    corners=np.concatenate([a0[:20,:20].reshape(-1,3),a0[:20,-20:].reshape(-1,3),
                            a0[-20:,:20].reshape(-1,3),a0[-20:,-20:].reshape(-1,3)])
    bgc=np.median(corners,axis=0).astype(np.uint8)
    outer0,_=outer_of(a0)
    fg0=(~outer0).astype(np.uint8)
    l0,n0=ndi.label(fg0); s0=np.bincount(l0.ravel()); s0[0]=0
    yy,xx=np.indices((H,W))
    a=a0.copy(); removed=0
    for k in range(1,n0+1):
        if s0[k]>=2000: continue
        ys,xs=np.where(l0==k)
        if len(xs)==0: continue
        cx,cy=xs.mean(),ys.mean()
        if cx>W*.72 and cy>H*.78:
            a[l0==k]=bgc; removed+=int(s0[k])
    outer,bg=outer_of(a)
    alpha=(~outer).astype(np.uint8)*255
    alpha=ndi.binary_fill_holes(alpha>128).astype(np.uint8)*255
    fg=(alpha>128).astype(np.uint8)
    l2,n2=ndi.label(fg); s2=np.bincount(l2.ravel()); s2[0]=0
    main=(l2==int(s2.argmax())); dropped=(fg>0)&(~main)
    roi=(xx>W*.72)&(yy>H*.78)
    alpha[(dropped&roi)]=0
    fg=(alpha>128).astype(np.uint8)
    fl0,fn0=ndi.label(fg); fs0=np.bincount(fl0.ravel()); fs0[0]=0
    main0=int(fs0.argmax())
    tiny=(fl0!=main0)&(fl0>0)&(fs0[fl0]<500)
    alpha[tiny]=0
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
    aa=np.array(sq)[:,:,3]; keep=aa>128
    holes=int((ndi.binary_fill_holes(keep)&(~keep)).sum())
    inv=~keep; il,ic=ndi.label(inv)
    ie=set(il[0,:].tolist())|set(il[-1,:].tolist())|set(il[:,0].tolist())|set(il[:,-1].tolist())
    holes=max(holes,sum(1 for k in range(1,ic+1) if k not in ie and int((il==k).sum())>20))
    ca=np.array(sq.convert('RGB')); cr,cg,cb=[ca[:,:,i].astype(np.float32) for i in range(3)]
    cbg=(cr>cg*1.35)&(cb>cg*1.08)&(cr>85)&(cg<150)&(cr>cb*0.95)
    resid_pct=float((cbg&keep).sum())/max(1,int(keep.sum()))*100
    fl,fn=ndi.label(keep); fs=np.bincount(fl.ravel());fs[0]=0
    main=int(fs.argmax()); islands=int(((fs>20)&(fs<2000)).sum())
    hh,ww=keep.shape; ry,rx=np.indices((hh,ww))
    rroi=(rx>ww*.72)&(ry>hh*.78)
    lum=ca.mean(axis=2); neutral=(ca.max(axis=2)-ca.min(axis=2))<70
    wm_left=int(((lum>190)&neutral&keep&rroi&(fl!=main)&(fl>0)).sum())
    # 画风指标：色温(暖冷)、暗线占比、灰调占比、鲜色占比、轮廓密度
    px=ca.reshape(-1,3).astype(np.float32)
    warm=float((px[:,0]-px[:,2]).mean())
    dark=float((px.max(axis=1)<90).mean()*100)
    gray=float(((px.max(axis=1)-px.min(axis=1))<28).mean()*100)
    vivid=float(((px.max(axis=1)-px.min(axis=1))>90).mean()*100)
    edge=float(cv2.Canny(cv2.cvtColor(ca,cv2.COLOR_RGB2GRAY),60,140).mean()/255*100)
    return {'label':label,'exprkey':key[4:] and (JOBS[[j[0] for j in JOBS].index(key)][2]) if False else None,
            'holes':holes,'residual_pct':round(resid_pct,4),
            'fg_pct':round(float(keep.mean())*100,2),'cut':list(sq.size),
            'wm_pixels_removed':removed,'wm_left':wm_left,'islands':islands,
            'warm':round(warm,2),'dark':round(dark,2),'gray':round(gray,2),
            'vivid':round(vivid,2),'edge':round(edge,2)},emb

QC,EMB,META={},{},{}
for key,label,ekey in JOBS:
    q,emb=cut_one(key,label)
    q['exprkey']=ekey
    QC[key]=q; EMB[key]=emb; META[key]={'exprkey':ekey,'label':label}
    print('%-18s %-12s holes=%d resid=%.4f%% fg=%.1f%% | 预清=%d 右下残留=%d 小岛=%d | 暖冷=%+.1f 暗线=%.1f%% 灰=%.1f%% 鲜=%.1f%% 边缘=%.1f%%'%(
        key,label,q['holes'],q['residual_pct'],q['fg_pct'],
        q['wm_pixels_removed'],q['wm_left'],q['islands'],
        q['warm'],q['dark'],q['gray'],q['vivid'],q['edge']))

json.dump({'QC':QC,'META':META},open(D+'/_QC.json','w'),ensure_ascii=False,indent=1)
json.dump(EMB,open(D+'/_EMB.json','w'))

cols=3; rows=(len(JOBS)+cols-1)//cols
S=Image.new('RGB',(cols*300,50+rows*310),(250,247,240));d=ImageDraw.Draw(S)
d.text((14,14),'R61  9 张 AI 图生图（上排宣纸底 / 下排夜雨底）· 水印源头已清',font=f18,fill=(60,46,38))
for idx,(key,label,ekey) in enumerate(JOBS):
    cut=Image.open(D+'/cut/'+key+'.png').convert('RGBA').resize((260,260),Image.LANCZOS)
    cx,cy=(idx%cols)*300,(idx//cols)*310+50
    for row,kd in enumerate(['paper','night']):
        col=(240,234,220) if kd=='paper' else (38,44,56)
        tile=Image.new('RGB',(300,310),col);tile.paste(cut,(20,10),cut)
        ImageDraw.Draw(tile).text((10,276),label+( '' if kd=='paper' else ' · 夜雨'),font=f14,
            fill=(70,58,48) if kd=='paper' else (232,226,214))
        S.paste(tile,(cx,cy+row*0 if False else cx*0+cx and cx))
S.save(D+'/_R61_双底联系表.jpg',quality=88)
print('contact',os.path.getsize(D+'/_R61_双底联系表.jpg'))
