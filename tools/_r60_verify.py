import asyncio, json
from playwright.async_api import async_playwright
URL='file:///data/workspace/杯雪游戏总站_轻量版.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--disable-gpu'])
        out={}
        for name,vp in [('竖屏',{'width':420,'height':900}),('横屏',{'width':900,'height':420}),('桌面',{'width':1440,'height':900})]:
            ctx=await b.new_context(viewport=vp)
            pg=await ctx.new_page(); errs=[]
            pg.on('pageerror',lambda e:errs.append(str(e)))
            pg.on('console',lambda m: errs.append('CONSOLE:'+m.text) if m.type=='error' else None)
            await pg.goto(URL); await pg.wait_for_timeout(1800)
            r=await pg.evaluate("""() => {
              const o={};
              try{o.EXPR=EXPR.length;}catch(e){o.EXPR='UNDEF';}
              try{o.ART=Object.keys(ART).length;}catch(e){o.ART='UNDEF';}
              try{o.SPECIAL=Object.keys(EXPR_SPECIAL).length;}catch(e){o.SPECIAL='UNDEF';}
              try{o.PROC=PROC_ART.size;}catch(e){o.PROC='UNDEF';}
              try{o.DATA=Object.keys(DATA).length;}catch(e){o.DATA='UNDEF';}
              o.audio = (window.__AUD!==undefined)?window.__AUD:(document.querySelectorAll('audio').length);
              o.bodyLen = document.body.innerHTML.length;
              o.btns = document.querySelectorAll('#app button, .card, .lv').length;
              o.overflowX = document.documentElement.scrollWidth - window.innerWidth;
              // 表情解析自检
              try{
                const keys=Object.keys(DATA); let miss=[];
                const moods=['静息','喜','怒','哀','惊','疑','决','醉'];
                keys.forEach(k=>{ const st=(DATA[k]&&DATA[k].A)?null:null; });
                o.resolveOK = (typeof exprResolve==='function');
                if(o.resolveOK){
                  let bad=0, got=new Set();
                  ['cos_base','cos_luo','cos_jin','cos_yi','cos_zhu'].forEach(c=>{
                    moods.forEach(m=>{ const r=exprResolve(c,m,k); if(!r||!r.art||!ART[r.art]) bad++; else got.add(r.art); });
                  });
                  o.resolveBad=bad; o.resolveDistinct=got.size;
                }
              }catch(e){ o.resolveErr=String(e).slice(0,120); }
              // 24 关接管是否都能取到层
              try{
                let bad=[],casts=new Set();
                Object.keys(DATA).forEach(k=>{
                  const st=(typeof stageFor==='function')?stageFor(k):null; if(!st){bad.push(k+':nostate');return;}
                  const c=exprCanon?exprCanon(st.cast||'cos_base'):'cos_base'; casts.add(c);
                  const r=exprResolve(c,exprMoodFor?exprMoodFor(k):'静息',k);
                  if(!r||!r.art||!ART[r.art]) bad.push(k+':'+c);
                });
                o.stageBadCount=bad.length; o.stageBad=bad.slice(0,6); o.castCount=casts.size;
              }catch(e){ o.stageErr=String(e).slice(0,160); }
              return o; }""")
            r['jsErrors']=errs.length if False else len(errs)
            r['errSample']=errs[:5]
            out[name]=r
            await ctx.close()
        print(json.dumps(out,ensure_ascii=False,indent=1))
        await b.close()
asyncio.run(main())
