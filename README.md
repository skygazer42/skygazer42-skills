# skygazer42-skills

个人与团队共用的 AI Skill 主仓库。候选 Skill 先进入孵化区，经过来源核验、整理和测试后，才能成为正式能力。

## 目录

- `skills/`：已审核、可以依赖的正式 Skill
- `packs/`：只引用 Skill 的能力组合包
- `incubator/`：尚未审核的外部候选
- `templates/`：新建 Skill 的统一模板
- `tools/`：注册表生成和仓库校验工具
- `registry.yaml`：由 Manifest 自动生成的索引

## 生命周期

```text
Discover -> Incubator -> Review -> Normalize -> Test -> Publish -> Package
```

## 规则

1. 一个 Skill 对应一个目录，并拥有全仓唯一且稳定的 ID。
2. 外部 Skill 必须记录仓库、精确 revision、原路径和 License。
3. 未完成审核的内容不得进入 `skills/`。
4. Pack 只保存 Skill 引用，不复制 `SKILL.md`。
5. 权限和依赖必须在 `manifest.yaml` 中显式声明。
6. 密钥、本机路径和生成产物不得提交。

## 开始使用

```bash
python -m pip install -r requirements.txt
python tools/validate_repository.py
python tools/build_registry.py --check
```

创建 Skill 时复制 `templates/skill/`，填写所有占位内容，再放入 `skills/<category>/<skill-name>/`。修改 Manifest 或 Pack 后运行：

```bash
python tools/build_registry.py
python tools/validate_repository.py
```

候选 Skill 的目录格式和审核要求见 [`incubator/README.md`](incubator/README.md)，Pack 格式见 [`packs/README.md`](packs/README.md)。
