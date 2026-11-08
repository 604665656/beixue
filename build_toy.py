#!/usr/bin/env python3
"""把单文件《杯雪》游戏总站构建成 B站 Toy 上架包。

平台硬规则：入口 index.html 解压后 <= 1MB，所有资源必须相对路径。
做法（只作用于 toy/ 产物，原始 HTML 一个字不改）：
  1. 把 252 处 data:image/...;base64 解码成真实图片，按内容指纹去重；
  2. 两个内联 <style> 外置为 ./styleN.css；
  3. 内联 JSON 数据块外置为 ./data.js（运行时回填同 id 的 script 节点，
     这样主脚本里的 JSON.parse(document.getElementById('DATA').textContent) 不用改）；
  4. 主脚本外置为 ./app.js；
  5. index.html 只留骨架与相对引用。

用法： python build_toy.py
"""
import base64
import hashlib
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "10_杯雪游戏总站.html"
OUT = ROOT / "toy"
ASSETS = OUT / "assets"

EXT = {"webp": "webp", "jpeg": "jpg", "jpg": "jpg", "png": "png", "gif": "gif"}

if not SRC.exists():
    raise SystemExit("找不到主游戏文件：%s" % SRC)

s = SRC.read_text(encoding="utf-8")
print("源文件：%s / %d B" % (SRC.name, SRC.stat().st_size))

if OUT.exists():
    shutil.rmtree(OUT)
ASSETS.mkdir(parents=True)

# ---------- 1. base64 图片外置 ----------
written = {}
seen = {}


def img_repl(m):
    mime, b64 = m.group(1), m.group(2)
    key = hashlib.sha1(b64.encode("ascii")).hexdigest()[:16]
    if key not in written:
        fn = "%s.%s" % (key, EXT[mime])
        (ASSETS / fn).write_bytes(base64.b64decode(b64))
        written[key] = fn
    seen[key] = seen.get(key, 0) + 1
    return "./assets/" + written[key]


PAT = re.compile(r"data:image/(webp|jpeg|jpg|png|gif);base64,([A-Za-z0-9+/=]+)")
s, n = PAT.subn(img_repl, s)
print("外置图片：%d 处引用 / %d 个唯一文件" % (n, len(written)))
if n < 200:
    raise SystemExit("图片外置数量异常，构建中止")

# ---------- 2. 内联 style 外置 ----------
style_no = [0]


def style_repl(m):
    style_no[0] += 1
    fn = "style%d.css" % style_no[0]
    (OUT / fn).write_text(m.group(2), encoding="utf-8")
    return '<link rel="stylesheet" href="./%s">' % fn


s, ns = re.subn(r"<style([^>]*)>(.*?)</style>", style_repl, s, flags=re.S | re.I)
print("外置样式块：%d" % ns)

# ---------- 3. 内联 JSON 外置为 data.js ----------
m = re.search(
    r'<script([^>]*type="application/json"[^>]*)>(.*?)</script>', s, re.S | re.I
)
if not m:
    # 属性顺序可能不同，放宽再找
    m = re.search(r"<script([^>]*id=\"DATA\"[^>]*)>(.*?)</script>", s, re.S | re.I)
if not m:
    raise SystemExit("未找到 DATA JSON 块，构建中止")
json_text = m.group(2)
parsed = json.loads(json_text)  # 校验是合法 JSON，避免静默写坏
js = (
    "(function(){var e=document.createElement('script');"
    "e.type='application/json';e.id='DATA';"
    "e.textContent=%s;document.head.appendChild(e);})();\n"
    % json.dumps(json_text, ensure_ascii=False)
)
(OUT / "data.js").write_text(js, encoding="utf-8")
s = s[: m.start()] + '<script src="./data.js"></script>' + s[m.end() :]
print("外置数据块：%d B / %d 个顶层键" % (len(json_text.encode()), len(parsed)))

# ---------- 4. 主脚本外置 ----------
script_no = [0]


def script_repl(m):
    script_no[0] += 1
    fn = "app%d.js" % script_no[0]
    (OUT / fn).write_text(m.group(2), encoding="utf-8")
    return '<script src="./%s"></script>' % fn


# 只匹配「无 src 属性」的内联脚本，别把刚插入的 <script src="./data.js"> 也吃掉。
s, nj = re.subn(
    r"<script(?![^>]*\ssrc=)([^>]*)>(.*?)</script>", script_repl, s, flags=re.S | re.I
)
print("外置脚本块：%d" % nj)
if nj == 0:
    raise SystemExit("未找到主脚本，构建中止")

# ---------- 5. 写入口 ----------
(OUT / "index.html").write_text(s, encoding="utf-8")
size = (OUT / "index.html").stat().st_size
print("入口 index.html：%d B（上限 1,048,576 B）" % size)
if size > 1048576:
    raise SystemExit("入口超过 1MB，构建中止")

# ---------- 6. 自检 ----------
bad_abs = re.findall(r'(?:src|href)\s*=\s*["\']/(?!/)', s)
bad_url = re.findall(r"url\(\s*[\"']?/", s)
leftover = len(PAT.findall(s))
ext_links = len(re.findall(r"https?://", s))
print("根绝对路径 src/href: %d / url(/): %d / 残留 base64: %d / 外链: %d"
      % (len(bad_abs), len(bad_url), leftover, ext_links))
for f in sorted(OUT.rglob("*")):
    if f.is_file() and f.suffix.lower() in (".js", ".css", ".html"):
        t = f.read_text(encoding="utf-8")
        if re.search(r'(?:src|href)\s*=\s*["\']/(?!/)', t):
            print("  ! 绝对路径:", f.relative_to(OUT))
        if PAT.search(t):
            print("  ! 残留 base64:", f.relative_to(OUT))
print("产物：%d 个文件 / %d B"
      % (sum(1 for f in OUT.rglob("*") if f.is_file()),
         sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())))
