---
name: writing-skills
description: Use when creating new skills, editing existing skills, or verifying skills work before deployment
---

# 写 Skill

## 概述

**写 Skill 就是把 TDD 应用于流程文档。**

先用子代理运行压力场景（基线），看它们没 Skill 时怎么做；再写 Skill；再看它们是否遵守；最后堵漏洞（重构）。

**核心原则：**没见过代理没 Skill 时失败的样子，就不知道这个 Skill 教的东西对不对。

**必备背景：**必须理解 `engineering.test-driven-development` 再读本 Skill。

## Skill 是什么

Skill 是经过验证的技术、模式或工具的参考指南。Skill **是**可复用技术/模式/工具/参考指南。Skill **不是**关于你某次解决问题的叙事。

## 何时创建 Skill

**创建：**技术对你不是直觉、你会跨项目引用、模式有广泛适用性、别人也会受益。

**不创建：**一次性方案、别处已充分记录的标准实践、项目专属规范（放 instructions 文件）、机械化约束（可用 regex/校验自动化就自动化——文档留给判断难题）。

## 目录结构

```
skills/<category>/<skill-name>/
  SKILL.md              # 主体参考（必需）
  附属文件               # 仅在需要时
```

按本仓规范（`AGENTS.md` §4），正式 Skill 还需 `manifest.yaml`、`README.md`、`provenance.yaml`、`tests/cases.yaml`。

## SKILL.md 结构

- YAML frontmatter（必需：`name`、`description`；description 用 "Use when..." 开头，只描述触发条件，**绝不**总结 Skill 流程）。
- `## 概述`：核心原则 1-2 句。
- `## 何时使用`：症状和场景清单，何时不用。
- `## 核心模式`（技术/模式类）：执行前后对比。
- `## 快速参考`：扫描用表格。
- `## 常见错误`：什么问题 + 怎么修。

## 反模式

- ❌ 叙事性案例（"在 2025-10-03 的 session 中我们发现..."）→ 太具体，不可复用。
- ❌ 多语言稀释 → 一个优秀示例足矣。
- ❌ 流程图里放代码 → 不可复制粘贴。

## TDD for Skills: RED-GREEN-REFACTOR

- **RED**：无 Skill 跑压力场景，记录代理的精确行为和合理化借口。
- **GREEN**：写刚好解决那些具体问题的 Skill。
- **REFACTOR**：代理找到新合理化借口？加显式反驳。重新测试直到无懈可击。

**铁律：没有先跑失败测试，不写任何 Skill。**

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：目录结构适配本仓两层规范；Skill 引用改为 engineering.*；翻译精简；附加入库规范（manifest/README/provenance/cases）。
