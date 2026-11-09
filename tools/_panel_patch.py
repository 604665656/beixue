# -*- coding: utf-8 -*-
p = '/data/workspace/杯雪游戏集_build.py'
b = open(p, encoding='utf-8').read()

def rep(old, new, label, must=1):
    global b
    n = b.count(old)
    print(label, 'count', n)
    assert n == must, label
    b = b.replace(old, new)
    return True

# ================= 1) 面板：分页卡片 + 关闭 + 滚动 =================
old_start = b.find('function toggleA11y(k){')
old_end = b.find('/* ---------- 渲染后：装饰、读屏标注、自动朗读 ---------- */', old_start)
assert old_start > 0 and old_end > old_start
new_block = r'''function toggleA11y(k){
 if(k==='hc'){HC=HC?0:1;try{localStorage.setItem(AKEY_HC,HC);}catch(e){}}
 else if(k==='big'){BIG=BIG?0:1;try{localStorage.setItem(AKEY_BIG,BIG);}catch(e){}}
 else if(k==='reduce'){REDUCE=REDUCE?0:1;try{localStorage.setItem(AKEY_RED,REDUCE);}catch(e){}}
 applyA11y(); renderA11yPanel();
 announce(({hc:'高对比',big:'大字号',reduce:'减少动效'})[k]+(k==='hc'?(HC?'已开':'已关'):k==='big'?(BIG?'已开':'已关'):(REDUCE?'已开':'已关')));
}
function setRate(v){
 RATE=[0.8,1,1.2].includes(+v)?+v:1;
 try{localStorage.setItem(AKEY_RATE,RATE);}catch(e){}
 renderA11yPanel(); announce('朗读语速 '+RATE+' 倍'); if(TTS)ttsReadNow();
}
function toggleAuto(){ TTSAUTO=TTSAUTO?0:1; renderA11yPanel();
 announce('自动跟屏朗读'+(TTSAUTO?'已开':'已关')); }

/* ---------- 设置面板：四个卡片页，一屏只给一组；可关、可滚、可 Esc ---------- */
let PANEL_TAB='sound';
const PANEL_IDS=['modePanel','diffPanel','skinPanel','a11yPanel'];
function closePanels(){ PANEL_IDS.forEach(id=>{const o=$('#'+id);if(o)o.hidden=true;}); }
function anyPanelOpen(){ return PANEL_IDS.some(id=>{const o=$('#'+id);return o&&!o.hidden;}); }
function openPanel(id){
 closePanels(); const p=$('#'+id); if(p)p.hidden=false;
 if(id==='a11yPanel')renderA11yPanel();
 if(id==='modePanel')renderModePanel();
 if(id==='diffPanel')renderDiffPanel();
 if(id==='skinPanel')renderSkinPanel();
}
function togglePanel(id){ const p=$('#'+id); if(p&&!p.hidden)closePanels(); else openPanel(id); }
function panelHead(title){
 return `<div class="pnl-h"><b>${title}</b>
  <button data-act="panel_close" aria-label="关闭设置面板" title="关闭（也可按 Esc 或点面板外）">✕ 关闭</button></div>`;
}
function openA11yPanel(){ openPanel('a11yPanel'); }

/* 四张卡：声音 / 朗读 / 视觉 / 语音。每卡最多 6 个按钮，不再一次铺 20 个 */
function renderA11yPanel(){
 const p=$('#a11yPanel'); if(!p)return;
 const b=(act,on,label,extra)=>`<button class="${on?'on':''}" data-act="${act}" ${extra||''}>${label}</button>`;
 const tabs=[['sound','声音','♫'],['read','朗读','🔊'],['view','视觉','◑'],['asr','语音','🎙']];
 const tabbar=`<div class="pnl-tabs" role="tablist" aria-label="设置分类">${tabs.map(([k,l,ic])=>
   `<button role="tab" aria-selected="${PANEL_TAB===k}" class="${PANEL_TAB===k?'on':''}"
     data-act="panel_tab" data-v="${k}">${ic} ${l}</button>`).join('')}</div>`;
 let body='';
 if(PANEL_TAB==='sound'){
  body=`<div class="grp"><b>两路背景 · 一路音效</b>
   <div class="actl">
    ${b('bgm',BGM>0,'♫ 背景 / 场景音 · '+['关','随场景','＋琴'][BGM],'title="关 → 随场景自动换音景 → 音景＋琴音"')}
    ${b('sfx',SFX>0,'♪ 点选音效 · '+(SFX?'开':'关'),'title="点击拨弦，独立于背景音"')}
   </div>
   <div class="asrstate">背景音会<b>跟着当前场景自动换音色</b>：雨驿听雨、渡口听水、书楼极静、辕门听风、秦淮带琴。点选项另有轻拨弦反馈。两者互不影响，也都不影响朗读与语音。</div></div>
   <div class="grp"><b>四路开关互不串扰</b>
   <div class="actl">
    ${b('tts',TTS>0,'🔊 朗读 · '+(TTS?'开':'关'))}
    ${b('asr',ASR>0,'🎙 语音 · '+(ASR?'开':'关'))}
   </div><div class="asrstate">朗读、语音每次打开都默认关闭且不记住；背景音、音效、高对比会记住。</div></div>`;
 }else if(PANEL_TAB==='read'){
  body=`<div class="grp"><b>朗读控制</b>
   <div class="actl">
    ${b('tts',TTS>0,'🔊 朗读 · '+(TTS?'开':'关'))}
    ${b('tts_read',0,'🔁 重读本屏')}
    ${b('tts_pause',0,'⏸ 暂停')}
    ${b('tts_stop',0,'⏹ 停止')}
    ${b('tts_auto',TTSAUTO>0,'自动跟屏 · '+(TTSAUTO?'开':'关'))}
    ${b('tts_resume',0,'▶ 继续')}
   </div></div>
   <div class="grp"><b>语速</b><div class="actl three">
    ${b('rate_set',RATE===0.8,'0.8 慢','data-v="0.8"')}
    ${b('rate_set',RATE===1,'1.0 中','data-v="1"')}
    ${b('rate_set',RATE===1.2,'1.2 快','data-v="1.2"')}
   </div><div class="asrstate">朗读用系统中文语音；<code>R</code> 重读、<code>Esc</code> 停止朗读（面板开着时先关面板）。</div></div>`;
 }else if(PANEL_TAB==='view'){
  body=`<div class="grp"><b>视觉与键盘</b><div class="actl">
    ${b('a11y_toggle',HC>0,'◑ 高对比 · '+(HC?'开':'关'),'data-v="hc"')}
    ${b('a11y_toggle',BIG>0,'🔍 大字号 · '+(BIG?'开':'关'),'data-v="big"')}
    ${b('a11y_toggle',REDUCE>0,'🍃 减少动效 · '+(REDUCE?'开':'关'),'data-v="reduce"')}
    ${b('a11y_help',0,'⌨ 键盘说明')}
   </div><div class="asrstate">高对比会压过三套皮肤，强制纯白底纯黑字；减少动效会关掉舞台入场与点选反馈动画。</div></div>
   <div class="grp"><b>界面皮肤</b><div class="actl three">
    ${SKINS.map(([k,n])=>b('skin_set',SKIN===k,n,'data-v="'+k+'"')).join('')}
   </div><div class="asrstate">只改观感，不动关卡与无障碍。header 的「◐ 皮肤」也可切。</div></div>`;
 }else{
  body=`<div class="grp"><b>🎙 语音控制</b><div class="actl">
    ${b('asr',ASR>0,'语音 · '+(ASR?'开':'关'))}
    ${b('a11y_help',0,'⌨ 键盘说明')}
   </div><div id="asrState" class="asrstate">${ASR_MSG||(SR_CTOR?'语音控制默认关闭；点此开启并授权麦克风。':'<b>当前浏览器不支持语音识别</b>　键盘与点按完全可用，所有游戏不依赖语音。')}</div></div>
   <div class="grp"><b>可以说</b><ol class="cmdlist">
    <li>开始 / 出发</li><li>下一题 / 继续</li><li>选一 ～ 选四</li>
    <li>回大厅 / 返回</li><li>朗读开 / 朗读关 / 重读</li>
    <li>背景音 / 音效 / 高对比 / 大字 / 帮助</li></ol>
   <div class="asrstate">需 Chrome / Edge 并授权麦克风；本地 <code>file://</code> 若受限，用本地 http 服务打开即可。不支持时键盘 1–4 选项、N 下一题、H 大厅、R 重读照常可用。</div></div>`;
 }
 p.innerHTML=panelHead('◐ 设置')+tabbar+`<div class="pnl-body" role="tabpanel">${body}</div>`+
  `<div class="pnl-foot">点面板外、按 Esc 或点「✕ 关闭」都能收起；四个分类随时切换。</div>`;
}

'''
b = b[:old_start] + new_block + b[old_end:]

# ================= 2) 事件：toggle / 关闭 / 分页 / 面板外点击 / 点选反馈 =================
rep("""document.body.addEventListener('click',e=>{
 const t=e.target.closest('[data-act]'); if(!t)return;
 const a=t.dataset.act, v=t.dataset.v;""",
"""document.body.addEventListener('click',e=>{
 /* 点面板外一律收起；点面板开关按钮不在这里关，交给各自分支 toggle */
 const _inPanel=e.target.closest('.modepanel');
 const _isPanelBtn=e.target.closest('[data-act$="_panel"]');
 if(!_inPanel&&!_isPanelBtn&&anyPanelOpen())closePanels();
 const t=e.target.closest('[data-act]'); if(!t)return;
 const a=t.dataset.act, v=t.dataset.v;
 /* 点选反馈：按下即给一层朱砂描边，180ms 后收；读屏同时播报 */
 if(t.matches('.opt,.eopt,.act,.m4,.mode,.d4,.d4i,.lvl,.btn,.sk-i,.pnl-tabs button')){
  t.classList.add('pressed'); setTimeout(()=>t.classList.remove('pressed'),190);
 }
 if(a==='panel_close'){ closePanels(); announce('已关闭设置面板'); return; }
 if(a==='panel_tab'){ PANEL_TAB=v; renderA11yPanel(); return; }""", 'dispatch 头部')

rep(""" if(a==='skin_panel'){
  const p=$('#skinPanel'); if(p){p.hidden=!p.hidden; if(!p.hidden)renderSkinPanel();}
  ['modePanel','diffPanel','a11yPanel'].forEach(id=>{const o=$('#'+id);if(o)o.hidden=true;});
  return;
 }
 if(a==='skin_set'){ setSkin(v); const p=$('#skinPanel'); if(p)p.hidden=true; return; }
 if(a==='mode_panel'){
  const p=$('#modePanel'); if(p){p.hidden=!p.hidden; if(!p.hidden)renderModePanel();}
  return;
 }
 if(a==='mode_set'){ setMode(v); const p=$('#modePanel'); if(p)p.hidden=true; return; }
 if(a==='diff_panel'){
  const p=$('#diffPanel'); if(p){p.hidden=!p.hidden; if(!p.hidden)renderDiffPanel();}
  const m=$('#modePanel'); if(m)m.hidden=true;
  return;
 }
 if(a==='diff_set'){ setDiff(v); const p=$('#diffPanel'); if(p)p.hidden=true; return; }""",
""" if(a==='skin_panel'){ togglePanel('skinPanel'); return; }
 if(a==='skin_set'){ setSkin(v); if(PANEL_TAB==='view')renderA11yPanel(); else closePanels(); return; }
 if(a==='mode_panel'){ togglePanel('modePanel'); return; }
 if(a==='mode_set'){ setMode(v); closePanels(); return; }
 if(a==='diff_panel'){ togglePanel('diffPanel'); return; }
 if(a==='diff_set'){ setDiff(v); closePanels(); return; }""", '面板 toggle')

rep(" if(a==='a11y_panel'){ openA11yPanel(); return; }",
    " if(a==='a11y_panel'){ togglePanel('a11yPanel'); return; }", 'a11y toggle')

# Esc 优先关面板
rep(" if(k==='escape'){ttsStop();announce('已停止朗读');return;}",
""" if(k==='escape'){ if(anyPanelOpen()){closePanels();announce('已关闭设置面板');return;} ttsStop();announce('已停止朗读');return; }""", 'Esc 关面板')

# ================= 3) 面板头部 CSS + 横屏 CSS =================
CSS = r'''
/* ---------- 设置面板：卡片分页 ---------- */
.pnl-h{display:flex;align-items:center;justify-content:space-between;gap:10px;
 padding:0 2px 9px;border-bottom:1px solid var(--line);margin-bottom:9px}
.pnl-h b{font-size:13px;letter-spacing:.08em;font-family:var(--titlefont)}
.pnl-h button{border:1px solid var(--line);background:var(--card);color:var(--ink);
 border-radius:7px;padding:4px 9px;font-size:11px;cursor:pointer;white-space:nowrap}
.pnl-h button:hover{border-color:var(--red);color:var(--red)}
.pnl-tabs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:5px;margin-bottom:10px}
.pnl-tabs button{border:1px solid var(--line);background:var(--paper);color:var(--muted);
 border-radius:7px;padding:7px 2px;font-size:11px;cursor:pointer;white-space:nowrap}
.pnl-tabs button.on{background:var(--green);border-color:var(--green);color:#fff;font-weight:700}
.pnl-body{min-height:120px}
.pnl-foot{font-size:10px;color:var(--muted);line-height:1.7;margin-top:9px;
 padding-top:8px;border-top:1px dashed var(--line)}
.actl.three{grid-template-columns:repeat(3,minmax(0,1fr))}
.modepanel{max-height:calc(100vh - 92px);max-height:calc(100dvh - 92px);
 overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch}
.a11ypanel .cmdlist{margin:6px 0 0;padding-left:18px}
/* 点选反馈：按下瞬间的朱砂描边 + 轻缩 */
.pressed{animation:pressPulse .19s ease-out both}
@keyframes pressPulse{0%{box-shadow:0 0 0 0 rgba(155,58,47,.42);transform:scale(.985)}
 100%{box-shadow:0 0 0 5px rgba(155,58,47,0);transform:scale(1)}}
body.hc .pressed{animation:none;outline:3px solid #000}
body.reduce .pressed{animation:none}

/* ---------- 舞台动画表演 ---------- */
@keyframes stageIn{from{opacity:.45;filter:blur(3px)}to{opacity:1;filter:blur(0)}}
@keyframes catIn{from{opacity:0;transform:translateY(16px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
@keyframes catNod{0%{transform:translateY(0)}38%{transform:translateY(-9px) scale(1.02)}100%{transform:translateY(0)}}
@keyframes catShake{0%{transform:translateX(0)}30%{transform:translateX(-5px)}65%{transform:translateX(4px)}100%{transform:translateX(0)}}
.stage{animation:stageIn .55s ease-out both}
.stage .stagecut{animation:catIn .48s cubic-bezier(.22,.9,.3,1) both}
.stage.ok .stagecut{animation:catNod .5s ease-out both}
.stage.no .stagecut{animation:catShake .42s ease-out both}
.stage.ok{box-shadow:0 0 0 2px rgba(165,130,62,.55),var(--shadow)}
.stage.no{box-shadow:0 0 0 2px rgba(155,58,47,.55),var(--shadow)}
body.reduce .stage,body.reduce .stage .stagecut,
body.reduce .stage.ok .stagecut,body.reduce .stage.no .stagecut{animation:none}

/* ---------- 手机横屏 ---------- */
@media (orientation:landscape) and (max-height:560px){
 header{padding:6px 12px 5px;gap:6px;flex-wrap:nowrap}
 .seal{width:28px;height:28px;font-size:9px;border-radius:3px}
 h1{font-size:15px;margin:0}
 .sub{display:none}
 .brand{gap:8px}
 .hctl{gap:4px;flex-wrap:nowrap;overflow-x:auto;justify-content:flex-end;scrollbar-width:none}
 .hctl::-webkit-scrollbar{display:none}
 .hctl button{padding:4px 8px;font-size:10.5px;flex:0 0 auto}
 #nav{overflow-x:auto;white-space:nowrap}
 #nav button{padding:5px 10px;font-size:11px}
 .stage,.stage.sm{aspect-ratio:auto;height:clamp(112px,26vh,186px);max-height:none}
 .stage .stagecut{background-size:auto 100%;background-position:center bottom;
  transform:scale(1.04);transform-origin:center bottom}
 .stage .stagecap{padding:5px 9px;font-size:9.5px}
 .hallhero2{padding:12px 16px;gap:14px;grid-template-columns:minmax(0,1fr) 230px}
 .hh-cat img{max-height:170px;object-fit:cover;object-position:center 42%}
 .hh-txt h2{font-size:20px;line-height:1.4;margin-bottom:6px}
 .hallhero2 p{font-size:12px;line-height:1.7;margin-bottom:8px}
 .hallhero2 .quote{font-size:11.5px;margin-bottom:9px;padding:6px 9px}
 .sig{margin-top:6px;font-size:9.5px}
 .hero{padding:14px 16px;margin:8px 0 12px}
 .hero h2{font-size:19px}
 .hero p{font-size:12.5px;line-height:1.75}
 .lvlmap{grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
 .lvl{padding:10px 11px}
 .modes4{grid-template-columns:repeat(4,minmax(0,1fr))}
 .d4{grid-template-columns:repeat(3,minmax(0,1fr))}
 .m4,.d4i{padding:9px}
 .modepanel{width:min(420px,calc(100vw - 24px));right:12px;top:100%;
  max-height:calc(100vh - 74px);max-height:calc(100dvh - 74px)}
 .catbar{padding:7px 9px}
 .cb-note{display:none}
 footer{padding-bottom:14px}
}
'''
rep('</style>\n</head>', CSS + '\n</style>\n</head>', '面板与横屏 CSS')

# 启动：渲染空面板内容
rep('renderA11yPanel();\n/* 上次若开着背景音',
    'renderA11yPanel();\n/* 上次若开着背景音', 'noop', 1)

open(p, 'w', encoding='utf-8').write(b)
print('SAVED panel+landscape')
