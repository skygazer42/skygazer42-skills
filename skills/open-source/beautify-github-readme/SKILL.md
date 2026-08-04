---
name: beautify-github-readme
description: 当用户想让 GitHub 个人主页 README 更好看、更专业、更有吸引力时使用——包括添加徽章、统计卡片、排版优化、内容布局和视觉美化。
---

# 美化 GitHub README

## 概述

把平淡的 GitHub 个人主页 README 变成好看、专业、一眼就想了解的页面。不改动实质内容的前提下，通过排版、徽章、统计卡片、分割线和布局来提升视觉吸引力。

**核心原则：**先读现有 README，不改已有实质内容，在其上叠加视觉增强。

## 何时使用

- 用户说"我的 GitHub 主页好丑"、"帮我美化 README"、"让我的 profile 好看点"。
- 用户的 GitHub README 只有纯文字，没有任何视觉元素。
- 用户想加 GitHub 统计、常用技术徽章、访客计数、动态排版等。
- 用户想重新组织已有内容的布局让它更有层次感。

**不用时：**
- 用户只是想改 README 里的**实质内容**（项目介绍、技能列表等）——那是内容编辑，不是美化。
- README 是项目文档而非个人主页——项目 README 用不同标准。

## 执行流程

1. **读现有 README**：完整读用户的 GitHub profile README（通常是 `用户名/用户名` 仓库的 `README.md`）。理解已有的内容结构。

2. **分析现状**：现有 README 有什么？纯文字？有图片吗？有表格吗？组织方式怎么样？哪些部分最需要视觉提升？

3. **提出美化方案**：根据现有内容，推荐 2-3 种美化方向（如简洁专业 vs 活泼个性 vs 极简技术感），让用户选。

4. **实施美化**：在用户选定方向后，改写 README。保留所有原有实质内容，叠加：

   | 元素 | 说明 |
   | --- | --- |
   | **头部横幅** | 动态打字效果、个人介绍、社交链接 |
   | **技术徽章** | 常用语言/工具/框架的 shields.io 徽章 |
   | **GitHub 统计卡片** | 通过 `github-readme-stats` 展示提交、PR、Star 等 |
   | **常用语言卡片** | 展示使用最多的语言分布 |
   | **访客计数** | 可选，简单的访客计数器 |
   | **分割线** | HTML `<hr>` 或 emoji 分割线改善阅读节奏 |
   | **排版** | 标题层级、emoji 引导、折叠区、引用块、代码高亮 |
   | **布局** | HTML `<table>` / `<div align="center">` 控制居中和对齐 |

5. **给出预览和回调**：改写后展示改动 diff 或预览，让用户确认。若用户想调徽章颜色、统计类型、布局等，继续迭代。

## 常用工具与资源

| 用途 | 工具/URL | 说明 |
| --- | --- | --- |
| 技术徽章 | `https://img.shields.io/badge/<标签>-<颜色>?style=flat&logo=<图标>` | shields.io，最通用 |
| GitHub 统计 | `https://github-readme-stats.vercel.app/api?username=<用户名>&show_icons=true` | 开源统计卡片 |
| 常用语言 | `https://github-readme-stats.vercel.app/api/top-langs?username=<用户名>&layout=compact` | 语言分布卡片 |
| Streak 统计 | `https://github-readme-streak-stats.herokuapp.com/?user=<用户名>` | 连续提交天数 |
| 访客计数 | `https://visitor-badge.laobi.icu/badge?page_id=<用户名>.<用户名>` | 简单计数器 |
| 动态打字 | `https://readme-typing-svg.herokuapp.com?lines=<文字>` | 打字动画 SVG |
| 贡献网格 | `https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=<用户名>` | 详细贡献图 |
| Emoji 参考 | 使用 Unicode emoji 作为视觉引导符 | 不依赖外部资源 |

## 美化原则

- **先读后改**：不改用户已有的实质内容。
- **克制**：徽章最多 8-10 个，统计卡片最多 3-4 个——太多等于没有重点。
- **对齐和间距**：居中头部、合理空行、层级分明的标题。
- **暗色兼容**：选择的徽章和卡片风格要同时适配 GitHub 亮色和暗色主题。
- **可维护**：用户要知道怎么加新徽章或改统计，注释关键配置。
- **不依赖收费服务**：只用免费开源工具。

## 交付结果

- 改写后的 `README.md`。
- 一行为什么这样排版的解释（让用户理解布局逻辑）。
- 若用户要求，附一份"以后怎么自己改"的简要指南。

---

## 来源

原创 Skill，为 skygazer42-skills 专门编写。
