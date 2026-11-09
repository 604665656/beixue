import json, re
from playwright.sync_api import sync_playwright

src = open('/data/workspace/44_表情管理/R55_自检.py', encoding='utf-8').read()
js = src.split('JS = r"""')[1].split('"""')[0]
js = js.replace("  const sw=", "  const __D={}; window.__DBG=__D; const sw=", 1)
js = js.replace("  EXPR_APPLY=0;\n",
                "  EXPR_APPLY=0;\n  Object.assign(__D,{footAll,footOwn,csvName,csvGen,head,domOK,voiceOK,hit,miss,nameBad,cross,badArt,zeroRoles,imgBad,r55e?(r55e.art+"|"+r55e.name+"|"+r55e.src):"null","
                "gifVar:(getComputedStyle(document.documentElement).getPropertyValue('--catAnimGif')||'').length});\n", 1)
js = js.replace("return {sw,iw,", "return {dbg:__D,sw,iw,", 1)

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/local/bin/chromium', args=['--no-sandbox', '--disable-gpu'])
    for f in ['杯雪游戏总站.html', '杯雪游戏总站_轻量版.html']:
        pg = b.new_page(viewport={'width': 420, 'height': 900})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('file:///data/workspace/' + f, wait_until='load', timeout=120000)
        pg.wait_for_timeout(900)
        try:
            r = pg.evaluate(js)
            d = {k: v for k, v in r['dbg'].items() if k not in ('miss', 'nameBad')}
            print(f, json.dumps(d, ensure_ascii=False)[:900])
            print('  footAll:', r['dbg']['footAll'][:160])
            print('  footOwn:', r['dbg']['footOwn'][:200])
        except Exception as e:
            print(f, 'EVAL ERR', str(e)[:200])
        print('  errs', errs[:3])
        pg.close()
    b.close()
