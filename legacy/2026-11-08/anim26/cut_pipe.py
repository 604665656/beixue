from PIL import Image
import numpy as np, cv2, sys, os
from scipy import ndimage as ndi

def cut(src, outprefix, size=1024):
    im=Image.open(src).convert('RGB'); a=np.array(im); H,W=a.shape[:2]
    r,g,b=[a[:,:,i].astype(np.float32) for i in range(3)]
    # ① 色相键控：品红/玫红/紫红系，按相对色相容纳渐变暗玫红
    bg=(r>g*1.35)&(b>g*1.08)&(r>85)&(g<150)&(r>b*0.95)
    bg=cv2.morphologyEx(bg.astype(np.uint8),cv2.MORPH_CLOSE,np.ones((3,3),np.uint8))>0
    # ② 与四角连通的最大外部背景
    lab,n=ndi.label(bg)
    corners={lab[0,0],lab[0,-1],lab[-1,0],lab[-1,-1]}
    sizes=np.bincount(lab.ravel()); sizes[0]=0
    cand=[c for c in corners if c>0]
    seed=max(cand,key=lambda c:sizes[c]) if cand else sizes.argmax()
    outer=(lab==seed)
    near=cv2.dilate(outer.astype(np.uint8),np.ones((9,9),np.uint8))>0
    outer=outer|(bg&near)
    alpha=(~outer).astype(np.uint8)*255
    # ③ 填实内部孔洞
    alpha=ndi.binary_fill_holes(alpha>128).astype(np.uint8)*255
    # ④ 清右下角水印：只保留连通域里的主体（最大分量），丢弃独立小岛
    fg=(alpha>128).astype(np.uint8)
    l2,n2=ndi.label(fg)
    s2=np.bincount(l2.ravel()); s2[0]=0
    main=(l2==s2.argmax())
    dropped=(fg>0)&(~main)
    # 仅清理右下角区域的小岛，避免误删镜片高光等主体内部细节
    yy,xx=np.indices((H,W))
    roi=(xx>W*.72)&(yy>H*.78)
    alpha[(dropped&roi)]=0
    fg=(alpha>128).astype(np.uint8)
    # ⑤ 去色溢
    resid=(fg&bg)
    if resid.sum():
        mask=(resid.astype(np.uint8)*255)
        a=cv2.cvtColor(cv2.inpaint(cv2.cvtColor(a,cv2.COLOR_RGB2BGR),mask,5,cv2.INPAINT_TELEA),cv2.COLOR_BGR2RGB)
    alpha=cv2.GaussianBlur(alpha,(3,3),0.55)
    rgba=np.dstack([a,alpha]).astype(np.uint8)
    # 居中裁到角色包围盒外留 6% 边，再等比缩到 size
    ys,xs=np.where(alpha>128)
    x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max()
    m=int(max(x1-x0,y1-y0)*.06)
    x0=max(0,x0-m);y0=max(0,y0-m);x1=min(W,x1+m);y1=min(H,y1+m)
    crop=Image.fromarray(rgba,'RGBA').crop((x0,y0,x1,y1))
    S=max(crop.size); sq=Image.new('RGBA',(S,S),(0,0,0,0))
    sq.paste(crop,((S-crop.width)//2,(S-crop.height)//2))
    sq=sq.resize((size,size),Image.LANCZOS)
    sq.save('cut/'+outprefix+'.png')
    sq.save('cut/'+outprefix+'.webp','WEBP',quality=80)
    aa=np.array(sq)[:,:,3]
    holes=(ndi.binary_fill_holes(aa>128)&(aa<=128)).sum()
    rb=(aa>128)&bg if False else None
    print('%s → 孔洞 %d | 前景 %.1f%% | 成品 %dx%d'%(outprefix,holes,(aa>128).mean()*100,size,size))
    return sq

if __name__=='__main__':
    cut(sys.argv[1],sys.argv[2])
