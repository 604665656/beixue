# -*- coding: utf-8 -*-
"""R44 自检：语法 / DATA / 谱系 ID 对齐 / 键池纯净 / 语音包仍为零 / 三尺寸浏览器 / 接管命中"""
import json, re, os, subprocess, tempfile
from playwright.sync_api import sync_playwright

P = '/data/workspace/杯雪游戏总站.html'
OUT = '/data/workspace/44_表情管理/R44_自检结果.json'
s = open(P, encoding='utf-8').read()
R = {'checks': [], 'browser': [], 'errors': []}


def ck(name, cond, detail=''):
    R['checks'].append({'name': name, 'ok': bool(cond), 'detail': str(detail)})
    if not cond:
        R['errors'].append(name + ' :: ' + str(detail))


# 1) JS 语法
scripts = re.findall(r'<script(?![^>]*application/json)[^>]*>([\s\S]*?)</script>', s)
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
    f.write('\n;\n'.join(scripts)); jsp = f.name
r = subprocess.run(['node', '--check', jsp], capture_output=True, text=True)
ck('node --check 内联 JS', r.returncode == 0, (r.stderr or '')[:300])
os.unlink(jsp)

# 2) DATA
D = json.loads(re.search(r'<script type="application/json" id="DATA">([\s\S]*?)</script>', s).group(1))
ck('DATA JSON.parse · 24 关', len(D['meta']['levels']) == 24)

# 3) 语音包仍为零（上一轮约束不能回退）
ck('运行时不创建 Audio', 'new Audio(' not in s)
ck('无 vp_* 动作分支', "if(a==='vp_" not in s)
ck('无内嵌音频 URI', not re.search(r'data:audio/(wav|mp4|ogg|mpeg)', s))
ck('内置包置空', 'const BUILTIN_VOICE_PACK=null;' in s)

# 4) 谱系静态检查
ck('无占位角色 cos_extra_', 'cos_extra_' not in s[s.index('/* ===== R44 表情管理'):])
ck('专属映射全部用真实 cos_ 短键', all(re.match(r'^cos_[a-z0-9_]+$', k.split('|')[0])
                              for k in re.findall(r"'(cos_[a-z0-9_]+\|[^']+)'\s*:\s*'R4[34]_", s)))
ck('10 张 R44 键注入', all(('"R44_%s"' % k) in s for k in
    ['zhu_zui','yuancl_scar','jiao_scar','shen_beard','yi_beard','jin_nu','luo_ai','xiao_xi','zhu_nu','qin_jing']))

# 5) 拼接动画规则区
css = re.sub(r'/\*[\s\S]*?\*/', '', '\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', s)))
ck('CSS 规则区无 step-end', 'step-end' not in css)
ck('CSS 规则区无 steps(1,end)', 'steps(1,end)' not in css)

# 6) 三尺寸真实浏览器 + 谱系运行时验证
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
            info = pg.evaluate("""() => {
              const metaKeys = Object.keys(CAST_META);
              const badPool = EXPR_POOL.filter(k=>/^(bg_|fx_|cover$|cat\\d|catorg|catav|cat3|[A-Z]$)/i.test(k));
              const badCast = EXPR_CASTS.filter(c=>!metaKeys.includes(c[0]));
              const badArt  = EXPR.filter(e=>!ART[e.art]).map(e=>e.cast+'|'+e.mood+'->'+e.art);
              // 接管后：逐关 stageFor 的 cast 能在 EXPR 命中，且返回的 art 是角色层
              let hit=0, miss=[];
              EXPR_APPLY=1;
              for(const lv of D.meta.levels.map(l=>l.id)){
                try{ const st=stageFor(lv); const r=exprResolve(st.cast||'cos_base',exprMoodFor(lv),lv);
                  if(r&&r.cast===exprCanon(st.cast||'cos_base')&&ART[r.art])hit++; else miss.push(lv+':'+(st.cast||'') ); }
                catch(e){ miss.push(lv+':ERR'); }
              }
              EXPR_APPLY=0;
              let cells=0; try{openExpr();cells=document.querySelectorAll('#exprPanel .exprcell').length;closeExpr();}catch(e){}
              return {sw:document.documentElement.scrollWidth, iw:innerWidth, aud:window.__AUD||0,
                exprN:EXPR.length, castN:EXPR_CASTS.length, poolN:EXPR_POOL.length,
                stat:exprStat(), badPool:badPool, badCast:badCast, badArt:badArt,
                hit:hit, miss:miss, cells:cells,
                r43ok:!!ART['R43_jin_xi'], r44ok:!!ART['R44_zhu_zui'],
                canonSample:['cos_shen','R30_K_read','H_cost_shi','B_face_yi','R32_M_zhu'].map(exprCanon),
                audioRefs:(document.documentElement.outerHTML.match(/data:audio\\//g)||[]).length};
            }""")
            ok = (not errs and info['sw'] <= info['iw'] + 1 and info['exprN'] == info['castN'] * 8
                  and info['aud'] == 0 and not info['badPool'] and not info['badCast']
                  and not info['badArt'] and info['hit'] == 24 and info['cells'] > 0
                  and info['r43ok'] and info['r44ok'])
            R['browser'].append({'label': label, 'ok': bool(ok), 'info': info, 'errors': errs[:6]})
            ck('浏览器 ' + label, ok,
               'sw=%s/iw=%s expr=%s hit=%s badArt=%s badPool=%s aud=%s errs=%s' %
               (info['sw'], info['iw'], info['exprN'], info['hit'], len(info['badArt']),
                len(info['badPool']), info['aud'], errs[:1]))
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
