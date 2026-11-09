# -*- coding: utf-8 -*-
"""R44：修谱系 ID 对齐 / 资源键池混入背景板 / 接管恒静息，并注入 10 张新素材。"""
import re, json, os

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

# ---------- 1. 真实角色全集：CAST_META 里的 cos_* 短键 ----------
a = s.index('const CAST_META={')
b = s.index('\n};', a) + 3
meta_blk = s[a:b]
pairs = re.findall(r'^\s*(cos_[a-z0-9_]+)\s*:\s*\[\s*[\'\"]([^\'\"]+)[\'\"]', meta_blk, re.M)
# 只取基础角色键（短 ID，不含 _cost_/_face_ 等具体层）
CASTS = []
for k, cn in pairs:
    if re.match(r'^cos_[a-z0-9]+$', k) or k in ('cos_shen_argue', 'cos_luo_draw', 'cos_yi_grief', 'cos_zhu_resolve'):
        if k not in [c[0] for c in CASTS]:
            CASTS.append([k, cn])
if 'cos_base' not in [c[0] for c in CASTS]:
    CASTS.insert(0, ['cos_base', '哈士喵'])
log.append('真实角色 %d 位: %s' % (len(CASTS), ','.join(c[0] for c in CASTS[:8])) + '...')

# ---------- 2. 资源键池：只取角色层，排除背景/特效/通用图 ----------
art_blk = re.search(r'const ART = (\{[\s\S]*?\});', s).group(1)
artkeys = re.findall(r'"([A-Za-z0-9_]+)"\s*:\s*"data:', art_blk)
meta_keys = set(re.findall(r'^\s*([A-Za-z0-9_]+)\s*:\s*\[', meta_blk, re.M))
BAD = re.compile(r'^(bg_|fx_|cover$|cat$|cat\d|catav|catorg|cat3|[A-Z]$|wx|scene|ripple|nod|shake|breath|flag|dust|ray|bird|lamp|snow|splash|rain|wind|reed|firefly|snowedge)', re.I)
POOL = [k for k in artkeys if (k in meta_keys or k.startswith('cos_')) and not BAD.match(k)]
log.append('角色层键池 %d 个（ART 共 %d）' % (len(POOL), len(artkeys)))
assert not any(BAD.match(k) for k in POOL), '键池混入非角色层'

# ---------- 3. 专属层映射（真实 ID × 表情） ----------
SPECIAL = {
    # R43 七张重映射到真实 ID
    'cos_jin|喜': 'R43_jin_xi', 'cos_shen|惊': 'R43_shen_jing',
    'cos_yi|哀': 'R43_yi_ai', 'cos_luo|怒': 'R43_luo_nu',
    'cos_xiao|决': 'R43_xiao_jue', 'cos_qinwen|喜': 'R43_qin_xi',
    'cos_geng|怒': 'R43_geng_nu',
    # R44 九张（R44_jiao_scar 行头缺失，不接入）
    'cos_zhu|醉': 'R44_zhu_zui', 'cos_zhu|怒': 'R44_zhu_nu',
    'cos_yuancl|静息': 'R44_yuancl_scar',
    'cos_shen|静息': 'R44_shen_beard', 'cos_yi|静息': 'R44_yi_beard',
    'cos_jin|怒': 'R44_jin_nu', 'cos_luo|哀': 'R44_luo_ai',
    'cos_xiao|喜': 'R44_xiao_xi', 'cos_qinwen|惊': 'R44_qin_jing',
}
for k, v in list(SPECIAL.items()):
    if v not in artkeys and not v.startswith('R44_'):
        log.append('WARN 专属键不在 ART: ' + v)

# ---------- 4. 替换整个表情管理 JS 块 ----------
a = s.index('/* ===== R43 表情管理：单一谱系')
b = s.index('\n</script>', a)
NEW = r'''
/* ===== R44 表情管理：真实角色 ID 对齐 CAST_META，键池只含角色层 ===== */
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
 const art=EXPR_SPECIAL[key]||EXPR_POOL[idx%EXPR_POOL.length];
 /* 专属 = 这一格有独立生成并通过质检的层；复用 = 同一位角色借用另一张已通过层，源键可见 */
 const src=EXPR_SPECIAL[key]?'专属':'复用';
 EXPR.push({cast:c[0],name:c[1],mood:m,art:art,src:src,
   unlock:Math.min(24,ci),anim:(m==='怒'?'摇头':(m==='喜'||m==='醉'?'点头':'呼吸')),
   qc:src==='专属'?'通过':'复用已通过层'});
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
function exprStat(){ const o={专属:0,复用:0,待补:0}; EXPR.forEach(e=>o[e.src]++); return o; }
function exprList(){ return EXPR.filter(e=>(!EXPR_F.cast||e.cast===EXPR_F.cast)&&(!EXPR_F.mood||e.mood===EXPR_F.mood)&&(!EXPR_F.src||e.src===EXPR_F.src)); }
function exprMoodFor(k){
 try{ const st=S[k]; const i=(st&&typeof st.i==='number')?st.i:((st&&typeof st.node==='number')?st.node:0);
   return EXPR_MOODS[((i%8)+8)%8]; }catch(e){ return '静息'; }
}
function exprPanelHTML(){
 const st=exprStat(), list=exprList();
 const opts=(arr,cur)=>arr.map(x=>'<option value="'+x[0]+'"'+(cur===x[0]?' selected':'')+'>'+x[1]+'</option>').join('');
 const cards=list.slice(0,120).map(e=>{
   const uri=ART[e.art]||'';
   return '<div class="exprcell"><img loading="lazy" alt="" src="'+uri+'"><div class="exprtxt"><b>'+e.name+' · '+e.mood+'</b><span>'+e.art+'</span><em class="'+e.src+'">'+e.src+(e.src==='复用'?' · 复用':'')+'</em></div></div>';
 }).join('');
 return '<div id="exprPanel" class="exprwrap"><div class="exprbox">'+
  '<div class="exprh"><b>☰ 表情管理</b><span>'+EXPR_CASTS.length+' 角色 × '+EXPR_MOODS.length+' 表情 = '+EXPR.length+' 格 ｜ 专属 '+st.专属+' · 复用 '+st.复用+' · 待补 '+st.待补+'</span>'+
   '<button data-act="expr_close" class="exprclose">✕ 关闭</button></div>'+
  '<div class="exprf">筛选 <select data-expr="cast"><option value="">全部角色</option>'+opts(EXPR_CASTS,EXPR_F.cast)+'</select>'+
   '<select data-expr="mood"><option value="">全部表情</option>'+opts(EXPR_MOODS.map(m=>[m,m]),EXPR_F.mood)+'</select>'+
   '<select data-expr="src"><option value="">全部状态</option>'+opts([['专属','专属'],['复用','复用']],EXPR_F.src)+'</select>'+
   '<button data-act="expr_apply" class="'+(EXPR_APPLY?'on':'')+'">'+(EXPR_APPLY?'✓ 谱系接管中':'按谱系接管')+'</button>'+
   '<button data-act="expr_export">↧ 导出 CSV</button></div>'+
  '<div class="exprgrid">'+cards+'</div>'+
  '<div class="exprfoot">显示 '+Math.min(120,list.length)+'/'+list.length+' 格。角色 ID 已对齐 CAST_META，资源键池只含角色层（背景板/天气特效已排除）。复用格显示源键，不冒充专属层。</div>'+
 '</div></div>';
}
function openExpr(){ let w=$('#exprPanel'); if(w)w.remove(); document.body.insertAdjacentHTML('beforeend',exprPanelHTML()); }
function closeExpr(){ const w=$('#exprPanel'); if(w)w.remove(); }
function exprExport(){
 const rows=[['角色ID','角色','表情','资源键','来源','解锁关','动画组','质检']];
 EXPR.forEach(e=>rows.push([e.cast,e.name,e.mood,e.art,e.src,e.unlock,e.anim,e.qc]));
 const csv='\ufeff'+rows.map(r=>r.map(x=>'"'+String(x).replace(/"/g,'""')+'"').join(',')).join('\r\n');
 const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
 a.download='杯雪表情谱系_R44.csv'; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),3000);
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
NEW = (NEW.replace('__CASTS__', json.dumps(CASTS, ensure_ascii=False))
          .replace('__POOL__', json.dumps(POOL, ensure_ascii=False))
          .replace('__SPECIAL__', json.dumps(SPECIAL, ensure_ascii=False)))
s = s[:a] + NEW + s[b:]
log.append('OK   表情管理 JS 整块替换（真实 ID / 安全键池 / 按幕取表情）')

# ---------- 5. 面板 CSS：复用色类名 ----------
s = s.replace('.exprtxt em.代用{color:#8A5A22}', '.exprtxt em.复用{color:#8A5A22}')
log.append('OK   CSS 复用色类名')

# ---------- 6. 注入 10 张 WebP（插在 ART 对象结束之后，避免 R43 的语法事故） ----------
EMB = json.load(open('/data/workspace/anim39/_EMB.json'))
emb = ('/* R44 补 10 张：逐张独立生成的整帧（非拼接），9 接入 1 行头缺失不接入显示 */\n'
       'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + emb + s[e:]
log.append('OK   10 张 WebP 注入 ART（在 }; 之后）')

# ---------- 7. 版本号 ----------
s = s.replace('R43', 'R44', 1)
open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
