# -*- coding: utf-8 -*-
"""R28：夜雨皮肤下「校勘」选中卡浅底配浅字 → 字看不清。
统一三套皮肤 + 高对比的选中态配色变量，并覆盖所有同类卡的文字色。"""
import re, os, json

ROOT='/data/workspace'
MAIN=[ROOT+'/杯雪游戏总站.html',ROOT+'/杯雪离线总栈.html',ROOT+'/杯雪互动游戏集.html']
b=open(MAIN[0],encoding='utf-8').read()

# ---------- 1) 各皮肤新增选中态变量 ----------
VARS={
 ':root{': ' --onbg:#F2EEF4; --onink:#221C28; --onmuted:#4A3C55; --onaccent:#6A5076; --ontagink:#FFFDF6;\n',
 'html[data-skin="plain"]{': ' --onbg:#F0ECF5; --onink:#221C28; --onmuted:#4A3C55; --onaccent:#6B5478; --ontagink:#FFFDF6;\n',
 'html[data-skin="night"]{': ' --onbg:#241E2C; --onink:#FFF8EC; --onmuted:#E9DCF3; --onaccent:#C9A9DE; --ontagink:#1B1420;\n',
 'body.hc{': ' --onbg:#FFFFFF; --onink:#000000; --onmuted:#000000; --onaccent:#000000; --ontagink:#FFFFFF;\n',
}
for anchor,ins in VARS.items():
    i=b.find(anchor)
    assert i>0,anchor
    b=b[:i+len(anchor)]+ins+b[i+len(anchor):]

# ---------- 2) 小字字号提高（未选中卡也要更清楚） ----------
SZ=[
 ('.d4i .lead{font-size:10px;','.d4i .lead{font-size:11px;'),
 ('.d4i ul{margin:0;padding-left:13px;font-size:9.5px;','.d4i ul{margin:0;padding-left:13px;font-size:10.5px;'),
 ('.m4 ul{margin:0;padding-left:14px;font-size:10px;','.m4 ul{margin:0;padding-left:14px;font-size:10.5px;'),
 ('.mhcard ul{margin:0;padding-left:15px;font-size:10.5px;','.mhcard ul{margin:0;padding-left:15px;font-size:11px;'),
]
for old,new in SZ:
    assert old in b,old
    b=b.replace(old,new,1)
# 手机窄屏覆盖也同步
b=b.replace('.d4i .lead{font-size:9.5px}', '.d4i .lead{font-size:10.5px}',1)

# ---------- 3) 主样式表末尾追加统一规则（放在最后，压过旧的 night 专属 m4.on） ----------
FIX = r"""
/* ---------- R28：选中卡文字可读性（修夜雨下浅底配浅字） ----------
   根因：.d4i.on 硬编码 #F2EEF4 浅底，而夜雨皮肤 --ink/--muted/--purple 全是浅色，
   选中「校勘」时浅底上写浅紫/浅米字，几乎不可读。改为按皮肤给一组选中态变量。 */
.d4i.on,.m4.on,.mhcard.on,.mp-i.on{
 background:var(--onbg)!important;color:var(--onink)!important;
 border-color:var(--purple);
}
.m4.on,.mhcard.on,.mp-i.on{border-color:var(--green)}
.d4i.on b,.m4.on b,.mhcard.on b,.mp-i.on b,
.d4i.on .ico,.m4.on .ico,.mhcard.on .ico,
.d4i.on .chk,.m4.on .chk,.mhcard.on .chk{color:var(--onink)!important}
.d4i.on .lead,.m4.on .lead,.mhcard.on .lead,
.d4i.on ul,.m4.on ul,.mhcard.on ul,
.d4i.on li,.m4.on li,.mhcard.on li{color:var(--onmuted)!important}
.d4i.on ul li::marker,.m4.on ul li::marker,.mhcard.on ul li::marker{color:var(--onink)!important}
.d4i.on .tag,.m4.on .tag,.mhcard.on .tag{
 background:var(--onaccent)!important;color:var(--ontagink)!important;
 font-weight:700;
}
/* 选中卡在主文字下加一层极淡内描边，避免任何皮肤下再次出现「浅底浅字」 */
.d4i.on,.m4.on,.mhcard.on{box-shadow:inset 0 0 0 1px var(--onaccent)}
html[data-skin="night"] .d4i.on{background:var(--onbg)!important}
html[data-skin="night"] .m4.on,
html[data-skin="night"] .mp-i.on{background:var(--onbg)!important}
body.hc .d4i.on,body.hc .m4.on,body.hc .mhcard.on{
 background:#FFFFFF!important;color:#000000!important;box-shadow:inset 0 0 0 2px #000}
body.hc .d4i.on .lead,body.hc .d4i.on ul,body.hc .m4.on ul,body.hc .mhcard.on ul{color:#000000!important}
"""
# 插到主样式表（第二个 style）末尾，而不是第一个（只有背景图 base64）
ends=[m.start() for m in re.finditer(r'</style>',b)]
pos=ends[-1]
b=b[:pos]+FIX+b[pos:]
print('CSS 修复已追加，长度',len(FIX))

# ---------- 4) DATA 说明 ----------
dm=re.search(r'(<script type="application/json" id="DATA">(.*?)</script>)',b,re.S)
data=json.loads(dm.group(2))
data['perf']['note']=(data['perf'].get('note','')+
 ' R28：修「选择阅读难度」在夜雨皮肤下选中卡字看不清——根因是 .d4i.on 硬编码浅紫底，'
 '而夜雨皮肤的字色全是浅色。改为按皮肤统一 --onbg/--onink/--onmuted/--onaccent 四变量，'
 '覆盖 d4i/m4/mhcard/mp-i 全部选中态与高对比；小字 9.5→10.5px。')
b=b[:dm.start(2)]+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+b[dm.end(2):]

for fp in MAIN:open(fp,'w',encoding='utf-8').write(b)
open(ROOT+'/_z.js','w',encoding='utf-8').write(re.findall(r'<script>(.*?)</script>',b,re.S)[-1])
print('HTML KB',round(len(b.encode())/1024,1))

# ---------- 5) 登记 ----------
import csv
p=ROOT+'/杯雪动画素材缺口登记表.csv'
rows=list(csv.reader(open(p,encoding='utf-8-sig')))
rows.append(['R28','UI · 选中卡文字可读性','夜雨下 .d4i.on 硬编码浅底 vs 浅色字，校勘卡几乎不可读','难度/模式卡','1 项','P0',
             '按皮肤统一 --onbg/--onink/--onmuted/--onaccent，覆盖全部 on 态与高对比','已修复'])
with open(p,'w',encoding='utf-8-sig',newline='') as fo:csv.writer(fo).writerows(rows)
md=open(ROOT+'/杯雪动画素材缺口登记表.md',encoding='utf-8').read()
md+=("\n\n## R28 · 选中卡文字可读性\n\n"
 "**根因**：`.d4i.on` 硬编码 `background:#F2EEF4`（浅紫底），但夜雨皮肤的 "
 "`--ink:#EDE6D7` / `--muted:#C9C0AC` / `--purple:#B89CCB` 全是浅色——"
 "浅底上写浅字，选中「校勘」时三行说明几乎看不见。模式卡此前单独补过 night 深底，"
 "难度卡漏了，所以只有这一处翻车。\n\n"
 "**修法**：给三套皮肤与高对比各定义 `--onbg / --onink / --onmuted / --onaccent / --ontagink`，"
 "统一覆盖 `.d4i.on / .m4.on / .mhcard.on / .mp-i.on` 的背景、主字、副字、列表圆点与标签；"
 "夜雨下选中卡改深紫底 `#241E2C` + 近白字，标签浅紫底配深字。"
 "小字 9.5→10.5px、说明 10→11px。高对比强制纯白底纯黑字。\n")
open(ROOT+'/杯雪动画素材缺口登记表.md','w',encoding='utf-8').write(md)
print('登记 +1')
