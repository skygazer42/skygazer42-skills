# Writing Skills（写 Skill）

## 一句话定位

用 TDD 方法论创建和验证 Skill——先跑代理在没有 Skill 时的基线行为（RED），再写 Skill（GREEN），再堵漏洞（REFACTOR）。

## 适用场景

- 创建一个新的 Skill。
- 编辑现有 Skill 的行为。
- 部署前验证 Skill 是否真的有效。

## 不适用场景

- 纯文档修正（不改行为）——可直接改，但改了行为就必须走 TDD。
- 简单的一次性脚本——不需要 Skill。
- 机械化约束——用自动化校验，别用 Skill。

## 执行流程

1. RED：无 Skill 跑压力场景，记录精确基线行为。
2. GREEN：写刚好解决那些具体问题的 Skill。
3. REFACTOR：代理找到新合理化借口？加显式反驳。重新测试。
4. 按本仓规范补齐 5 件套（manifest/provenance/README/cases）。
5. 部署前完成检查表。

## 交付结果

- 完整的 5 件套 Skill（SKILL.md + manifest + README + provenance + cases）。
- TDD 测试证据（基线 → 遵从）。
- 合理化借口表和 Red Flags 清单（discipline 类 Skill）。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。
