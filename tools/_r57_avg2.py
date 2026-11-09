import asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':420,'height':900})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///data/workspace/杯雪游戏总站.html',wait_until='load',timeout=120000)
        await pg.wait_for_timeout(2500)
        await pg.evaluate("""()=>{const b=[...document.querySelectorAll('[data-act="go"]')].find(x=>(x.dataset.v||'')==='A'); b&&b.click();}""")
        await pg.wait_for_timeout(1500)
        # 过模式选择
        for lbl in ['进店，坐下','新手模式','◈ 新手模式']:
            try:
                el=await pg.query_selector(f"#app button:has-text('{lbl}')")
                if el: await el.click(); await pg.wait_for_timeout(700); break
            except Exception as e: pass
        await pg.wait_for_timeout(900)
        print("APP首幕:", (await pg.evaluate("()=>(document.querySelector('#app')||{innerText:''}).innerText"))[0:500].replace('\n','|'))
        # 点第一个选项（真实鼠标点击）
        btns=await pg.query_selector_all('#app .opt')
        print("opts:",len(btns))
        if btns:
            await btns[0].click()
            await pg.wait_for_timeout(1000)
            print("APP点后:", (await pg.evaluate("()=>(document.querySelector('#app')||{innerText:''}).innerText"))[0:600].replace('\n','|'))
            print("PERF:",json.dumps(await pg.evaluate("""()=>({
              sub:((document.querySelector('#app .avgwho .avgsub')||{}).textContent||''),
              who:((document.querySelector('#app .avgwho b')||{}).textContent||''),
              icon:((document.querySelector('#app .perficon')||{}).className||''),
              node:(window.S&&window.S.A)?S.A.node:null})"""),ensure_ascii=False))
        print("errs",errs[:3])
        await b.close()
asyncio.run(main())
