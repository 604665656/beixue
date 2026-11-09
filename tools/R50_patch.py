# -*- coding: utf-8 -*-
"""R50 主站 patch：10 张接入 + 修 3 个 bug + 版本推进。
   bug①（真）：gen 判断写死 'R49_' 前缀 -> 新轮次程序化层会被冒充 AI 原画。
               改为显式 PROC_ART 集合，后续轮次只往集合加，不误伤历史真原画。
   bug②（真）：CSV 导出文件名写死 R49。
   bug③（真）：面板脚注版本写死 R49。"""
import json

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s); log = []

R49 = ["R49_jinhe_scar","R49_jinhe_hat","R49_tie_jing","R49_tian_jue","R49_tian_zui",
       "R49_ying_nu","R49_jin_jue","R49_jin_zui","R49_qinwen_yi","R49_tian_nu"]
QC = json.load(open('/data/workspace/anim45/_QC.json'))
NEW = {QC['META'][k]['exprkey']: k for k in QC['META']}
R50 = list(NEW.values())

# ---------- 1. bug①：gen 判断改为显式集合 ----------
old_gen = "gen:String(art).indexOf('R49_')===0?'程序化本体重绘·待AI重画':'AI原画'});"
assert old_gen in s, 'gen anchor missing'
s = s.replace(old_gen, "gen:PROC_ART.has(art)?'程序化本体重绘·待AI重画':'AI原画'});", 1)
anchor = "const EXPR_APPLY_KEY='beixue_expr_apply_v1';"
assert anchor in s, 'APPLY_KEY anchor missing'
decl = ("/* R50 bug①：R49 把 gen 写死 'R49_' 前缀，任何后续轮次的新程序化层都不会被标注，\n"
        "   面板/CSV 会把程序化层显示成 AI 原画。改成显式集合：只列真程序化层，\n"
        "   不误伤 R22_/R30_/R47_ 等历史真 AI 原画，后续轮次往集合追加即可。 */\n"
        "const PROC_ART=new Set(" + json.dumps(R49 + R50, ensure_ascii=False) + ");\n")
s = s.replace(anchor, decl + anchor, 1)
log.append('OK  bug① gen 判断改 PROC_ART 集合（%d 项），R50 层不会被冒充 AI 原画' % len(R49+R50))

# ---------- 2. EXPR_SPECIAL 新增 10 项 ----------
a = s.index('const EXPR_SPECIAL='); b = s.index(';', a) + 1
cur = json.loads(s[s.index('{', a):b-1])
for k, v in NEW.items():
    assert k not in cur, '新增格重复: ' + k
    cur[k] = v
s = s[:a] + 'const EXPR_SPECIAL=' + json.dumps(cur, ensure_ascii=False) + ';' + s[b:]
log.append('OK  EXPR_SPECIAL %d -> %d 项（R50 新增 10）' % (len(cur)-10, len(cur)))

# ---------- 3. bug② CSV 文件名版本 ----------
assert "a.download='杯雪表情谱系_R49_'" in s
s = s.replace("a.download='杯雪表情谱系_R49_'", "a.download='杯雪表情谱系_R50_'", 1)
log.append('OK  bug② CSV 文件名 R49 -> R50')

# ---------- 4. bug③ 脚注版本 ----------
assert "'<div class=\"exprfoot\">R49：当前筛选 '" in s
s = s.replace("'<div class=\"exprfoot\">R49：当前筛选 '", "'<div class=\"exprfoot\">R50：当前筛选 '", 1)
log.append('OK  bug③ 面板脚注版本 R49 -> R50')

# ---------- 5. 注入 10 张 WebP ----------
EMB = json.load(open('/data/workspace/anim45/_EMB.json'))
assign = ('/* R50：AI 图生图服务本轮未产出，10 张沿用 R49 口径走程序化本体表情重绘，\n'
          '   基于同角色已过检原图的整张像素改 哀/惊/疑/怒，非贴片叠加、非切片拼接。 */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = '); e = s.index('};', art) + 2
s = s[:e] + '\n' + assign + s[e:]
log.append('OK  10 张 WebP 注入 ART')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s)-orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
