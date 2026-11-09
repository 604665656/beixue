# -*- coding: utf-8 -*-
"""R47 自检：主站 + 轻量版双文件、三尺寸真实浏览器；验证 46 专属、2 个修掉的 bug、图片可解码。"""
import json, re, os, io, base64, subprocess, tempfile
from PIL import Image
from playwright.sync_api import sync_playwright

FULL = '/data/workspace/杯雪游戏总站.html'
LITE = '/data/workspace/杯雪游戏总站_轻量版.html'
OUT = '/data/workspace/44_表情管理/R47_自检结果.json'
R = {'checks': [], 'browser': [], 'errors': []}


def ck(name, cond, detail=''):
    R['checks'].append({'name': name, 'ok': bool(cond), 'detail': str(detail)})
    if not cond:
        R['errors'].append(name + ' :: ' + str(detail))


def static(path, tag, lite=False):
    s = open(path, encoding='utf-8').read()
    scripts = re.findall(r'<script(?![^>]*application/json)[^>]*>([\s\S]*?)</script>', s)
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write('\n;\n'.join(scripts)); jsp = f.name
    r = subprocess.run(['node', '--check', jsp], capture_output=True, text=True)
    os.unlink(jsp)
    ck(tag + ' node --check', r.returncode == 0, (r.stderr or '')[:300])
    D = json.loads(re.search(r'<script type="application/json" id="DATA">([\s\S]*?)</script>', s).group(1))
    ck(tag + ' DATA 24 关', len(D['meta']['levels']) == 24)
    # R47 自检自身 bug：历史档案叙述里保留着 R36 修 bug 时提到的「data:audio/」字面量，
    # 旧口径把它误判成运行时音频残留。只认真实音频 URI（含 ;base64,）与 Audio 构造调用。
    ck(tag + ' 语音包撤除', 'new Audio(' not in s
       and not re.search(r'data:audio/[a-z0-9.+-]+;base64,', s, re.I)
       and 'const BUILTIN_VOICE_PACK=null;' in s)
    ck(tag + ' 46 项专属', s.count('"R47_') >= 10 and '杯雪表情谱系_R47.csv' in s)
    ck(tag + ' 导出文件名 R47', '杯雪表情谱系_R47.csv' in s and '杯雪表情谱系_R45.csv' not in s)
    ck(tag + ' 面板脚注动态', 'var st=exprStat();' in s and 'R46：角色全集' not in s)
    css = re.sub(r'/\*[\s\S]*?\*/', '', '\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', s)))
    ck(tag + ' CSS 无拼接动画', 'step-end' not in css and 'steps(1,end)' not in css)
    ck(tag + ' 无外链资源', '<script src=' not in s and 'href="http' not in s and 'url(http' not in s)
    uris = re.findall(r'data:image/(?:webp|gif|png|jpeg);base64,[A-Za-z0-9+/=]+', s)
    ck(tag + ' 内嵌图片数', len(uris) >= 380, len(uris))
    # 全部唯一 URI 必须可被 PIL 解码
    bad = []
    for u in set(uris):
        try:
            im = Image.open(io.BytesIO(base64.b64decode(u.split(',', 1)[1])))
            im.load()
            if lite and u.startswith('data:image/webp') and max(im.size) > 224:
                bad.append('oversize:' + str(im.size))
        except Exception as e:
            bad.append(repr(e)[:60])
    ck(tag + ' 全部内嵌图可解码' + ('（且 ≤224px）' if lite else ''), not bad, bad[:3])
    ck(tag + ' 尾部完整', s.rstrip().endswith('</html>'))
    if lite:
        ck(tag + ' 标题标识', '轻量版' in re.search(r'<title>(.*?)</title>', s, re.S).group(1))
        ck(tag + ' 体积 < 7 MB', os.path.getsize(path) < 7 * 1048576,
           round(os.path.getsize(path) / 1048576, 2))
    return s


sf = static(FULL, '主站')
sl = static(LITE, '轻量版', lite=True)
ck('轻量版显著小于主站', os.path.getsize(LITE) < os.path.getsize(FULL) * .5,
   '%.2f / %.2f MB' % (os.path.getsize(LITE) / 1048576, os.path.getsize(FULL) / 1048576))

JS = r"""async () => {
  const sw=document.documentElement.scrollWidth, iw=innerWidth;
  const badArt=EXPR.filter(e=>!ART[e.art]).map(e=>e.cast+'|'+e.mood+'->'+e.art);
  const cross=EXPR.filter(e=>e.src==='复用' && !(ROLE_POOL[e.cast]||[]).includes(e.art));
  const moodSet={}; D.meta.levels.forEach(l=>{const m=exprMoodFor(l.id);moodSet[m]=(moodSet[m]||0)+1;});
  const saved=S.G?S.G.i:0; const seq=[];
  for(let m=0;m<8;m++){ if(S.G)S.G.i=m; seq.push(exprMoodFor('G')); }
  if(S.G)S.G.i=saved;

  let hit=0, layerHit=0, nameBad=[], miss=[];
  EXPR_APPLY=1;
  for(const lv of D.meta.levels.map(l=>l.id)){
    try{ const st=stageFor(lv); const r=exprResolve(st.cast||'cos_base',exprMoodFor(lv),lv);
      if(r&&r.cast===exprCanon(st.cast||'cos_base')&&ART[r.art])hit++; else miss.push(lv);
      if(EXPR.some(e=>e.art===st.cast))layerHit++;
      const nm=(castMeta(st.cast)||[])[0]||'';
      if(nm==='哈士喵'&&st.cast!=='cos_base'&&!String(st.cast).startsWith('R45_base')&&!String(st.cast).startsWith('R46_base')&&!String(st.cast).startsWith('R47_base'))nameBad.push(lv+':'+st.cast);
    }catch(e){miss.push(lv+':ERR');}
  }
  let domOK=false, voiceOK=false;
  try{ TAB='G'; if(S.G)S.G.i=2; render();
    const key=stageFor('G').cast;
    const catav=document.documentElement.style.getPropertyValue('--catav')||'';
    domOK=!!(ART[key]&&catav.indexOf(ART[key].slice(0,34))!==-1);
    voiceOK=!!(typeof VOICE_LINE!=='undefined'&&VOICE_LINE[key]);
  }catch(e){}

  /* 真调用 queuePerf：构造同角色用例，验证最终换到别的人物 */
  let perfOK=false, perfCase=null;
  const levels=D.meta.levels.map(l=>l.id);
  outer:
  for(const lv of levels){
    TAB=lv; try{render();}catch(e){continue;}
    const baseCanon=exprCanon(stageFor(lv).cast||'cos_base');
    const lvIdx=Math.max(0,levels.indexOf(lv));
    for(let idx=0;idx<OPT_MOODS.length;idx++){
      const m=OPT_MOODS[idx]; let mi=(lvIdx+idx)%m.arts.length;
      if(exprCanon(m.arts[mi])!==baseCanon)continue;
      STAGE_LOG.length=0;
      try{queuePerf(idx);}catch(e){break outer;}
      await new Promise(r=>setTimeout(r,160));
      const last=STAGE_LOG.filter(x=>x.type==='perf').pop();
      perfCase={lv,idx,baseCanon,chosen:last?last.art:null};
      perfOK=!!(last&&exprCanon(last.art)!==baseCanon);
      break outer;
    }
  }

  /* 面板：全量 184 格 + 脚注动态统计 */
  let cells=0, foot='';
  try{ openExpr(); cells=document.querySelectorAll('#exprPanel .exprcell').length;
       foot=(document.querySelector('#exprPanel .exprfoot')||{}).textContent||''; closeExpr(); }catch(e){}

  /* 图片浏览器端解码抽样（ART 前 24 个键） */
  let imgOK=0, imgBad=0;
  const keys=Object.keys(ART).slice(0,24);
  await Promise.all(keys.map(k=>new Promise(res=>{
    const im=new Image();
    const t=setTimeout(()=>{imgBad++;res();},4000);
    im.onload=()=>{imgOK++;clearTimeout(t);res();};
    im.onerror=()=>{imgBad++;clearTimeout(t);res();};
    im.src=ART[k];
  })));

  EXPR_APPLY=0;
  return {sw,iw,aud:window.__AUD||0,exprN:EXPR.length,castN:EXPR_CASTS.length,
    artN:Object.keys(ART).length,specialN:Object.keys(EXPR_SPECIAL).length,stat:exprStat(),
    badArt,cross:cross.length,crossFn:exprCrossCount(),
    hit,miss,layerHit,nameBad,domOK,voiceOK,cells,foot,
    moodKinds:Object.keys(moodSet).length,seqN:new Set(seq).size,
    perfOK,perfCase,imgOK,imgBad,
    gifVar:getComputedStyle(document.documentElement).getPropertyValue('--catAnimGif').length};
}"""

try:
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/usr/local/bin/chromium',
                               args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu'])
        for tag, path in [('主站', FULL), ('轻量版', LITE)]:
            for label, w, h in [('竖屏 420×900', 420, 900), ('横屏 900×420', 900, 420), ('桌面 1440×900', 1440, 900)]:
                pg = b.new_page(viewport={'width': w, 'height': h})
                errs = []
                pg.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)))
                pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' else None)
                pg.add_init_script("window.__AUD=0; var _A=window.Audio; "
                                   "window.Audio=function(){window.__AUD++; return new _A();}; "
                                   "window.Audio.prototype=_A.prototype;")
                pg.goto('file://' + path, wait_until='load', timeout=120000)
                pg.wait_for_timeout(900)
                info = pg.evaluate(JS)
                ok = (not errs and info['sw'] <= info['iw'] + 1
                      and info['exprN'] == 184 and info['castN'] == 23
                      and info['specialN'] == 46 and info['stat']['专属'] == 46
                      and info['stat']['复用'] == 138 and info['stat']['待补'] == 0
                      and not info['badArt'] and info['cross'] == 0 and info['crossFn'] == 0
                      and info['hit'] == 24 and info['layerHit'] == 24 and not info['nameBad']
                      and info['domOK'] and info['voiceOK'] and info['cells'] == 184
                      and '专属 46' in info['foot'] and '复用 138' in info['foot']
                      and info['moodKinds'] == 8 and info['seqN'] == 8 and info['perfOK']
                      and info['imgBad'] == 0 and info['imgOK'] >= 20
                      and info['aud'] == 0 and info['gifVar'] > 50)
                R['browser'].append({'tag': tag, 'label': label, 'ok': bool(ok), 'info': info, 'errors': errs[:6]})
                ck(tag + ' ' + label, ok,
                   'sw=%s/iw=%s 专属=%s 复用=%s cross=%s hit=%s moods=%s perf=%s cells=%s img=%s/%s foot=%s errs=%s' %
                   (info['sw'], info['iw'], info['stat']['专属'], info['stat']['复用'], info['cross'],
                    info['hit'], info['moodKinds'], info['perfOK'], info['cells'], info['imgOK'],
                    info['imgBad'], ('专属 46' in info['foot']), errs[:1]))
                pg.close()
        b.close()
except Exception as e:
    ck('真实浏览器自检', False, repr(e))

R['summary'] = {'total': len(R['checks']), 'passed': sum(1 for c in R['checks'] if c['ok']),
                'failed': len(R['errors']),
                'full_MB': round(os.path.getsize(FULL) / 1048576, 2),
                'lite_MB': round(os.path.getsize(LITE) / 1048576, 2)}
json.dump(R, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(R['summary'], ensure_ascii=False))
for c in R['checks']:
    print(('PASS ' if c['ok'] else 'FAIL ') + c['name'] + ('  ' + c['detail'] if c['detail'] else ''))
print('ERRORS', R['errors'])
