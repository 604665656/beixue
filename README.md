# 杯雪 · 互动游戏集

小椴《杯雪》的**机制化拆读互动游戏**：二十四关、七卷、四种模式、三档难度，带水墨场景板、分层角色立绘、换装台、AVG 画面演出与离线朗读。全部内容在**一个 HTML 文件里**，断网双击即可玩。

- 🎮 **主游戏**：[`10_杯雪游戏总站.html`](10_杯雪游戏总站.html)（9,624,892 B，离线单文件）
- 🌐 **B站 Toy**：<https://www.bilibili.com/toy/beixue/index.html>
- 📖 **完整使用说明**：[`00_使用说明.md`](00_使用说明.md)
- 🗂 **设计说明**：[`10_杯雪游戏总站_设计说明.md`](10_杯雪游戏总站_设计说明.md)

> `08_杯雪互动游戏集.html` / `09_杯雪离线总栈.html` 与主文件内容完全相同，任选其一即可；`杯雪游戏总站.html` 是略早的版本（9,607,935 B）。全部为机制化解读，不含小说原文，不指向盗版全文站。

## 仓库里有什么

| 目录 / 文件 | 内容 |
| --- | --- |
| `00`–`18`、`29`–`44` 等编号目录 | 拆读文稿、人物关系图、思维导图、考据补遗、关卡配图计划、动画素材缺口登记、一致性检查报告 |
| `美术归档/`、`分层资产/`、`抠图源图/`、`anim26/` | 厚涂主视觉、原稿风角色层、23 张纯抠图源图、场景板与序列帧 |
| `19`–`38` 编号目录 | 各批次表情 / 动作帧 / 天气粒子 / 换装素材的 `art.json` 与 PNG |
| `toy/` | **B站 Toy 上架包产物**（由构建脚本生成，入口 `index.html` 3,199 B） |
| `deliver/` | 封面、图标与 `杯雪_Toy上架包.zip` |
| `build_toy.py` | 分包构建脚本：base64 图片外置 + 样式/数据/脚本外置 |
| `gen_cover_icon.py` | 程序化生成封面与图标（不依赖游戏内截图） |

## 复现 Toy 上架包

平台硬规则：**入口 `index.html` 解压后 ≤ 1MB**、所有资源必须相对路径（Toy 跑在 `/toy/<slug>/` 子路径下）。原始单文件 9.6MB 不能直接传，构建脚本只作用于 `toy/`，**不改动任何原始文件**：

```bash
python build_toy.py        # 生成 toy/
python gen_cover_icon.py   # 生成 deliver/cover.png 与 icon.png
```

构建做的事：

1. 250 处 `data:image/...;base64` 解码成真实图片，按内容 SHA1 去重 → **239 个文件**，引用改为 `./assets/<hash>.<ext>`；
2. 两个内联 `<style>` → `./style1.css`、`./style2.css`；
3. 957,972 B 的内联 `<script type="application/json" id="DATA">` → `./data.js`，运行时回填同 id 节点，主脚本里的 `JSON.parse(document.getElementById('DATA').textContent)` **一行都不用改**；
4. 主脚本 → `./app1.js`；
5. 入口只剩 3,199 B 的骨架与相对引用，外链 0、根绝对路径 0、残留 base64 0。

产物共 244 个文件 / 7,388,125 B，上架 ZIP 6,724,252 B。发布前四道校验：`node --check` 两个 JS、资源引用完整性、`toy_doctor.py` 预检、本地起 `/toy/beixue/` 子路径服务器用真实浏览器确认大厅 → 关卡舞台（场景板 + 立绘 + 对话）全部渲染且资源全 200。

```bash
toy create toy --title "杯雪 · 互动游戏集" --slug beixue --category GAME \
  --watermark --poster deliver/cover.png --icon deliver/icon.png --yes --json
```

## 说明

原始资料、美术归档与判废素材均按原样保留，未做删减；合规分包只发生在 `toy/` 产物层。如平台侧内容审核要求调整，也只改构建产物，不动源文件。

记录日期：2026-11-08 · Toy CLI v0.6.4
