---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.


---

## 来源与改造说明

本 Skill 基于 [mattpocock/skills](https://github.com/mattpocock/skills)（MIT License，commit `8b36d4f`），本地改造：

1. 上游 SKILL.md 原文完整保留，仅末尾追加本节。
2. 按本仓库目录契约补充 manifest.yaml、中文 README.md、provenance.yaml、tests/cases.yaml。
3. 归入 `engineering` 分类，与现有工程流程 Skill 互补。
