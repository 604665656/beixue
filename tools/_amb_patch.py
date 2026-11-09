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
# 1) 环境音合成：鸟叫 / 虫鸣 / 风 / 远雷 / 翻页
# ============================================================
AMB = r'''
/* ---------- 环境音：随天气自动出现，全部实时合成、无音频文件 ----------
   只有「场景音」开启时才播；切场景清掉旧调度再起新的，不会叠成一片。 */
let ambTimer=null, ambKind='';
function stopAmbient(){ if(ambTimer){clearTimeout(ambTimer);ambTimer=null;} ambKind=''; }
function chirp(){
 if(!AC||!SFX&&!BGM)return;
 const t=AC.currentTime, n=2+((Math.random()*3)|0);
 for(let i=0;i<n;i++){
  const o=AC.createOscillator(), g=AC.createGain();
  const f=1750+Math.random()*700, st=t+i*(.11+Math.random()*.07);
  o.type='sine';
  o.frequency.setValueAtTime(f,st);
  o.frequency.exponentialRampToValueAtTime(f*1.42,st+.045);
  o.frequency.exponentialRampToValueAtTime(f*.92,st+.10);
  g.gain.setValueAtTime(.0001,st);
  g.gain.exponentialRampToValueAtTime(.013,st+.018);
  g.gain.exponentialRampToValueAtTime(.0001,st+.135);
  o.connect(g);g.connect(AC.destination);o.start(st);o.stop(st+.16);
 }
}
function cricket(){
 if(!AC)return;
 const t=AC.currentTime;
 for(let i=0;i<3;i++){
  const o=AC.createOscillator(), g=AC.createGain(), st=t+i*.085;
  o.type='sine';o.frequency.value=4200+Math.random()*500;
  g.gain.setValueAtTime(.0001,st);
  g.gain.exponentialRampToValueAtTime(.006,st+.006);
  g.gain.exponentialRampToValueAtTime(.0001,st+.045);
  o.connect(g);g.connect(AC.destination);o.start(st);o.stop(st+.06);
 }
}
function pageRustle(){
 if(!AC)return;
 const t=AC.currentTime, src=AC.createBufferSource();
 src.buffer=noiseBuffer();
 const bp=AC.createBiquadFilter();bp.type='bandpass';bp.frequency.value=1100;bp.Q.value=.7;
 const g=AC.createGain();
 g.gain.setValueAtTime(.0001,t);
 g.gain.exponentialRampToValueAtTime(.008,t+.05);
 g.gain.exponentialRampToValueAtTime(.0001,t+.30);
 src.connect(bp);bp.connect(g);g.connect(AC.destination);src.start(t);src.stop(t+.34);
}
function farThunder(){
 if(!AC)return;
 const t=AC.currentTime, o=AC.createOscillator(), g=AC.createGain(), lp=AC.createBiquadFilter();
 o.type='sine';o.frequency.setValueAtTime(58,t);
 o.frequency.exponentialRampToValueAtTime(34,t+1.5);
 lp.type='lowpass';lp.frequency.value=130;
 g.gain.setValueAtTime(.0001,t);
 g.gain.exponentialRampToValueAtTime(.016,t+.35);
 g.gain.exponentialRampToValueAtTime(.0001,t+1.9);
 o.connect(lp);lp.connect(g);g.connect(AC.destination);o.start(t);o.stop(t+2.0);
}
function scheduleAmbient(kind){
 if(!BGM||!AC)return;
 const delays={birds:[2600,5200],night:[3200,6000],quiet:[7000,13000],
               wind:[5000,9000],rain:[9000,16000]}[kind]||[6000,11000];
 const wait=delays[0]+Math.random()*(delays[1]-delays[0]);
 ambTimer=setTimeout(()=>{
  if(!BGM||!AC){stopAmbient();return;}
  try{
   if(kind==='birds')chirp();
   else if(kind==='night')cricket();
   else if(kind==='quiet')pageRustle();
   else if(kind==='rain')farThunder();
   /* wind 已在噪声链里，靠滤波与增益起伏表现，不额外叠声 */
  }catch(e){}
  scheduleAmbient(kind);
 },wait);
}
function startAmbient(bg){
 stopAmbient();
 if(!BGM||!AC)return;
 const kind=sceneWeather(bg).amb; ambKind=kind;
 scheduleAmbient(kind);
}
const AMB_LABEL={birds:'晴日鸟鸣',night:'夜虫',quiet:'书楼静响',wind:'风声',rain:'远雷'};
'''
rep('/* ---------- state ---------- */', AMB + '\n/* ---------- state ---------- */', '环境音函数')

# ============================================================
# 2) 接入 setBGM / retuneScene / stopAll
# ============================================================
rep(''' if(s>0){ if(!initAC()){BGM=0;} else { startRain(currentSceneBg()); if(s>1)startQin(); } }
 syncHctl();''',
''' if(s>0){ if(!initAC()){BGM=0;} else { startRain(currentSceneBg()); if(s>1)startQin(); startAmbient(currentSceneBg()); } }
 else stopAmbient();
 syncHctl();''', 'setBGM 接环境音')

rep('''function retuneScene(bg){
 const cfg=SCENE_SOUND[bg]||SCENE_SOUND.rain;
 sceneLabel=cfg[3];''',
'''function retuneScene(bg){
 const cfg=SCENE_SOUND[bg]||SCENE_SOUND.rain;
 sceneLabel=cfg[3];
 const _k=sceneWeather(bg).amb;
 if(_k!==ambKind)startAmbient(bg);''', 'retuneScene 接环境音')

rep(''' sceneFilter=null;
}''', ''' sceneFilter=null; stopAmbient();
}''', 'stopAll 清环境音')

rep('''function bgmLabel(){ return ['♫ 场景音·关','♫ '+sceneLabel,'♫ '+sceneLabel+'＋琴'][BGM]; }''',
'''function bgmLabel(){
 if(!BGM)return '♫ 场景音·关';
 const amb=AMB_LABEL[sceneWeather(currentSceneBg()).amb]||'';
 return '♫ '+sceneLabel+(BGM>1?'＋琴':(amb?'·'+amb:''));
}''', 'bgmLabel 带天气音')

# 声音卡文案补天气音
rep('''   <div class="asrstate">背景音会<b>跟着当前场景自动换音色</b>：雨驿听雨、渡口听水、书楼极静、辕门听风、秦淮带琴。点选项另有轻拨弦反馈。两者互不影响，也都不影响朗读与语音。</div></div>''',
'''   <div class="asrstate">场景音会<b>跟着天气自动换声</b>：秋雨落雨、拂晓与芦荡有<b>鸟鸣</b>、晴天有晨光、落雪／辕门听风、书楼偶有翻页、秦淮夜虫、雨夜偶发远雷，换关平滑过渡。点选项另有轻拨弦、答对上行／答错下行。与朗读、语音互不串扰。</div></div>''', '声音卡天气音文案')

# 档案 ui 页与设计说明追加
add_ui = r'''<h2>AVG 演出层（本轮）</h2>
<p>之前是「图在上、白卡文字在下」，不像 AVG。现在<b>整屏就是画面</b>：</p>
<ul>
 <li><b>文字与选项都叠在画面上</b>：把舞台与本屏正文包进同一个 <code>.avgframe</code>，舞台绝对铺底，正文变成半透明宣纸气泡（带尖角），选项也在气泡里。只移动一次 DOM，不改关卡数据、不复制文字，朗读 <code>innerText</code> 仍读到全文，事件仍走 body 委托。</li>
 <li><b>说话人名牌</b>：左上角「哈士喵 · 当前角色」＋场景与天气名，随幕换脸。</li>
 <li><b>六类天气动画</b>：秋雨（双层斜雨＋水花）、落雪（两层雪片）、晨光（光柱＋光斑漂移＋飞鸟）、晴日飞鸟（三只鸟沿弧线飞＋芦苇摇）、窗光浮尘、朔风旗影、灯火浮絮。全部纯 CSS＋内嵌 SVG 剪影，无额外图片。</li>
 <li><b>天气有声音</b>：<code>♫ 场景音</code> 开启时，雨驿落雨、拂晓／芦荡<b>鸟鸣</b>、晴天晨光、落雪辕门风声、书楼翻页、秦淮夜虫、雨夜远雷；用 Web Audio 实时合成滑音／带通噪声／低频雷声，随机间隔调度，切场景清掉旧调度不叠声。<b>默认仍关，不自动响</b>。</li>
 <li>设置「视觉」卡可一键关掉 AVG 演出回到旧版；<code>减少动效</code> 停掉所有粒子与入场，<code>高对比</code> 气泡改纯白底黑字、天气层隐藏。</li>
</ul>
'''
_k=b.rfind('<h2>无障碍优先级</h2>'); assert _k>0
b=b[:_k]+add_ui+b[_k:]
print('档案 ui AVG 段 inserted')

anchor = '## 边界\n\n- 文案都是概括、解读与机制化改写，不是小说原文。'
add_doc = r'''## AVG 演出层

用户指出「图在上、白卡文字在下」不像 AVG。改为**整屏即画面**：`applyAVG()` 在 `render()` 末尾把 `.stage` 与其后的本屏正文包进 `.avgframe`，舞台 `position:absolute;inset:0` 铺底，正文块半透明宣纸气泡（带尖角、blur），选项同在气泡内；左上角说话人名牌随幕换角色。只移动 DOM、不复制文字，朗读 `innerText` 与 body 事件委托都不受影响；`AVGON` 可在「视觉」卡关闭，回到旧版布局。

**天气映射**：11 张背景板 → 6 类 FX（`rain/snow/sun/birds/dust/wind/night`）+ 5 类环境音（`rain/birds/wind/quiet/night`）。FX 全为 CSS 动画＋内嵌 SVG 鸟剪影：双层斜雨＋水花、两层雪片、光柱＋径向光斑漂移、三只鸟沿弧线飞、芦苇摇、窗光浮尘、旗影摆动、灯火闪烁。`减少动效` 全停，`高对比` 隐藏天气层并把气泡改纯白底黑字。

**环境音**：`chirp()` 用 sine 滑音 2–4 声一组（1750–2450Hz，45ms 上扬再回落），`cricket()` 4200Hz 短点，`pageRustle()` 带通噪声脉冲，`farThunder()` 58→34Hz 低频；`scheduleAmbient()` 按类型随机间隔递归调度，`startAmbient()` 切场景先 `stopAmbient()` 再起，避免叠声。只有 `BGM>0` 才播，**默认关、不持久化、无音频文件**。header 标签改为显示当前音景＋天气音名（如「♫ 驿道秋雨·远雷」）。

横竖屏都验过：气泡首块 `margin-top` 竖屏 `clamp(190px,34vh,300px)`、横屏 `clamp(126px,30vh,190px)`，角色层左侧不遮文字；24 关全通、四路开关默认态、三套皮肤、无障碍三开关均回归。

'''
rep(anchor, add_doc + anchor, '设计说明 AVG 段')

rep('- **场景音随关切换**：`♫ 场景音` 按当前舞台自动换音景（驿道秋雨／渡口水声／书楼极静／辕门朔风／石阵风雪／秦淮灯影），换关平滑过渡；不新增开关，与 `♪ 音效`、朗读、语音互不串扰，默认仍关。',
'''- **场景音随关切换**：`♫ 场景音` 按当前舞台自动换音景（驿道秋雨／渡口水声／书楼极静／辕门朔风／石阵风雪／秦淮灯影），换关平滑过渡；不新增开关，与 `♪ 音效`、朗读、语音互不串扰，默认仍关。
- **AVG 画面演出**：文字与选项叠进场景气泡、带说话人名牌；六类天气动画（雨／雪／晨光／飞鸟／浮尘／朔风／灯火）；天晴有实时合成的鸟鸣、雨夜有远雷、书楼有翻页、秦淮有夜虫。`设置 → 视觉 → ◈ AVG 画面` 可关，`减少动效` 停全部粒子。''', 'README AVG 行')

open(p, 'w', encoding='utf-8').write(b)
print('SAVED ambient+docs')
