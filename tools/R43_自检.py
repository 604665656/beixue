# -*- coding: utf-8 -*-
"""R43 自检：语法 / DATA / 语音包清零 / 表情谱系 / 三尺寸真实浏览器 / 紧凑规则"""
import json, re, os, subprocess, sys, tempfile

P = '/data/workspace/杯雪游戏总站.html'
OUT = '/data/workspace/44_表情管理/R43_自检结果.json'
s = open(P, encoding='utf-8').read()
R = {'checks': [], 'browser': [], 'errors': []}


def ck(name, cond, detail=''):
    R['checks'].append({'name': name, 'ok': bool(cond), 'detail': str(detail)})
    if not cond:
        R['errors'].append(name + ' :: ' + str(detail))


# 1) JS 语法（提取所有非 JSON script）
scripts = re.findall(r'<script(?![^>]*application/json)[^>]*>([\s\S]*?)</script>', s)
js = '\n;\n'.join(scripts)
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
    f.write(js)
    jsp = f.name
r = subprocess.run(['node', '--check', jsp], capture_output=True, text=True)
ck('node --check 内联 JS', r.returncode == 0, (r.stderr or '')[:400])
os.unlink(jsp)

# 2) DATA JSON
dm = re.search(r'<script type="application/json" id="DATA">([\s\S]*?)</script>', s)
try:
    D = json.loads(dm.group(1))
    ck('DATA JSON.parse', len(D['meta']['levels']) == 24, 'levels=' + str(len(D['meta']['levels'])))
except Exception as e:
    ck('DATA JSON.parse', False, e)

# 3) 语音包清零
ck('无 vp_* 动作分支', "if(a==='vp_" not in s)
ck('运行时不创建 Audio', 'new Audio(' not in s, 'count=%d' % s.count('new Audio('))
ck('无 VOICE_PACK.clips 读取', 'VOICE_PACK.clips' not in s)
ck('无语音包导入/试听调用', 'importVoicePack(' not in s and 'demoVoice(' not in s)
ck('无内嵌音频 URI', 'data:audio/wav' not in s and 'data:audio/mp4' not in s and 'data:audio/ogg' not in s)
ck('内置包置空', 'const BUILTIN_VOICE_PACK=null;' in s)
ck('设置面板仍可关闭', "data-act=\"panel_close\"" in s)
ck('系统 TTS 保留', 'function performLines(txt,cast){' in s and 'SpeechSynthesisUtterance' in s)

# 4) 表情管理谱系
ck('EXPR 单一入口落地', 'function exprResolve(' in s and 'window.stageFor=function(k)' in s)
ck('表情管理入口按钮', "b('expr_open',0,'☰ 表情管理')" in s)
ck('8 张新素材键注入', all(('"R43_%s"' % k) in s for k in
                     ['jin_xi', 'shen_jing', 'yi_ai', 'luo_nu', 'xiao_jue', 'zhu_zui', 'qin_xi', 'geng_nu']))
ck('EXPR_CASTS 28 位', 'const EXPR_CASTS=' in s)
ck('导出 CSV 带 BOM', "'\\ufeff'" in s)

# 5) 拼接动画规则区（剥离注释后）
css = re.sub(r'/\*[\s\S]*?\*/', '', '\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', s)))
ck('CSS 规则区无 step-end', 'step-end' not in css, 'count=%d' % css.count('step-end'))
ck('CSS 规则区无 steps(1,end)', 'steps(1,end)' not in css)
ck('紧凑 CSS 竖屏两列', 'grid-template-columns:repeat(2,1fr)' in css)
ck('紧凑 CSS 横屏三列', 'grid-template-columns:repeat(3,1fr)' in css)
ck('真旋转横屏也收紧', 'html.rot-landscape .grp' in css)

# 6) 三尺寸真实浏览器
try:
    from playwright.sync_api import sync_playwright
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
            pg.wait_for_timeout(900)
            info = pg.evaluate("""() => ({
              sw: document.documentElement.scrollWidth, iw: innerWidth,
              aud: window.__AUD||0, levels: (typeof D!=='undefined'&&D.meta&&D.meta.levels)?D.meta.levels.length:-1,
              expr: (typeof EXPR!=='undefined')?EXPR.length:-1,
              stat: (typeof exprStat==='function')?exprStat():null,
              exprBtn: (function(){try{PANEL_TAB='view';renderA11yPanel();return !!document.querySelector('[data-act="expr_open"]');}catch(e){return String(e)}})(),
              panelCells: (function(){try{openExpr();var n=document.querySelectorAll('#exprPanel .exprcell').length;closeExpr();return n;}catch(e){return String(e)}})(),
              gridCols: (function(){var e=document.createElement('div');e.className='exprgrid';document.body.appendChild(e);var v=getComputedStyle(e).gridTemplateColumns;e.remove();return v;})(),
              asrMax: (function(){var e=document.createElement('div');e.className='asrstate';e.textContent='x';document.body.appendChild(e);var v=getComputedStyle(e).maxHeight;e.remove();return v;})(),
              htmlBytes: document.documentElement.outerHTML.length
            })""")
            ok = (not errs) and info['sw'] <= info['iw'] + 1 and info['levels'] == 24 and info['expr'] == 224 \
                 and info['aud'] == 0 and info['exprBtn'] is True and isinstance(info['panelCells'], int) and info['panelCells'] > 0
            R['browser'].append({'label': label, 'ok': bool(ok), 'info': info, 'errors': errs[:6]})
            ck('浏览器 ' + label, ok, 'sw=%s iw=%s aud=%s expr=%s cells=%s errs=%s' %
               (info['sw'], info['iw'], info['aud'], info['expr'], info['panelCells'], errs[:2]))
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
