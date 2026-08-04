# Requesting Code Review（请求代码审查）

## 一句话定位

完成任务或合并前，派发代码审查子代理验证工作正确性。通用审查后路由到领域审查 Skill 做深度检查。

## 适用场景

- 每个 task 完成后（subagent-driven 模式）。
- 大功能完成后。
- 合并到 main 之前。

## 不适用场景

- 审查本身由领域 Skill 处理时（`web.frontend-review` / `backend.backend-review`），本 Skill 做请求的**编排和路由**。
- 收到审查反馈之后——用 `engineering.receiving-code-review`。

## 执行流程

1. 获取 BASE/HEAD SHA。
2. 构造审查上下文（做了什么、应该做什么）。
3. 派发通用审查子代理。
4. 按严重度处理反馈。
5. 按领域路由到 web.frontend-review 或 backend.backend-review 做深度审查。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。
