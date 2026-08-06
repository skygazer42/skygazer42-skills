# UI/UX Pro Max · 中文速查指南

> 本文件由中文教程站点 [bbylw/ui-ux-pro-max-skill-cn](https://github.com/bbylw/ui-ux-pro-max-skill-cn)（v2.0，MIT）
> 与上游 [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) 内容提炼、校对而成。
> 作为英文 `SKILL.md` 的中文速查补充；完整执行流程以 `SKILL.md` 为准。

## 一句话定位

一个面向 AI 编码助手（Claude Code / Cursor / Windsurf / Codex CLI / Gemini CLI / Copilot 等）的**设计系统生成器**：
给一句需求，AI 通过推理引擎并行检索产品类型、UI 风格、配色、落地页模式与字体配对，几秒内输出一份完整、可落地的设计系统。

## 核心工作流（5 步）

1. **你提出请求** — 任何 UI/UX 任务：构建、设计、创建、实现、审查、修复、改进。
2. **生成设计系统** — AI 自动调用 `search.py ... --design-system` 用推理引擎生成完整设计系统。
3. **智能建议** — 按产品类型匹配最合适的风格、配色、排版。
4. **代码生成** — 用正确颜色/字体/间距/最佳实践实现 UI（注意技术栈）。
5. **交付前检查** — 对照常见反模式与无障碍规则自查。

## 示例提示词

```text
为我的 SaaS 产品构建一个着陆页
创建一个医疗分析仪表盘
设计一个具有深色模式的个人作品集网站
为电商应用制作一个移动端 UI
构建一个深色主题的金融科技银行应用
Build a landing page for my SaaS product
Create a dashboard for healthcare analytics
```

## 常用命令

```bash
python3 <skill>/scripts/search.py "beauty spa wellness" --design-system -p "Serenity Spa"   # ASCII 输出
python3 <skill>/scripts/search.py "fintech banking" --design-system -f markdown             # 文档输出
python3 <skill>/scripts/search.py "glassmorphism" --domain style                            # 按领域查询
python3 <skill>/scripts/search.py "elegant serif" --domain typography
python3 <skill>/scripts/search.py "dashboard" --domain chart
python3 <skill>/scripts/search.py "form validation" --stack react                           # 技术栈专属
python3 <skill>/scripts/search.py "responsive layout" --stack html-tailwind
```

> 注意：若用 Continue 安装，把命令中的 `.claude/skills/` 换成 `.continue/skills/`；
> Droid (Factory) 用 `.factory/skills/`。

## 持久化设计系统（Master + Overrides）

同一项目的设计系统可保存到文件，跨会话**分层检索**：

```bash
python3 <skill>/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp"
python3 <skill>/scripts/search.py "SaaS dashboard" --design-system --persist -p "MyApp" --page "dashboard"
```

生成结构：

```
design-system/
├── MASTER.md           # 全局事实来源（颜色、排版、间距、组件）
└── pages/
    └── dashboard.md    # 页面级覆盖（只记录与 Master 的差异）
```

分层检索规则：
1. 构建某页（如 "Checkout"）时先查 `design-system/pages/checkout.md`；
2. 存在则其规则**覆盖** Master；不存在则只用 Master；
3. 检索提示词可写成：「请读取 design-system/MASTER.md；并检查 design-system/pages/[page].md
   是否存在；存在则优先用页面规则，否则只用 Master 规则，然后生成代码」。

## 设计系统生成器原理

```
用户请求 ──► 并行的多域检索 ──► 推理引擎 ──► 完整输出
              (5 路并行)         (筛选排序)     Pattern + Style + Colors
  · 产品类型 161 类              · 分类规则     + Typography + Effects
  · UI 风格  67 种               · BM25 排名    + 反模式 + 交付前检查清单
  · 配色     161 套              · 行业反模式
  · 落地页模式 24 种             · 条件规则(JSON)
  · 字体配对  57 种
```

## 能力速览

- **67 种 UI 风格**：玻璃拟态、粘土拟态、极简主义、野兽派、新拟态、Bento Grid、深色模式、AI-Native UI 等。
- **161 种配色**：与产品类型一一对应的行业色板。
- **57 种字体配对**：含 Google Fonts 导入。
- **161 条行业推理规则**（v2.0）：覆盖科技/SaaS、金融、医疗、电商、服务业、创意、生活方式、新兴技术等领域，
  每条含——推荐落地页模式、风格优先级、色彩氛围、排版氛围、关键效果、避开的反模式（如银行不要用"AI 紫/粉渐变"）。
- **25 种图表类型**、**22 种技术栈**（React/Next/Vue/Nuxt/Svelte/Astro/SwiftUI/RN/Flutter/Tailwind/shadcn/ui/Jetpack Compose/Angular/Laravel/JavaFX/WPF/WinUI/Avalonia/Uno/UWP/Three.js）、**99 条 UX 指南**。

## 常见故障排查

| 问题 | 处理 |
| --- | --- |
| `uipro: unknown command 'uninstall'/'update'` | CLI 版本过旧，更新 `ui-ux-pro-max-cli`（旧 `uipro-cli` 已废弃） |
| `uipro uninstall` 提示未检测到已安装技能 | 进入最初安装技能的项目根目录再执行；或手动删除全局安装 |
| Marketplace 安装失败 "Zip contains a symbolic link" | 改用 CLI / npx 安装 |
| `npm install -g` 权限错误 | 用 Node 版本管理器（推荐）或 sudo；或改用 `npx` 免全局安装 |
| 找不到 Python | 安装 Python 3.x 或用 `python3`/`py -3` |
| 输出被截断/字段不全 | 调大输出宽度限制（0=不限） |
