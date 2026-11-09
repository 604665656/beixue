# 《杯雪》开源 AVG 与视觉小说引擎借鉴调研

## 摘要

本报告把《杯雪》的真实约束置于首位：成品是约 9.2MB、base64 WebP 内嵌、纯前端离线运行、无框架、无构建、无服务端的单文件 HTML；已有四模式三档难度、24 关 7 卷、进度解锁档案，以及背景板／透明立绘分层、AVG 气泡、CSS/SVG 粒子、Web Audio 程序化声音、系统 TTS、Web Speech ASR、无障碍、双指缩放拖动、横屏旋转、三套皮肤和品红底抠图检查管线。因此“换引擎”不是合理目标；应把开源方案当作**设计范式、协议与可抄写的小机制**来借鉴，而不是整包引入。

最值得立即抄写的是 WebGAL 的舞台—演出指令模型、Twine 的 Passage 非线性结构、ink/inkjs 的会话快照思想；中期可引入资源清单（manifest）、内容寻址哈希、版本化存档 Schema 与可重放指令队列；Unity/Godot 的 Fungus、Naninovel、Dialogic 适合学习 Flowchart、序列化演出状态和角色层编排，但不适合移植进单文件 HTML。WebGAL、Twine、inkjs 在运行形态上与本项目最接近；Ren’Py、Fungus、Naninovel、Dialogic 主要提供架构范式。

**数据口径（2026-11-08 二次补检）**：初稿因抓取受限未填运营指标，本轮已用公开检索补齐主要候选的许可证、最新稳定版与部分可核的星标/提交时间，见下节「零、核实后的运营数据」。仍未能可靠交叉验证的字段一律标注「未核实」，不填推测数字；聚合站与二手测评只作旁证，关键结论以官方仓库页、官方文档或官网为准。候选官方地址清单见 `候选官方地址清单.csv`（见压缩包 `39_开源方案调研/`）。


## 零、核实后的运营数据（2026-11-08 补检）

以下为公开可核字段；「未核实」表示本轮没有拿到一手可信来源，不做推测。| 项目 | 许可证 / 版本 / 活跃度 | 对《杯雪》的结论 |
|---|---|---|
| WebGAL | MPL-2.0；4.6.6（2026-10-08）；约 4.0k stars、2,546 commits、最近提交 2026-10-08 | 最贴近「Web 单文件 AVG」的完整范式，**抄命令模型，不整包引入** |
| Monogatari | MIT；`@monogatari/core` 提供浏览器 bundle 与 ES module、TS 类型；GitHub 15 个 tag | 角色 id + 表情 id + 分层立绘的声明式配置可直接抄 |
| inkjs / ink | ink MIT；inkjs MIT、零依赖、TypeScript，约 664 stars，最近推送 2026-09-01，2.4.0（2026-02） | 零依赖可 `<script>` 直引，但会引入解析器与内容格式，**只借会话快照思想** |
| Twine (twinejs) | GPL-3.0；约 8.5k stars，最后提交 2026-05（二手测评口径，未在仓库页复核） | Passage 节点图适合档案/关卡建模；许可证与运行链不适合内嵌 |
| Yarn Spinner / ink | 均 MIT（二手归纳，未逐仓库复核） | 只参考「持久变量 + 节点游标」字段设计 |
| Ren'Py | 开源且可商用；最新稳定 8.5.3（2026-05-15），8.6.0 预发布（2026-11-01）；官网称已被 8,000+ 作品使用 | 完整 AVG 全栈范式；Python 运行与构建流程**根本冲突** |
| Dialogic (Godot 4) | MIT；约 6.1k stars，组织页更新至 2026-08-30 | 只学 Timeline / 可序列化演出图 |
| Fungus、Naninovel | 本轮未取得一手 LICENSE 页，**未核实**（Naninovel 以 Unity Asset Store 商用发行为主） | 仅作流程图与序列化状态的参考 |

**注意**：WebGAL 是 **MPL-2.0**（文件级 copyleft），不是 MIT——若将来真的复制其源码文件进单文件 HTML，需保留对应文件级许可与修改声明；只借鉴「命令名与舞台模型」的设计思想则不涉及代码复制。Twine 的 GPL-3.0 同理，拷贝其编辑器代码会触发传染性许可，只采用「节点图」概念无此问题。## 一、判断标准：先按运行形态筛，再按演出能力排

**本项目的“适配”不等于“功能更全”，而是零构建、零依赖、离线、中文演出和手动维护能否保留。** 一个成熟引擎若必须安装 Python、Node、Unity 或 Godot，再导出可执行文件，即使功能更强，也不能直接改善既有单文件 HTML。它只能提供可手写的模型、协议或算法。因此本报告把候选分成三类：可直接借鉴的 Web 运行时；提供设计范式但运行环境不同的引擎；可补充特定子系统而非完整 AVG 的库或标准。

| 类别 | 候选 | 对本项目的主要价值 |
|---|---|---|
| 最接近 Web 运行形态 | WebGAL、Monogatari、inkjs、Twine | 浏览器运行时、脚本化叙事、独立部署 |
| 强设计范式、非 Web 单文件 | Ren’Py、Yarn Spinner、Fungus、Naninovel、Dialogic | 存档、立绘、状态机、流程图、演出序列化 |
| 子系统补充 | Web Speech API、TTS/图像/状态库 | 仅补某一层，不等于完整 AVG 框架 |

**四块痛点的判断结论如下。** 第一，对话演出与立绘分层最值得借鉴的是“舞台状态 + 不可变指令 + 角色槽”模型；它比把所有动画、位置、透明度散落在事件处理函数里更容易回放、测试和撤销。第二，存档应把“叙事状态”与“运行时演出状态”分开：前者是稳定业务数据，后者可重建，不应全量深拷贝。第三，无障碍朗读的核心不是简单调用 TTS，而是建立结构化朗读队列、可见文本与播报文本分离，并把 aria-live、逐字动画和 TTS 用统一时钟同步。第四，9.2MB 的瓶颈首先不是运行时框架，而是资源寻址和编码；把 base64 改为外部资源，并用 manifest、哈希、尺寸规范、质量阶梯和一致性门禁，是最高性价比的改造。

## 二、WebGAL：最接近“单文件 Web AVG”的完整范式

**WebGAL 的第一价值是把“说台词”改造成“舞台指令”，而非只增加脚本语法。** 对《杯雪》来说，一次演出应被写成可序列化的命令，例如 `changeBg`、`chooseLabel`、`playEffect`、`setAnimation`、`say`；运行时只消费命令队列。这样气泡文字、立绘入场、背景切换、天气粒子、音效、ASR 指令都能共用同一时间线。公开仓库地址为 <https://github.com/OpenWebGAL/WebGAL>；其许可证与本次可核验的具体版本、星标、最近提交均应在集成前再次从 LICENSE 文件与 Releases 页面人工复核，本报告不填未经核验数字。

最值得借鉴的 2—3 点：

1. **脚本与演出分离。** 脚本只描述意图，运行时负责解析和调度；新增难度、模式或皮肤时无需修改演出引擎。
2. **立绘槽和背景层解耦。** 每个角色应绑定稳定 id、表情、位置、缩放、层级、过渡和遮挡关系，而不是用一组 DOM 元素临时拼装。
3. **场景/标签可跳转。** 24 关 7 卷的结构应映射为稳定内容 id，跳转、重试和回溯通过状态快照而非重新执行副作用实现。

适配差距仍不小。WebGAL 是完整产品，有自身资源结构、UI、构建与部署方式；《杯雪》若要保持单文件、手工实现与既有交互，不应把 WebGAL 源码整包塞入。更合理的做法是抽取其“命令式演出脚本”与“舞台状态”两层，并以纯 JavaScript 重写一次小型解释器。

## 三、Monogatari：可视化舞台适合借鉴立绘层，不适合承担四模式玩法

**Monogatari 的优势是浏览器内的立绘、背景、对话与选择编排，但其重心是线性 AVG 演出。** 它把场景、角色、媒体和文本组织成声明式配置，便于美术、文案和开发共同维护；这正是《杯雪》在“透明角色立绘分层”上最缺的抽象。公开仓库地址为 <https://github.com/Monogatari/Monogatari>，许可证与当前版本需复核。

值得借鉴的是：

1. 用**角色 id + 状态 id**表达立绘，而非图片文件名；
2. 把立绘变换定义为显式过渡，包括进入、退出、换表情、移动、缩放和高亮；
3. 把选项结果回写成持久状态变量，供后续对话和档案条件判断。

差距在于，《杯雪》还有战斗/闯关玩法、三档难度、四模式、天气粒子和实时音频，这些不是 Monogatari 的默认舞台模型。若引入它，等于在既有玩法之上再造一层游戏循环。因此更适合“观察其分层与演出数据格式”，不建议将现有项目迁移到 Monogatari。

## 四、ink 与 inkjs：应借叙事内核，不应借整包运行时

**ink 把故事写成选择、分支、汇聚和变量状态，是本项目分支叙事的理想最小模型；inkjs 让它能在浏览器解释。** ink 官方仓库为 <https://github.com/inkle/ink>，inkjs 官方仓库为 <https://github.com/y-lohse/inkjs>。二者适合把“剧情内容”从“游戏玩法”中拆出，而不是把立绘、天气、ASR 全部塞进故事语言。

值得借鉴：

1. **内容文本版本化。** 每个节点有稳定名称，修改台词不改变所有引用；
2. **会话状态与全局状态分离。** 一次阅读位置可保存，跨章节变量另存；
3. **叙事选择可回滚。** ink 的会话快照思想适合实现对话倒回，但不应把不可撤销的玩法结果一并倒回。

差距也很明确：ink 不是立绘引擎，也没有 Web Audio、CSS 粒子、存档压缩、横屏旋转等机制。对《杯雪》的正确用法是手写小型 ink 兼容子集或自研 DSL，让 `say`、`choice`、`setFlag`、`jump` 由自己的解释器执行；若引入 inkjs 则会引入解析器、加载方式和依赖约定，违反当前“无构建”的强约束。

## 五、Twine：Passage 模型适合档案与章节节点，不适合承担 AVG 演出

**Twine 的 Passage 图是管理 24 关 7 卷和复杂解锁条件的好模型，但不是立绘演出框架。** 每个 Passage 是内容节点，链接表达可选路径，变量和条件控制后续节点；编辑器本身适合非程序员编辑故事。公开仓库地址为 <https://github.com/klembot/twinejs>。

值得借鉴：

1. 把关卡、章节、档案条目都建模成有唯一 id 的节点；
2. 用条件标签管理“已读、已通关、已解锁、不同难度可见”；
3. 把剧情地图与运行时逻辑分开，使内容编辑不再直接改 DOM 事件。

问题在于，Twine 默认产物仍依赖其故事格式与运行环境，且原生形态偏互动小说而非 AVG 分层演出。更适配《杯雪》的是采用“内容图 + 自定义渲染器”，而不是迁到 Twine 的完整编辑器与输出链。

## 六、Yarn Spinner：数据模型可学，Unity 依赖与单文件目标冲突

**Yarn Spinner 的强项是结构化对话、变量存储与运行时选择，但它是面向 Unity/C# 的叙事引擎。** 官方仓库为 <https://github.com/YarnSpinnerTool/YarnSpinner>。其对话节点、命令语法、变量表和本地化思路适合复盘，而 Unity 的编译、资产和运行时环境并不适配离线单文件 HTML。

值得借鉴：

1. 把变量、命令和节点文本放进声明式内容文件；
2. 为选项结果定义明确的语义，而非依赖运行时临时变量；
3. 把存档拆成“持久变量”和“当前节点游标”。

迁移成本很高。即便能手工移植 Yarn 的脚本语法，也仍需重写加载器、变量绑定、本地化解析和命令调度。若目标是保持现有项目，只建议参考其数据字段设计。

## 七、Ren’Py：专业 AVG 的全栈范式，但不能直接落到浏览器单文件

**Ren’Py 是成熟的 Python 视觉小说框架，拥有完整的脚本、存档、角色、转场和本地化体系；它的主要价值是“完整产品应有什么”，而不是“如何嵌入 HTML”。** 官方仓库为 <https://github.com/renpy/renpy>。其 ATL/转场、角色对象、语句预测、自动存档和回放机制都值得研究。

值得借鉴：

1. **立绘角色对象。** 角色绑定显示名、语音、默认位置和默认过渡，减少重复代码；
2. **并行与串行演出。** 背景音乐、立绘移动、文字动画可组成同一场景的不同轨道；
3. **确定性回放。** 只要状态与随机种子一致，演出可复现，这对调试和回溯尤其有用。

适配差距是根本性的：Ren’Py 需要 Python 运行环境和项目构建/打包流程。不能把 Ren’Py 项目原样变成 9.2MB 单文件 HTML；其价值在于证明 AVG 应采用声明式内容、版本化存档和分层演出。

## 八、Fungus、Naninovel、Dialogic：适合学流程图与序列化，不适合迁移

**三者的共同优势是可视化或声明式编排，共同限制是 Unity/Godot 生态。** Fungus 用流程图组织对话块，适合理解“块—命令—执行指针”；Naninovel 提供成熟的 Unity 视觉小说架构，包括角色、背景、文本、选项、保存和本地化；Dialogic 则是 Godot 4 的对话与分支叙事插件。仓库地址分别为 <https://github.com/snozbot/fungus>、<https://github.com/Naninovel/Naninovel>、<https://github.com/dialogic-godot/dialogic>。

值得借鉴的是：

1. 把对话块、演出命令、条件判断表示成可编辑且可序列化的节点；
2. 区分叙事状态、场景状态与 UI 状态，存档只保留稳定子集；
3. 为立绘、背景、气泡、选择定义统一命令接口，使自动测试能重放。

迁移成本都很高：需要相应编辑器、运行时、资产数据库和项目结构。对《杯雪》而言，只有“命令接口”和“可序列化演出图”值得抄写；整包 Unity/Godot 方案与单文件、离线、无构建、无服务端目标冲突。

## 九、四块痛点能否直接改善：结论与具体做法

### ① 对话演出与立绘分层：有可直接改善的成熟做法，但应借鉴接口而非引擎

**建议引入“舞台 + 角色槽 + 命令队列”，这是 Ren’Py、WebGAL、Monogatari、Naninovel、Dialogic 共同验证过的模型。** 舞台保持背景层、天气层、后方角色层、主角层、前景层、UI 层和气泡层；每个立绘槽只保存 `{id, expression, x, y, scale, opacity, z, transition}`，不直接保存 `<img>`。命令描述“从 A 状态到 B 状态”，解释器按统一时钟驱动 CSS、Web Animations、SVG 属性或 canvas。

可直接落地的最小命令集：`enterCharacter`、`exitCharacter`、`changeExpression`、`moveCharacter`、`showBackground`、`playSfx`、`startWeather`、`speak`、`choose`。每个命令有稳定类型、参数和持续时间；当前演出状态可由命令序列重放。这样双指拖动、缩放、真横屏旋转只是改变视图，不污染内容层。

### ② 存档与进度状态：有成熟做法，但必须重构存档 Schema

**不应继续把运行时快照和游戏进度混在一起。** ink 的会话状态、Ren’Py/Naninovel/Dialogic 的序列化状态都说明：存档至少包含 schema 版本、内容游标、持久变量、模式/难度结果、解锁集合、随机种子、校验和，以及可选的快速存档元数据。演出层的位置、动画、Web Audio 实时节点应可丢弃并由内容状态重建。

建议短期采用三个独立命名空间：`cup-snow.progress`（稳定通关进度与解锁）、`cup-snow.preferences`（皮肤、减少动效、音量、TTS/ASR 设置）、`cup-snow.checkpoint`（当前检查点）。中期采用命令日志加状态快照：每关保存开始快照和有限增量命令，既支持回放，也避免 localStorage 写入过大。存档大小应设上限，写前 JSON 序列化，失败时保留旧存档；对 9.2MB 单文件，不要重复复制全部 base64。

### ③ 无障碍朗读：TTS 本身不是成熟完整方案，朗读架构有成熟模式

**Web Speech API 提供了 `SpeechSynthesis`，但没有统一的朗读队列、播报文本规范、暂停恢复语义或中文质量承诺。** W3C 规范地址为 <https://www.w3.org/TR/speech-api/>，其中 `SpeechSynthesis` 是脚本能力，不是可直接复用的 AVG 朗读框架。因此“有没有成熟做法”的答案是：浏览器能力成熟，完整无障碍朗读方案仍需项目自建。

建议把可见文本与播报文本分开：气泡展示原文，朗读时按标点、角色、旁白、音效提示和速度设置切分成 `SpeechSegment[]`。统一朗读控制器负责排队、取消、暂停、速率、语言、失败降级和 `prefers-reduced-motion`；`aria-live` 只播报语义变化，不与 TTS 重复朗读整段。ASR 的 `SpeechRecognition` 也不应成为唯一操作方式，所有语音命令都要有可见按钮、键盘等价操作和失败提示。

### ④ 素材与资源管线：有成熟做法，且是 9.2MB 单文件的首要优化面

**资源清单化、自动化检查和增量构建能直接改善手工管线，但会与“无构建单文件”发生策略冲突。** sharp、ImageMagick、Squoosh 等工具可做 WebP 质量阶梯、尺寸生成、元数据清理、一致性校验；但 sharp 有 Node.js 原生依赖，ImageMagick 是命令行工具，Squoosh 更适合浏览器/构建工具，都不应直接塞入运行期。仓库地址分别为 <https://github.com/lovell/sharp>、<https://github.com/ImageMagick/ImageMagick>、<https://github.com/GoogleChromeLabs/squoosh>。

资源管线应改成“开发期多文件，发布期生成单文件”：每个角色建立 manifest，记录源文件、裁剪框、目标宽高、表情 id、WebP 质量、透明区域、品红残留阈值和哈希；检查脚本自动检测品红像素、实心层空洞、透明边缘、命名不一致、尺寸变化和重复资源。短期可继续 base64 内嵌，但把资源改成外部文件、按需加载、使用 `Cache`/`IndexedDB` 缓存并保留离线包，是下一步最合理的折中。


## 九点五、落到《杯雪》现有代码的具体改造点

报告上文是通用结论；这一节把 P0 建议逐条映射到站内**真实存在的命名**，便于直接开工，不新增抽象层。

### ① 舞台命令协议 → 收编现有三个散点

站内目前由三处共同决定「一屏演什么」：`stageFor(TAB)` 返回 `{bg, cast}`、`queuePerf(idx)` 在选项点击后换表情层、`refreshStageCast()` 把结果写回 `.stagecut`。三者各自直接改 DOM，正是报告说的「演出状态散落在事件处理函数里」。

建议不引入框架，只加一个纯函数层：

```
StageCmd[] = [
  {t:'bg', id:'rain'}, {t:'cast', id:'R25_I_zhu', slot:'main'},
  {t:'speak', text:'…', who:'…'}, {t:'weather', fx:'rain'},
  {t:'choose', opts:[…]}
]
StageState = { bg, slots:{main:{id,expr,x,y,s,z,transition}}, bubble, weather, audio }
```

`stageFor / queuePerf / refreshStageCast` 改为「产出命令 → 解释器 `applyStage()` 消费」；重放、撤销、自动测试都只对 `StageCmd[]` 做，不再碰 DOM。这一步能直接解决此前反复出现的**名牌与立绘不同步**、**选项表演 2.3 秒后复原错位**这类 bug。

### ② 立绘声明式槽位 → 合并四张表

站内现有 `ART`（229 个 base64 WebP 层）、`CAST`/`CAST_META`（名牌与花名）、`COSTUME_REMAP`（31 项一致性代用）、`I_CAST`/`G_CAST`/`H_CAST`/`A_CAST`（逐关逐题换脸）。四张表本质都是「角色 id → 层 key → 元数据」，却分散维护，才出现 R21 那次「11 项名牌兜底成哈士喵」。

建议合成一张：

```
CHAR = { id: { name, alias, role, layers:{ normal, angry, scar, … },
               defaultExpr, bgHint, dressCheck:'ok|pending' } }
```

`ART` 退化为纯资源池；`COSTUME_REMAP` 变成 `layers` 里的一条 fallback，不再单独维护。这与 Monogatari 的 `characters({sprites,expressions,default_expression})` 是同一模型。### ③ 存档三命名空间 → 现有 19 个 localStorage 键归类

站内当前有 `beixue_prog_v1`（进度）、`beixue_mode_v1` / `beixue_diff_v1` / `beixue_skin_v2` / `beixue_bgm_v2` / `beixue_sfx_v2` / `beixue_breathe_v1` / `beixue_vib_v1` / `beixue_perf_gate_v1`（偏好）、`beixue_spr_v1`（立绘位置/倍率）、`beixue_bublay_v1`（气泡摆位）、`beixue_games_v1`（关卡内状态）、`beixue_streak_v1`（升降档连胜）、`beixue_last_v1` 等共 19 个键。

按报告建议收敛为三个命名空间，并**把 `SPR` 明确划为视图状态**：

- `cup-snow.progress`：通关星级、档案解锁、QKEYS 成绩、随机种子（稳定业务数据）
- `cup-snow.preferences`：皮肤、模式、难度、四路音控、透明度滑杆、震动、减少动效、演出门槛
- `cup-snow.view`：立绘 `SPR`、气泡摆位、场景选择、全屏查看器倍率——**可随时丢弃重建，不参与存档校验**

这一步能根治 R24 查到的那类问题：旋转画布下 `clampSpr` 与 `ensureSpriteVisible` 误用设备 `innerWidth/innerHeight` 去判断局部坐标，本质就是「视图状态」被当成「进度状态」硬 clamp。加 `schemaVersion` 与写前校验，旧键自动迁移一次即可。

### ④ 朗读统一队列 → 现有 TTS/ASR 四路开关之上加一层

站内已有 `TTS / ASR / BGM / SFX` 四路独立、默认全关，以及 `aria-live` 播报与「分句扮演」（引号内台词用角色声线）。缺的是报告说的**统一时钟**：现在气泡换幕、天气音切换、TTS 分段、aria-live 播报各自 setTimeout，容易叠声或抢读。

建议加一个 `SpeechSegment[]` 队列：`{visible, spoken, aria, rate, role, interruptible}`，由单一 `Narrator` 驱动；`aria-live` 只播 `aria` 字段的语义变化，不重复整段。ASR 命令继续保留键盘等价（现有 `1–4 / N / H / R / Esc`），符合报告「语音不能是唯一操作方式」的要求。

### ⑤ 资源 manifest → 接入现有检查器

站内已有 `角色一致性检查.py`（v5 双锚点：裸猫原稿锚点 + 31 张整装层中位锚点）、`行头目检登记.csv`、纯品红底抠图管线（色相键控 → 填实孔洞 → 去色溢）、`杯雪动画素材缺口登记表.md/csv`（202 项）。这套**已经是报告里说的「自动化一致性门禁」雏形**，差的只是把它从「人跑一次」变成「发布前必跑」并输出 manifest：

```
asset: { key, src, crop, w/h, webpQ, exprId, seed, holes:0, magenta:0.013%, hash, anchor:'dressed' }
```

主 HTML 现在 9.2MB、内嵌 229 层 base64 WebP；按报告建议先做「开发期多文件 + 发布期合并单文件」，用 manifest 去重与质量阶梯，比直接换引擎收益高得多。**注意**：这一步会改变「绝对单文件」的形态，需你先拍板是否接受附带一个离线资源包。

## 十、行动清单：先降低维护成本，再扩大架构能力

### P0：可立即借鉴

1. **建立舞台命令协议。** 定义背景、立绘、气泡、粒子、音频、选择六类最小命令，不用外部框架，一周内即可覆盖多数手工事件。
2. **把角色立绘改为声明式槽位。** 用角色 id 和表情 id 寻址，保存位置、缩放、层级和过渡；不再直接操作图片元素。
3. **拆分三份存储命名空间。** 进度、偏好、检查点隔离；读取时先校验 schema 版本，兼容旧字段。
4. **建立朗读与 aria-live 统一队列。** 可见文本、TTS 文本、读屏文本三者解耦；ASR 命令保留键盘等价操作。
5. **建立角色资源 manifest。** 每个立绘记录规范尺寸、品红底用途、WebP 质量、哈希和一致性状态。

### P1：中期重构

1. **引入内容节点图。** 以稳定 id 表示关卡、章节、档案、选项节点；剧情脚本只引用 id。
2. **实现版本化快照存档。** 包含 schema 版本、内容游标、变量、解锁集合、校验和；必要时加入可截断命令日志。
3. **把程序化音效做成可序列化音效图。** 音效参数、随机种子和触发时间写入状态，确保重放一致。
4. **把资源管线从手工变成脚本化。** 用命令行工具完成 WebP 压缩、尺寸生成、品红检测、重复哈希和清单校验；即使最终仍生成单文件，开发期不再逐个手写 base64。
5. **建立跨模式测试夹具。** 用固定初始状态、输入序列和种子验证 24 关、四模式、三档难度的解锁与表现。

### P2：不建议照搬

1. 不建议整包迁移到 Ren’Py、Unity 或 Godot；它们会破坏单文件、离线、无构建和无服务端约束。
2. 不建议把 Twine、WebGAL、Monogatari 的完整运行层引入既有项目；其 UI、资源加载和游戏循环会与现有实现重复。
3. 不建议整包引入 inkjs、Yarn Spinner、Redux、Zustand、XState；它们不是不能用，而是需要构建、依赖管理或适配层，短期收益低于手写状态切片。
4. 不建议把系统 TTS 当作完整无障碍方案；中文支持、打断、并发、读屏重复和错误恢复都必须项目内处理。
5. 不建议继续把全部资源永久固化为 base64；若必须单文件，也应先完成清单化、去重和质量压缩，再在发布时合并。

## 十一、推荐组合与实施顺序

**最终建议不是“选一个引擎”，而是组合四种成熟思想。** 叙事层采用 Twine 的节点图与 ink 的会话快照思想；演出层采用 WebGAL/Monogatari 的命令式舞台模型；状态层采用 Ren’Py/Naninovel 的持久变量与序列化状态分层；资源层采用清单、哈希和自动图像检查。这个组合保留了《杯雪》已经实现的差异化能力，也避免为了引入框架而推倒现有项目。

实施顺序应是：第一周完成命令协议、角色槽和存储命名空间；第二至三周完成资源 manifest 与一致性检查；第四至六周迁移剧情节点和存档 schema；中期再决定是继续单文件内嵌，还是采用“离线包 + 缓存/按需加载”。这一顺序能先消除手工维护风险，再处理文件体积与架构扩展，避免在稳定模型尚未建立时仓促换工具。

## 引用来源

[1] https://github.com/OpenWebGAL/WebGAL
> 这是 WebGAL 官方开源仓库地址，可用于核对许可证、Releases、提交记录与源码。

[2] https://github.com/Monogatari/Monogatari
> 这是 Monogatari 官方开源仓库地址，用于核对许可证、脚本模型与发布版本。

[3] https://github.com/inkle/ink
> 这是 inkle/ink 的官方仓库地址，适合研究叙事语言、变量与分支模型。

[4] https://github.com/y-lohse/inkjs
> 这是 inkjs 的官方仓库地址，用于了解 ink 在 JavaScript/浏览器中的运行方式。

[5] https://github.com/klembot/twinejs
> 这是 Twine 编辑器的官方仓库地址，可用于核对许可证、版本与项目活动。

[6] https://github.com/YarnSpinnerTool/YarnSpinner
> 这是 Yarn Spinner 的官方仓库地址，适合研究对话节点、命令和变量存储。

[7] https://github.com/renpy/renpy
> 这是 Ren’Py 的官方仓库地址，可用于核对许可证、版本与完整视觉小说运行时。

[8] https://github.com/snozbot/fungus
> 这是 Fungus 的官方仓库地址，适合研究基于流程图的 Unity 对话编排。

[9] https://github.com/Naninovel/Naninovel
> 这是 Naninovel 的官方仓库地址，适合研究 Unity 视觉小说框架的演出与状态模型。

[10] https://github.com/dialogic-godot/dialogic
> 这是 Godot Dialogic 的官方仓库地址，适合研究 Godot 4 对话、分支和变量系统。

[11] https://www.w3.org/TR/speech-api/
> This specification defines a JavaScript API for speech recognition and synthesis in web applications.

[12] https://github.com/pmndrs/zustand
> 这是 Zustand 官方仓库地址，适合研究轻量状态管理与持久化中间件设计。

[13] https://github.com/reduxjs/redux-toolkit
> 这是 Redux Toolkit 官方仓库地址，适合研究可预测状态容器、Slice 与不可变更新。

[14] https://github.com/statelyai/xstate
> 这是 XState 官方仓库地址，适合研究有限状态机、状态图和可序列化状态。

[15] https://github.com/netease-youdao/Confucius4-TTS
> 这是 Confucius4-TTS 官方仓库地址，可用于核对开源模型、许可和部署要求。

[16] https://github.com/lovell/sharp
> 这是 sharp 官方仓库地址，适合研究 Node.js 环境下的高效 WebP/图像处理。

[17] https://github.com/GoogleChromeLabs/squoosh
> 这是 Squoosh 官方仓库地址，适合研究浏览器或构建环境中的图像压缩。

[18] https://github.com/ImageMagick/ImageMagick
> 这是 ImageMagick 官方仓库地址，适合研究命令行批处理、格式转换与质量参数。

[19] https://wicg.github.io/speech-api/
> Web Speech API 的公开规范地址，用于核对 SpeechSynthesis 等浏览器能力。

## 补检来源（2026-11-08）

[20] https://github.com/OpenWebGAL/WebGAL — 仓库页：MPL-2.0、Stars 4.0k、Forks 367、Commits 2,546、最近提交 2026-10-08
[21] https://mygit.top/repository/407346682 — 镜像页：WebGAL 4.6.6（2026-10-08）、Star 4020、TypeScript、MPL-2.0
[22] http://docs.openwebgal.com/webgal-script/bg-and-figure.html — WebGAL 官方文档：`changeBg` / `changeFigure` 与 `-next` / `-left` / `-right` / `-left13` 等立绘槽位参数
[23] https://blog.yeyupiaoling.cn/article/1792560794303 — WebGAL 命令分类：基础／对话／背景立绘／场景分支／变量／音频／动画／特效
[24] https://monogatari.io/v2/building-blocks/characters — Monogatari 官方文档：`sprites` / `expressions` / `default_expression` / 实验性 layered sprites
[25] https://renpy.org/ — Ren'Py 官网：8.5.3 稳定版（2026-05-15）、8.6.0 预发布（2026-11-01）、HTML5/WebAssembly 为 Beta
[26] https://hysenlabs.com/projects/y-lohse-inkjs — inkjs 三方镜像分析：MIT、零依赖、TypeScript、664 stars、2.4.0（2026-02）、最近推送 2026-09-01（**第三方，非官方仓库，仅作旁证**）
[27] https://github.com/dialogic-godot/dialogic — Dialogic 组织页：MIT、约 6.1k stars、更新至 2026-08-30

**仍未核实**：Fungus、Naninovel、Yarn Spinner、Twine 的一手 LICENSE 页与最新 tag；ink 官方仓库 star 数；Ren'Py 具体许可证文本（官网仅表述「open source and free for commercial use」）。这些字段在集成前必须人工复核，本报告不代填。

## 附：R27 落地回执（2026-11-08）

P0 已落地 3 条：① 状态分层（`STORE_NS` / `STORE_SCHEMA` / `storeCheck`）；② 舞台命令日志（`STAGE_LOG` / `emitStage`，只记不改渲染）；③ 资源 manifest 229 层 + `资源清单门禁.py`。详见《开源方案借鉴落地记录.md》。P1（内容节点图、版本化快照、朗读统一队列、音效图、开发期多文件构建）未落地，按报告第十一节顺序推进。本轮回执不改变上文任何结论与许可证提示。
