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

# ============================================================
# 1) 天气 / 场景演出映射
# ============================================================
SCENE_MAP = r'''
/* ---------- AVG 演出：天气、光、飞鸟与场景音 ----------
   11 张背景板 -> 6 类天气动画 + 4 类环境音。纯 CSS 动画与 Web Audio 实时合成，无图片/音频文件。 */
const SCENE_WEATHER={
 rain:      {fx:'rain',  amb:'rain',  label:'秋雨'},
 qilipu:    {fx:'rain',  amb:'rain',  label:'驿道冷雨'},
 haodenglou:{fx:'rain',  amb:'rain',  label:'临安夜雨'},
 dujiang:   {fx:'sun',   amb:'birds', label:'拂晓晴光'},
 bailuzhou: {fx:'birds', amb:'birds', label:'芦荡晴日'},
 shulou:    {fx:'dust',  amb:'quiet', label:'书楼窗光'},
 moling:    {fx:'snow',  amb:'wind',  label:'秣陵落雪'},
 dashipo:   {fx:'snow',  amb:'wind',  label:'石阵风雪'},
 yuanmen:   {fx:'wind',  amb:'wind',  label:'辕门朔风'},
 huai:      {fx:'night', amb:'quiet', label:'淮上夜帐'},
 qinhuai:   {fx:'night', amb:'night', label:'秦淮灯夜'}
};
const FX_LABEL={rain:'雨丝',sun:'晨光与飞鸟',birds:'晴日飞鸟',dust:'窗光浮尘',snow:'落雪',wind:'朔风',night:'灯火浮絮'};
function sceneWeather(bg){ return SCENE_WEATHER[bg]||SCENE_WEATHER.rain; }
'''
rep('/* ---------- nav ---------- */', SCENE_MAP + '\n/* ---------- nav ---------- */', 'SCENE_WEATHER')

# ============================================================
# 2) stageBlock 注入天气层与名牌
# ============================================================
rep(''' return `<div class="stage ${compact?'sm':''}" role="img"
   aria-label="场景：${esc(bl)}；角色：哈士喵扮作${esc(cl)}">
   <div class="stagebg" data-bg="bg_${s.bg}"
     style="background-position:${vw[0]};filter:${vw[1]}"></div>
   <div class="stagecut" data-art="${s.cast}"></div>
   <div class="stagecap"><span class="stageloc">◈ ${esc(bl)}</span>
    <span class="stagewho">哈士喵 · ${esc(cl)}</span></div></div>`;''',
''' const wx=sceneWeather(s.bg);
 return `<div class="stage ${compact?'sm':''}" role="img" data-weather="${wx.fx}"
   aria-label="场景：${esc(bl)}，${esc(wx.label)}，${esc(FX_LABEL[wx.fx])}；角色：哈士喵扮作${esc(cl)}">
   <div class="stagebg" data-bg="bg_${s.bg}"
     style="background-position:${vw[0]};filter:${vw[1]}"></div>
   <div class="stagefx fx-${wx.fx}" aria-hidden="true">
    <i class="fx-a"></i><i class="fx-b"></i><i class="fx-c"></i>
    <span class="bird b1"></span><span class="bird b2"></span><span class="bird b3"></span>
    <span class="glow"></span><span class="spark s1"></span><span class="spark s2"></span><span class="spark s3"></span>
   </div>
   <div class="stagecut" data-art="${s.cast}"></div>
   <div class="stagevign" aria-hidden="true"></div>
   <div class="avgwho"><span class="avgdot"></span><b>哈士喵 · ${esc(cl)}</b>
    <em>◈ ${esc(bl)}　${esc(wx.label)}</em></div>
   <div class="stagecap"><span class="stageloc">◈ ${esc(bl)}</span>
    <span class="stagewho">哈士喵 · ${esc(cl)}</span></div></div>`;''', 'stageBlock 天气层')

# ============================================================
# 3) AVG 包装：把 stage 与本屏文字包进同一画面
# ============================================================
AVG_JS = r'''
/* ---------- AVG 演出层：文字与选项都叠在画面上 ----------
   只移动 DOM 一次，不改关卡数据；所有事件仍走 body 委托，朗读 innerText 仍能读到全文。 */
const AKEY_AVG='beixue_avg_v1';
let AVGON=1;
try{ const v=localStorage.getItem(AKEY_AVG); if(v!==null)AVGON=(+v===1)?1:0; }catch(e){}
function setAVG(v){
 AVGON=v?1:0; try{localStorage.setItem(AKEY_AVG,AVGON);}catch(e){}
 render(); announce('AVG 画面演出已'+(AVGON?'开启':'关闭'));
}
function applyAVG(){
 const app=$('#app'); if(!app)return;
 if(!AVGON||!D.meta.levels.some(l=>l.id===TAB))return;
 const st=app.querySelector('.stage'); if(!st)return;
 const wx=sceneWeather(stageFor(TAB).bg);
 const frame=document.createElement('div');
 frame.className='avgframe fx-'+wx.fx;
 frame.setAttribute('data-weather',wx.fx);
 st.parentNode.insertBefore(frame,st);
 frame.appendChild(st);
 const sibs=[...app.children].filter(el=>el!==frame);
 sibs.forEach((el,i)=>{
  if(el.id==='dressMount')return;
  el.classList.add('avgblock');
  if(i===0)el.classList.add('avgbubble');
  frame.appendChild(el);
 });
 frame.setAttribute('aria-label','场景画面：'+wx.label+'，'+FX_LABEL[wx.fx]+'；下方为对话与选项');
}
'''
rep('/* ---------- 渲染后：装饰、读屏标注、自动朗读 ---------- */',
    AVG_JS + '\n/* ---------- 渲染后：装饰、读屏标注、自动朗读 ---------- */', 'AVG JS')

rep(''' afterRender();
 if(BGM>0)retuneScene(currentSceneBg());''',
''' afterRender();
 applyAVG();
 if(BGM>0)retuneScene(currentSceneBg());''', 'render 调 applyAVG')

# ============================================================
# 4) 视觉卡加 AVG 开关
# ============================================================
rep('''    ${b('a11y_toggle',REDUCE>0,'🍃 减少动效 · '+(REDUCE?'开':'关'),'data-v="reduce"')}
    ${b('a11y_help',0,'⌨ 键盘说明')}
   </div><div class="asrstate">高对比会压过三套皮肤，强制纯白底纯黑字；减少动效会关掉舞台入场与点选反馈动画。</div></div>''',
'''    ${b('a11y_toggle',REDUCE>0,'🍃 减少动效 · '+(REDUCE?'开':'关'),'data-v="reduce"')}
    ${b('avg_set',AVGON>0,'◈ AVG 画面 · '+(AVGON?'开':'关'))}
    ${b('a11y_help',0,'⌨ 键盘说明')}
   </div><div class="asrstate">AVG 画面把文字与选项叠进场景气泡，并播放当前天气动画（雨／雪／晨光／飞鸟／灯火）；关掉则回到「图在上、白卡在下」。高对比压过皮肤，减少动效会停掉所有粒子与入场动画。</div></div>''', '视觉卡 AVG 开关')

rep(" if(a==='panel_tab'){ PANEL_TAB=v; renderA11yPanel(); return; }",
    """ if(a==='panel_tab'){ PANEL_TAB=v; renderA11yPanel(); return; }
 if(a==='avg_set'){ setAVG(AVGON?0:1); renderA11yPanel(); return; }""", 'AVG 事件')

# ============================================================
# 5) CSS：AVG 画面 + 六类天气动画
# ============================================================
AVG_CSS = r'''
/* ================= AVG 演出层：整屏就是画面 ================= */
.avgframe{position:relative;isolation:isolate;overflow:hidden;
 border-radius:var(--radius);margin:0 0 12px;
 min-height:clamp(420px,62vh,660px);
 box-shadow:var(--shadow);border:1px solid var(--line)}
.avgframe>.stage{position:absolute;inset:0;width:100%;height:100%;
 aspect-ratio:auto;max-height:none;border:0;border-radius:0;margin:0;
 animation:none;box-shadow:none;z-index:0}
.avgframe>.stage .stagebg{position:absolute;inset:0;background-size:cover;
 background-position:center 38%;animation:stagePan 18s ease-in-out infinite alternate}
.avgframe>.stage .stagecut{position:absolute;left:3%;top:4%;width:47%;height:58%;
 background-size:contain;background-repeat:no-repeat;background-position:left bottom;
 animation:catIn .55s cubic-bezier(.22,.9,.3,1) both;z-index:2}
.avgframe>.stage .stagevign{position:absolute;inset:0;z-index:1;pointer-events:none;
 background:linear-gradient(180deg,rgba(20,16,12,.10) 0%,transparent 34%,
  rgba(20,16,12,.10) 52%,rgba(20,16,12,.52) 100%)}
.avgframe>.stage .stagecap{display:none}
.avgframe>.stage .avgwho{position:absolute;z-index:3;left:3%;top:2.5%;
 display:flex;align-items:center;gap:7px;flex-wrap:wrap;
 padding:5px 10px;border-radius:6px;font-size:10.5px;letter-spacing:.05em;
 background:rgba(251,246,233,.88);color:var(--ink);
 border:1px solid rgba(155,58,47,.28);box-shadow:0 3px 12px rgba(0,0,0,.16)}
.avgwho .avgdot{width:7px;height:7px;background:var(--red);transform:rotate(45deg);flex:0 0 auto}
.avgwho b{font-family:var(--titlefont);font-size:12px}
.avgwho em{font-style:normal;color:var(--muted);font-size:9.5px}
/* 本屏文字：气泡 + 选项都浮在画面上 */
.avgframe>.avgblock{position:relative;z-index:4;margin:0 10px 9px;
 border-radius:12px;padding:12px 14px;
 background:rgba(251,246,233,.92);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);
 border:1px solid rgba(155,58,47,.20);
 box-shadow:0 6px 20px rgba(30,22,14,.22);
 color:var(--ink)}
.avgframe>.avgblock:first-of-type{margin-top:clamp(190px,34vh,300px)}
.avgframe>.avgbubble:before{content:"";position:absolute;top:-9px;left:26px;
 width:16px;height:16px;background:inherit;border-left:1px solid rgba(155,58,47,.20);
 border-top:1px solid rgba(155,58,47,.20);transform:rotate(45deg);border-radius:2px}
.avgframe>.avgblock h2,.avgframe>.avgblock h3{font-size:17px;margin:0 0 7px}
.avgframe>.avgblock p{font-size:13px;line-height:1.85;margin:0 0 7px}
.avgframe>.avgblock .opt{background:rgba(255,255,255,.78)}
.avgframe>.avgblock .btn{box-shadow:0 3px 10px rgba(0,0,0,.16)}
.avgframe>.avgblock .explain,.avgframe>.avgblock .guide,
.avgframe>.avgblock .hintbox{background:rgba(255,255,255,.55);border-radius:8px}
html[data-skin="night"] .avgframe>.avgblock{background:rgba(29,38,42,.90);
 border-color:rgba(217,168,92,.28);color:var(--ink)}
html[data-skin="night"] .avgblock .opt{background:rgba(20,26,29,.72)}
html[data-skin="night"] .avgwho{background:rgba(29,38,42,.90);color:var(--ink);
 border-color:rgba(217,168,92,.32)}
html[data-skin="night"] .avgframe>.stage .stagevign{
 background:linear-gradient(180deg,rgba(0,0,0,.22) 0%,transparent 34%,rgba(0,0,0,.30) 52%,rgba(0,0,0,.70) 100%)}
body.hc .avgframe>.avgblock{background:#fff!important;border:2px solid #000!important;
 color:#000!important;backdrop-filter:none}
body.hc .avgframe>.avgblock .opt{background:#fff;color:#000;border:2px solid #000}
body.hc .avgwho{background:#fff;color:#000;border:2px solid #000}

/* ---------- 六类天气动画（全部 pointer-events:none） ---------- */
.stagefx{position:absolute;inset:0;z-index:1;pointer-events:none;overflow:hidden}
.stagefx i,.stagefx span{position:absolute;display:block}
/* 雨：两层斜线错位滚动 + 底部水花 */
.fx-rain .fx-a{inset:-40% -20%;opacity:.34;
 background:repeating-linear-gradient(104deg,transparent 0 7px,rgba(214,229,238,.55) 7px 8px,transparent 8px 15px);
 animation:rainFall .62s linear infinite}
.fx-rain .fx-b{inset:-40% -20%;opacity:.20;
 background:repeating-linear-gradient(100deg,transparent 0 13px,rgba(235,244,250,.60) 13px 14px,transparent 14px 27px);
 animation:rainFall 1.05s linear infinite}
@keyframes rainFall{from{transform:translate3d(-4%,-8%,0)}to{transform:translate3d(4%,8%,0)}}
.fx-rain .fx-c{left:0;right:0;bottom:0;height:26%;opacity:.30;
 background:radial-gradient(ellipse at 20% 100%,rgba(226,238,246,.7) 0 2px,transparent 3px),
  radial-gradient(ellipse at 68% 100%,rgba(226,238,246,.6) 0 2px,transparent 3px);
 animation:puddle 1.7s ease-in-out infinite}
@keyframes puddle{0%,100%{opacity:.12}50%{opacity:.38}}
/* 雪：两层圆点飘落 */
.fx-snow .fx-a,.fx-snow .fx-b{inset:-20% -10%;
 background-image:radial-gradient(circle,rgba(255,255,255,.85) 0 1.6px,transparent 2px),
  radial-gradient(circle,rgba(255,255,255,.55) 0 1.1px,transparent 1.6px);
 background-size:74px 74px,52px 52px;background-position:0 0,26px 18px}
.fx-snow .fx-a{opacity:.55;animation:snowFall 9s linear infinite}
.fx-snow .fx-b{opacity:.35;background-size:110px 110px,86px 86px;animation:snowFall 15s linear infinite reverse}
@keyframes snowFall{from{transform:translate3d(-14px,-40px,0)}to{transform:translate3d(22px,80px,0)}}
.fx-snow .fx-c{inset:0;background:linear-gradient(180deg,rgba(196,214,224,.10),transparent 60%)}
/* 晨光：斜射光柱 + 光斑缓慢漂移 */
.fx-sun .glow{width:62%;height:62%;left:34%;top:-16%;border-radius:50%;
 background:radial-gradient(circle,rgba(255,226,158,.52),rgba(255,214,130,.14) 48%,transparent 72%);
 animation:sunDrift 11s ease-in-out infinite alternate}
@keyframes sunDrift{from{transform:translate(-14px,-8px) scale(1)}to{transform:translate(18px,14px) scale(1.12)}}
.fx-sun .fx-a{inset:-10%;opacity:.24;
 background:linear-gradient(112deg,transparent 34%,rgba(255,236,186,.50) 42%,transparent 50%,
  transparent 62%,rgba(255,236,186,.34) 68%,transparent 76%);
 animation:raySwing 13s ease-in-out infinite alternate}
@keyframes raySwing{from{transform:translateX(-24px) skewX(-3deg)}to{transform:translateX(26px) skewX(3deg)}}
.fx-sun .fx-b{inset:0;background:radial-gradient(circle at 78% 22%,rgba(255,245,214,.30),transparent 42%)}
/* 飞鸟（晴日 / 晨光共用） */
.bird{width:16px;height:8px;opacity:.62;
 background:no-repeat center/contain url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'><path d='M1 8 Q6 1 12 7 Q18 1 23 8' fill='none' stroke='%233B3630' stroke-width='1.7' stroke-linecap='round'/></svg>")}
.fx-sun .bird,.fx-birds .bird{animation:birdFly linear infinite}
.b1{left:-8%;top:20%;animation-duration:13s!important;animation-delay:0s!important}
.b2{left:-8%;top:29%;animation-duration:17s!important;animation-delay:4s!important;transform:scale(.75)}
.b3{left:-8%;top:15%;animation-duration:20s!important;animation-delay:9s!important;transform:scale(.58)}
@keyframes birdFly{0%{transform:translate(-10vw,10px) scale(1)}
 25%{transform:translate(26vw,-16px) scale(.92)}
 50%{transform:translate(58vw,4px) scale(.86)}
 75%{transform:translate(90vw,-12px) scale(.78)}
 100%{transform:translate(122vw,8px) scale(.7)}}
.fx-birds .glow{width:54%;height:54%;right:4%;top:-14%;border-radius:50%;
 background:radial-gradient(circle,rgba(255,232,174,.42),transparent 70%);
 animation:sunDrift 14s ease-in-out infinite alternate}
.fx-birds .fx-c{left:0;right:0;bottom:0;height:34%;opacity:.30;
 background:repeating-linear-gradient(88deg,transparent 0 16px,rgba(120,132,86,.30) 16px 18px,transparent 18px 34px);
 animation:reedSway 5s ease-in-out infinite alternate}
@keyframes reedSway{from{transform:skewX(-1.5deg)}to{transform:skewX(1.5deg)}}
/* 窗光浮尘 */
.fx-dust .glow{inset:0;background:linear-gradient(118deg,rgba(255,238,196,.28),transparent 46%)}
.fx-dust .spark{width:4px;height:4px;border-radius:50%;background:rgba(255,240,204,.75);
 box-shadow:0 0 6px rgba(255,238,190,.7);animation:dustFloat linear infinite}
.fx-dust .s1{left:22%;top:70%;animation-duration:11s}
.fx-dust .s2{left:56%;top:80%;animation-duration:14s;animation-delay:3s}
.fx-dust .s3{left:76%;top:64%;animation-duration:17s;animation-delay:7s}
@keyframes dustFloat{0%{transform:translate(0,0);opacity:0}
 20%{opacity:.8}80%{opacity:.6}100%{transform:translate(-40px,-160px);opacity:0}}
/* 朔风 / 旗影 */
.fx-wind .fx-a{inset:0;opacity:.26;
 background:repeating-linear-gradient(6deg,transparent 0 20px,rgba(214,202,176,.42) 20px 21px,transparent 21px 44px);
 animation:windGust 3.4s ease-in-out infinite}
@keyframes windGust{0%,100%{transform:translateX(-16px);opacity:.12}
 50%{transform:translateX(26px);opacity:.34}}
.fx-wind .fx-b{right:8%;top:10%;width:34%;height:40%;opacity:.22;
 background:linear-gradient(160deg,rgba(155,58,47,.5),transparent 70%);
 clip-path:polygon(0 0,100% 12%,86% 52%,100% 100%,0 84%);
 transform-origin:left center;animation:flagWave 2.6s ease-in-out infinite alternate}
@keyframes flagWave{from{transform:skewY(-5deg) scaleX(.94)}to{transform:skewY(6deg) scaleX(1.04)}}
/* 灯火浮絮 / 夜 */
.fx-night .spark{width:5px;height:5px;border-radius:50%;
 background:rgba(255,206,120,.9);box-shadow:0 0 12px 3px rgba(255,190,96,.5);
 animation:lampBlink ease-in-out infinite alternate}
.fx-night .s1{left:16%;top:34%;animation-duration:2.1s}
.fx-night .s2{left:72%;top:26%;animation-duration:2.8s;animation-delay:.7s}
.fx-night .s3{left:88%;top:48%;animation-duration:3.3s;animation-delay:1.4s}
@keyframes lampBlink{from{opacity:.35;transform:scale(.8)}to{opacity:1;transform:scale(1.25)}}
.fx-night .fx-c{inset:0;background:radial-gradient(ellipse at 50% 100%,transparent 40%,rgba(12,18,22,.28))}
.fx-night .fx-a{inset:-20%;opacity:.22;
 background-image:radial-gradient(circle,rgba(255,232,188,.5) 0 1.2px,transparent 1.8px);
 background-size:96px 96px;animation:snowFall 22s linear infinite}
/* 减少动效：粒子全停 */
body.reduce .stagefx i,body.reduce .stagefx span,
body.reduce .avgframe>.stage .stagebg,body.reduce .avgframe>.stage .stagecut,
body.reduce .stagebg,body.reduce .stage{animation:none!important}
body.hc .stagefx{display:none}
/* 横屏：画面区压缩，气泡更早出现 */
@media (orientation:landscape) and (max-height:560px){
 .avgframe{min-height:clamp(280px,72vh,420px)}
 .avgframe>.stage .stagecut{width:34%;height:66%;left:2%;top:2%}
 .avgframe>.avgblock:first-of-type{margin-top:clamp(126px,30vh,190px)}
 .avgframe>.avgblock{padding:9px 12px;margin:0 10px 7px}
 .avgframe>.avgblock p{font-size:12px;line-height:1.7}
 .avgwho{font-size:9.5px;padding:3px 8px;top:1.5%}
 .avgwho b{font-size:10.5px}.avgwho em{display:none}
}
'''
rep('</style>\n</head>', AVG_CSS + '\n</style>\n</head>', 'AVG CSS')

open(p, 'w', encoding='utf-8').write(b)
print('SAVED avg layer')
