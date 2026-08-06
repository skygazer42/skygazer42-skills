# Workflow Runner（工作流执行器）

## 一句话定位

在 Claude Code / Codex / Cursor 中直接运行 YAML 工作流——无需 API key，使用当前会话的 LLM 作为执行引擎。

## 适用场景

- 用户提供 .yaml 工作流文件
- 要求多角色协作完成任务
- 需要结构化的多步骤 Agent 编排

## 不适用场景

- 简单的单步任务
- 已有 subagent-driven-development 覆盖的并行代理场景

## 执行前需要的信息

- YAML 工作流定义文件
- 任务上下文

## 交付结果

- 工作流执行结果

## 默认边界

- **读文件**：是
- **写文件**：否
- **执行命令**：否
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.subagent-driven-development` | 子代理驱动开发，本 Skill 是 YAML 工作流编排 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)（MIT License），做本仓适配。