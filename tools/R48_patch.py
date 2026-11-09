# -*- coding: utf-8 -*-
"""R48：10 张零专属角色专属层接入 + 修 3 个真 bug。"""
import json

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

# ---------- 1. 10 项专属层（R48 均衡轮：11 位零专属角色先补 10 位） ----------
NEW = {
    'cos_jinhe|静息': 'R48_jinhe_jing', 'cos_du|静息': 'R48_du_jing',
    'cos_jiao|喜': 'R48_jiao_xi', 'cos_gbx|怒': 'R48_gbx_nu',
    'cos_qu|静息': 'R48_qu_jing', 'cos_yuaner|怒': 'R48_yuaner_nu',
    'cos_wen|怒': 'R48_wen_nu', 'cos_mi|静息': 'R48_mi_jing',
    'cos_shi|静息': 'R48_shi_jing', 'cos_zwl|静息': 'R48_zwl_jing',
}
a = s.index('const EXPR_SPECIAL='); b = s.index(';', a) + 1
cur = json.loads(s[s.index('{', a):b - 1])
for k, v in NEW.items():
    assert k not in cur, '专属格重复: ' + k
    cur[k] = v
s = s[:a] + 'const EXPR_SPECIAL=' + json.dumps(cur, ensure_ascii=False) + ';' + s[b:]
log.append('OK  EXPR_SPECIAL 46 -> %d 项（R48 10 格）' % len(cur))

# ---------- 2. 真 bug①：CSV「解锁关」按角色数组下标算、运行时从不消费 ----------
FIRST = json.load(open('/data/workspace/44_表情管理/R48_首次出场关.json'))
const = ('/* R48 bug①：旧 unlock=Math.min(24,ci) 只是 EXPR_CASTS 数组下标，伪装成「解锁关」，'
         '运行时 exprResolve 从不消费；改为逐关 stageFor 实算的首次出场关，0=仅图鉴/拆读站出场。 */\n'
         'const FIRST_LV=' + json.dumps(FIRST, ensure_ascii=False) + ';\n')
anchor = 'const EXPR_CASTS=['
s = s.replace(anchor, const + anchor, 1)
old_unlock = 'unlock:Math.min(24,ci),'
assert old_unlock in s
s = s.replace(old_unlock, 'unlock:(FIRST_LV[c[0]]||0),', 1)
old_hdr = "const rows=[['角色ID','角色','表情','资源键','来源','解锁关','动画组','质检']];"
assert old_hdr in s
s = s.replace(old_hdr, "const rows=[['角色ID','角色','表情','资源键','来源','首次出场关(0=仅图鉴)','动画组','质检']];", 1)
log.append('OK  bug① CSV 解锁关 -> 首次出场关实算 %d 位，其余 9 位为 0' % len(FIRST))

# ---------- 3. 真 bug②：面板头部/脚注统计不跟随筛选 ----------
old_head = ("'<div class=\"exprh\"><b>☰ 表情管理</b><span>'+EXPR_CASTS.length+' 角色 × '+EXPR_MOODS.length+' 表情 = '+EXPR.length+' 格 ｜ 专属 '+st.专属+' · 复用 '+st.复用+' · 待补 '+st.待补+' ｜ 串脸 '+exprCrossCount()+'</span>'+")
new_head = ("'<div class=\"exprh\"><b>☰ 表情管理</b><span>全谱系 '+EXPR_CASTS.length+' 角色 × '+EXPR_MOODS.length+' 表情 = '+EXPR.length+' 格 ｜ 专属 '+st.专属+' · 复用 '+st.复用+' · 待补 '+st.待补+' ｜ 串脸 '+exprCrossCount()+'</span>'+")
assert old_head in s, 'head anchor missing'
s = s.replace(old_head, new_head, 1)

old_foot = ("(function(){var st=exprStat();return '<div class=\"exprfoot\">R47：'+EXPR_CASTS.length+' 位真实角色 × '+EXPR_MOODS.length+' 表情 = '+EXPR.length+' 格；专属 '+st.专属+' / 复用 '+st.复用+' / 待补 '+st.待补+'；复用只从本角色池取（串脸 0）。当前列出 '+list.length+'/'+EXPR.length+' 格，源键可见。</div>';})()+")
assert old_foot in s, 'foot anchor missing'
new_foot = ("(function(){var f={专属:0,复用:0,待补:0};list.forEach(function(e){f[e.src]++;});"
            "return '<div class=\"exprfoot\">R48：当前筛选 '+list.length+'/'+EXPR.length+' 格 ｜ 专属 '+f.专属+' · 复用 '+f.复用+' · 待补 '+f.待补+"
            "'（全谱系 专属 '+st.专属+' / 复用 '+st.复用+' / 待补 '+st.待补+'）；复用只从本角色池取（串脸 '+exprCrossCount()+'）。源键可见。</div>';})()+")
s = s.replace(old_foot, new_foot, 1)
log.append('OK  bug② 面板脚注改按筛选列表实算，头部明确标「全谱系」；串脸数也改实算')

# ---------- 4. 版本号 / 导出文件名 ----------
s = s.replace("a.download='杯雪表情谱系_R47.csv';", "a.download='杯雪表情谱系_R48.csv';", 1)
log.append('OK  CSV 导出文件名 R47 -> R48')

# ---------- 5. 注入 10 张 WebP ----------
EMB = json.load(open('/data/workspace/anim43/_EMB.json'))
assign = ('/* R48 补 10 张：11 位零专属角色先补 10 位，逐张独立整帧（非拼接） */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + assign + s[e:]
log.append('OK  10 张 WebP 注入 ART')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
