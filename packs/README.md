# Skill Packs

每个 Pack 位于 `packs/<pack-name>/`，只包含说明文件和 `pack.yaml`，不复制 Skill 内容。

```yaml
schema_version: 1

id: pack.software-engineering
name: Software Engineering
version: 1.0.0
description: Skills for software engineering work.

skills:
  - id: engineering.review-pull-request
    version: ">=1.0.0 <2.0.0"
```
