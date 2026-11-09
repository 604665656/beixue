# -*- coding: utf-8 -*-
"""R52 自检：主站 + 轻量版 × 三尺寸；95 专属 / 89 复用 / 零专属 0、
   两个系统性 bug 回归、AI 原画标注、版本推进、CSV 导出真调用验证。"""
import json, re, os, io, base64, subprocess, tempfile, sys
from PIL import Image
from playwright.sync_api import sync_playwright

FULL = '/data/workspace/杯雪游戏总站.html'
LITE = '/data/workspace/杯雪游戏总站_轻量版.html'
OUT = '/data/workspace/44_表情管理/R52_自检结果.json'
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
    ck(tag + ' 语音包撤除', 'new Audio(' not in s
       and not re.search(r'data:audio/[a-z0-9.+-]+;base64,', s, re.I)
       and 'const BUILTIN_VOICE_PACK=null;' in s)
    ck(tag + ' R49/R50/R51/R52 各 10 键', all(len(re.findall(r'"R%d_[a-z_]+"\s*:\s*"data:image/webp'%n, s)) == 10 for n in (49,50,51,52)))
    ck(tag + ' bug① 导出跟随筛选', 'const list=exprList();' in s and 'list.forEach(e=>rows.push' in s
       and 'EXPR.forEach(e=>rows.push' not in s and '筛选' in s)
    ck(tag + ' bug① gen 集合重构', "const PROC_ART=new Set(" in s and "gen:PROC_ART.has(art)" in s
       and "gen:String(art).indexOf('R49_')" not in s
       and "本体重绘待AI" in s and "生成方式" in s)
    ck(tag + ' FIRST_LV 实算保留', 'const FIRST_LV=' in s and 'unlock:(FIRST_LV[c[0]]||0)' in s
       and 'unlock:Math.min(24,ci)' not in s)
    ck(tag + ' 脚注/CSV 版本 R52', "R52：当前筛选 " in s and "杯雪表情谱系_R52_" in s and "程序化本体重绘" in s)
    css = re.sub(r'/\*[\s\S]*?\*/', '', '\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>', s)))
    ck(tag + ' CSS 无拼接动画', 'step-end' not in css and 'steps(1,end)' not in css)
    ck(tag + ' 无外链资源', '<script src=' not in s and 'href="http' not in s and 'url(http' not in s)
    uris = re.findall(r'data:image/(?:webp|gif|png|jpeg);base64,[A-Za-z0-9+/=]+', s)
    ck(tag + ' 内嵌图片数', len(uris) >= 400, len(uris))
    bad = []
    for u in set(uris):
        try:
            im = Image.open(io.BytesIO(base64.b64decode(u.split(',', 1)[1]))); im.load()
            if lite and u.startswith('data:image/webp') and max(im.size) > 224:
                bad.append('oversize:' + str(im.size))
        except Exception as e:
            bad.append(repr(e)[:60])
    ck(tag + ' 全部内嵌图可解码' + ('（≤224px）' if lite else ''), not bad, bad[:3])
    ck(tag + ' 尾部完整', s.rstrip().endswith('</html>'))
    if lite:
        ck(tag + ' 标题标识', '轻量版' in re.search(r'<title>(.*?)</title>', s, re.S).group(1))
        ck(tag + ' 体积 < 7 MB', os.path.getsize(path) < 7 * 1048576,
           round(os.path.getsize(path) / 1048576, 2))
    return s


static(FULL, '主站')
static(LITE, '轻量版', lite=True)
ck('轻量版显著小于主站', os.path.getsize(LITE) < os.path.getsize(FULL) * .5,
   '%.2f / %.2f MB' % (os.path.getsize(LITE) / 1048576, os.path.getsize(FULL) / 1048576))
try:
    g = subprocess.run([sys.executable, '/data/workspace/44_表情管理/R48_轻量版一致性门禁.py'],
                       capture_output=True, text=True, timeout=180)
    gj = json.load(open('/data/workspace/44_表情管理/R48_轻量版一致性门禁.json'))
    ck('轻量版一致性门禁纳入', g.returncode == 0 and gj['summary']['failed'] == 0, gj['summary'])
except Exception as e:
    ck('轻量版一致性门禁纳入', False, repr(e))

JS = r"""async () => {
  const sw=document.documentElement.scrollWidth, iw=innerWidth;
  const badArt=EXPR.filter(e=>!ART[e.art]).map(e=>e.cast+'|'+e.mood+'->'+e.art);
  const cross=EXPR.filter(e=>e.src==='复用' && !(ROLE_POOL[e.cast]||[]).includes(e.art));
  const zeroRoles=EXPR_CASTS.filter(c=>!EXPR.some(e=>e.cast===c[0]&&e.src==='专属')).map(c=>c[0]);
  const proc=EXPR.filter(e=>e.gen&&e.gen!=='AI原画');
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
      if(nm==='哈士喵'&&st.cast!=='cos_base'&&!String(st.cast).match(/^R4[5-9]_base/))nameBad.push(lv+':'+st.cast);
    }catch(e){miss.push(lv+':ERR');}
  }
  let domOK=false, voiceOK=false;
  try{ TAB='G'; if(S.G)S.G.i=2; render();
    const key=stageFor('G').cast;
    const catav=document.documentElement.style.getPropertyValue('--catav')||'';
    domOK=!!(ART[key]&&catav.indexOf(ART[key].slice(0,34))!==-1);
    voiceOK=!!(typeof VOICE_LINE!=='undefined'&&VOICE_LINE[key]);
  }catch(e){}

  let perfOK=false;
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
      perfOK=!!(last&&exprCanon(last.art)!==baseCanon);
      break outer;
    }
  }

  /* bug① 真调用 exprExport：拦截 Blob 与 click，验证行数确实跟随筛选 */
  let csvAll=-1,csvOwn=-1,csvName='',csvGen='';
  try{
    const origCreate=URL.createObjectURL, origClick=HTMLAnchorElement.prototype.click;
    let blob=null;
    URL.createObjectURL=function(b){blob=b;return 'blob:stub';};
    HTMLAnchorElement.prototype.click=function(){csvName=this.download;};
    EXPR_F.src=''; exprExport(); csvAll=(await blob.text()).trim().split('\r\n').length-1;
    EXPR_F.src='专属'; exprExport();
    const t=await blob.text(); csvOwn=t.trim().split('\r\n').length-1;
    csvGen=(t.split('\r\n').find(x=>x.indexOf('R49_jinhe_scar')>=0)||'');
    URL.createObjectURL=origCreate; HTMLAnchorElement.prototype.click=origClick; EXPR_F.src='';
  }catch(e){}

  /* 面板：全量 / 筛选 / 脚注 / 生成方式标注 */
  let footAll='',footOwn='',cellsAll=0,cellsOwn=0,head='',procTag=0;
  try{
    EXPR_F.src=''; openExpr();
    footAll=(document.querySelector('#exprPanel .exprfoot')||{}).textContent||'';
    cellsAll=document.querySelectorAll('#exprPanel .exprcell').length;
    head=(document.querySelector('#exprPanel .exprh span')||{}).textContent||'';
    procTag=(document.querySelector('#exprPanel .exprgrid')||{}).innerHTML.split('本体重绘待AI').length-1;
    closeExpr();
    EXPR_F.src='专属'; openExpr();
    footOwn=(document.querySelector('#exprPanel .exprfoot')||{}).textContent||'';
    cellsOwn=document.querySelectorAll('#exprPanel .exprcell').length;
    closeExpr(); EXPR_F.src='';
  }catch(e){}

  /* 金和尚替换层的 canon 与名牌 */
  const jin=EXPR.find(e=>e.cast==='cos_jinhe'&&e.mood==='静息');
  const jinCanon=exprCanon(jin.art), jinName=(castMeta(jin.art)||[])[0]||'';

  const flv={n:Object.keys(FIRST_LV).length,zhu:EXPR.find(e=>e.cast==='cos_zhu').unlock,
    tie:EXPR.find(e=>e.cast==='cos_tie').unlock,max:Math.max(...EXPR.map(e=>e.unlock))};

  let imgOK=0,imgBad=0;
  await Promise.all(Object.keys(ART).slice(0,24).map(k=>new Promise(res=>{
    const im=new Image(); const t=setTimeout(()=>{imgBad++;res();},4000);
    im.onload=()=>{imgOK++;clearTimeout(t);res();};
    im.onerror=()=>{imgBad++;clearTimeout(t);res();}; im.src=ART[k];
  })));
  EXPR_APPLY=0;
  const procArtN=(typeof PROC_ART!=='undefined')?PROC_ART.size:-1;
  const r50Gen=EXPR.filter(e=>String(e.art).indexOf('R50_')===0 && e.gen==='程序化本体重绘·待AI重画').length;
  const r51AI=EXPR.filter(e=>String(e.art).indexOf('R51_')===0 && e.gen==='AI原画').length;
  const r51Wrong=EXPR.filter(e=>String(e.art).indexOf('R51_')===0 && e.gen!=='AI原画').length;
  const r52AI=EXPR.filter(e=>String(e.art).indexOf('R52_')===0 && e.gen==='AI原画').length;
  const r52Wrong=EXPR.filter(e=>String(e.art).indexOf('R52_')===0 && e.gen!=='AI原画').length;
  const hashKeys=['B_face_yi','B_face_jiao','D_face_xiaoru','D_face_zhuyan','D_face_luohan',
    'B_face_qinwen','D_face_shen','D_face_yuancl','E_face_wink'];
  const badKeys=['G_cost_verify','G_cost_compare','G_cost_brush','G_cost_startled','G_cost_smile',
    'G_cost_turn','G_cost_scroll','G_cost_blink','G_cost_open','H_cost_yuchi'];
  const hashLeft=hashKeys.filter(k=>castMeta(k)[0]==='哈士喵').length;
  const badCanonLeft=badKeys.filter(k=>exprCanon(k)==='cos_base').length;
  const defHash=D.meta.levels.map(l=>l.id).filter(lv=>castMeta(String(stageFor(lv).cast||''))[0]==='哈士喵').length;
  const aliasOK=(typeof R52_LAYER_ALIAS!=='undefined' && Object.keys(R52_LAYER_ALIAS).length===19);
  const histGen=EXPR.filter(e=>/^R(2[0-9]|3[0-9]|4[0-8])_/.test(String(e.art)) && e.gen==='AI原画').length;
  const footVer=footAll.slice(0,40);
  return {procArtN,r50Gen,histGen,r51AI,r51Wrong,r52AI,r52Wrong,hashLeft,badCanonLeft,defHash,aliasOK,footVer:footVer.slice(0,40),
   sw,iw,aud:window.__AUD||0,exprN:EXPR.length,castN:EXPR_CASTS.length,
    artN:Object.keys(ART).length,specialN:Object.keys(EXPR_SPECIAL).length,stat:exprStat(),
    badArt,cross:cross.length,crossFn:exprCrossCount(),zeroRoles,procN:proc.length,
    hit,miss,layerHit,nameBad,domOK,voiceOK,
    csvAll,csvOwn,csvName,csvGen:csvGen.slice(0,160),
    cellsAll,cellsOwn,footAll,footOwn,head,procTag,jinCanon,jinName,jinArt:jin.art,flv,
    moodKinds:Object.keys(moodSet).length,seqN:new Set(seq).size,perfOK,
    imgOK,imgBad,gifVar:getComputedStyle(document.documentElement).getPropertyValue('--catAnimGif').length};
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
                      and info['specialN'] == 95 and info['stat']['专属'] == 95
                      and info['stat']['复用'] == 89 and info['stat']['待补'] == 0
                      and len(info['zeroRoles']) == 0 and info['procN'] == 20
                      and not info['badArt'] and info['cross'] == 0 and info['crossFn'] == 0
                      and info['hit'] == 24 and info['layerHit'] == 24 and not info['nameBad']
                      and info['domOK'] and info['voiceOK']
                      and info['csvAll'] == 184 and info['csvOwn'] == 95
                      and '筛选95格' in info['csvName']
                      and '程序化本体重绘' in info['csvGen']
                      and info['cellsAll'] == 184 and info['cellsOwn'] == 95
                      and '当前筛选 184/184' in info['footAll']
                      and '当前筛选 95/184' in info['footOwn']
                      and '专属 95 · 复用 0 · 待补 0' in info['footOwn']
                      and '程序化本体重绘 20 张待 AI 重画' in info['footOwn']
                      and info['procTag'] >= 20
                      and '全谱系' in info['head']
                      and info['jinArt'] == 'R49_jinhe_scar' and info['jinCanon'] == 'cos_jinhe'
                      and info['jinName'] == '金和尚'
                      and info['flv']['n'] == 14 and info['flv']['zhu'] == 1
                      and info['flv']['tie'] == 0 and info['flv']['max'] == 22
                      and info['moodKinds'] == 8 and info['seqN'] == 8 and info['perfOK']
                      and info['imgBad'] == 0 and info['imgOK'] >= 20
                      and info['aud'] == 0 and info['gifVar'] > 50
                      and info['procArtN'] == 20 and info['r50Gen'] == 10 and info['histGen'] > 0
                      and info['r51AI'] == 10 and info['r51Wrong'] == 0
                      and info['r52AI'] == 10 and info['r52Wrong'] == 0
                      and info['hashLeft'] == 0 and info['badCanonLeft'] == 0
                      and info['defHash'] == 0 and info['aliasOK']
                      and 'R52：' in info['footVer'] and '杯雪表情谱系_R52_' in info['csvName'])
                R['browser'].append({'tag': tag, 'label': label, 'ok': bool(ok), 'info': info, 'errors': errs[:6]})
                ck(tag + ' ' + label, ok,
                   'sw=%s/iw=%s 专属=%s 复用=%s 零专属=%s 程序化=%s ProcArt=%s R50gen=%s R51AI=%s R51wrong=%s R52AI=%s R52wrong=%s hash=%s canon=%s defHash=%s alias=%s histGen=%s cross=%s hit=%s csv=%s/%s cells=%s/%s procTag=%s jin=%s/%s moods=%s perf=%s img=%s/%s errs=%s' %
                   (info['sw'], info['iw'], info['stat']['专属'], info['stat']['复用'],
                    len(info['zeroRoles']), info['procN'], info['procArtN'], info['r50Gen'], info['r51AI'], info['r51Wrong'], info['r52AI'], info['r52Wrong'],
                    info['hashLeft'], info['badCanonLeft'], info['defHash'], info['aliasOK'], info['histGen'], info['cross'], info['hit'],
                    info['csvAll'], info['csvOwn'], info['cellsAll'], info['cellsOwn'],
                    info['procTag'], info['jinCanon'], info['jinName'],
                    info['moodKinds'], info['perfOK'], info['imgOK'], info['imgBad'], errs[:1]))
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
