# -*- coding: utf-8 -*-
"""R45：修 125 格跨角色串脸 / 4 个伪角色 / 按角色池复用；接入 10 张高频专属层。"""
import re, json, os, collections

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

# ---------- 1. 真实角色全集：CAST_META 短键（23 位），4 个表情层键不再算角色 ----------
a = s.index('const CAST_META={'); b = s.index('\n};', a) + 3
meta_blk = s[a:b]
pairs = re.findall(r'^\s*([A-Za-z0-9_]+)\s*:\s*\[\s*[\'\"]([^\'\"]+)[\'\"]', meta_blk, re.M)
SHORT = [(k, n) for k, n in pairs if re.match(r'^cos_[a-z0-9]+$', k)]
CASTS = [[k, n] for k, n in SHORT]
name2base = {}
for k, n in SHORT:
    name2base.setdefault(n, k)
log.append('真实角色 %d 位（R44 的 27 位含 4 个表情层伪角色）' % len(CASTS))

# ---------- 2. ART 键池 ----------
art_blk = re.search(r'const ART = (\{[\s\S]*?\});', s).group(1)
artkeys = re.findall(r'"([A-Za-z0-9_]+)"\s*:\s*"data:', art_blk)
artset = set(artkeys)
BAD = re.compile(r'^(bg_|fx_|cover$|cat$|cat\d|catav|catorg|cat3|[A-Z]$|wx|scene|ripple|nod|shake|breath|flag|dust|ray|bird|lamp|snow|splash|rain|wind|reed|firefly|snowedge)', re.I)

# ---------- 3. 按角色归池：CAST_META 中文名前缀 -> 基础角色 ----------
pool = collections.defaultdict(list)
for k, cn in pairs:
    if k not in artset or BAD.match(k):
        continue
    nm = cn.split('·')[0].strip().split(' ')[0].strip()
    base = name2base.get(nm)
    if not base:
        base = next((v for n, v in name2base.items() if n and nm.startswith(n)), None)
    if base:
        pool[base].append(k)
ROLE_POOL = {c[0]: pool.get(c[0], []) for c in CASTS}
# 兜底：任何空池至少放该角色自己的短键
for c in CASTS:
    if not ROLE_POOL[c[0]] and c[0] in artset:
        ROLE_POOL[c[0]] = [c[0]]
log.append('角色池 %d 个 / %d 层，空池 %d' %
          (len(ROLE_POOL), sum(len(v) for v in ROLE_POOL.values()),
           sum(1 for v in ROLE_POOL.values() if not v)))
assert all(ROLE_POOL.values()), '存在空角色池'
assert not any(BAD.match(k) for v in ROLE_POOL.values() for k in v), '池内混入非角色层'

# ---------- 4. 专属层映射：R44 16 + R45 10 ----------
SPECIAL = {
    'cos_jin|喜': 'R43_jin_xi', 'cos_shen|惊': 'R43_shen_jing',
    'cos_yi|哀': 'R43_yi_ai', 'cos_luo|怒': 'R43_luo_nu',
    'cos_xiao|决': 'R43_xiao_jue', 'cos_qinwen|喜': 'R43_qin_xi',
    'cos_geng|怒': 'R43_geng_nu',
    'cos_zhu|醉': 'R44_zhu_zui', 'cos_zhu|怒': 'R44_zhu_nu',
    'cos_yuancl|静息': 'R44_yuancl_scar',
    'cos_shen|静息': 'R44_shen_beard', 'cos_yi|静息': 'R44_yi_beard',
    'cos_jin|怒': 'R44_jin_nu', 'cos_luo|哀': 'R44_luo_ai',
    'cos_xiao|喜': 'R44_xiao_xi', 'cos_qinwen|惊': 'R44_qin_jing',
    # R45：按 24 关逐幕出场频次 Top10 复用格专属化
    'cos_base|喜': 'R45_base_xi', 'cos_zhu|静息': 'R45_zhu_jing',
    'cos_yi|喜': 'R45_yi_xi', 'cos_ying|喜': 'R45_ying_xi',
    'cos_tian|喜': 'R45_tian_xi', 'cos_base|静息': 'R45_base_jing',
    'cos_base|疑': 'R45_base_yi', 'cos_zhu|喜': 'R45_zhu_xi',
    'cos_xiao|静息': 'R45_xiao_jing', 'cos_tian|静息': 'R45_tian_jing',
}
valid_casts = set(c[0] for c in CASTS)
for k in SPECIAL:
    assert k.split('|')[0] in valid_casts, '专属映射用了伪角色/非法键: ' + k
log.append('专属层 %d 项（R44 16 + R45 10）' % len(SPECIAL))

# ---------- 5. 替换表情管理 JS 块 ----------
a = s.index('/* ===== R44 表情管理')
b = s.index('\n</script>', a)
NEW = r'''
/* ===== R45 表情管理：23 真实角色 / 按角色池复用（杜绝跨角色串脸） / 26 格专属 ===== */
const EXPR_MOODS=['静息','喜','怒','哀','惊','疑','决','醉'];
const EXPR_CASTS=__CASTS__;
const EXPR_POOL=__POOL__;              /* 仅作兜底，主取值走 ROLE_POOL */
const ROLE_POOL=__ROLE_POOL__;         /* 角色 -> 该角色自己的已过检层 */
const EXPR_SPECIAL=__SPECIAL__;        /* 该格有独立生成并过检的专属层 */
const EXPR_APPLY_KEY='beixue_expr_apply_v1';
let EXPR_APPLY=0, EXPR_F={cast:'',mood:'',src:''};
try{EXPR_APPLY=+(localStorage.getItem(EXPR_APPLY_KEY)||0);}catch(e){}
const EXPR=[];
EXPR_CASTS.forEach((c,ci)=>EXPR_MOODS.forEach((m,mi)=>{
 const key=c[0]+'|'+m;
 /* R44 的 idx%全局池 会让 125 格指向别的角色；R45 只从本角色池取 */
 const own=ROLE_POOL[c[0]]||[];
 const art=EXPR_SPECIAL[key]||own[mi%own.length]||EXPR_POOL[(ci*8+mi)%EXPR_POOL.length];
 const src=EXPR_SPECIAL[key]?'专属':'复用';
 EXPR.push({cast:c[0],name:c[1],mood:m,art:art,src:src,
   unlock:Math.min(24,ci),anim:(m==='怒'?'摇头':(m==='喜'||m==='醉'?'点头':'呼吸')),
   qc:src==='专属'?'通过':'同角色已过检层'});
}));
const EXPR_CACHE=new Map();
/* stageFor 返回两种 ID：基础角色键(cos_shen) 与具体层键(R30_K_read/B_face_yi/H_cost_shi)。
   谱系只按基础角色建表，必须先把层键按 CAST_META 中文名/角色短码规整回基础键。 */
function exprCanon(cast){
 const ids=new Set(EXPR_CASTS.map(c=>c[0]));
 if(ids.has(cast))return cast;
 try{
  const m=CAST_META[cast];
  if(m&&m[0]){
   const nm=String(m[0]).split('·')[0].trim();
   let hit=EXPR_CASTS.find(c=>c[1]===nm||nm.indexOf(c[1])===0||c[1].indexOf(nm)===0);
   if(hit)return hit[0];
  }
 }catch(e){}
 try{ const o=origCast(cast); if(ids.has(o))return o; }catch(e){}
 /* 形如 B_face_yi / R32_M_luo：从下划线片段里取角色短码 */
 try{
  const parts=String(cast).split('_');
  for(let i=parts.length-1;i>=1;i--){
   const c='cos_'+parts[i];
   if(ids.has(c))return c;
  }
 }catch(e){}
 return 'cos_base';
}
function exprResolve(cast,mood,ctx){
 cast=exprCanon(cast||'cos_base');
 const key=cast+'|'+(mood||'静息')+'|'+(ctx||'');
 if(EXPR_CACHE.has(key))return EXPR_CACHE.get(key);
 let r=EXPR.find(e=>e.cast===cast&&e.mood===mood);
 if(!r)r=EXPR.find(e=>e.cast==='cos_base'&&e.mood===mood)||EXPR[0];
 const out=Object.assign({},r,{ctx:ctx||''});
 EXPR_CACHE.set(key,out); return out;
}
function exprStat(){ const o={专属:0,复用:0,待补:0}; EXPR.forEach(e=>o[e.src]++); return o; }
function exprList(){ return EXPR.filter(e=>(!EXPR_F.cast||e.cast===EXPR_F.cast)&&(!EXPR_F.mood||e.mood===EXPR_F.mood)&&(!EXPR_F.src||e.src===EXPR_F.src)); }
/* 运行时自检：复用格必须落在本角色池内，专属格必须确实存在 */
function exprCrossCount(){
 return EXPR.filter(e=>{
  if(e.src==='专属')return !ART[e.art];
  return !(ROLE_POOL[e.cast]||[]).includes(e.art);
 }).length;
}
function exprMoodFor(k){
 try{ const st=S[k]; const i=(st&&typeof st.i==='number')?st.i:((st&&typeof st.node==='number')?st.node:0);
   return EXPR_MOODS[((i%8)+8)%8]; }catch(e){ return '静息'; }
}
function exprPanelHTML(){
 const st=exprStat(), list=exprList();
 const opts=(arr,cur)=>arr.map(x=>'<option value="'+x[0]+'"'+(cur===x[0]?' selected':'')+'>'+x[1]+'</option>').join('');
 const cards=list.slice(0,120).map(e=>{
   const uri=ART[e.art]||'';
   return '<div class="exprcell"><img loading="lazy" alt="" src="'+uri+'"><div class="exprtxt"><b>'+e.name+' · '+e.mood+'</b><span>'+e.art+'</span><em class="'+e.src+'">'+e.src+(e.src==='复用'?' · 同角色':'')+'</em></div></div>';
 }).join('');
 return '<div id="exprPanel" class="exprwrap"><div class="exprbox">'+
  '<div class="exprh"><b>☰ 表情管理</b><span>'+EXPR_CASTS.length+' 角色 × '+EXPR_MOODS.length+' 表情 = '+EXPR.length+' 格 ｜ 专属 '+st.专属+' · 复用 '+st.复用+' · 待补 '+st.待补+' ｜ 串脸 '+exprCrossCount()+'</span>'+
   '<button data-act="expr_close" class="exprclose">✕ 关闭</button></div>'+
  '<div class="exprf">筛选 <select data-expr="cast"><option value="">全部角色</option>'+opts(EXPR_CASTS,EXPR_F.cast)+'</select>'+
   '<select data-expr="mood"><option value="">全部表情</option>'+opts(EXPR_MOODS.map(m=>[m,m]),EXPR_F.mood)+'</select>'+
   '<select data-expr="src"><option value="">全部状态</option>'+opts([['专属','专属'],['复用','复用']],EXPR_F.src)+'</select>'+
   '<button data-act="expr_apply" class="'+(EXPR_APPLY?'on':'')+'">'+(EXPR_APPLY?'✓ 谱系接管中':'按谱系接管')+'</button>'+
   '<button data-act="expr_export">↧ 导出 CSV</button></div>'+
  '<div class="exprgrid">'+cards+'</div>'+
  '<div class="exprfoot">R45：角色全集对齐 CAST_META 短键（23 位），4 个表情层键归回各自角色；复用只从本角色池取，跨角色串脸 0。显示 '+Math.min(120,list.length)+'/'+list.length+' 格，源键可见。</div>'+
 '</div></div>';
}
function openExpr(){ let w=$('#exprPanel'); if(w)w.remove(); document.body.insertAdjacentHTML('beforeend',exprPanelHTML()); }
function closeExpr(){ const w=$('#exprPanel'); if(w)w.remove(); }
function exprExport(){
 const rows=[['角色ID','角色','表情','资源键','来源','解锁关','动画组','质检']];
 EXPR.forEach(e=>rows.push([e.cast,e.name,e.mood,e.art,e.src,e.unlock,e.anim,e.qc]));
 const csv='\ufeff'+rows.map(r=>r.map(x=>'"'+String(x).replace(/"/g,'""')+'"').join(',')).join('\r\n');
 const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
 a.download='杯雪表情谱系_R45.csv'; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),3000);
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
/* 默认保留逐关换脸；开启接管后按关卡当前幕推表情，缓存键含 ctx 防串 */
try{
 const _stageForOrig=stageFor;
 window.stageFor=function(k){
   const base=_stageForOrig(k);
   if(!EXPR_APPLY)return base;
   try{
     const r=exprResolve(base.cast||'cos_base',exprMoodFor(k),k);
     if(r&&r.art&&ART[r.art])base.art=r.art;
   }catch(err){}
   return base;
 };
}catch(err){}
'''
fallback = [k for k in artkeys if (k in set(x[0] for x in pairs) or k.startswith('cos_')) and not BAD.match(k)]
NEW = (NEW.replace('__CASTS__', json.dumps(CASTS, ensure_ascii=False))
          .replace('__POOL__', json.dumps(fallback, ensure_ascii=False))
          .replace('__ROLE_POOL__', json.dumps(ROLE_POOL, ensure_ascii=False))
          .replace('__SPECIAL__', json.dumps(SPECIAL, ensure_ascii=False)))
s = s[:a] + NEW + s[b:]
log.append('OK   表情管理 JS 整块替换（23 角色 / 角色池 / 26 专属 / 串脸计数）')

# ---------- 6. 注入 10 张 WebP（插在 ART 对象结束后，与 R44 并列） ----------
EMB = json.load(open('/data/workspace/anim40/_EMB.json'))
emb = ('/* R45 补 10 张：按 24 关逐幕出场频次 Top10 复用格专属化，逐张独立整帧（非拼接） */\n'
       'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + emb + s[e:]
log.append('OK   10 张 WebP 注入 ART（在 }; 之后）')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
