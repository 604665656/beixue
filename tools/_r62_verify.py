from playwright.sync_api import sync_playwright
import json
PROBE="""()=>{const o={};
 o.err=window.__ERRS__||[];
 o.expr=typeof EXPR!=='undefined'?EXPR.length:null;
 o.st=typeof exprStat!=='undefined'?exprStat():null;
 o.cross=typeof exprCrossCount!=='undefined'?exprCrossCount():null;
 o.art=typeof ART!=='undefined'?Object.keys(ART).length:null;
 o.r62=typeof EXPR_SPECIAL!=='undefined'?Object.keys(EXPR_SPECIAL).filter(k=>k.indexOf('R62')>=0).length:null;
 o.mood=(typeof exprMoodFor!=='undefined')?[0,1,2,3,4,5,6,7].map(i=>exprMoodFor('A'+i)):null;
 o.scroll=document.documentElement.scrollWidth-innerWidth;
 o.audio=(window.AUDIO_CREATED||0);
 o.imgs=(()=>{let bad=0,n=0;for(const k in ART){n++;const u=ART[k];if(!u||u.indexOf('data:image/')!==0)bad++;}return n+'/'+bad;})();
 // real <img> decode check
 o.domImg=(()=>{const im=[...document.querySelectorAll('img')];return im.length+'/'+im.filter(x=>x.complete&&x.naturalWidth>0).length;})();
 return o;}"""
files=['杯雪游戏总站.html','杯雪游戏总站_轻量版.html']
sizes=[(420,900,'竖屏'),(900,420,'横屏'),(1440,900,'桌面')]
res=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/local/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
    for f in files:
        for w,h,tag in sizes:
            errs=[]
            pg=b.new_page(viewport={'width':w,'height':h})
            pg.on('pageerror',lambda e:errs.append('PAGEERROR: '+str(e)[:160]))
            pg.on('console',lambda m: errs.append('CONSOLE: '+m.text[:160]) if m.type=='error' else None)
            pg.goto('file:///data/workspace/'+f); pg.wait_for_timeout(4500)
            r=pg.evaluate(PROBE); r['file']=f; r['vp']=tag; r['errs']=errs
            res.append(r)
            print(f[-14:],tag,'expr',r['expr'],r['st'],'R62',r['r62'],'cross',r['cross'],'scroll',r['scroll'],'img',r['imgs'],'dom',r['domImg'],'ERR',len(errs))
            for e in errs[:4]:print('   ',e)
            pg.close()
    b.close()
json.dump(res,open('anim62/_verify.json','w'),ensure_ascii=False,indent=1)
bad=[r for r in res if r['errs'] or r['scroll']>0 or r['expr']!=192 or r['cross']!=0]
print('FAIL GROUPS',len(bad))
