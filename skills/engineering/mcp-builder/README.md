# MCP Server Builder（MCP 服务器构建）

## 一句话定位

MCP 服务器构建方法论——系统化构建生产级 MCP 工具，让 AI 助手连接外部能力。

## 适用场景

- 构建新的 MCP 服务器
- 为 AI 助手添加外部工具/API 集成
- 设计 MCP 工具接口

## 不适用场景

- 使用已有 MCP 工具（直接调用即可）
- 非 MCP 协议的 API 集成

## 执行前需要的信息

- 需要暴露给 AI 的能力/API
- 目标平台（Claude Code/Codex/Cursor 等）

## 交付结果

- 可运行的 MCP 服务器代码

## 默认边界

- **读文件**：是
- **写文件**：是
- **执行命令**：是
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.writing-skills` | 写 SKILL.md，本 Skill 是写 MCP 服务器 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)（MIT License），做本仓适配。