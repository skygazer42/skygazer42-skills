# Incubator

从外部发现的 Skill 必须先进入 `incubator/<candidate-name>/`：

```text
<candidate-name>/
├── source.yaml
├── review.md
└── candidate/
```

`source.yaml` 至少记录：

```yaml
repository: "<source-repository-url>"
revision: "<exact-commit-or-release>"
path: "<source-path>"
license: "<license-identifier>"
captured_at: "<YYYY-MM-DD>"
```

`review.md` 应说明保留理由、需要修改的内容、安全与 License 检查，以及最终处理结果。审核通过后再按 `templates/skill/` 规范化到 `skills/`。
