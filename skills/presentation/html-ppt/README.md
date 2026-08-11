# HTML PPT Generator（交互式 HTML 演示文稿）

## 一句话定位

根据用户提供的配色方案、主题和逐页内容，生成单个自包含、浏览器即开即播的交互式 `.html` 演示文稿，**零外部依赖**。

## 适用场景

- 任何"帮我做个 PPT / 演示文稿"的请求，且接受浏览器直开 HTML 而非 .pptx 编辑文件
- 快速看效果、本地演示、发给他人即点即看
- 需要交互（粒子背景/毛玻璃/键盘导航/缩略图/全屏）而非静态图片/纯文档的演示

## 不适用场景

- 需要原生可编辑 `.pptx` 或 OOXML 精确控制（转 `presentation.open-kimi-ppt` / `presentation.ppt-agent`）
- 需要"内容调研→大纲→人审→出片→QA"的重度流水线（转 `presentation.ppt-agent`）
- 纯文档、品牌视觉体系、页面级前端实现（转 `writing.*` / `web.brandkit` / `web.frontend-implementation`）

## 执行前需要的信息

- 配色方案（8 套预设之一，或自定义颜色配置）
- 主题 / 标题 / 副标题
- 每页标题 + 内容类型（文字/列表/卡片/代码/图片等）+ 具体内容

## 执行流程

1. **确认需求**：确认配色、主题、每页内容；信息不足先询问，不编造。
2. **生成初级 HTML 框架**：按 `references/color_schemes.json` 取配色值，替换 `references/base_template.html` 的颜色占位符。
3. **渲染完整 PPT**：逐页渲染标题与内容，内容过少时添加与内容相关的装饰图形。
4. **检查与验证**：对照 SKILL.md 的「功能与布局检查清单」逐项确认后交付单个 `.html`。

## 交付结果

- 单个 `{主题名称}.html` 文件，写入用户指定目录或当前工作目录。
- 内含全部 CSS/JS（内联），无 CDN/字体/库依赖，离线可播。

## 默认边界

- **读文件**：否（默认不主动读取用户文件）
- **写文件**：是（仅生成目标 `.html`，不触碰其他文件）
- **执行命令**：否（无脚本）
- **网络**：否（无任何网络访问）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `presentation.open-kimi-ppt` | 产出 PPTD 项目 + 可编辑 .pptx（依赖 node + Kimi 远程服务）；本 Skill 产出离线可播的单文件 HTML |
| `presentation.ppt-agent` | 内容驱动七阶段流水线，产出 SVG + 原生可编辑 .pptx；本 Skill 是直给式"内容→HTML"，无调研无人审 |
| `web.design-system` | 给产品页面定 token/组件规范；本 Skill 产出可交互的整页演示文稿 |

三者输出物、依赖栈、触发场景均不重叠，相互独立、可互补。

## 行为案例

### 案例 1：典型创建

**输入**：用户要求做"产品发布会"PPT，选择商务蓝配色，提供每页标题和内容（产品介绍、功能特性、使用示例、总结等）。

**预期行为**：按商务蓝配色生成单文件 HTML，逐页渲染用户提供的标题和内容，包含粒子/毛玻璃/导航/缩略图/全屏等交互，交付 `{主题名称}.html`。

### 案例 2：信息不全

**输入**：用户只说"帮我做个 PPT"，未提供配色、主题或内容。

**预期行为**：先询问配色方案、主题、每页内容；停住等待补充，不自行编造完整 PPT。

### 案例 3：零外部依赖

**输入**：任何生成请求的产物。

**预期行为**：HTML 中无 `<script src>`、`<link href="http…">`、CDN 域名或 Google Fonts；幻灯片 `100vw×100vh`、`overflow:hidden`，进度条横向。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [Xusq513/skills-html-ppt](https://github.com/Xusq513/skills-html-ppt)（revision `dcd4e146…`）。
- **许可证**：上游 README 声明 MIT 但仓库未提供 LICENSE 文件；本目录 `LICENSE` 为依该声明复制的 MIT 许可证文本，详见 `provenance.yaml`。