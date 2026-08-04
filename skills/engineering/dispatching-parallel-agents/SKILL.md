---
name: dispatching-parallel-agents
description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
---

# 派发并行代理

## 概述

把独立任务委派给拥有隔离上下文的专用代理。通过精确 crafting 指令和上下文，确保它们聚焦并成功完成任务。它们不应继承你 session 的上下文或历史——你只构造它们需要的。这也保护你自己的上下文用于协调工作。

**核心原则：**每个独立问题领域派一个代理。让它们并发工作。

## 何时使用

- 3+ 测试文件失败，根因各不相同
- 多个子系统独立损坏
- 每个问题可以在不理解其他问题上下文的情况下被理解
- 调查之间无共享状态

**不要用时：**失败相关（修一个可能修全部）、需要完整系统全貌、代理会互相干扰。

## 模式

### 1. 识别独立领域

按问题所在分组——各自独立，领域互不干扰。

### 2. 创建聚焦的代理任务

每个代理得到：**具体范围**（一个测试文件或子系统）、**清晰目标**、**约束**（不改其他代码）、**预期输出**（发现了什么、修了什么）。

### 3. 并行派发

在同一响应中发出所有子代理派发——它们并行运行。同一响应中多个 dispatch = 并行。一次一个 = 串行。

### 4. 审查和集成

代理返回后：读每个摘要、核实修复不冲突、跑完整测试套件、集成所有变更。

## 与领域 Skill 的关系

并行派发的是**工作单元**。每个工作单元完成后，根据领域可能需要：

| 问题领域 | 后续步骤 |
| --- | --- |
| 前端测试/UI 问题 | `web.frontend-testing` 验证 |
| 前端代码问题 | `web.frontend-review` 审查 |
| 后端 API/数据问题 | `backend.backend-debugging` 诊断 |
| 后端代码问题 | `backend.backend-review` 审查 |

并行代理是**编排模式**；领域 Skill 是**执行能力**。派发时把领域 Skill 知识注入代理 prompt。

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：新增领域 Skill 路由映射。
