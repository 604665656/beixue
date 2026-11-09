import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--disable-gpu'])
        pg = await (await b.new_context(viewport={'width':420,'height':900})).new_page()
        errs=[]
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: errs.append('CONSOLE:'+m.text) if m.type=='error' else None)
        await pg.goto('file:///data/workspace/杯雪游戏总站.html')
        await pg.wait_for_timeout(2500)
        r = await pg.evaluate("""() => {
          const o={};
          o.EXPR = typeof EXPR!=='undefined'?EXPR.length:'UNDEF';
          o.ART = typeof ART!=='undefined'?Object.keys(ART).length:'UNDEF';
          o.DATA = typeof DATA!=='undefined'?Object.keys(DATA).length:'UNDEF';
          o.EXPR_SPECIAL = (typeof EXPR_SPECIAL!=='undefined')? (EXPR_SPECIAL.size||EXPR_SPECIAL.length) : 'UNDEF';
          o.PROC = (typeof PROC_ART!=='undefined')? (PROC_ART.size||PROC_ART.length):'UNDEF';
          o.exprApply = typeof EXPR_APPLY;
          o.bodyLen = document.body.innerHTML.length;
          o.cards = document.querySelectorAll('.card,.lv,button').length;
          return o; }""")
        print('RESULT', r)
        print('ERRS', len(errs))
        for e in errs[:12]: print('  !', e[:300])
        await b.close()
asyncio.run(main())
