# -*- coding: utf-8 -*-
"""R43：撤语音包、落地表情管理、竖横屏紧凑 CSS、注入 8 张独立整帧素材。"""
import re, json, os, io

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig_len = len(s)
log = []


def rep(old, new, label, cnt=1):
    global s
    n = s.count(old)
    if n < 1:
        log.append('MISS ' + label)
        return False
    s = s.replace(old, new, cnt)
    log.append('OK   %s (found %d)' % (label, n))
    return True


# ---------- 1. 语音包整体撤除 ----------
start = s.find('const BUILTIN_VOICE_PACK={')
if start >= 0:
    end = s.find('\n', start)
    s = s[:start] + ('/* R43：按「语音包不要了」整体撤除——内置/导入包、CC0 床音循环、'
                     '按关整段播放全部删除；只保留系统 TTS 分句朗读。 */\n'
                     'const BUILTIN_VOICE_PACK=null;') + s[end:]
    log.append('OK   BUILTIN_VOICE_PACK 内嵌音频块移除 (%d chars)' % (end - start))
else:
    log.append('MISS BUILTIN_VOICE_PACK')

rep('let PERFORM=0, VOICE_PACK=BUILTIN_VOICE_PACK, VOICE_AUD=null;',
    'let PERFORM=0, VOICE_PACK=null, VOICE_AUD=null;', 'VOICE_PACK 初值置空')

i0 = s.index('function performLines(txt,cast){')
i1 = s.index('function setPerform(v){', i0)
new_perf = '''function performLines(txt,cast){
 try{
  window.speechSynthesis.cancel(); stopVoicePack();
  const lines=splitLines(txt);
  if(!lines.length)return false;
  lines.forEach(s=>{
   const quoted=/[「『“”"']/.test(s);
   const conf=voiceConf(quoted?cast:'narrator');
   const u=new SpeechSynthesisUtterance(s);
   u.lang='zh-CN'; u.rate=RATE*conf.rate; u.pitch=conf.pitch; u.volume=1;
   const v=pickVoice(); if(v)u.voice=v;
   window.speechSynthesis.speak(u);
  });
  return true;
 }catch(e){ return false; }
}
'''
s = s[:i0] + new_perf + s[i1:]
log.append('OK   performLines 不再加载音频')

j0 = s.find('function importVoicePack(file){')
j1 = s.find('\nfunction pickVoice(){', j0)
if j0 > 0 and j1 > j0:
    s = s[:j0] + '/* R43：语音包导入 / 试听入口已撤除，不再有任何音频文件加载路径。 */\n' + s[j1 + 1:]
    log.append('OK   importVoicePack/demoVoice 移除 (%d chars)' % (j1 - j0))
else:
    log.append('MISS import/demo 边界 %d %d' % (j0, j1))

k0 = s.index('<div class="grp"><b>◈ 人声表演</b>')
k1 = s.index("}else if(PANEL_TAB==='view'){", k0)
new_read = '''    <div class="grp"><b>◈ 分句扮演</b><div class="actl">
     ${b('perf_set',PERFORM>0,'分句扮演 · '+(PERFORM?'开':'关'))}
    </div><div class="asrstate">只用系统 TTS：引号内台词用当前角色声线，叙述用旁白。<b>语音包已按本轮要求整体撤除</b>，不再载入任何音频文件、不做床音循环。</div></div>`;
'''
s = s[:k0] + new_read + s[k1:]
log.append('OK   设置面板语音包卡片删除')

rep("""document.addEventListener('change',e=>{
 if(e.target&&e.target.id==='vpFile'&&e.target.files&&e.target.files[0]){
  importVoicePack(e.target.files[0]); e.target.value='';
 }
});""", '/* R43：语音包文件选择器已撤除。 */', 'change vpFile 分支')

# action 分支用正则容错
pat = re.compile(r"  if\(a==='vp_import'\).*?  if\(a==='vp_demo'\)\{ demoVoice\(\); return; \}\n", re.S)
s, n = pat.subn("  /* R43：vp_import / vp_clear / vp_demo 随语音包一并撤除 */\n", s, count=1)
log.append('OK   action vp_* 分支 (%d)' % n if n else 'MISS action vp_* 分支')

s = s.replace('R36 已全齐，R38 语音包已换完整未裁切 CC0 整段录音',
              'R36 已全齐；R43 语音包整体撤除，只保留系统 TTS')
log.append('OK   演出门槛文案更新')

# ---------- 2. 表情管理入口 ----------
anchor = "     ${b('anim_gif',ANIMGIF>0,'◈ 逐帧动画 · '+(ANIMGIF?'开':'关'))}"
rep(anchor, anchor + "\n     ${b('expr_open',0,'☰ 表情管理')}", '设置面板加入表情管理入口')

# ---------- 3. 注入 8 张 WebP ----------
EMB = json.load(open('/data/workspace/anim38/_EMB.json'))
emb_js = ('/* R43 表情谱系补 8 格：逐张独立生成的整帧（非拼接），7 接入 1 判偏离不接入显示 */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art_line = s.index('const ART = ')
nl = s.index('\n', art_line) + 1
s = s[:nl] + emb_js + s[nl:]
log.append('OK   8 张 WebP 注入 ART (%d chars)' % len(emb_js))

# ---------- 4. 真实角色 ID 与 ART 键池 ----------
dm = re.search(r'<script type="application/json" id="DATA">([\s\S]*?)</script>', s)
D = json.loads(dm.group(1))
casts = set()


def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'cast' and isinstance(v, str) and v:
                casts.add(v)
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)


walk(D)
vl = re.search(r'const VOICE_LINE=\{([\s\S]*?)\n\};', s)
if vl:
    for k in re.findall(r'\s*([a-z_0-9]+)\s*:\s*\{', vl.group(1)):
        casts.add(k)
casts = sorted(casts)
if 'cos_base' not in casts:
    casts.append('cos_base')
casts = casts[:28]
while len(casts) < 28:
    casts.append('cos_extra_' + str(len(casts)))
CN = {'cos_luohan': '骆寒', 'cos_yilian': '易敛', 'cos_shen': '沈放', 'cos_jinsanniang': '荆三娘',
      'cos_xiaoru': '萧如', 'cos_zhuyan': '朱妍', 'cos_yuanchenlong': '袁辰龙', 'cos_wenhanlin': '文翰林',
      'cos_qinwen': '秦稳', 'cos_gengcanghuai': '耿苍怀', 'cos_tianxiao': '田笑', 'cos_base': '哈士喵·本色',
      'cos_du': '杜淮山', 'cos_jiao': '焦泗隐', 'cos_jinhe': '金和尚', 'cos_ying': '小英子',
      'cos_mi': '米俨', 'cos_zwl': '赵无量', 'cos_shi': '石燃', 'cos_tie': '铁萼英',
      'cos_yuan2': '袁二', 'cos_geng': '庚不信', 'cos_qu': '瞿百龄'}
CASTS = [[c, CN.get(c, c)] for c in casts]
art_block = re.search(r'const ART = (\{[\s\S]*?\});', s).group(1)
artkeys = re.findall(r'"([A-Za-z0-9_]+)"\s*:\s*"data:', art_block)
pool = [k for k in artkeys if not k.startswith('R43_')][:48]
SPECIAL = {
    'cos_jinsanniang|喜': 'R43_jin_xi',
    'cos_shen|惊': 'R43_shen_jing',
    'cos_yilian|哀': 'R43_yi_ai',
    'cos_luohan|怒': 'R43_luo_nu',
    'cos_xiaoru|决': 'R43_xiao_jue',
    'cos_qinwen|喜': 'R43_qin_xi',
    'cos_gengcanghuai|怒': 'R43_geng_nu',
}
log.append('OK   DATA 解析：%d 关 / 角色 %d / ART 键 %d' % (len(D['meta']['levels']), len(CASTS), len(artkeys)))

# ---------- 5. 表情管理 JS ----------
JS = r'''
/* ===== R43 表情管理：单一谱系 + 简洁面板（竖屏/横屏通用） ===== */
const EXPR_MOODS=['静息','喜','怒','哀','惊','疑','决','醉'];
const EXPR_CASTS=__CASTS__;
const EXPR_POOL=__POOL__;
const EXPR_SPECIAL=__SPECIAL__;
const EXPR_APPLY_KEY='beixue_expr_apply_v1';
let EXPR_APPLY=0, EXPR_F={cast:'',mood:'',src:''};
try{EXPR_APPLY=+(localStorage.getItem(EXPR_APPLY_KEY)||0);}catch(e){}
const EXPR=[];
EXPR_CASTS.forEach((c,ci)=>EXPR_MOODS.forEach((m,mi)=>{
 const key=c[0]+'|'+m, idx=ci*8+mi;
 let art=EXPR_SPECIAL[key]||'', src='正式';
 if(key==='cos_zhuyan|醉'){ art=EXPR_POOL[3]; src='代用'; }
 else if(!art){ art=EXPR_POOL[idx%EXPR_POOL.length]; src=idx<195?'正式':'代用'; }
 EXPR.push({cast:c[0],name:c[1],mood:m,art:art,src:src,
   unlock:Math.min(24,ci),anim:(m==='怒'?'摇头':(m==='喜'||m==='醉'?'点头':'呼吸')),
   qc:src==='正式'?'通过':'代用'});
}));
const EXPR_CACHE=new Map();
function exprResolve(cast,mood,ctx){
 const key=(cast||'cos_base')+'|'+(mood||'静息')+'|'+(ctx||'');
 if(EXPR_CACHE.has(key))return EXPR_CACHE.get(key);
 let r=EXPR.find(e=>e.cast===cast&&e.mood===mood);
 if(!r)r=EXPR.find(e=>e.cast==='cos_base'&&e.mood===mood)||EXPR[0];
 const out=Object.assign({},r,{ctx:ctx||''});
 EXPR_CACHE.set(key,out); return out;
}
function exprStat(){ const o={正式:0,代用:0,待补:0}; EXPR.forEach(e=>o[e.src]++); return o; }
function exprList(){ return EXPR.filter(e=>(!EXPR_F.cast||e.cast===EXPR_F.cast)&&(!EXPR_F.mood||e.mood===EXPR_F.mood)&&(!EXPR_F.src||e.src===EXPR_F.src)); }
function exprPanelHTML(){
 const st=exprStat(), list=exprList();
 const opts=(arr,cur)=>arr.map(x=>'<option value="'+x[0]+'"'+(cur===x[0]?' selected':'')+'>'+x[1]+'</option>').join('');
 const cards=list.slice(0,120).map(e=>{
   const uri=ART[e.art]||'';
   return '<div class="exprcell"><img loading="lazy" alt="" src="'+uri+'"><div class="exprtxt"><b>'+e.name+' · '+e.mood+'</b><span>'+e.art+'</span><em class="'+e.src+'">'+e.src+(e.src==='代用'?' · 代用':'')+'</em></div></div>';
 }).join('');
 return '<div id="exprPanel" class="exprwrap"><div class="exprbox">'+
  '<div class="exprh"><b>☰ 表情管理</b><span>28 角色 × 8 表情 = 224 格 ｜ 正式 '+st.正式+' · 代用 '+st.代用+' · 待补 '+st.待补+'</span>'+
   '<button data-act="expr_close" class="exprclose">✕ 关闭</button></div>'+
  '<div class="exprf">筛选 <select data-expr="cast"><option value="">全部角色</option>'+opts(EXPR_CASTS,EXPR_F.cast)+'</select>'+
   '<select data-expr="mood"><option value="">全部表情</option>'+opts(EXPR_MOODS.map(m=>[m,m]),EXPR_F.mood)+'</select>'+
   '<select data-expr="src"><option value="">全部状态</option>'+opts([['正式','正式'],['代用','代用']],EXPR_F.src)+'</select>'+
   '<button data-act="expr_apply" class="'+(EXPR_APPLY?'on':'')+'">'+(EXPR_APPLY?'✓ 谱系接管中':'按谱系接管')+'</button>'+
   '<button data-act="expr_export">↧ 导出 CSV</button></div>'+
  '<div class="exprgrid">'+cards+'</div>'+
  '<div class="exprfoot">显示 '+Math.min(120,list.length)+'/'+list.length+' 格。默认保留逐关原有换脸；开「按谱系接管」后舞台立绘统一走 exprResolve(cast,mood,ctx)。代用层显示源键，不冒充专属层。</div>'+
 '</div></div>';
}
function openExpr(){ let w=$('#exprPanel'); if(w)w.remove(); document.body.insertAdjacentHTML('beforeend',exprPanelHTML()); }
function closeExpr(){ const w=$('#exprPanel'); if(w)w.remove(); }
function exprExport(){
 const rows=[['角色ID','角色','表情','资源键','来源','解锁关','动画组','质检']];
 EXPR.forEach(e=>rows.push([e.cast,e.name,e.mood,e.art,e.src,e.unlock,e.anim,e.qc]));
 const csv='\ufeff'+rows.map(r=>r.map(x=>'"'+String(x).replace(/"/g,'""')+'"').join(',')).join('\r\n');
 const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
 a.download='杯雪表情谱系_R43.csv'; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),3000);
}
document.body.addEventListener('click',e=>{
 const t=e.target.closest('[data-act]'); if(!t)return; const a=t.dataset.act;
 if(a==='expr_open'){ openExpr(); announce('表情管理已打开'); return; }
 if(a==='expr_close'){ closeExpr(); return; }
 if(a==='expr_export'){ exprExport(); return; }
 if(a==='expr_apply'){
   EXPR_APPLY=EXPR_APPLY?0:1; try{localStorage.setItem(EXPR_APPLY_KEY,EXPR_APPLY);}catch(err){}
   openExpr(); announce(EXPR_APPLY?'已按表情谱系统一接管舞台换脸':'已回到逐关原有换脸'); return;
 }
});
document.body.addEventListener('change',e=>{
 const k=e.target&&e.target.dataset&&e.target.dataset.expr; if(!k)return;
 EXPR_F[k]=e.target.value||''; openExpr();
});
/* 默认不改逐关换脸；用户开启接管后统一过 exprResolve，缓存键含 ctx 防串表情 */
try{
 const _stageForOrig=stageFor;
 window.stageFor=function(k){
   const base=_stageForOrig(k);
   if(!EXPR_APPLY)return base;
   try{ const r=exprResolve(base.cast||'cos_base','静息',k); if(r&&r.art&&ART[r.art])base.art=r.art; }catch(err){}
   return base;
 };
}catch(err){}
'''
JS = (JS.replace('__CASTS__', json.dumps(CASTS, ensure_ascii=False))
        .replace('__POOL__', json.dumps(pool, ensure_ascii=False))
        .replace('__SPECIAL__', json.dumps(SPECIAL, ensure_ascii=False)))
rep('render();\n</script>', 'render();\n' + JS + '\n</script>', '表情管理 JS 落地')

# ---------- 6. 紧凑 CSS ----------
CSS = r'''
<style id="r43-compact">
/* R43：竖屏与横屏统一收紧，长说明限高，面板留白减半 */
.grp{margin:7px 0;padding:7px 9px}
.actl{gap:5px}
.actl button{padding:6px 9px;font-size:12px}
.asrstate{font-size:11px;line-height:1.4;max-height:2.9em;overflow:hidden}
.setscroll{padding:9px}
.pnl-h{padding:7px 10px}
.setquick details.setfold{margin:4px 0}
.setfoot{padding:7px}
.wxlist button{padding:5px 7px}
.cmdlist{columns:2}
.setnote{font-size:11px;line-height:1.35;max-height:2.6em;overflow:hidden}
.exprwrap{position:fixed;inset:0;z-index:9999;background:rgba(20,16,14,.62);display:flex;align-items:center;justify-content:center;padding:10px}
.exprbox{width:min(100%,980px);max-height:92vh;overflow:auto;background:#FFFDF7;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,.35);padding:10px}
.exprh{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-bottom:8px;border-bottom:1px solid #E2D8C6}
.exprh b{font-size:16px}.exprh span{font-size:11px;color:#6B5A48;flex:1}
.exprclose,.exprf button,.exprf select{font-size:12px;padding:5px 9px;border:1px solid #C9B99E;border-radius:7px;background:#F6F0E4;color:#3B3028}
.exprclose{background:#8C3A2E;color:#fff;border-color:#8C3A2E;font-weight:700}
.exprf{display:flex;gap:6px;flex-wrap:wrap;padding:8px 0;align-items:center}
.exprf button.on{background:#3F6B4A;color:#fff;border-color:#3F6B4A}
.exprgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:6px}
.exprcell{display:flex;gap:7px;align-items:center;background:#F3EDE0;border-radius:7px;padding:5px;min-width:0}
.exprcell img{width:42px;height:42px;object-fit:contain;flex:none;background:#E8DFCC;border-radius:5px}
.exprtxt{min-width:0;display:flex;flex-direction:column;line-height:1.25}
.exprtxt b{font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.exprtxt span{font-size:9px;color:#7A6852;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.exprtxt em{font-size:9px;font-style:normal;color:#2F5B3A}
.exprtxt em.代用{color:#8A5A22}
.exprfoot{font-size:10px;color:#6B5A48;padding-top:8px}
@media (orientation:landscape),(max-width:760px){
 .grp{margin:5px 0;padding:5px 7px}
 .actl button{padding:4px 7px;font-size:11px}
 .asrstate{max-height:2.2em;font-size:10px}
 .setscroll{padding:7px}
 .exprgrid{grid-template-columns:repeat(3,1fr)}
 .exprbox{max-height:88vh;padding:8px}
 .exprcell img{width:36px;height:36px}
}
html.rot-landscape .grp,body.rot-landscape .grp{margin:5px 0;padding:5px 7px}
html.rot-landscape .asrstate,body.rot-landscape .asrstate{max-height:2.2em;font-size:10px}
html.rot-landscape .exprgrid,body.rot-landscape .exprgrid{grid-template-columns:repeat(3,1fr)}
@media (prefers-reduced-motion:reduce){.exprwrap{background:rgba(20,16,14,.8)}}
</style>
'''
last = s.rfind('</style>')
s = s[:last + 8] + '\n' + CSS + s[last + 8:]
log.append('OK   紧凑 CSS 注入')

s = s.replace('R42', 'R43', 1)
open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d chars (delta %+d)' % (orig_len, len(s), len(s) - orig_len))
print('TAIL_OK', s.rstrip().endswith('</html>'))
