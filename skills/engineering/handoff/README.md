# Agent Handoff（会话交接）

## 一句话定位

将当前对话压缩为交接文档，供另一个 Agent 继续工作。包含建议 Skill、已完成工作摘要和关键上下文。

## 适用场景

- 当前会话工作量大，需拆分到多个 Agent 并行处理
- 需要把当前进度移交给另一个 Agent 继续
- 跨会话的长期任务需要状态保留

## 不适用场景

- 简单的一次性任务
- 已经有完整 specs/plans/ADRs/issues 记录的工作（直接引用这些制品即可）

## 执行前需要的信息

- 下一会话的用途描述
- 当前已完成的工作和待办事项

## 执行流程

1. 总结当前对话的关键决策和状态
2. 列出建议的 Skill 清单
3. 引用已有制品（specs/plans/ADRs/issues）
4. 脱敏（移除 API 密钥、密码等）
5. 保存到用户 OS 临时目录

## 交付结果

- 交接文档（Markdown）

## 默认边界

- **读文件**：是
- **写文件**：是
- **执行命令**：否
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.finishing-a-development-branch` | 功能分支完结流程，本 Skill 是会话级交接 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [mattpocock/skills](https://github.com/mattpocock/skills) 的 `handoff`（MIT License），做本仓适配。