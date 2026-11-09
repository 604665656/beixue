# -*- coding: utf-8 -*-
"""把 game/index.html（20.2MB 单文件）拆成 B站 Toy 上架包。

只做两件事，其余内容一字不改：
  1. 平台强制分包：5 段 <style> -> styleN.css；DATA JSON -> data.js（运行时回填同 id 节点）；
     主脚本 -> app1.js。入口 index.html 因此从 20.2MB 降到 1MB 以下。
  2. 已实测的合规处理：清空 DATA.readB64（626,796 字符的 base64 内嵌 HTML 子页面）。
     2026-11-08 首轮上架实测：正是这个字段导致「内容审核未通过」，清空后过审，
     24 关 / 档案 / 美术全部保留。

CSS 里 515 张图片是 data URI，外置后仍然有效；全文 url(#...) 与 assets/ 引用均为 0，
不存在 fragment 或相对路径失效风险。源文件 toy_src/game/index.html 保持只读。
"""
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "toy_src" / "game" / "index.html"
OUT = ROOT / "toy"

if not SRC.exists():
    raise SystemExit("找不到 " + str(SRC))
s = SRC.read_text(encoding="utf-8")
print("源文件 %s / %d B" % (SRC.name, SRC.stat().st_size))

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

# ---------- 1) 外置全部 <style> ----------
style_no = [0]


def style_repl(m):
    style_no[0] += 1
    fn = "style%d.css" % style_no[0]
    (OUT / fn).write_text(m.group(2), encoding="utf-8")
    return '<link rel="stylesheet" href="./%s">' % fn


s, n_style = re.subn(r"<style([^>]*)>(.*?)</style>", style_repl, s, flags=re.S | re.I)
print("外置样式块: %d" % n_style)

# ---------- 2) 外置全部内联 <script> ----------
def script_repl(m):
    attr, body = m.group(1), m.group(2)
    if "application/json" in attr:
        obj = json.loads(body)
        removed = len(obj.get("readB64", ""))
        if "readB64" in obj:
            obj["readB64"] = ""
        lit = json.dumps(obj, ensure_ascii=True, separators=(",", ":"))
        js = "(function(){var e=document.getElementById('DATA');"
        js += "if(e)e.textContent=JSON.stringify(" + lit + ");})();"
        (OUT / "data.js").write_text(js, encoding="utf-8")
        print("合规裁剪: 清空 readB64（原 %d 字符），其余数据全部保留" % removed)
        return ('<script type="application/json" id="DATA"></script>'
                '<script src="./data.js"></script>')
    (OUT / "app1.js").write_text(body, encoding="utf-8")
    return '<script src="./app1.js"></script>'


s, n_script = re.subn(
    r"<script(?![^>]*\ssrc=)([^>]*)>(.*?)</script>",
    script_repl, s, flags=re.S | re.I)
print("外置脚本块: %d" % n_script)
if n_script != 2:
    raise SystemExit("预期 2 个内联脚本，实得 %d 个，构建中止" % n_script)

(OUT / "index.html").write_text(s, encoding="utf-8")
size = (OUT / "index.html").stat().st_size
print("入口 index.html: %d B（上限 1,048,576 B）" % size)
if size > 1048576:
    raise SystemExit("入口超过 1MB，构建中止")

# ---------- 3) 自检 ----------
bad_abs = s.count('src="/') + s.count('href="/') + s.count("src='/") + s.count("href='/")
print("根绝对路径: %d / 入口内 data:image: %d / SVG fragment: %d"
      % (bad_abs, s.count("data:image"), len(re.findall(r"url\(#", s))))
files = [f for f in sorted(OUT.rglob("*")) if f.is_file()]
for f in files:
    print("  %-14s %10d B" % (f.name, f.stat().st_size))
print("产物: %d 个文件 / %d B" % (len(files), sum(f.stat().st_size for f in files)))
