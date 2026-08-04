---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
---

# 请求代码审查

派发一个代码审查子代理，在问题放大之前抓住它们。审查者拿到的是精确构造的评估上下文——不是你 session 的历史。

**核心原则：早审查，常审查。**

## 何时请求审查

**强制：**每次完成 task 后（subagent-driven 模式）、完成大功能后、合并到 main 之前。

**可选但有价值：**卡住时（新鲜视角）、重构前（基线检查）、修完复杂 bug 后。

## 如何请求

1. 获取 git SHAs（BASE_SHA、HEAD_SHA）。
2. 派发审查子代理，填入描述（你做了什么）、计划/需求（应该做什么）、base/head SHA。
3. 处理反馈：Critical → 立即修；Important → 继续前修；Minor → 标记后续处理。

## 路由到领域审查 Skill

| 审查领域 | 应路由到的 Skill |
| --- | --- |
| 前端代码（UI/交互/组件/无障碍） | `web.frontend-review` |
| 后端代码（API/服务/数据库/安全） | `backend.backend-review` |

代码审查子代理做**通用的正确性和质量审查**；领域审查 Skill 做**领域专属检查**（无障碍、安全、并发、数据完整性）。两者互补——通用审查先过，领域审查覆盖盲区。

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：新增「路由到领域审查 Skill」节；Skill 引用中立化。
