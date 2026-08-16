# gpt-image（GPT Image 2 生成 / 编辑）

## 一句话定位

基于 OpenAI GPT Image 2 的通用图像生成、编辑与修复 Skill：先在本仓内置的 162 条提示词
Gallery 与工艺清单里检索匹配范式，再起草高质量提示词，最后通过 `gpt-image` CLI 调用
OpenAI API 输出图像。不是裸的 API 封装，而是一套「范例驱动的提示词工作流」。

## 适用场景

- 文本生图：`generate`——按描述生成海报、插画、摄影、UI 示意图、图表、像素画等
- 参考图编辑：`edit`——给一张或多张参考图配指令，做风格迁移、换装、翻译图中文字等
- 局部修复：`inpaint`——参考图 + alpha 蒙版，只重绘蒙版透明区域
- 提示词质量提升：用户给出模糊需求，需要先检索 Gallery / craft 再产出结构化提示词
- 中文排版、密集文字、海报层级、学术示意图等需要 `high` 质量与精确文字约束的输出

## 不适用场景

- 用户照片 → 摄影 + 抽象面板编辑作品（转 `art.photo-abstract-editorial`，内容源必须是上传照片）
- 截图 → 前端代码还原（转 `web.image-to-code` / `web.frontend-implementation`）
- 网页视觉方向探索、界面设计规范、品牌体系（转 `web.frontend-design` / `web.interface-design` / `web.brandkit`）
- 需要可交互 HTML/PPT 而非位图（转 `presentation.html-ppt` / `presentation.ppt-agent`）
- 明确要求写图像生成代码或改本 Skill 仓库——默认不写代码，只调用现有 CLI

## 执行前需要的信息

- 请求类型：`generate` / `edit` / `inpaint` / `multi-reference`，以及目标资产类型、画布比例、尺寸、质量档
- 必须的文字内容（原文逐字给出，含中文；需要精确渲染的文本用引号包裹）
- 参考图 / 蒙版路径（`edit` / `inpaint` 必需）；期望的输出路径
- 运行前提：Python 3.11+ 且具备 `gpt-image`、`uv`、`uvx` 之一；`OPENAI_API_KEY`（env / `.env` / `~/.env`）
- 预算/质量档：`low`（草稿）/ `medium`（探索）/ `high`（最终资产、中文、图表、UI）

## 执行流程

1. **分类请求**：判定 `generate` / `edit` / `inpaint` / `multi-reference`，抽取文字、比例、参考图、安全约束与质量档。
2. **先检索参考**：打开 `references/gallery.md` 路由索引，加载最接近的 1 个（最多 2–3 个）
   `references/gallery-<category>.md`，读取真实 `**Prompt**` 文本后再选范式。
3. **用 craft 打磨**：涉及密集文字、图表、UI、数据可视化、多面板布局、弱提示词或没有接近范例时，
   加载 `references/craft.md`（19 节清单）。
4. **必要时沟通**：昂贵 / 模糊 / 高打磨请求前，给出 1–3 个匹配方向与计划 size/quality，最多问一个简洁问题；
   明确「现在生成」的请求跳过讨论。
5. **预检、无副作用**：检查 CLI 可用性（`command -v gpt-image` 等），不擅自重装、不改 `.env`、不写 API key。
6. **仅通过 CLI 执行**：调用 `gpt-image` 或 `scripts/generate.py`，不另写生成脚本。
7. **汇报**：输出文件路径、关键 flag、一句可行的精调建议。

快路径：提示词明确 + 明确「现在生成」→ 快速查参考/工艺，直接调 CLI。

## 交付结果

- 生成/编辑/修复后的图像文件（输出路径打印在 stdout）
- 执行时的关键 flag（模型、size、quality、n 等）
- 若需要，一句精调建议（参考图、质量档、尺寸、提示词微调）

## 默认边界

- **读文件**：是——`references/`、`-i` 参考图、`-m` 蒙版、`.env` 中的 `OPENAI_API_KEY`
- **写文件**：是——输出图像（`-f` 指定路径或默认 `cwd`/`cwd/fig/`）；不写 `.env`、不写 API key、不覆盖 skill 目录
- **执行命令**：是——运行 `gpt-image` / `scripts/generate.py` / `uvx`（Python 3.11+）
- **网络**：是——调用 OpenAI API（产生账单）；`scripts/generate.py` 无本地后端时会经 `uvx` 临时从作者 GitHub 安装 CLI（见下方风险提示）
- **绝不做**：打印密钥、把 key 写进文件、无授权覆盖/重装工具、把参考图之外的内容当作素材

### 风险提示

- **远程安装回退**：`scripts/generate.py` 的最后一级回退会执行
  `uvx --from git+https://github.com/wuyoscar/gpt_image_2_skill gpt-image`，
  即从作者 GitHub 临时安装并运行 CLI 包。仅在本地无 `gpt-image` / `gpt_image_cli` 时触发。
  不想走这条路时，可先手动 `uv tool install git+https://github.com/wuyoscar/gpt_image_2_skill`
  安装后端，或临时 `unset OPENAI_API_KEY` 禁止用本地 key 调用。
- **API 费用**：每次成功调用会从你的 OpenAI 账号计费；`quality` 档位是成本旋钮（`low`/`medium`/`high`）。

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `art.photo-abstract-editorial` | 单张上传照片 → 摄影+抽象面板编辑作品，内容源必须来自照片；gpt-image 是通用生成/编辑 + 提示词库，可凭空生图 |
| `web.image-to-code` | 截图 → 前端代码（HTML/CSS），方向与 gpt-image 相反 |
| `web.frontend-design` / `web.interface-design` | 界面设计规范与探索流程，不负责调用图像模型出图 |
| `presentation.html-ppt` / `presentation.ppt-agent` | 产出可交互 HTML / PPTX，gpt-image 产出位图 |

## 行为案例

### 案例 1：典型成功——从模糊需求到成品海报

**输入**：用户说「帮我生成一张 3:4 的茶叶促销海报，品牌叫『山川茶事』，要显示中杯 16 元、大杯 19 元」，
`OPENAI_API_KEY` 已配置且 `gpt-image` CLI 可用。

**预期行为**：
1. 判定 `generate`，抽取精确文字（`"山川茶事"` / `"中杯 16 元"` / `"大杯 19 元"`）与 `portrait` / `high` 质量档
2. 打开 `gallery.md` 路由到 `gallery-typography-and-posters.md`，参考中文排版与促销层级范例；需要时加载 `craft.md`
3. 用 `gpt-image -p "..." --size portrait --quality high -f poster.png` 调用 CLI
4. 汇报输出路径与使用的 flag；文案逐字保留、不 paraphrase

### 案例 2：边界——禁止静默改配置

**输入**：用户请求生成图片，但本地既没有 `gpt-image`，也没有 `uv`/`uvx`，也没有 `OPENAI_API_KEY`。

**预期行为**：不擅自安装工具、不创建/改写 `.env`、不写入 API key；明确报告缺什么（CLI 后端或 key），
并给出安装/配置指引（如 `uv tool install git+...`、把 key 放入 env）；绝不打印或落盘密钥。

### 案例 3：失败——错误参数早失败

**输入**：用户对 `edit` 请求只给了 `-m` 蒙版却没给 `-i` 参考图，或 `-i` 指向不存在的文件。

**预期行为**：在调用 API 之前报错退出（`--mask requires --image` / `--image not found`），退出码 2；
不会把错误的参数透传给 API 浪费一次计费调用。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：内化自 [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill)
  （MIT，Copyright (c) 2026 Wuyoscar），固定 revision `068dd9e2`，原路径 `skills/gpt-image`。
- **本地改动**：剥离 `docs/` 示例图引用、移除 openclaw 平台元数据、补全契约文件；提示词文本与工作流未改动。
  完整修改记录见 `provenance.yaml`，审核记录见 `incubator/gpt-image/review.md`。
