import re,io,base64,os
from PIL import Image, ImageSequence
SRC='杯雪游戏总站.html'; DST='杯雪游戏总站_轻量版.html'
h=open(SRC,encoding='utf-8').read()
if os.path.exists(DST): os.remove(DST)
pat=re.compile(r'"(data:image/(?:webp|png|jpeg|gif);base64,[^"]+)"')
cache={}; g={}; g["gif"]=0; g["sh"]=0
def enc_im(im):
    im=im.convert('RGBA'); w,hh=im.size
    if max(w,hh)>224:
        s=224/max(w,hh); im=im.resize((max(1,int(w*s)),max(1,int(hh*s))),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=46,method=4); return b.getvalue()
def enc_gif(raw):
    pass
    src=Image.open(io.BytesIO(raw))
    frames=[f.convert('RGBA').copy() for f in ImageSequence.Iterator(src)]
    if not frames: return raw
    w,hh=frames[0].size
    if max(w,hh)>224:
        s=224/max(w,hh); frames=[f.resize((max(1,int(w*s)),max(1,int(hh*s))),Image.LANCZOS) for f in frames]
    out=io.BytesIO()
    frames[0].save(out,'GIF',save_all=True,append_images=frames[1:],loop=src.info.get('loop',0),
                   duration=src.info.get('duration',120),disposal=2,transparency=0)
    g["gif"]+=1; return out.getvalue()
def rep(m):
    uri=m.group(1)
    if uri in cache: return '"'+cache[uri]+'"'
    raw=base64.b64decode(uri.split(',',1)[1])
    try:
        im=Image.open(io.BytesIO(raw)); fmt=im.format
    except Exception:
        cache[uri]=uri; return '"'+uri+'"'
    if fmt=='GIF':
        new=enc_gif(raw)
    else:
        new=enc_im(im); g["sh"]+=1
    nu='data:image/webp;base64,'+base64.b64encode(new).decode() if fmt!='GIF' else 'data:image/gif;base64,'+base64.b64encode(new).decode()
    cache[uri]=nu; return '"'+nu+'"'
out=pat.sub(rep,h)
# strip HTML comments + indentation whitespace in the static markup (keep <pre>/<textarea> content untouched)
out=re.sub(r'<!--.*?-->','',out,flags=re.S)
open(DST,'w',encoding='utf-8').write(out)
print("gif kept",g["gif"],"webp shrunk",g["sh"],'unique',len(cache))
print('src MB',round(len(h)/1048576,2),'dst MB',round(len(out)/1048576,2))
