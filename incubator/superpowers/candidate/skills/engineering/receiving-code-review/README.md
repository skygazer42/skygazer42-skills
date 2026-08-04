# Receiving Code Review（接收代码审查）

## 一句话定位

收到审查反馈后，先验证再实现。技术正确性优先，不表演同意，不盲从建议。

## 适用场景

- 收到来自用户或外部审查者的代码审查反馈。
- 反馈中有你不确定或认为技术上不正确的条目。
- 多条目反馈需要先理清再逐条实现。

## 不适用场景

- 请求审查——用 `engineering.requesting-code-review`。
- 实现新功能——走 `engineering.brainstorming` → `engineering.writing-plans`。

## 执行流程

1. 完整读反馈，不立即反应。
2. 用自己的话重述每个需求。
3. 对照代码库实际情况验证每条。
4. 技术上评估——对当前代码库真的正确吗？
5. 回应——技术确认或有理有据反驳。
6. 逐条实现，每条跑测试。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。
