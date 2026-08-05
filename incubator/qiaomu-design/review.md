# Qiaomu Design 审核报告

> 审核日期：2026-08-05 · 来源 MIT，作者 joeseesun · commit 39dac82

## 定位

大而全的"偏执型设计顾问"：三拨盘（VARIANCE/MOTION/DENSITY）自适应 + 三阶段工作流
（诊断→四方向预览→执行）+ 融合多套设计 skill 精华 + 58 个 DESIGN.md 参考库。

## 与本仓三件套的关系

它实质是 frontend-design/interface-design/enterprise-design 的超集且更深，
但组织哲学不同（一个 skill + 拨盘 vs 三个按场景切分的 skill）。

## 决策（按仓库所有者原则：不下线、外部不主导、一个场景不重复、选择性吸收互补）

| qiaomu 内容 | 处理 | 理由 |
| --- | --- | --- |
| 动效工艺（motion-craft/animation-vocabulary/apple-fluid-interfaces/motion-review） | ✅ 吸收进 frontend-design/references | 本仓完全缺、跨场景、不冲突 |
| 中文排版（chinese-typography） | ✅ 吸收进 frontend-design/references | 本仓缺 |
| 三拨盘替换机制、三阶段工作流、"设计顾问"人格 | ❌ 不吸收 | 会与三件套 + brainstorming 冲突、喧宾夺主 |
| Carbon 定位 | ❌ 不吸收 | enterprise-design 已对标 |
| AI 反套路 | ❌ 不吸收 | frontend-design 已有 |
| 58 DESIGN.md 参考库 | ⏸ 暂缓 | 大资产，后续按需再议 |

## 状态

未新建 qiaomu skill、未下线任何现有 skill。仅把动效工艺 + 中文排版作为 references
融入 frontend-design，并在 interface/enterprise-design 加引用。
