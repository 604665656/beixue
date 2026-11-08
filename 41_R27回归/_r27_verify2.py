# -*- coding: utf-8 -*-
"""R27 补充回归：损坏键检出、view 复位、perf 命令、24 关配图可渲染。"""
import json
from playwright.sync_api import sync_playwright
URL = 'file:///data/workspace/杯雪游戏总站.html'
out = {}
with sync_playwright() as p:
    br = p.chromium.launch(headless=True, executable_path='/usr/bin/google-chrome',
                           args=['--no-sandbox', '--disable-web-security', '--allow-file-access-from-files'])
    ctx = br.new_context(viewport={'width': 420, 'height': 900})
    pg = ctx.new_page()
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL, wait_until='load')
    pg.wait_for_timeout(900)

    out['badKeyDetect'] = pg.evaluate("""()=>{
      localStorage.setItem('beixue_spr_v1','{broken');
      const c=storeCheck();
      localStorage.removeItem('beixue_spr_v1');
      return {scanned:c.scanned,bad:c.bad,ok:c.ok};}""")

    out['viewReset'] = pg.evaluate("""()=>{
      STORE_NS.view.forEach(k=>localStorage.setItem(k,'{"x":1}'));
      const before=STORE_NS.view.filter(k=>localStorage.getItem(k)!==null).length;
      const n=storeResetView();
      const after=STORE_NS.view.filter(k=>localStorage.getItem(k)!==null).length;
      return {before:before,removed:n,after:after};}""")

    out['perfLog'] = pg.evaluate("""()=>new Promise(res=>{
      setTab('J');render();
      const n0=stageLogSummary().total;
      try{queuePerf(0)}catch(e){return res('queuePerf ERR:'+e)}
      setTimeout(()=>{const s=stageLogSummary();
        res({before:n0,after:s.total,types:s.types,last:s.last});},700);
    })""")

    out['allLevels'] = pg.evaluate("""()=>{
      const ids=D.meta.levels.map(l=>l.id);
      const bad=[];
      for(const k of ids){
        try{const s=stageFor(k);if(!s||!ART[s.cast])bad.push(k+':'+JSON.stringify(s));}
        catch(e){bad.push(k+':ERR '+e)}
      }
      return {count:ids.length,bad:bad};}""")

    out['archivePages'] = pg.evaluate(
        "()=>({keys:Object.keys(D.archive||{}).length,animLen:(D.archive.anim||'').length})")
    out['pageerrors'] = errs[:10]
    br.close()
print(json.dumps(out, ensure_ascii=False, indent=2))
open('/data/workspace/_r27_verify2.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=2))
