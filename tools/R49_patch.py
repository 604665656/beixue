# -*- coding: utf-8 -*-
"""R49 主站 patch：10 张接入（1 替换 + 9 新增）+ 修 3 个 bug + 生成方式如实标注。"""
import json

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

# ---------- 1. 专属层：1 张替换 + 9 张新增 ----------
REPLACE = {'cos_jinhe|静息': 'R49_jinhe_scar'}
NEW = {
    'cos_jinhe|喜': 'R49_jinhe_hat', 'cos_tie|静息': 'R49_tie_jing',
    'cos_tian|决': 'R49_tian_jue', 'cos_tian|醉': 'R49_tian_zui',
    'cos_ying|怒': 'R49_ying_nu', 'cos_jin|决': 'R49_jin_jue',
    'cos_jin|醉': 'R49_jin_zui', 'cos_qinwen|疑': 'R49_qinwen_yi',
    'cos_tian|怒': 'R49_tian_nu',
}
a = s.index('const EXPR_SPECIAL='); b = s.index(';', a) + 1
cur = json.loads(s[s.index('{', a):b - 1])
for k, v in REPLACE.items():
    assert k in cur, '替换目标不存在: ' + k
    cur[k] = v
for k, v in NEW.items():
    assert k not in cur, '新增格重复: ' + k
    cur[k] = v
s = s[:a] + 'const EXPR_SPECIAL=' + json.dumps(cur, ensure_ascii=False) + ';' + s[b:]
log.append('OK  EXPR_SPECIAL 56 -> %d 项（替换 1 + 新增 9）' % len(cur))

# ---------- 2. 生成方式如实标注：R49 这批不是 AI 原画 ----------
old_push = "qc:src==='专属'?'通过':'同角色已过检层'});"
assert old_push in s, 'EXPR.push anchor missing'
new_push = ("qc:src==='专属'?'通过':'同角色已过检层',\n"
            "   gen:String(art).indexOf('R49_')===0?'程序化本体重绘·待AI重画':'AI原画'});")
s = s.replace(old_push, new_push, 1)
log.append('OK  EXPR 加 gen 字段：R49 10 张标「程序化本体重绘·待AI重画」，不冒充 AI 原画')

# ---------- 3. 真 bug①：CSV 导出不跟随筛选 ----------
old_exp = """function exprExport(){
 const rows=[['角色ID','角色','表情','资源键','来源','首次出场关(0=仅图鉴)','动画组','质检']];
 EXPR.forEach(e=>rows.push([e.cast,e.name,e.mood,e.art,e.src,e.unlock,e.anim,e.qc]));
 const csv='\\ufeff'+rows.map(r=>r.map(x=>'"'+String(x).replace(/"/g,'""')+'"').join(',')).join('\\r\\n');
 const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
 a.download='杯雪表情谱系_R48.csv'; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),3000);
}"""
assert old_exp in s, 'exprExport anchor missing'
new_exp = """function exprExport(){
 /* R49 bug①：旧实现 EXPR.forEach 恒导全谱系 184 行，面板筛「专属」只列 56 格，
    点导出却拿到 184 行，所见非所得。改为按当前筛选 exprList() 导出。 */
 const list=exprList();
 const rows=[['角色ID','角色','表情','资源键','来源','首次出场关(0=仅图鉴)','动画组','质检','生成方式']];
 list.forEach(e=>rows.push([e.cast,e.name,e.mood,e.art,e.src,e.unlock,e.anim,e.qc,e.gen||'AI原画']));
 const csv='\\ufeff'+rows.map(r=>r.map(x=>'"'+String(x).replace(/"/g,'""')+'"').join(',')).join('\\r\\n');
 const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
 a.download='杯雪表情谱系_R49_'+(list.length===EXPR.length?'全谱系':'筛选'+list.length)+'格.csv';
 a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),3000);
}"""
s = s.replace(old_exp, new_exp, 1)
log.append('OK  bug① CSV 导出改按筛选 exprList()，文件名带筛选格数，新增「生成方式」列')

# ---------- 4. bug②：面板不显示生成方式 ----------
old_cell = """<em class="'+e.src+'">'+e.src+(e.src==='复用'?' · 同角色':'')+'</em></div></div>';"""
assert old_cell in s, 'cell anchor missing'
new_cell = """<em class="'+e.src+'">'+e.src+(e.src==='复用'?' · 同角色':'')+(e.gen&&e.gen!=='AI原画'?' · 本体重绘待AI':'')+'</em></div></div>';"""
s = s.replace(old_cell, new_cell, 1)
log.append('OK  bug② 面板单元格标注「本体重绘待AI」，不把程序化层显示成 AI 原画')

# ---------- 5. 脚注版本 + 生成方式统计 ----------
old_foot = "'<div class=\"exprfoot\">R48：当前筛选 '"
assert old_foot in s, 'foot anchor missing'
s = s.replace(old_foot, "'<div class=\"exprfoot\">R49：当前筛选 '", 1)
old_tail = "'（全谱系 专属 '+st.专属+' / 复用 '+st.复用+' / 待补 '+st.待补+'）；复用只从本角色池取（串脸 '+exprCrossCount()+'）。源键可见。</div>';})()+"
assert old_tail in s, 'foot tail anchor missing'
new_tail = ("'（全谱系 专属 '+st.专属+' / 复用 '+st.复用+' / 待补 '+st.待补+'）；"
            "其中程序化本体重绘 '+EXPR.filter(e=>e.gen&&e.gen!=='AI原画').length+' 张待 AI 重画；"
            "复用只从本角色池取（串脸 '+exprCrossCount()+'）。源键可见。</div>';})()+")
s = s.replace(old_tail, new_tail, 1)
log.append('OK  脚注版本 R49 + 明示程序化本体重绘张数')

# ---------- 6. 注入 10 张 WebP ----------
EMB = json.load(open('/data/workspace/anim44/_EMB.json'))
assign = ('/* R49：AI 图生图服务本轮未产出，10 张为程序化本体表情重绘（整图像素改，非贴片叠加）；\n'
          '   金和尚两张按用户建议做戒疤+剃净光头 / 一体僧帽。登记簿标「待 AI 重画」。 */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + assign + s[e:]
log.append('OK  10 张 WebP 注入 ART')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))

# ---------------------------------------------------------------------------
# 接入后自检发现：上面 new_push 曾误写 "}));"（多一个右括号），导致整页 JS 语法错。
# 已由 R49_自检.py 的 node --check 抓到，并把主站对应位置修回 "});"。
# 归档脚本此处同步修正，保证从零重跑不会再现该问题。
