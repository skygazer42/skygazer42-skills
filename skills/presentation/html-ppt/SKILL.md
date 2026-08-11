---
name: html-ppt
description: 根据用户提供的配色方案、主题和逐页内容，生成单个自包含的交互式 HTML 演示文稿（.html）。支持 8 套预设配色与自定义配色。触发场景：任何"帮我做个 PPT / 演示文稿"且接受浏览器直开 HTML 而非 .pptx 编辑文件的请求。
---

# HTML PPT Generator

## 能力概述

根据用户提供的**配色方案**、**主题**和**每页标题+内容**，生成一个可直接在浏览器中打开的单个 `.html` 演示文稿。

- **8 套预设配色**：赛博朋克 / 商务蓝 / 暗夜紫 / 森林绿 / 日落橙 / 极简灰 / 企业红 / 海洋蓝，每套包含深背景、卡片背景、主色调、辅助色、强调色、文字色与边框发光色。
- **自定义配色**：用户可自行指定完整颜色配置（`bg-deep`、`bg-card`、`primary`、`secondary`、`accent`、`text-primary`、`text-secondary`、`border-glow`）。
- **交互能力**：粒子背景、毛玻璃、入场动画、键盘/触摸/滚轮导航、缩略图（T）、全屏（F）、帮助（H）、进度条与进度点、首次气泡指引。
- **零依赖**：所有 CSS/JS 内联进生成的 HTML；不使用任何外部 CDN、字体或库。

完整模板见 `references/base_template.html`，配色配置见 `references/color_schemes.json`（生成前必须按该文件替换 `{{PLACEHOLDER}}` 并填充 `{{SLIDES_CONTENT}}`）。

## 用户必须提供的信息

开始前必须确认以下三项，缺一不可：

1. **配色方案**：从 8 套预设中选择，或提供自定义颜色配置。
2. **主题**：PPT 的标题与副标题。
3. **每页内容**：按顺序列出每页标题、内容类型（文字/列表/卡片/代码/图片等）与具体内容。

信息不完整时必须先询问补充，不得自行编造配色、主题或页面内容。

## 执行流程

1. **确认需求**：向用户确认配色方案、主题、每页内容；给出来回确认的示例格式（第 1 页标题…、第 2 页…）。
2. **生成初级 HTML 框架**：依据 `references/color_schemes.json` 选中配色或用户自定义色，替换 `references/base_template.html` 中的 `{{BG_DEEP}}`、`{{PRIMARY}}` 等占位符，生成不含内容的框架。
3. **渲染完整 PPT**：将每页标题与内容渲染成对应幻灯片；根据内容多寡调整展示形式（卡片列表/代码块/对比卡片/时间线/统计卡片等），内容过少时添加**与内容相关**的装饰图形。
4. **检查与验证**：对照下方「功能与布局检查清单」逐项确认，最后交付。

## 输出契约

- **输出文件**：单个 `.html` 文件，文件名 `{主题名称}.html`，写入**用户指定目录或当前工作目录**。
- **写入边界**：只生成这一个 HTML 文件；不修改、不删除用户其他文件，不触碰系统路径，不向网络发送任何内容。
- **依赖**：零外部依赖；所有 CSS/JS 内联。禁止 CDN、Google Fonts、Bootstrap 等外链。
- **字体**：正文 `"Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", -apple-system, BlinkMacSystemFont, sans-serif`；代码 `"Cascadia Code", "Fira Code", "Source Code Pro", Consolas, "Courier New", monospace`。

## 布局规范（必须遵守）

1. **尺寸与滚动**：幻灯片容器 `width: 100vw; height: 100vh; overflow: hidden`；每页禁止滚动条，内容必须在可视区域，溢出时拆分多页或缩小字号/列表项。
2. **无大面积留白**：内容用 Flexbox 垂直居中；内容过少时添加**与页面主题/内容相关**的装饰图形（团队→同心圆/径向渐变、产品→六边形 polygon、数据→柱状/趋势线、流程→连接线/箭头、时间→时间轴节点等，`opacity: 0.1~0.3`，用 `::before/::after` 不增加 DOM）。
3. **响应式**：字体用 `clamp(min, val, max)`；包含 `@media (max-width: 900px)` 断点；卡片用 `grid-template-columns: repeat(auto-fit, minmax(...))`。
4. **配色一致性**：所有颜色取自当前配色方案的 CSS 变量（`var(--primary)` 等），由第 2 步替换而来。

## 功能与布局检查清单

生成时必须包含以下**全部**功能，不得遗漏：

- [ ] 粒子浮动 `.particles` + `particleFloat` + JS `createParticles`
- [ ] 毛玻璃 `backdrop-filter: blur(10px)`（卡片与导航）
- [ ] `bgFloat` 背景漂移动画、`tourPop` 弹性入场、`guideFadeIn`
- [ ] 缩略图视图（T 键/按钮）、全屏（F 键/双击）、帮助覆盖层（H 键）
- [ ] 键盘导航（←/→/空格/ESC）、触摸滑动、节流滚轮切换
- [ ] 进度条**横向**（`width` 而非 `height`）+ 进度点
- [ ] 首次气泡指引（`.guide-tooltip`），localStorage 键 `ppt_guide_shown` 记录，关闭后不再显示
- [ ] 组件：`example-box`、`tool-badge`、`title-slide`
- [ ] 幻灯片容器 `100vw × 100vh`、`overflow: hidden`、`clamp()` 响应式字体、内容均衡无大留白

调试标记（用于自检）必须存在：

```html
<div class="particles" id="particles"></div>
<div class="thumbnail-view" id="thumbnailView">
<div class="help-overlay" id="helpOverlay">
<button onclick="toggleThumbnailView()">
<button onclick="toggleFullscreen()">
<button onclick="toggleHelp()">
```

滚轮节流与横向进度条：

```javascript
document.addEventListener('wheel', (e) => {
    if (wheelTimeout) return;
    if (e.deltaY > 0) nextSlide();
    else if (e.deltaY < 0) prevSlide();
}, { passive: true });
```

```css
.progress-bar { width: 0%; height: 4px; transition: width 0.3s ease; }
```

## 约束

- 不得编造缺失信息；用户未提供配色/主题/内容时先询问。
- 生成的 HTML 中严禁任何外部 JS/CSS/CDN/字体；代码块内容需转义 HTML 特殊字符。
- 中英文混排注意字体兼容；确保不同浏览器与移动端可用。

## 失败处理

用户信息不完整或无法确认上下文时，说明缺少什么、需要什么才能继续，不生成残缺 PPT。检测到生成结果与检查清单不符时，修复后重新渲染再交付。