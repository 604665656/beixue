# -*- coding: utf-8 -*-
"""R46：修 3 个真 bug（表情恒定 / 表演同角色 / 面板只显示 120 格）+ 接入 10 张专属层。"""
import json, re

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

# ---------- 1. 追加 10 项专属层 ----------
NEW_SPECIAL = {
    'cos_base|决': 'R46_base_jue', 'cos_base|醉': 'R46_base_zui',
    'cos_luo|静息': 'R46_luo_jing', 'cos_jin|静息': 'R46_jin_jing',
    'cos_yi|决': 'R46_yi_jue', 'cos_yi|醉': 'R46_yi_zui',
    'cos_zhu|决': 'R46_zhu_jue',
    'cos_xiao|怒': 'R46_xiao_nu', 'cos_xiao|哀': 'R46_xiao_ai',
    'cos_qinwen|醉': 'R46_qin_zui',
}
a = s.index('const EXPR_SPECIAL='); b = s.index(';', a) + 1
cur = json.loads(s[s.index('{', a):b - 1])
for k, v in NEW_SPECIAL.items():
    assert k not in cur, '专属格重复: ' + k
    cur[k] = v
s = s[:a] + 'const EXPR_SPECIAL=' + json.dumps(cur, ensure_ascii=False) + ';' + s[b:]
log.append('OK  EXPR_SPECIAL 26 -> %d 项（R46 10 格）' % len(cur))

# ---------- 2. 真 bug①：24 关表情恒定「静息」 ----------
OLD_MOOD = """function exprMoodFor(k){
 try{ const st=S[k]; const i=(st&&typeof st.i==='number')?st.i:((st&&typeof st.node==='number')?st.node:0);
   return EXPR_MOODS[((i%8)+8)%8]; }catch(e){ return '静息'; }
}"""
NEW_MOOD = """/* R46 bug①：旧实现只读 S[k].i，24 关初始全是 0 -> 全落 EXPR_MOODS[0]='静息'；
   A 关 node 是字符串 's1' -> NaN -> EXPR_MOODS[undefined] -> 回退静息。
   实测 24/24 关恒定静息，8 种表情只用到 1 种。改为「关卡稳定偏移 + 当前幕」双因子。 */
function exprMoodFor(k){
 try{
  const st=S[k]||{};
  let n=st.i;
  if(typeof n!=='number')n=st.node;
  if(typeof n!=='number')n=st.k;
  if(typeof n!=='number')n=st.qi;
  if(typeof n==='string'){ let h=0; for(let j=0;j<n.length;j++)h=(h*31+n.charCodeAt(j))|0; n=Math.abs(h); }
  if(typeof n!=='number'||!isFinite(n))n=0;
  let off=0; const id=String(k||'');
  for(let j=0;j<id.length;j++)off=(off*31+id.charCodeAt(j))|0;
  const idx=((Math.trunc(Math.abs(n)+Math.abs(off))%EXPR_MOODS.length)+EXPR_MOODS.length)%EXPR_MOODS.length;
  return EXPR_MOODS[idx];
 }catch(e){ return '静息'; }
}"""
assert OLD_MOOD in s, 'exprMoodFor anchor missing'
s = s.replace(OLD_MOOD, NEW_MOOD, 1)
log.append('OK  bug① exprMoodFor 改为关卡偏移+当前幕，24 关不再恒定静息')

# ---------- 3. 真 bug②：接管后 queuePerf 的 root() 认不出同角色 ----------
OLD_ROOT = """  const root=k=>k.split('_').slice(0,2).join('_');   /* 尽量换成与当前立绘不同的人物，表演才看得见 */
  if(root(key)===root(base)){ mi=(mi+1)%m.arts.length; key=m.arts[mi]; }"""
NEW_ROOT = """  /* R46 bug②：接管后 base 变成层键（R46_yi_jue），旧 root() 得 'R46_yi'，
     而 m.arts 是 cos_yi_cup -> 'cos_yi'，比较永远不等，「换不同人物」失效。
     统一走 exprCanon 规整成基础角色键再比。 */
  const root=k=>{ try{ return exprCanon(k); }catch(e){ return k.split('_').slice(0,2).join('_'); } };
  if(root(key)===root(base)){ mi=(mi+1)%m.arts.length; key=m.arts[mi]; }"""
assert OLD_ROOT in s, 'queuePerf root anchor missing'
s = s.replace(OLD_ROOT, NEW_ROOT, 1)
log.append('OK  bug② queuePerf root 改走 exprCanon，接管后表演仍会换不同人物')

# ---------- 4. 真 bug③：面板默认只显示 120/184 格 ----------
old_cards = "const cards=list.slice(0,120).map(e=>{"
assert old_cards in s
s = s.replace(old_cards, "const cards=list.map(e=>{", 1)
old_foot = "'<div class=\"exprfoot\">R45：角色全集对齐 CAST_META 短键（23 位），4 个表情层键归回各自角色；复用只从本角色池取，跨角色串脸 0。显示 '+Math.min(120,list.length)+'/'+list.length+' 格，源键可见。</div>'+"
new_foot = "'<div class=\"exprfoot\">R46：角色全集 23 位，复用只从本角色池取（串脸 0）；面板默认列出筛选结果全部 '+list.length+' 格，不截断。显示 '+list.length+'/'+EXPR.length+' 格，源键可见。</div>'+"
assert old_foot in s, 'exprfoot anchor missing'
s = s.replace(old_foot, new_foot, 1)
log.append('OK  bug③ 表情面板不再截断 120 格，筛选结果全量列出')

# ---------- 5. 注入 10 张 WebP ----------
EMB = json.load(open('/data/workspace/anim41/_EMB.json'))
assign = ('/* R46 补 10 张：按 R46 排期把高频复用格专属化，逐张独立整帧（非拼接） */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + assign + s[e:]
log.append('OK  10 张 WebP 注入 ART（在 }; 之后）')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
