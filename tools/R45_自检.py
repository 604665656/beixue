# -*- coding: utf-8 -*-
"""R45 自检：串脸归零 / 真角色全集 / 26 专属 / 接管真的写进渲染链 / 语音包为零 / 三尺寸浏览器。"""
import json, re, os, subprocess, tempfile
from playwright.sync_api import sync_playwright

P = '/data/workspace/杯雪游戏总站.html'
OUT = '/data/workspace/44_表情管理/R45_自检结果.json'
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
ck('无 vp_* 动作分支', "if(a==='vp_" not in s)
ck('无内嵌音频 URI', not re.search(r'data:audio/(wav|mp4|ogg|mpeg|aac|m4a)', s))
ck('内置包置空', 'const BUILTIN_VOICE_PACK=null;' in s)

blk = s[s.index('/* ===== R45 表情管理'):s.index('\n</script>', s.index('/* ===== R45 表情管理'))]
ck('无占位角色 cos_extra_', 'cos_extra_' not in blk)
for fake in ['cos_shen_argue', 'cos_luo_draw', 'cos_yi_grief', 'cos_zhu_resolve']:
    ck('伪角色不作谱系 ID：' + fake, not re.search(r"\[\s*'"+fake+r"'\s*,", blk))
ck('R45 10 张键注入', all(('"R45_%s"' % k) in s for k in
    ['base_xi','zhu_jing','yi_xi','ying_xi','tian_xi','base_jing','base_yi','zhu_xi','xiao_jing','tian_jing']))
ck('接管写回 cast（非空操作）', 'base.cast=r.art' in s and 'exprRegisterMeta()' in s)
css = re.sub(r'/\*[\s\S]*?\*/', '', '\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', s)))
ck('CSS 规则区无拼接动画', 'step-end' not in css and 'steps(1,end)' not in css)

JS = r"""() => {
  const sw=document.documentElement.scrollWidth, iw=innerWidth;
  const badPool=Object.entries(ROLE_POOL).filter(([c,v])=>!v.length).map(x=>x[0]);
  const dirty=Object.entries(ROLE_POOL).flatMap(([c,v])=>v.filter(k=>/^(bg_|fx_|cover$|cat\d|catorg|catav|cat3|[A-Z]$)/i.test(k)));
  const badArt=EXPR.filter(e=>!ART[e.art]).map(e=>e.cast+'|'+e.mood+'->'+e.art);
  const cross=EXPR.filter(e=>e.src==='复用' && !(ROLE_POOL[e.cast]||[]).includes(e.art)).map(e=>e.cast+'|'+e.mood+'->'+e.art);
  const metaBad=EXPR.filter(e=>!(CAST_META[e.art]||[])[0]||!CAST.some(x=>x[0]===e.art)).length;
  let hit=0, layerHit=0, nameBad=[], miss=[];
  EXPR_APPLY=1;
  for(const lv of D.meta.levels.map(l=>l.id)){
    try{ const st=stageFor(lv); const r=exprResolve(st.cast||'cos_base',exprMoodFor(lv),lv);
      if(r&&r.cast===exprCanon(st.cast||'cos_base')&&ART[r.art])hit++; else miss.push(lv+':'+(st.cast||''));
      if(EXPR.some(e=>e.art===st.cast))layerHit++;
      const nm=(castMeta(st.cast)||[])[0]||'';
      if(nm==='哈士喵'&&st.cast!=='cos_base'&&!String(st.cast).startsWith('R45_base'))nameBad.push(lv+':'+st.cast+'->'+nm);
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
  EXPR_APPLY=0;
  let cells=0, panelText='';
  try{ openExpr(); cells=document.querySelectorAll('#exprPanel .exprcell').length;
       panelText=(document.querySelector('#exprPanel .exprh span')||{}).textContent||''; closeExpr(); }catch(e){}
  return {sw, iw, aud:window.__AUD||0, exprN:EXPR.length, castN:EXPR_CASTS.length,
    poolRoles:Object.keys(ROLE_POOL).length, poolLayers:Object.values(ROLE_POOL).reduce((a,v)=>a+v.length,0),
    specialN:Object.keys(EXPR_SPECIAL).length, stat:exprStat(),
    badPool, dirty, badArt, cross, crossFn:exprCrossCount(), metaBad,
    hit, miss, layerHit, nameBad, domOK, voiceOK, cells, panelText,
    r43ok:!!ART['R43_jin_xi'], r44ok:!!ART['R44_zhu_zui'], r45ok:!!ART['R45_base_xi'],
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
                  and info['specialN'] == 26 and info['stat']['专属'] == 26
                  and info['hit'] == 24 and info['layerHit'] == 24 and info['metaBad'] == 0
                  and not info['nameBad'] and info['domOK'] and info['voiceOK']
                  and info['cells'] > 0 and info['aud'] == 0
                  and info['r43ok'] and info['r44ok'] and info['r45ok'])
            R['browser'].append({'label': label, 'ok': bool(ok), 'info': info, 'errors': errs[:6]})
            ck('浏览器 ' + label, ok,
               'sw=%s/iw=%s expr=%s cast=%s cross=%s badArt=%s hit=%s layer=%s metaBad=%s nameBad=%s dom=%s voice=%s aud=%s errs=%s' %
               (info['sw'], info['iw'], info['exprN'], info['castN'], len(info['cross']),
                len(info['badArt']), info['hit'], info['layerHit'], info['metaBad'],
                len(info['nameBad']), info['domOK'], info['voiceOK'], info['aud'], errs[:1]))
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
