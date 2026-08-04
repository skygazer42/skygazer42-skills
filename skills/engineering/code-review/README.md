# Code Review（代码审查）

## 一句话定位

完成任务或合并前请求代码审查；收到审查反馈后先验证再实现。早审查，常审查。

## 适用场景

- 每个 task 完成后。
- 大功能完成后。
- 合并到 main 之前。
- 收到审查反馈后需要严谨处理。

## 不适用场景

- 领域深度审查——通用审查后路由到 `web.frontend-review` 或 `backend.backend-review`。
- 实现新功能——先走 `engineering.brainstorming`。

## 执行流程

**请求审查：**获取 SHA → 构造上下文 → 派发审查子代理 → 按严重度处理 → 路由领域审查。

**接收反馈：**读 → 理解 → 验证 → 评估 → 回应 → 逐条实现。

## 默认边界

- **读文件**：是。
- **写文件**：否（审查不改代码）。
- **执行命令**：是（跑测试、获取 git SHA）。
- **网络**：否。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：合并自 [obra/superpowers](https://github.com/obra/superpowers) 的 `requesting-code-review` + `receiving-code-review`（MIT License）。
