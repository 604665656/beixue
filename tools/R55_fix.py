# -*- coding: utf-8 -*-
"""R55 修复：
   ① PROC_ART 游离键 R50_ying_ai（R55 已把 cos_ying|哀 换成 AI 原画，旧程序化层
      被挤出谱系但仍在集合里，脚注「待 AI 重画」计数虚高）→ 按当前谱系重建集合
   ② 导出 CSV 文件名写死「筛选125格」→ 跟随 exprList().length 实算
   ③ 脚注「待 AI 重画 N 张」按 PROC_ART 全量 → 只数当前谱系内的程序化格
   幂等。"""
import re, json

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

spec = json.loads(re.search(r'const EXPR_SPECIAL=(\{[\s\S]*?\});', s).group(1))
vals = set(spec.values())

# ① 重建 PROC_ART，只留当前谱系内的键
m = re.search(r'const PROC_ART=new Set\((\[[\s\S]*?\])\);', s)
old = set(re.findall(r'"([^"]+)"', m.group(1)))
stale = sorted(old - vals)
keep = [k for k in json.loads(m.group(1)) if k in vals]
s = s[:m.start()] + 'const PROC_ART=new Set(' + json.dumps(keep, ensure_ascii=False) + ');' + s[m.end():]
log.append('OK  PROC_ART %d -> %d，剔除游离键 %s' % (len(old), len(keep), stale))

# ②③ 导出文件名与脚注改为按当前谱系实算
n = s.count('筛选125格')
s = s.replace('筛选125格', '筛选"+list.length+"格')
log.append('OK  导出文件名写死格数改实算 %d 处' % n)

# 脚注里的程序化计数：找形如 PROC_ART.size 的用法，换成谱系内实算
pat = re.findall(r'PROC_ART\.size', s)
log.append('info PROC_ART.size 出现 %d 处（脚注/面板）' % len(pat))
repl = 'EXPR.filter(function(e){return PROC_ART.has(e.art);}).length'
s = s.replace('PROC_ART.size', repl)
log.append('OK  程序化计数改为只数谱系内格')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (%+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
