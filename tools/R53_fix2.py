# -*- coding: utf-8 -*-
"""R53 fix2：池同步后暴露的 3 处口径错位。
   复用格借用了程序化源层，却被脚注/卡片/CSV 当成「待 AI 重画的新层」计数。
   幂等。"""
P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []


def rep(old, new):
    global s
    if new in s:
        log.append('OK  已修复（幂等跳过）: ' + old[:46])
        return
    assert old in s, 'MISS: ' + old[:80]
    s = s.replace(old, new, 1)
    log.append('OK  ' + old[:46])


# ① 脚注：待 AI 重画张数只数【专属格】，复用格借用不算新增层
rep("EXPR.filter(e=>e.gen&&e.gen!=='AI原画').length+' 张待 AI 重画",
    "EXPR.filter(e=>e.src==='专属'&&e.gen&&e.gen!=='AI原画').length+' 张待 AI 重画")

# ② 卡片标签：只在专属格标「本体重绘待AI」
rep("+(e.gen&&e.gen!=='AI原画'?' · 本体重绘待AI':'')",
    "+(e.src==='专属'&&e.gen&&e.gen!=='AI原画'?' · 本体重绘待AI':'')")

# ③ CSV 生成方式列：复用格写清是借用，不冒充该格生成方式
rep("list.forEach(e=>rows.push([e.cast,e.name,e.mood,e.art,e.src,e.unlock,e.anim,e.qc,e.gen||'AI原画']));",
    "list.forEach(e=>rows.push([e.cast,e.name,e.mood,e.art,e.src,e.unlock,e.anim,e.qc,"
    "e.src==='专属'?(e.gen||'AI原画'):'同角色复用（源层生成方式见资源键）']));")

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
