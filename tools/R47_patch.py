# -*- coding: utf-8 -*-
"""R47：最后一轮 10 张专属层接入 + 修 2 个过期/统计 bug。"""
import json

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

# ---------- 1. 追加 10 项专属层（R47 队列，按修复后 mood 算法实算的 Top10） ----------
NEW = {
    'cos_yi|怒': 'R47_yi_nu', 'cos_yi|疑': 'R47_yi_yi',
    'cos_zhu|疑': 'R47_zhu_yi', 'cos_yi|惊': 'R47_yi_jing',
    'cos_xiao|醉': 'R47_xiao_zui', 'cos_base|惊': 'R47_base_jing',
    'cos_jin|哀': 'R47_jin_ai', 'cos_jin|惊': 'R47_jin_jing',
    'cos_jin|疑': 'R47_jin_yi', 'cos_xiao|惊': 'R47_xiao_jing',
}
a = s.index('const EXPR_SPECIAL='); b = s.index(';', a) + 1
cur = json.loads(s[s.index('{', a):b - 1])
for k, v in NEW.items():
    assert k not in cur, '专属格重复: ' + k
    cur[k] = v
s = s[:a] + 'const EXPR_SPECIAL=' + json.dumps(cur, ensure_ascii=False) + ';' + s[b:]
log.append('OK  EXPR_SPECIAL 36 -> %d 项（R47 10 格）' % len(cur))

# ---------- 2. 真 bug①：CSV 导出文件名写死 R45 ----------
old_csv = "a.download='杯雪表情谱系_R45.csv';"
assert old_csv in s
new_csv = "a.download='杯雪表情谱系_R47.csv';"
s = s.replace(old_csv, new_csv, 1)
log.append('OK  bug① 导出 CSV 文件名 R45 -> R47（否则导出文件看起来像旧数据）')

# ---------- 3. 真 bug②：面板脚注写死 R46 且不显示覆盖度 ----------
old_foot = "'<div class=\"exprfoot\">R46：角色全集 23 位，复用只从本角色池取（串脸 0）；面板默认列出筛选结果全部 '+list.length+' 格，不截断。显示 '+list.length+'/'+EXPR.length+' 格，源键可见。</div>'+"
assert old_foot in s, 'exprfoot anchor missing'
new_foot = ("(function(){var st=exprStat();return '<div class=\"exprfoot\">R47：'+EXPR_CASTS.length+' 位真实角色 × '+EXPR_MOODS.length+' 表情 = '+EXPR.length+' 格；"
            "专属 '+st.专属+' / 复用 '+st.复用+' / 待补 '+st.待补+'；复用只从本角色池取（串脸 0）。"
            "当前列出 '+list.length+'/'+EXPR.length+' 格，源键可见。</div>';})()+")
s = s.replace(old_foot, new_foot, 1)
log.append('OK  bug② 面板脚注改动态统计（专属/复用/待补实算），不再写死 R46')

# ---------- 4. 注入 10 张 WebP（放在 ART 字面量 }; 之后，避免语法错） ----------
EMB = json.load(open('/data/workspace/anim42/_EMB.json'))
assign = ('/* R47 补 10 张：专属化队列最后一轮，逐张独立整帧（非拼接） */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + assign + s[e:]
log.append('OK  10 张 WebP 注入 ART')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
