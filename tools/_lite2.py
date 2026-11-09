import re,base64,io,json,os
from PIL import Image
SRC='/data/workspace/杯雪游戏总站.html'; DST='/data/workspace/杯雪游戏总站_轻量版.html'
s=open(SRC,encoding='utf-8').read(); ob=os.path.getsize(SRC)
URI=re.compile(r'data:image/(?:webp|gif);base64,[A-Za-z0-9+/=]+')
cache={}; st={'w':0,'g':0,'b':0,'a':0}
def shr(u):
    if u in cache: return cache[u]
    st['b']+=len(u)
    if u.startswith('data:image/gif'):
        cache[u]=u; st['g']+=1; return u
    try:
        im=Image.open(io.BytesIO(base64.b64decode(u.split(',',1)[1]))).convert('RGBA')
    except Exception:
        cache[u]=u; return u
    if max(im.size)>224:
        k=224/max(im.size); im=im.resize((max(1,round(im.width*k)),max(1,round(im.height*k))),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=40,method=4)
    out='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode(); st['w']+=1; st['a']+=len(out)
    cache[u]=out; return out
s=URI.sub(lambda m:shr(m.group(0)),s)
m=re.search(r'(<script type="application/json" id="DATA">)([\s\S]*?)(</script>)',s)
if m:
    try:
        c=json.dumps(json.loads(m.group(2)),ensure_ascii=False,separators=(',',':'))
        s=s[:m.start(2)]+c+s[m.end(2):]; dj=[len(m.group(2)),len(c)]
    except Exception as e: dj='SKIP '+repr(e)
s=re.sub(r'<title>(.*?)</title>',lambda mm:'<title>'+mm.group(1)+' · 轻量版</title>',s,count=1)
s=s.replace('<html','<!-- 杯雪轻量版：内嵌 WebP 224px/q40，逐帧 GIF 原样保留，无外置依赖 -->\n<html',1)
open(DST,'w',encoding='utf-8').write(s)
nb=os.path.getsize(DST)
print('webp',st['w'],'gif保留',st['g'],'唯一',len(cache),'b64 %.2f→%.2fMB'%(st['b']/1048576,st['a']/1048576),'DATA',dj)
print('%.2f→%.2f MB -%.1f%%'%(ob/1048576,nb/1048576,100*(1-nb/ob)),'外链',s.count('<script src='),s.count('href="http'),s.count('url(http'),'尾',s.rstrip().endswith('</html>'))
