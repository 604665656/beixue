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

# ============ 1) 气泡更通透 ============
rep(""" background:rgba(251,246,233,.92);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);
 border:1px solid rgba(155,58,47,.20);
 box-shadow:0 6px 20px rgba(30,22,14,.22);""",
""" background:rgba(251,246,233,.70);backdrop-filter:blur(7px) saturate(1.05);-webkit-backdrop-filter:blur(7px) saturate(1.05);
 border:1px solid rgba(155,58,47,.13);
 box-shadow:0 4px 15px rgba(30,22,14,.15);""", '气泡透明度')

rep(".avgframe>.avgblock .opt{background:rgba(255,255,255,.78)}",
    " .avgframe>.avgblock .opt{background:rgba(255,255,255,.56)}", '选项底色')
rep(".avgframe>.avgblock .explain,.avgframe>.avgblock .guide,\n.avgframe>.avgblock .hintbox{background:rgba(255,255,255,.55);border-radius:8px}",
    ".avgframe>.avgblock .explain,.avgframe>.avgblock .guide,\n.avgframe>.avgblock .hintbox{background:rgba(255,255,255,.42);border-radius:8px}", '解释块底色')
rep("html[data-skin=\"night\"] .avgframe>.avgblock{background:rgba(29,38,42,.90);",
    "html[data-skin=\"night\"] .avgframe>.avgblock{background:rgba(29,38,42,.68);", '夜雨气泡')
rep("html[data-skin=\"night\"] .avgblock .opt{background:rgba(20,26,29,.72)}",
    "html[data-skin=\"night\"] .avgblock .opt{background:rgba(20,26,29,.52)}", '夜雨选项')
rep(" background:rgba(251,246,233,.88);color:var(--ink);\n border:1px solid rgba(155,58,47,.28);box-shadow:0 3px 12px rgba(0,0,0,.16)}",
    " background:rgba(251,246,233,.78);color:var(--ink);\n border:1px solid rgba(155,58,47,.18);box-shadow:0 2px 9px rgba(0,0,0,.12)}", '名牌更淡')
rep("html[data-skin=\"night\"] .avgwho{background:rgba(29,38,42,.90);color:var(--ink);",
    "html[data-skin=\"night\"] .avgwho{background:rgba(29,38,42,.76);color:var(--ink);", '夜雨名牌')

# ============ 2) 界面更简洁：引用、标签、说明折叠、选项颜色 ============
rep(""".hallhero2 .quote{font-size:12px;line-height:1.85;border-left:3px solid var(--red);padding:3px 0 3px 11px;
 color:var(--ink);margin:0 0 12px;background:linear-gradient(90deg,rgba(168,66,58,.06),transparent)}""",
""".hallhero2 .quote{font-size:12px;line-height:1.8;border-left:1px solid var(--line);padding:2px 0 2px 10px;
 color:var(--muted);margin:0 0 10px;background:transparent}""", '引用框变淡')

rep(""".eopt{display:block;width:100%;text-align:left;border:1px solid var(--line);background:var(--card);
 border-radius:11px;padding:12px 13px;margin:0 0 8px;font-size:13px;line-height:1.7;cursor:pointer}""",
""".eopt{display:block;width:100%;text-align:left;border:1px solid var(--line);background:rgba(255,255,255,.62);
 border-radius:10px;padding:11px 12px;margin:0 0 7px;font-size:13px;line-height:1.65;
 color:var(--ink);cursor:pointer}""", '选项去蓝字')

# 大厅 pill 精简
rep("""   <div class="btnrow"><span class="pill">二十四关 · 七卷 · 四模式 · 三难度</span><span class="pill">档案逐步解锁</span>
    <span class="pill">单文件 · 离线</span><span class="pill">♫ 背景／♪ 音效／🔊 朗读／🎙 语音 各自独立</span></div>
   <div class="sig">哈士喵 · 作者授权厚涂风格角色　｜　水墨题图为非原著插图　｜　${modeInfo().icon} <b>${modeInfo().name}</b>　·　${diffInfo().icon} <b>${diffInfo().name}</b></div>""",
"""   <div class="btnrow"><span class="pill">二十四关 · 七卷</span><span class="pill">档案逐步解锁 · 单文件离线</span></div>
   <div class="sig">哈士喵 · 作者授权厚涂角色　｜　${modeInfo().icon} ${modeInfo().name} · ${diffInfo().icon} ${diffInfo().name}</div>""", '大厅标签精简')

# 大厅长说明折叠
rep(""" <div class="inkdiv"></div>
 <div class="btnrow"><button class="btn" data-act="go" data-v="${LAST}">继续上次 · ${esc((D.meta.levels.find(l=>l.id===LAST)||{}).t||'你是《杯雪》里的谁')}</button>
  <button class="btn ghost" data-act="go" data-v="arch">翻档案 · ${au}/${at} 页已开</button></div>
 <p class="hint">七卷按「入局 → 章句 → 人事 → 武学 → 世道 → 改编 → 补遗」排：卷一打底并留两处翻底，卷二到卷五把词源、人事、武学、史实逐层拆开，卷六专练「把改编新增的还给改编」，卷七把上一轮标「资料不足」的逐项填平。第七关起建议先把难度切到「● 校勘」，否则考据题不出现。前三关不卡满星，是故意留的进入余量。</p>
 <p class="music-note">顶部 <b>♫ 场景音</b>（关 → 随场景自动换音景 → 音景＋琴音）与 <b>♪ 音效</b>（点选拨弦、答对上行／答错下行）是<b>两个独立开关</b>；雨驿听雨、渡口听水、书楼极静、辕门听风、秦淮带琴，换关自动平滑过渡。全部由浏览器实时合成，无音频文件、不联网，默认都关。</p>`;""",
""" <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="go" data-v="${LAST}">继续上次 · ${esc((D.meta.levels.find(l=>l.id===LAST)||{}).t||'你是《杯雪》里的谁')}</button>
  <button class="btn ghost" data-act="go" data-v="arch">翻档案 · ${au}/${at} 页已开</button></div>
 <details class="hallmore"><summary>读法与说明</summary>
  <p>七卷按「入局 → 章句 → 人事 → 武学 → 世道 → 改编 → 补遗」排：卷一打底并留两处翻底，卷二到卷五把词源、人事、武学、史实逐层拆开，卷六专练「把改编新增的还给改编」，卷七把上一轮标「资料不足」的逐项填平。第七关起建议先把难度切到「● 校勘」；前三关不卡满星，是故意留的进入余量。</p>
  <p>顶部 <b>♫ 场景音</b> 与 <b>♪ 音效</b> 是两个独立开关；天晴有鸟鸣、雨夜有远雷，换关自动平滑过渡。全部实时合成、无音频文件、默认都关。朗读与语音默认关闭。</p>
 </details>`;""", '大厅说明折叠')

# 折叠块 CSS
rep('</style>\n</head>', r'''
/* ---------- 简洁化：说明折叠、细分隔 ---------- */
.hallmore{margin:12px 2px 0;border-top:1px dashed var(--line);padding-top:8px;
 font-size:11px;color:var(--muted);line-height:1.75}
.hallmore summary{cursor:pointer;list-style:none;font-size:11px;letter-spacing:.06em;
 color:var(--purple);padding:3px 0}
.hallmore summary::-webkit-details-marker{display:none}
.hallmore summary:before{content:"◇ ";}
.hallmore[open] summary:before{content:"◆ ";}
.hallmore p{margin:7px 0 0}
.avgframe>.avgblock .hallmore{border-color:rgba(155,58,47,.18)}
body.hc .hallmore{color:#000}
''' + '\n</style>\n</head>', '折叠块 CSS')

# ============ 3) E 关：去掉重复标签 ============
rep("""  <div class="bar" style="margin:0 0 10px"><span class="pill">当前模式</span>${chip}
   <span class="pill">★ ${(PROG.E||{}).stars||0}/3</span><span class="pill">八种侠气</span></div>""",
"""  <div class="bar" style="margin:0 0 10px">${chip}<span class="pill">12 题 · 八种侠气</span></div>""", 'E intro 去重')

rep(""" return `<div class="bar">${chip}<span class="pill">${E.i+1} / ${d.quiz.length}</span>
  <span class="pill">${modeInfo().name}</span></div>
  <div class="prog"><i style="width:${pct}%"></i></div>""",
""" return `<div class="bar">${chip}<span class="pill">${E.i+1} / ${d.quiz.length}</span></div>
  <div class="prog"><i style="width:${pct}%"></i></div>""", 'E play 去重')

# ============ 4) applyAVG：合并空条与进度条，不再出现孤立白块 ============
rep(""" const sibs=[...app.children].filter(el=>el!==frame);
 sibs.forEach((el,i)=>{
  if(el.id==='dressMount')return;
  el.classList.add('avgblock');
  if(i===0)el.classList.add('avgbubble');
  if(el.querySelector('.opt,[data-act$="_ans"],[data-act$="_choose"],[data-act$="_sel"],[data-act$="_start"]'))
   el.classList.add('avg-noscroll');
  frame.appendChild(el);
 });""",
""" const sibs=[...app.children].filter(el=>el!==frame);
 let first=true, last=null;
 sibs.forEach(el=>{
  if(el.id==='dressMount')return;
  /* 进度条、装饰分隔、纯空占位并进上一块，避免屏幕上出现孤立的空白米白条 */
  if(el.classList.contains('prog')||el.classList.contains('inkdiv')||
     (!el.textContent.trim()&&!el.querySelector('button,img,[data-bg],[data-art]'))){
   (last||frame).appendChild(el); return;
  }
  el.classList.add('avgblock');
  if(first){el.classList.add('avgbubble');first=false;}
  frame.appendChild(el); last=el;
 });""", 'AVG 合并空块')

open(p, 'w', encoding='utf-8').write(b)
print('SAVED clean+transparent')
