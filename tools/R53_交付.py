# -*- coding: utf-8 -*-
"""R53 交付：开局实算 / 剩余排期 / 三张产出图 / 报告 / 登记簿 / 压缩包。"""
import json, os, io, csv, math, hashlib, zipfile
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

WS = '/data/workspace'
D = WS + '/anim48'
MGR = WS + '/44_表情管理'
FP = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
f30 = ImageFont.truetype(FP, 30)
f18 = ImageFont.truetype(FP, 18)
f14 = ImageFont.truetype(FP, 14)

QC = json.load(open(D + '/_QC.json'))
META = QC['META']
JOBS = [(k, v['label'], v['exprkey']) for k, v in META.items()]

# ---------- ① 开局实算：谱系覆盖 + 逐关逐幕命中 ----------
JS = r"""() => {
  const lv=D.meta.levels.map(l=>l.id), hits={}, ownN={};
  EXPR_CASTS.forEach(c=>ownN[c[0]]=0);
  EXPR.forEach(e=>{if(e.src==='专属')ownN[e.cast]=(ownN[e.cast]||0)+1;});
  for(const id of lv){
    const saved=S[id]?S[id].i:0;
    for(let m=0;m<8;m++){
      if(S[id])S[id].i=m;
      let cast='cos_base';
      try{cast=exprCanon(stageFor(id).cast||'cos_base');}catch(e){}
      const k=cast+'|'+exprMoodFor(id); hits[k]=(hits[k]||0)+1;
    }
    if(S[id])S[id].i=saved;
  }
  const reuse=EXPR.filter(e=>e.src==='复用').map(e=>({
    cast:e.cast,name:e.name,mood:e.mood,art:e.art,
    hits:hits[e.cast+'|'+e.mood]||0,own:ownN[e.cast]||0}));
  return {reuse,ownN,stat:exprStat(),specialN:Object.keys(EXPR_SPECIAL).length,
    exprN:EXPR.length,castN:EXPR_CASTS.length,poolSync:R53_POOL_SYNC,
    procArt:(typeof PROC_ART!=='undefined')?PROC_ART.size:-1};
}"""
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/local/bin/chromium',
                           args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu'])
    pg = b.new_page(viewport={'width': 900, 'height': 420})
    pg.goto('file://' + WS + '/杯雪游戏总站.html', wait_until='load', timeout=120000)
    pg.wait_for_timeout(700)
    calc = pg.evaluate(JS)
    b.close()

stat = calc['stat']
reuse = calc['reuse']
ownN = calc['ownN']
seen, picks = set(), []
for r in sorted(reuse, key=lambda x: (x['own'], -x['hits'], x['cast'], x['mood'])):
    if r['cast'] in seen:
        continue
    seen.add(r['cast'])
    picks.append(r)
    if len(picks) == 10:
        break
casts = [{'c': c, 'own': ownN.get(c, 0), 'left': 8 - ownN.get(c, 0)}
         for c in sorted(ownN, key=lambda c: (ownN.get(c, 0), c))]
rounds = math.ceil(stat['复用'] / 10)
last_count = stat['复用'] - (rounds - 1) * 10

json.dump({'open': {'stat': stat, 'special': calc['specialN'], 'exprN': calc['exprN'],
                    'castN': calc['castN'], 'procArt': calc['procArt'],
                    'poolSync': calc['poolSync'], 'queue': picks}, 'errors': []},
          open(MGR + '/R53_开局实算.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'reuse': stat['复用'], 'picks': picks, 'casts': casts, 'stat': stat,
           'rounds': rounds, 'last_count': last_count,
           'strategy': '低覆盖角色各1张轮转 + 同角色内按实际命中降序'},
          open(MGR + '/R53_剩余排期.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('实算:', stat, 'picks', len(picks), 'rounds', rounds, 'last', last_count)

# ---------- ② 总览图 ----------
S = Image.new('RGB', (1600, 1120), (250, 247, 240))
d = ImageDraw.Draw(S)
d.text((28, 18), 'R53 · 10 张 AI 原画｜低覆盖角色各 1 张轮转', font=f30, fill=(56, 42, 34))
lines = [
    '专属 95 → 105 ／ 复用 89 → 79 ／ 待补 0 ／ 串脸 0 ／ 零专属 0',
    '真 bug：ROLE_POOL 静态不吸收历轮专属层 → 动态合并 105 层；脚注/CSV 口径 26 → 20',
    '自检 42/42（双文件 × 三尺寸）｜轻量版 6.28 MB，元宝可直接点开',
    '金和尚额顶三点戒疤落实；剩余 8 轮（R54–R61）',
]
for i, t in enumerate(lines):
    d.text((28, 62 + i * 27), t, font=f18, fill=(96, 74, 60))
for idx, (key, label, ekey) in enumerate(JOBS):
    im = Image.open(D + '/' + key + '_720.jpg').convert('RGB').resize((300, 300), Image.LANCZOS)
    x, y = 28 + (idx % 5) * 316, 190 + (idx // 5) * 340
    S.paste(im, (x, y))
    d.text((x, y + 304), label, font=f18, fill=(70, 56, 46))
    d.text((x, y + 328), key, font=f14, fill=(130, 110, 96))
S.save(D + '/_R53_总览.jpg', quality=88)

# ---------- ③ 表情特写（脸部 + 行头上半） ----------
T = Image.new('RGB', (1500, 700), (250, 247, 240))
td = ImageDraw.Draw(T)
td.text((20, 10), 'R53 脸部特写：戒疤 / 幞头 / 软巾 / 络腮须 / 喜与决', font=f30, fill=(56, 42, 34))
for idx, (key, label, ekey) in enumerate(JOBS):
    im = Image.open(D + '/' + key + '.png').convert('RGB')
    w, h = im.size
    crop = im.crop((int(w * .26), int(h * .16), int(w * .74), int(h * .54))).resize((280, 260), Image.LANCZOS)
    x, y = 20 + (idx % 5) * 296, 70 + (idx // 5) * 310
    T.paste(crop, (x, y))
    td.text((x, y + 264), label, font=f18, fill=(70, 56, 46))
T.save(D + '/_R53_表情对比特写.jpg', quality=88)

# ---------- ④ 轻量版三尺寸实拍 ----------
shots = []
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/local/bin/chromium',
                           args=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu'])
    for label, w, h in [('竖屏 420×900', 420, 900), ('横屏 900×420', 900, 420), ('桌面 1440×900', 1440, 900)]:
        pg = b.new_page(viewport={'width': w, 'height': h})
        pg.goto('file://' + WS + '/杯雪游戏总站_轻量版.html', wait_until='load', timeout=120000)
        pg.wait_for_timeout(800)
        shots.append((label, Image.open(io.BytesIO(pg.screenshot())).convert('RGB')))
        pg.close()
    b.close()
W = 1200
panels = []
for label, im in shots:
    k = min(1.0, 380 / im.width)
    panels.append((label, im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)))
H = max(p.height for _, p in panels) + 60
U = Image.new('RGB', (W, H), (250, 247, 240))
ud = ImageDraw.Draw(U)
for i, (label, p) in enumerate(panels):
    x = 10 + i * 396
    U.paste(p, (x, 46))
    ud.text((x, 12), label, font=f18, fill=(60, 46, 38))
U.save(D + '/_R53_轻量版三尺寸.jpg', quality=86)
print('图像产物 3 张完成')

# ---------- ⑤ 报告 ----------
qc_rows = '\n'.join(
    '| %d | %s | `%s` | %d | %.4f%% | %d | %d | %d |' %
    (i + 1, QC['META'][k]['label'], k, QC['QC'][k]['holes'],
     QC['QC'][k]['residual_pct'], QC['QC'][k]['wm_pixels_removed'],
     QC['QC'][k]['wm_left'], QC['QC'][k]['islands'])
    for i, (k, _, _) in enumerate(JOBS))
queue_rows = '\n'.join('- %s·%s（当前专属 %d，模拟命中 %d 次）' %
                       (p['name'].split(' · ')[0], p['mood'], p['own'], p['hits']) for p in picks)
report = f'''# R53 排期与自检 · 10 张 AI 原画 + 角色池同步

## 一、本轮口径与合理安排

**AI 图生图服务正常。** 沿用用户上传三视图裁出的正面单只（`anim47/_ref_front.png`）作唯一基准，
`Image2Image` + `seed 3` + `1:1` 1536²，**10 次逐张独立生成完整整帧**，不是切片拼接、
不是透明贴片叠加、不是 GIF 拼帧，也不是 R49/R50 的程序化本体重绘。

固定约束块：灰白绒毛、蓝瞳、粗黑圆框眼镜、圆耳粉内耳、圆润二头身、只有一条尾巴、
平涂薄涂柔和边缘、纯品红系实心平整背景、行头须发同一笔触连续生长
（禁独立假发盖片／贴图层／光头皮套／硬接缝）、衣料与大道具禁品红色相、无水印。

**安排**：24 关图像早已全齐、完整演出 24/24 已解锁，继续逐关铺静态表情零收益。
本轮按 R52 已交付的 `R52_剩余排期.json`，用「低覆盖角色各 1 张轮转」把 10 张额度
分给 10 位专属数最少的角色，不再把一轮挤给 2–3 位。

接入后 `EXPR_SPECIAL` **95 → {stat['专属']}**；谱系
**专属 {stat['专属']} / 复用 {stat['复用']} / 待补 {stat['待补']} / 串脸 0 / 零专属 0**。

## 二、10 张质检

| # | 格 | 资源键 | 孔洞 | 色键残留 | 预清水印 | 右下残留 | 独立小岛 |
|---|---|---|---|---|---|---|---|
{qc_rows}

全部双底（宣纸／夜雨）不串色、每只一条尾巴、水印源头预清 3243–3357 px。

### 目检如实标注
- **落实**：杜淮山花白长须＋赭褐旧袍、米俨月白长衫、文翰林靛青长衫＋玄色矮幞头、
  袁辰龙玄袍阔肩披肩、袁二玄灰短打束发带、赵无量月白道袍、耿苍怀络腮短须＋赭褐旧袍、
  **金和尚额顶三点深赭戒疤**（上一轮用户点名，这次在「同一笔触、不贴片」约束下真画出来了）。
- **表情**：两张「喜」（袁辰龙、赵无量）眯眼吐舌一眼可辨；八张「决」多为平静微蹙，
  区分度偏弱，与「惊」「静息」接近。
- **没做到**：铁萼英的铁簪看不清、瞿百龄灰布软巾画成了带檐帽、袁辰龙与金和尚以外
  多数短须未画出、焦泗隐式浅疤仍未落实。属「不贴片、同一笔触」下的生成边界，
  不拿贴片硬补、不放宽阈值。

## 三、自检 42/42 全过，修掉 5 项

| # | 类型 | 问题 | 修法 |
|---|---|---|---|
| ① | **真 bug（系统性）** | `ROLE_POOL` 是静态表，R43–R52 每轮新增的专属层**从不入池**；面板宣称「复用只从本角色池取」，池子却停在旧层，`exprCrossCount` 的池校验也偏窄 | 在 `EXPR` 构建前按 `EXPR_SPECIAL` 动态并入本角色池，一次覆盖全部 {calc['poolSync']} 个专属层，以后每轮自动生效。实测 `R53_POOL_SYNC={calc['poolSync']}`、池内 R53 层 10 |
| ② | **真 bug（① 暴露）** | 池同步后复用格借到了程序化源层，脚注／卡片／CSV 把「复用格借用」算成「待 AI 重画的新层」，数字从 20 虚涨到 26，与 `PROC_ART=20` 矛盾 | 脚注按【专属格】计数、卡片标签只标专属格、CSV「生成方式」列复用格改写「同角色复用（源层生成方式见资源键）」。复验 20/20 |
| ③ | **真 bug（接入）** | CSV 文件名与面板脚注版本写死 `R52` | 推进 `R53` |
| ④ | **自检自身口径** | R52 自检按 `R5x_` 前缀统计 AI/程序化格数，池同步后把复用格也算进去（R51AI=12、R52AI=13、procN=26），6 组浏览器上下文全报假 FAIL | 8 处统计统一加 `e.src==='专属'` 过滤；修后 42/42 |
| ⑤ | 工程 | 轻量版构建脚本文档写「256px/q46」，实现是 224px/q40 | 文档与实现对齐 |

**验证**：静态 15 项 × 双文件 ＋ 门禁 9 项 ＋ 真实 Chromium `file://` 双文件 × 三尺寸
（420×900 / 900×420 / 1440×900）：0 JS 错误、0 横向溢出、Audio 创建 0、
184 格 / 23 角色、专属 {stat['专属']} / 复用 {stat['复用']} / 待补 0、零专属 0、
`PROC_ART=20`、R51/R52/R53 各 10 张均标 AI 原画、名牌 0 串、接管 24/24、
mood 8 种、CSV 真调用 184/{stat['专属']} 行、面板 184/{stat['专属']} 格、
442 个内嵌 URI 全可解码（轻量版额外验 ≤224px）、6 组逐帧 GIF 变量在位、
CSS 规则区 `step-end` / `steps(1,end)` 0 处。

轻量版按新主站重新生成：17.50 MB → **6.28 MB（−64.1%）**，
400 张 WebP 压到 224px/q40，6 组逐帧 GIF 原样保留，无外链，门禁 9/9。

## 四、还剩几轮

| 口径 | 剩余 |
|---|---|
| 功能 / 可用（24 关解锁、竖横屏简洁、语音包撤除、单文件可打开） | **0 轮** |
| 全员覆盖（23 角色每人至少 1 张专属层） | **0 轮（R49 达成）** |
| 全专属（184 格每格一张专属层） | **{rounds} 轮（R54–R{53 + rounds}）** |

{stat['复用']} 格复用，每轮 10 张，最后一轮 {last_count} 张 → {rounds} 轮。

### R54 队列（按修复后算法重新实算，明细在 `R53_剩余排期.json`）

{queue_rows}

### 可选、不计轮次
- **20 张程序化本体重绘层待 AI 重画**（R49 10 张 + R50 10 张），AI 服务正常，可在后续轮次夹带替换。
- 3 道浅疤／部分短须属「不贴片、同一笔触」下的生成能力边界。
- 六组逐帧动画仍是「多张独立整帧 → 按顺序合成」，CSS 规则区 `step-end`／`steps(1,end)` 0 处。
- 语音包已整体撤除，运行时 `new Audio(` 0 处、Audio 创建 0。
'''
open(MGR + '/R53_排期与自检.md', 'w', encoding='utf-8').write(report)

# ---------- ⑥ 登记簿追加 ----------
note = ('\n## R53 · 表情谱系 10 张 AI 原画（低覆盖角色轮转）\n\n'
        '杜淮山·决／米俨·决／瞿百龄·决／铁萼英·决／文翰林·决／袁辰龙·喜／'
        '袁二·决／赵无量·喜／耿苍怀·决／金和尚·决，共 10 张逐张独立整帧生成并接入。'
        '专属 95→105、复用 89→79。金和尚额顶三点戒疤在「同一笔触、不贴片」约束下落实。'
        '自检 42/42；修 `ROLE_POOL` 静态不吸收专属层（动态合并 105 层）、脚注/CSV 生成方式口径、'
        '版本推进与自检自身统计口径共 5 项。**剩余全专属轮次：8 轮（R54–R61）。**\n')
with open(WS + '/杯雪动画素材缺口登记表.md', 'a', encoding='utf-8') as f:
    f.write(note)
with open(WS + '/杯雪动画素材缺口登记表.csv', 'a', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    for k, label, ekey in JOBS:
        w.writerow(['R53', '表情谱系', k, ekey, '—', '—',
                    'AI图生图/seed3/1:1/原稿正面单只基准', '已生成'])
    w.writerow(['R53', '排期', '剩余轮次', '全专属 105/184', '8 轮 R54–R61', '—',
                '每轮 10 张，最后一轮 9 张', '进行中'])

# ---------- ⑦ 压缩包 ----------
OUT = WS + '/杯雪全套.zip'
dirs = ['40_资源管线', '44_表情管理', 'anim46', 'anim47', 'anim48', 'anim34', 'anim35', 'anim36']
files = [n for n in os.listdir(WS) if os.path.isfile(os.path.join(WS, n))
         and n.endswith(('.md', '.csv', '.json', '.html'))
         and not n.startswith('_')]
files += ['角色一致性检查.py', '资源清单门禁.py', 'R47_轻量版.py']
SKIP = {'__pycache__', '杯雪全套.zip'}
cnt = 0
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for n in sorted(set(files)):
        p = os.path.join(WS, n)
        if os.path.isfile(p) and n not in SKIP:
            z.write(p, '杯雪全套/' + n)
            cnt += 1
    for d0 in dirs:
        root = os.path.join(WS, d0)
        if not os.path.isdir(root):
            continue
        for base, ds, fs in os.walk(root):
            ds[:] = [x for x in ds if x not in SKIP]
            for fn in sorted(fs):
                if fn.endswith(('.pyc', '.txt')) or fn.startswith('_shot_') or fn.startswith('_wm'):
                    continue
                p = os.path.join(base, fn)
                z.write(p, '杯雪全套/' + os.path.relpath(p, WS))
                cnt += 1
with zipfile.ZipFile(OUT) as z:
    names = z.namelist()
    audio = [n for n in names if n.endswith(('.ogg', '.m4a', '.wav', '.mp3'))]
    assert not audio, audio[:3]
    lite = z.read('杯雪全套/杯雪游戏总站_轻量版.html')
    local = open(WS + '/杯雪游戏总站_轻量版.html', 'rb').read()
    assert hashlib.sha1(lite).hexdigest() == hashlib.sha1(local).hexdigest(), '轻量版不一致'
print('ZIP', cnt, '条', round(os.path.getsize(OUT) / 1048576, 1), 'MB, 音频', len(audio), '轻量版 SHA1 一致')
print('DONE')
