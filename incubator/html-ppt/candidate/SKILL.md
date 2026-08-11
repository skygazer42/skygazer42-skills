---
name: html-ppt
description: 创建交互式HTML PPT演示文稿。支持多套配色方案，根据用户提供的配色方案、主题、每页标题和内容生成精美的HTML幻灯片。
---

## 技能概述

这是一个用于创建交互式HTML PPT演示文稿的技能。基于现有的PPT模板，支持多套配色方案，用户只需提供主题、配色和每页内容即可生成专业美观的演示文稿。

**执行步骤：**

1. **生成初级HTML框架** - 根据配色方案和模板生成不含内容的空壳HTML
2. **渲染完整PPT** - 根据用户提供的配色方案、主题、每页标题和内容渲染每页PPT
3. **检查与验证** - 确保HTML格式正确，所有功能正常

---

## 用户必须提供的信息

在创建PPT之前，用户必须明确提供以下信息：

### 1. 配色方案

从以下配色方案中选择，或自定义颜色：

| 方案名称 | 主色调 | 辅助色 | 强调色 | 背景色 |
|---------|--------|--------|--------|--------|
| **赛博朋克** | 青色 `#00f5d4` | 紫色 `#7b2cbf` | 橙色 `#ff6b35` | 深空黑 `#0a0a0f` |
| **商务蓝** | 蓝色 `#2563eb` | 深蓝 `#1e40af` | 金色 `#f59e0b` | 纯白 `#ffffff` |
| **暗夜紫** | 紫罗兰 `#8b5cf6` | 粉色 `#ec4899` | 青色 `#06b6d4` | 深灰 `#1a1a2e` |
| **森林绿** | 翠绿 `#10b981` | 深绿 `#047857` | 琥珀 `#f59e0b` | 米白 `#fefce8` |
| **日落橙** | 珊瑚 `#f97316` | 红色 `#ef4444` | 黄色 `#eab308` | 暖白 `#fff7ed` |
| **极简灰** | 黑色 `#000000` | 灰色 `#6b7280` | 红色 `#dc2626` | 白色 `#ffffff` |
| **企业红** | 深红 `#dc2626` | 暗红 `#991b1b` | 银灰 `#9ca3af` | 深灰 `#1f2937` |
| **海洋蓝** | 天蓝 `#0ea5e9` | 深蓝 `#0369a1` | 绿色 `#22c55e` | 浅蓝 `#f0f9ff` |

**自定义配色** - 用户也可以指定完整颜色配置：
- 背景色 (bg-deep, bg-card)
- 主色调 (primary)
- 辅助色 (secondary)
- 强调色 (accent)
- 文字色 (text-primary, text-secondary)
- 边框发光色 (border-glow)

### 2. 主题

PPT的主题/标题，例如：
- "产品发布会"
- "年度总结报告"
- "技术分享会"
- "团队介绍"

### 3. 每页内容

每页PPT需要提供：
- **标题** - 页面主标题
- **内容** - 可以是文字、列表、卡片、代码块等
- **展示形式** - 根据内容类型选择最合适的展示方式

---

## 幻灯片模板结构

### 通用样式

```css
/* 配色变量 - 会根据用户选择的配色方案动态生成 */
:root {
    --bg-deep: #背景深色;
    --bg-card: rgba(背景色, 0.8);
    --primary: #主色调;
    --secondary: #辅助色;
    --accent: #强调色;
    --text-primary: #文字主色;
    --text-secondary: #文字次色;
    --border-glow: rgba(主色调, 0.3);
}
```

### 可用组件

1. **标题幻灯片** - 大标题 + 副标题 + 动态背景
2. **内容幻灯片** - 标题 + 文字内容
3. **卡片列表** - 多列卡片展示特性
4. **代码块** - 带语法高亮的代码展示
5. **图片展示** - 图片/截图展示区域
6. **对比卡片** - 左右对比布局
7. **特性列表** - 带图标的特性项
8. **引用框** - 案例/引用展示
9. **总结幻灯片** - 总结内容 + 联系方式
10. **时间线** - 流程/步骤展示
11. **统计卡片** - 数字/统计展示

### 字体配置

> **⚠️ 重要：严禁使用任何外部字体 CDN，必须使用系统字体**

- **正文字体**: `"Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", -apple-system, BlinkMacSystemFont, sans-serif`
- **代码字体**: `"Cascadia Code", "Fira Code", "Source Code Pro", Consolas, "Courier New", monospace`

---

### 布局规范（重要）

#### 1. 浏览器分辨率兼容

- 幻灯片容器必须使用 `width: 100vw` 和 `height: 100vh`
- 使用响应式字体 `clamp(min, val, max)` 适配不同屏幕
- 包含 `@media (max-width: 900px)` 断点处理移动端
- 使用 `min()`、`max()`、`clamp()` 等CSS函数优化布局

#### 2. 滚动条控制（核心要求）

- **每页幻灯片禁止出现滚动条**
- 幻灯片容器必须设置 `overflow: hidden`
- 内容必须完全在可视区域内，不能溢出
- 如果内容过多，考虑：
  - 拆分到多页
  - 减小字体尺寸
  - 减少列表项数量
  - 使用折叠/收起组件

#### 3. 内容布局均衡

- **禁止大面积留白**：内容区域使用 Flexbox 垂直居中布局，但要根据内容调整：
  - 内容多时：顶部对齐，减少底部留白
  - 内容少时：添加装饰性图形/背景元素补充视觉
- **使用 Grid/Flex 布局**让内容均匀分布
- 标题与内容保持合理间距（使用 `gap` 而非固定 `margin`）
- 卡片列表使用 `grid-template-columns: repeat(auto-fit, minmax(...))` 自适应

#### 4. 内容过少时的视觉补充（与内容相关）

当单页内容较少时（如只有1-2个要点），**装饰图形必须与页面主题/内容相关**，不能随意添加无关装饰。

**根据内容类型选择对应的装饰图形：**

| 内容类型 | 装饰图形建议 | CSS实现方式 |
|---------|-------------|-------------|
| 团队/人物介绍 | 人物轮廓虚影、同心圆 | 使用 `radial-gradient` 模拟人物/圆形 |
| 产品/功能介绍 | 产品轮廓、六边形蜂巢 | 使用 `polygon` 或多重边框 |
| 数据/统计 | 数据点、柱状图简化、趋势线 | 使用伪元素创建条形/折线 |
| 流程/步骤 | 流程节点、连接线、箭头 | 使用 `::before/::after` 创建连接元素 |
| 总结/结论 | 光芒、光晕、星星 | 使用 `radial-gradient` + 动画 |
| 技术/代码 | 代码符号、括号、圆点 | 使用字符或几何形状 |
| 时间/历史 | 时间轴节点、圆点 | 使用伪元素创建时间轴装饰 |
| 列表/要点 | 圆点、勾选框、对勾 | 使用 SVG 或 CSS 绘制 |

**实现示例：**

```css
/* 团队介绍页 - 同心圆装饰 */
.slide[data-type="team"]::before {
    content: '';
    position: absolute;
    width: 400px;
    height: 400px;
    border: 2px solid var(--secondary);
    border-radius: 50%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.2;
}

/* 产品页 - 六边形蜂巢 */
.slide[data-type="product"]::after {
    content: '';
    position: absolute;
    width: 200px;
    height: 173px;
    background: linear-gradient(135deg, var(--primary) 0%, transparent 100%);
    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    opacity: 0.15;
    top: 20%;
    right: 10%;
}

/* 数据页 - 柱状图装饰 */
.slide[data-type="data"]::before {
    content: '';
    position: absolute;
    bottom: 15%;
    left: 10%;
    display: flex;
    gap: 10px;
    align-items: flex-end;
}
.slide[data-type="data"]::before::before,
.slide[data-type="data"]::before::after {
    content: '';
    width: 30px;
    background: var(--primary);
    opacity: 0.3;
    border-radius: 4px 4px 0 0;
}
```

**关键原则：**
- 装饰图形使用 `opacity: 0.1~0.3` 保持低调
- 使用 `::before/::after` 伪元素，不增加额外DOM
- 可以使用动画（如 `pulse`）增加动态感
- 颜色使用 `var(--primary)` / `var(--secondary)` 保持配色一致

```css
/* 内容少时的装饰示例 */
.slide:has(.content-block:only-child)::before {
    content: '';
    position: absolute;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, var(--secondary) 0%, transparent 70%);
    opacity: 0.3;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation: pulse 3s ease-in-out infinite;
}
```

---

## 执行流程

### 步骤1：确认需求

在开始创建之前，必须向用户确认以下信息：

```
请提供以下信息以创建PPT：

1. 配色方案：从"赛博朋克"/"商务蓝"/"暗夜紫"/"森林绿"/"日落橙"/"极简灰"/"企业红"/"海洋蓝"中选择，或指定自定义颜色
2. 主题：PPT的标题和副标题
3. 每页内容：按顺序列出每页的标题和内容，包括：
   - 每页的标题
   - 内容类型（文字/列表/卡片/代码/图片等）
   - 具体内容

示例格式：
- 第1页：标题"产品介绍"，内容为...
- 第2页：标题"功能特性"，内容为3个卡片...
- 第3页：标题"使用示例"，内容为代码块...
```

### 步骤2：生成初级HTML

根据配色方案生成HTML框架（不含内容），包含：
- CSS变量定义
- 基础样式和动画
- 导航组件
- 进度条组件
- 幻灯片容器结构

**输出示例：**
```html
<!-- 生成的初级框架结构 -->
<div class="presentation">
    <div class="slides-container" id="slidesContainer">
        <!-- 幻灯片将由步骤2动态生成 -->
    </div>
    <!-- 导航箭头 -->
    <div class="nav-arrow nav-prev" onclick="prevSlide()">...</div>
    <div class="nav-arrow nav-next" onclick="nextSlide()">...</div>
    <!-- 进度条 -->
    <div class="progress-container">...</div>
    <!-- 进度点 -->
    <div class="progress-dots" id="progressDots">...</div>
</div>
```

### 步骤3：渲染完整PPT

根据用户提供的每页内容，使用丰富的UI技术渲染：

1. **标题幻灯片**：
   - 动态渐变背景
   - 浮动粒子效果
   - 大标题 + 副标题动画

2. **内容幻灯片**：
   - 根据内容类型选择展示方式
   - 卡片列表：网格布局 + 悬停效果
   - 代码块：语法高亮 + 复制按钮
   - 特性列表：图标 + 描述

3. **动画效果**：
   - 入场动画（淡入 + 上浮）
   - 交错延迟动画
   - 页面切换动画

### 步骤4：检查与验证

1. 检查HTML语法正确性
2. 验证CSS变量是否正确应用
3. 确认导航功能正常
4. 检查进度条和进度点同步
5. 验证键盘快捷键支持
6. 检查响应式布局

---

## 输出要求

1. **输出文件**: 单个 `.html` 文件，可直接在浏览器中打开
2. **文件命名**: `{主题名称}.html` (如 `产品发布会.html`)
3. **依赖**: **严禁引入任何外部JS和CSS**（包括CDN链接、Google Fonts等），必须使用纯本地化方案
   - 字体：使用系统字体栈，如 `"Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", -apple-system, sans-serif`
   - 代码字体：使用 `"Cascadia Code", "Fira Code", Consolas, "Courier New", monospace`
   - 所有CSS和JS必须内联到HTML文件中

---

## 技能文件结构

```
.claude/skills/html-ppt/
├── SKILL.md                 # 技能说明文件
├── templates/
│   ├── base_template.html   # 基础HTML模板
│   └── color_schemes.json   # 配色方案配置
```

## 配色方案配置说明

配置文件 `color_schemes.json` 包含以下字段：

| 字段 | 说明 |
|------|------|
| bg-deep | 页面深色背景 |
| bg-card | 卡片背景色 |
| primary | 主色调（标题、强调） |
| secondary | 辅助色（渐变、图标） |
| accent | 强调色（重点突出） |
| text-primary | 主要文字颜色 |
| text-secondary | 次要文字颜色 |
| border-glow | 边框发光色 |
| bg-gradient-* | 背景渐变色（3层） |
| primary-shadow | 主色调阴影 |
| hover-shadow | 悬停阴影 |
| example-bg-* | 示例框背景渐变 |
| nav-* | 导航按钮样式 |

## 功能检查清单（必读）

生成PPT时，必须确保包含以下**所有功能**，不得遗漏：

### 核心视觉功能
- [ ] **粒子浮动效果** - `.particles` 容器 + `particleFloat` 动画 + JS创建粒子
- [ ] **毛玻璃效果** - `backdrop-filter: blur(10px)` 用于卡片和导航
- [ ] **响应式字体** - 使用 `clamp(min, val, max)` 而非固定像素
- [ ] **背景动画** - `bgFloat` 动画（漂移+旋转）
- [ ] **弹性入场动画** - `tourPop` 关键帧动画

### 交互功能
- [ ] **缩略图视图** - 按 `T` 键或点击按钮切换，显示所有幻灯片网格
- [ ] **全屏功能** - 按 `F` 键或双击切换
- [ ] **帮助覆盖层** - 按 `H` 键显示快捷键说明
- [ ] **键盘导航** - 左右箭头/空格/ESC
- [ ] **触摸滑动** - 移动端swipe支持
- [ ] **鼠标滚轮** - 滚动切换页面（带节流防抖）
- [ ] **进度条 + 进度点** - 底部导航，**进度条必须横向展示**
- [ ] **首次气泡指引** - 首次打开PPT时显示引导气泡，提示用户操作方式（如"点击右下角箭头或按右键切换下一页"），用户关闭后使用 localStorage 记录，不再重复显示

### 组件样式
- [ ] **example-box** - 示例框组件（左border强调）
- [ ] **tool-badge** - 工具徽章组件
- [ ] **title-slide** - 标题页专用样式（居中、大字号）
- [ ] **响应式布局** - `@media (max-width: 900px)` 断点

### 布局检查（重要）
- [ ] **幻灯片容器** - 使用 `width: 100vw; height: 100vh; overflow: hidden`
- [ ] **无滚动条** - 每页幻灯片内容不溢出，无滚动条出现
- [ ] **响应式字体** - 标题/正文使用 `clamp()` 函数
- [ ] **内容均衡** - 使用 Flex 垂直居中，内容过少时添加装饰图形
- [ ] **无大面积留白** - 内容区域合理分布，避免上下留白过多

### 调试验证
生成完成后，检查HTML是否包含：
```html
<!-- 必须包含 -->
<div class="particles" id="particles"></div>
<div class="thumbnail-view" id="thumbnailView">
<div class="help-overlay" id="helpOverlay">
<button onclick="toggleThumbnailView()">  <!-- T键 -->
<button onclick="toggleFullscreen()">    <!-- F键 -->
<button onclick="toggleHelp()">          <!-- H键 -->
```

**鼠标滚轮代码验证：**
```javascript
// 必须包含滚轮事件监听（带节流防抖）
document.addEventListener('wheel', (e) => {
    if (wheelTimeout) return;  // 节流
    if (e.deltaY > 0) nextSlide();
    else if (e.deltaY < 0) prevSlide();
}, { passive: true });
```

**进度条横向展示验证：**
```css
/* 进度条必须是横向的，使用 width 而不是 height */
.progress-bar {
    width: 0%;
    height: 4px;
    transition: width 0.3s ease;
}
```

**首次气泡指引验证：**
首次打开PPT时显示引导气泡，使用 localStorage 记录用户是否已看过指引，关闭后不再重复显示。

```html
<!-- 必须包含首次气泡指引元素 -->
<div id="guideTooltip" class="guide-tooltip">
    <div class="guide-content">
        <span class="guide-icon">?</span>
        <span class="guide-text">点击右下角箭头或按 → 键切换下一页</span>
        <button class="guide-close" onclick="closeGuide()">×</button>
    </div>
</div>
```

**首次气泡指引 CSS 样式要求：**
```css
.guide-tooltip {
    position: fixed;
    bottom: 100px;
    right: 80px;
    z-index: 1000;
    animation: guideFadeIn 0.5s ease;
}
.guide-content {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 16px;
    background: var(--bg-card);
    backdrop-filter: blur(10px);
    border: 1px solid var(--border-glow);
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.guide-icon {
    width: 24px;
    height: 24px;
    background: var(--primary);
    color: var(--bg-deep);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}
.guide-text {
    font-size: clamp(12px, 1.5vw, 14px);
    color: var(--text-primary);
}
.guide-close {
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 18px;
    cursor: pointer;
    padding: 0 4px;
}
@keyframes guideFadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
```

**首次气泡指引 JS 逻辑：**
```javascript
// 页面加载时检查是否需要显示引导
document.addEventListener('DOMContentLoaded', function() {
    if (!localStorage.getItem('ppt_guide_shown')) {
        showGuide();
    }
});

function showGuide() {
    const tooltip = document.getElementById('guideTooltip');
    if (tooltip) tooltip.style.display = 'flex';
}

function closeGuide() {
    const tooltip = document.getElementById('guideTooltip');
    if (tooltip) tooltip.style.display = 'none';
    localStorage.setItem('ppt_guide_shown', 'true');
}
```

## 注意事项

- 用户必须明确提供配色方案、主题和每页内容，三者缺一不可
- 如果用户信息不完整，需要询问补充
- 代码块内容需要适当转义HTML特殊字符
- 中英文混排时注意字体兼容性
- 确保生成的HTML在不同浏览器中兼容
- 生成的HTML文件保存在用户指定目录或当前工作目录
- **重要**：每次生成后必须对照功能检查清单验证，确保无遗漏
- **⚠️ 严格禁止**：严禁在生成的HTML中引入任何外部JS或CSS（包括CDN链接、Google Fonts、Bootstrap等），必须使用纯本地化方案
- **进度条要求**：进度条必须横向展示（使用 `width` 属性），不能纵向展示
- **首次气泡指引**：首次打开PPT时显示引导气泡，使用 localStorage 记录，关闭后不再重复显示

---

## 布局核心要求（必须遵守）

1. **浏览器分辨率兼容**
   - 幻灯片使用 `100vw × 100vh` 全屏尺寸
   - 字体使用 `clamp()` 函数自动适配
   - 响应式断点 `@media (max-width: 900px)`

2. **禁止滚动条**
   - 幻灯片容器设置 `overflow: hidden`
   - 内容必须完全在可视区域内
   - 内容过多时拆分为多页或减小尺寸

3. **内容均衡，无大面积留白**
   - 使用 Flexbox 垂直居中布局
   - 内容少时添加装饰图形（渐变光晕、几何图案等）
   - 避免上下留白过多

4. **视觉补充**
   - 单页内容少时添加装饰性背景元素
   - 可以使用 CSS 绘制圆形、菱形、线条等装饰
