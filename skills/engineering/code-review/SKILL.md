---
name: code-review
description: Use when completing tasks, implementing major features, before merging, or when receiving code review feedback — covers both requesting review and handling feedback
---

# 代码审查

两阶段——请求审查和接收反馈。早审查，常审查。

## 阶段 1：请求审查

完成任务、实现大功能或合并前，派发审查子代理验证工作正确性。

**强制：**每次 task 完成后、大功能完成后、合并到 main 之前。卡住时（新鲜视角）、重构前（基线检查）也推荐用。

**流程：**
1. 获取 BASE/HEAD SHA。
2. 构造审查上下文——做了什么、应该做什么。
3. 派发通用审查子代理。
4. 按严重度处理反馈：Critical → 立即修、Important → 继续前修、Minor → 标记后续。

**路由到领域审查：**通用审查后，按领域补深度审查——前端用 `web.frontend-review`、后端用 `backend.backend-review`。

## 阶段 2：接收反馈

收到审查反馈后，先验证再实现。技术正确优先，不表演同意，不盲从。

**响应模式：**完整读反馈 → 用自己的话重述 → 对照代码库验证 → 技术上评估 → 确认或反驳 → 逐条实现（每条跑测试）。

**禁止：**表演性同意（"你说得对！"、"好观点！"）、验证前实现、盲从技术上错的建议。

**何时反驳：**建议破坏现有功能、审查者缺完整上下文、违反 YAGNI、对技术栈不正确、有兼容性原因、与既有架构决策冲突。用技术推理和可运行代码反驳，涉及架构时让用户参与。

**不清晰时：**先问清再实现。"理解和做懂的、不懂的以后再问"= 错的——一次问清所有不清晰项。

## 快速参考

| 来源 | 处理 |
| --- | --- |
| 用户反馈 | 信任——理解后实现。范围不清时仍问 |
| 外部审查者 | 检查：对代码库正确？破坏现有功能？当前实现有原因？跨平台可行？审查者理解完整上下文？ |

---

## 来源与改造说明

合并自 [obra/superpowers](https://github.com/obra/superpowers) 的 `requesting-code-review` + `receiving-code-review`（MIT License）。改造：合并为一个 skill 的两个阶段；新增领域审查路由。
