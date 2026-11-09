import asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--disable-gpu'])
        out={}
        for name,vp in [('竖屏',{'width':420,'height':900}),('横屏',{'width':900,'height':420}),('桌面',{'width':1440,'height':900})]:
            ctx=await b.new_context(viewport=vp); pg=await ctx.new_page(); errs=[]
            pg.on('pageerror',lambda e:errs.append(str(e)))
            pg.on('console',lambda m: errs.append('C:'+m.text) if m.type=='error' else None)
            await pg.goto('file:///data/workspace/杯雪游戏总站.html'); await pg.wait_for_timeout(1500)
            r=await pg.evaluate("""()=>{const o={};
             o.special=Object.keys(EXPR_SPECIAL).length;o.art=Object.keys(ART).length;
             o.stat=exprStat();o.cross=exprCrossCount();
             o.r61=Object.entries(EXPR_SPECIAL).filter(([k,v])=>v.startsWith('R61')).map(([k,v])=>k+'='+(ART[v]?'ok':'MISSING'))
              .map(k=>k+'='+EXPR.find(e=>e.cast+'|'+e.mood===k).art+'/'+(ART[EXPR.find(e=>e.cast+'|'+e.mood===k).art]?'ok':'MISSING'));
             const miss={};EXPR_CASTS.forEach(([c,n])=>{const m=EXPR_MOODS.filter(m=>!EXPR.find(e=>e.cast===c&&e.mood===m));if(m.length)miss[n]=m;});o.missing=miss;
             let bad=[];Object.keys(DATA).forEach(k=>{const st=stageFor(k);const r=exprResolve(exprCanon(st&&st.cast||'cos_base'),exprMoodFor(k),k);if(!r||!ART[r.art])bad.push(k);});o.stageBad=bad.length;
             o.overflow=document.documentElement.scrollWidth-window.innerWidth;
             o.btns=document.querySelectorAll('button').length;
             return o;}""")
            r['errs']=errs[:5]; out[name]=r; await ctx.close()
        print(json.dumps(out,ensure_ascii=False,indent=1)); await b.close()
asyncio.run(main())
