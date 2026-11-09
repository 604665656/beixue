# -*- coding: utf-8 -*-
"""R46 自检：3 个真 bug 已修 / 36 专属 / 表情不再恒定 / 表演真换人 / 三尺寸浏览器。"""
import json, re, os, subprocess, tempfile
from playwright.sync_api import sync_playwright

P = '/data/workspace/杯雪游戏总站.html'
OUT = '/data/workspace/44_表情管理/R46_自检结果.json'
s = open(P, encoding='utf-8').read()
R = {'checks': [], 'browser': [], 'errors': []}


def ck(name, cond, detail=''):
    R['checks'].append({'name': name, 'ok': bool(cond), 'detail': str(detail)})
    if not cond:
        R['errors'].append(name + ' :: ' + str(detail))


scripts = re.findall(r'<script(?![^>]*application/json)[^>]*>([\s\S]*?)</script>', s)
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
    f.write('\n;\n'.join(scripts)); jsp = f.name
r = subprocess.run(['node', '--check', jsp], capture_output=True, text=True)
ck('node --check 内联 JS', r.returncode == 0, (r.stderr or '')[:300])
os.unlink(jsp)

D = json.loads(re.search(r'<script type="application/json" id="DATA">([\s\S]*?)</script>', s).group(1))
ck('DATA JSON.parse · 24 关', len(D['meta']['levels']) == 24)
ck('运行时不创建 Audio', 'new Audio(' not in s)
ck('无内嵌音频 URI', not re.search(r'data:audio/(wav|mp4|ogg|mpeg|aac|m4a)', s))
ck('内置包置空', 'const BUILTIN_VOICE_PACK=null;' in s)
ck('R46 10 张键注入', all(('"R46_%s"' % k) in s for k in
    ['base_jue','base_zui','luo_jing','jin_jing','yi_jue','yi_zui','zhu_jue','xiao_nu','xiao_ai','qin_zui']))
sp = json.loads(s[s.index('const EXPR_SPECIAL=') + len('const EXPR_SPECIAL='):s.index(';', s.index('const EXPR_SPECIAL='))])
ck('EXPR_SPECIAL 36 项', len(sp) == 36, len(sp))
ck('bug① 已修：关卡偏移+当前幕', 'let off=0; const id=String(k||' in s and "i%8" not in s[s.index('function exprMoodFor'):s.index('function exprMoodFor')+700])
ck('bug② 已修：queuePerf 走 exprCanon', 'const root=k=>{ try{ return exprCanon(k); }' in s)
ck('bug③ 已修：面板不截断', 'const cards=list.map(e=>{' in s and 'list.slice(0,120)' not in s)
css = re.sub(r'/\*[\s\S]*?\*/', '', '\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', s)))
ck('CSS 规则区无拼接动画', 'step-end' not in css and 'steps(1,end)' not in css)

JS = r"""async () => {
  const sw=document.documentElement.scrollWidth, iw=innerWidth;
  const badPool=Object.entries(ROLE_POOL).filter(([c,v])=>!v.length).map(x=>x[0]);
  const dirty=Object.entries(ROLE_POOL).flatMap(([c,v])=>v.filter(k=>/^(bg_|fx_|cover$|cat\d|catorg|catav|cat3|[A-Z]$)/i.test(k)));
  const badArt=EXPR.filter(e=>!ART[e.art]).map(e=>e.cast+'|'+e.mood+'->'+e.art);
  const cross=EXPR.filter(e=>e.src==='复用' && !(ROLE_POOL[e.cast]||[]).includes(e.art)).map(e=>e.cast+'|'+e.mood+'->'+e.art);
  const metaBad=EXPR.filter(e=>!(CAST_META[e.art]||[])[0]||!CAST.some(x=>x[0]===e.art)).length;

  /* bug① 验证：24 关起始表情分布；单关随幕推进覆盖 8 种 */
  const moodOf=lv=>exprMoodFor(lv);
  const moodSet={}; D.meta.levels.forEach(l=>{const m=moodOf(l.id);moodSet[m]=(moodSet[m]||0)+1;});
  const saved=S.G?S.G.i:0; const seq=[];
  for(let m=0;m<8;m++){ if(S.G)S.G.i=m; seq.push(exprMoodFor('G')); }
  if(S.G)S.G.i=saved;
  const seqN=new Set(seq).size;

  let hit=0, layerHit=0, nameBad=[], miss=[];
  EXPR_APPLY=1;
  for(const lv of D.meta.levels.map(l=>l.id)){
    try{ const st=stageFor(lv); const r=exprResolve(st.cast||'cos_base',exprMoodFor(lv),lv);
      if(r&&r.cast===exprCanon(st.cast||'cos_base')&&ART[r.art])hit++; else miss.push(lv+':'+(st.cast||''));
      if(EXPR.some(e=>e.art===st.cast))layerHit++;
      const nm=(castMeta(st.cast)||[])[0]||'';
      if(nm==='哈士喵'&&st.cast!=='cos_base'&&!String(st.cast).startsWith('R45_base')&&!String(st.cast).startsWith('R46_base'))nameBad.push(lv+':'+st.cast+'->'+nm);
    }catch(e){ miss.push(lv+':ERR'); }
  }
  let domOK=false, voiceOK=false;
  try{
    TAB='G'; if(S.G)S.G.i=2; render();
    const key=stageFor('G').cast;
    const catav=document.documentElement.style.getPropertyValue('--catav')||'';
    domOK=!!(ART[key]&&catav.indexOf(ART[key].slice(0,34))!==-1);
    voiceOK=!!(typeof VOICE_LINE!=='undefined'&&VOICE_LINE[key]);
  }catch(e){}

  /* bug② 真调用：找一个「初始选中层与当前立绘同角色」的用例，验证 queuePerf 会换到别的人物 */
  let perfCase=null, perfOK=false, perfErr='';
  const levels=D.meta.levels.map(l=>l.id);
  outer:
  for(const lv of levels){
    TAB=lv; try{render();}catch(e){continue;}
    const lvIdx=Math.max(0,levels.indexOf(lv));
    const baseCanon=exprCanon(stageFor(lv).cast||'cos_base');
    for(let idx=0;idx<OPT_MOODS.length;idx++){
      const m=OPT_MOODS[idx];
      let mi=(lvIdx+idx)%m.arts.length; const first=m.arts[mi];
      if(exprCanon(first)!==baseCanon)continue;
      if(!document.querySelector('#app .stagecut'))continue;
      STAGE_LOG.length=0;
      try{ queuePerf(idx); }catch(e){ perfErr='queuePerf ERR:'+e.message; break outer; }
      await new Promise(r=>setTimeout(r,160));
      const last=STAGE_LOG.filter(x=>x.type==='perf').pop();
      perfCase={lv,idx,baseCanon,first,chosen:last?last.art:null};
      perfOK=!!(last&&exprCanon(last.art)!==baseCanon);
      break outer;
    }
  }

  let cells=0, panelText='';
  try{ openExpr(); cells=document.querySelectorAll('#exprPanel .exprcell').length;
       panelText=(document.querySelector('#exprPanel .exprh span')||{}).textContent||''; closeExpr(); }catch(e){}
  EXPR_APPLY=0;
  return {sw, iw, aud:window.__AUD||0, exprN:EXPR.length, castN:EXPR_CASTS.length,
    poolRoles:Object.keys(ROLE_POOL).length, poolLayers:Object.values(ROLE_POOL).reduce((a,v)=>a+v.length,0),
    specialN:Object.keys(EXPR_SPECIAL).length, stat:exprStat(),
    badPool, dirty, badArt, cross, crossFn:exprCrossCount(), metaBad,
    hit, miss, layerHit, nameBad, domOK, voiceOK, cells, panelText,
    moodSet, moodKinds:Object.keys(moodSet).length, seqN, seq,
    perfCase, perfOK, perfErr,
    r45ok:!!ART['R45_base_xi'], r46ok:!!ART['R46_base_jue'],
    audioRefs:(document.documentElement.outerHTML.match(/data:audio\//g)||[]).length};
}"""

try:
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/usr/local/bin/chromium',
                               args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu'])
        for label, w, h in [('竖屏 420×900', 420, 900), ('横屏 900×420', 900, 420), ('桌面 1440×900', 1440, 900)]:
            pg = b.new_page(viewport={'width': w, 'height': h})
            errs = []
            pg.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)))
            pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' else None)
            pg.add_init_script("window.__AUD=0; var _A=window.Audio; "
                               "window.Audio=function(){window.__AUD++; return new _A();}; "
                               "window.Audio.prototype=_A.prototype;")
            pg.goto('file://' + P, wait_until='load', timeout=90000)
            pg.wait_for_timeout(800)
            info = pg.evaluate(JS)
            ok = (not errs and info['sw'] <= info['iw'] + 1
                  and info['exprN'] == 184 and info['castN'] == 23
                  and info['poolRoles'] == 23 and not info['badPool'] and not info['dirty']
                  and not info['badArt'] and not info['cross'] and info['crossFn'] == 0
                  and info['specialN'] == 36 and info['stat']['专属'] == 36
                  and info['hit'] == 24 and info['layerHit'] == 24 and info['metaBad'] == 0
                  and not info['nameBad'] and info['domOK'] and info['voiceOK']
                  and info['moodKinds'] >= 5 and info['seqN'] == 8
                  and info['perfOK'] and info['cells'] == 184
                  and info['aud'] == 0 and info['r45ok'] and info['r46ok'])
            R['browser'].append({'label': label, 'ok': bool(ok), 'info': info, 'errors': errs[:6]})
            ck('浏览器 ' + label, ok,
               'sw=%s/iw=%s expr=%s cast=%s cross=%s 专属=%s hit=%s layer=%s moods=%s seq=%s perf=%s cells=%s nameBad=%s aud=%s errs=%s' %
               (info['sw'], info['iw'], info['exprN'], info['castN'], len(info['cross']),
                info['stat']['专属'], info['hit'], info['layerHit'], info['moodKinds'],
                info['seqN'], info['perfOK'], info['cells'], len(info['nameBad']),
                info['aud'], errs[:1]))
            pg.close()
        b.close()
except Exception as e:
    ck('真实浏览器自检', False, repr(e))

R['summary'] = {'total': len(R['checks']), 'passed': sum(1 for c in R['checks'] if c['ok']),
                'failed': len(R['errors']), 'html_bytes': os.path.getsize(P)}
json.dump(R, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(R['summary'], ensure_ascii=False))
for c in R['checks']:
    print(('PASS ' if c['ok'] else 'FAIL ') + c['name'] + ('  ' + c['detail'] if c['detail'] else ''))
print('ERRORS', R['errors'])
