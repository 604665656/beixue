import asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':420,'height':900})
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///data/workspace/杯雪游戏总站.html',wait_until='load',timeout=120000)
        await pg.wait_for_timeout(3000)
        # 进 A 关
        r=await pg.evaluate("""()=>{
          const out={};
          try{ const b=[...document.querySelectorAll('[data-act="go"]')].find(x=>(x.dataset.v||'')==='A');
               if(b){b.click(); out.clicked='A';} else { out.clicked='NOTFOUND'; out.vs=[...document.querySelectorAll('[data-act=go]')].map(x=>x.dataset.v).slice(0,12);} }catch(e){ out.GOerr=e.message; }
          return out;}""")
        await pg.wait_for_timeout(1200)
        s1=await pg.evaluate("""()=>{
          const o={};
          const sc=document.querySelector('#app .stagecut');
          o.bg = sc? (sc.style.backgroundImage||'').slice(0,60):null;
          o.who = (document.querySelector('#app .stagewho')||{}).textContent||null;
          o.avgwho = (document.querySelector('#app .avgwho b')||{}).textContent||null;
          o.avgsub = (document.querySelector('#app .avgwho .avgsub')||{}).textContent||null;
          o.stage = (()=>{try{return JSON.stringify(stageFor('A'));}catch(e){return 'ERR '+e.message;}})();
          o.node = (typeof S!=='undefined'&&S.A)?S.A.node:null;
          o.actortxt = (document.querySelector('#app .actor')||{}).textContent||null;
          o.quotetxt = (document.querySelector('#app .quote')||{}).textContent||null;
          return o;}""")
        print("A关首幕:",json.dumps(s1,ensure_ascii=False))
        # 点第一个选项，看 queuePerf 后 who
        await pg.evaluate("""()=>{const b=document.querySelector('#app .opt'); if(b)b.click();}""")
        await pg.wait_for_timeout(900)
        s2=await pg.evaluate("""()=>({
           who:(document.querySelector('#app .avgwho b')||{}).textContent||null,
           sub:(document.querySelector('#app .avgwho .avgsub')||{}).textContent||null,
           bgimg:((document.querySelector('#app .stagecut')||{style:{}}).style.backgroundImage||'').slice(0,70),
           node:(typeof S!=='undefined'&&S.A)?S.A.node:null})""")
        print("点选项后:",json.dumps(s2,ensure_ascii=False))
        print("errs",errs[:3])
        await b.close()
asyncio.run(main())
