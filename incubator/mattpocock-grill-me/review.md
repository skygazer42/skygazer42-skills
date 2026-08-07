# Review: grill-me (from mattpocock/skills)

## 结论

**保留并晋级，但需要改写适配本仓。**

上游 `grill-me` 本身是极薄的触发器（SKILL.md 仅 8 行：「Run a `/grilling` session」），其价值在于**概念定位**而非实现内容：

- **stateless**：不写文件、不留工作区，一次对话结束后只在用户脑子里留下更清晰的方案。
- **user-invoked only**：Agent 不会自动调用，用户通过 `/grill-me` 主动发起。
- **any subject**：不只是代码——业务决策、写作、产品方向都可以 grill。
- **fresh conversation**：在一个干净的对话中开始，不给 Agent 预判上下文。

这些概念区别于本仓已有的 `engineering.grilling`：
- `engineering.grilling` 是**执行引擎**（grilling 协议实现）
- `grill-me` 是**用户入口**（stateless / no-repo / any-subject 的"前门"）

## 保留理由

- **补齐用户入口**：`engineering.grilling` 已经是成熟的 grilling 引擎，但缺少一个显式的、无状态、无仓库依赖的用户入口。grill-me 填补这个空白。
- **概念区分**：grill-me 的「stateless / any subject / fresh conversation / grillable vs ungrillable」概念在本仓 grilling 中未充分体现。
- **与现有 Skill 不重复**：grill-me 路由到 `engineering.grilling` 执行实际 grilling 协议，自己只负责入口定位和边界说明。

## 安全与 License 检查

- **License**：MIT（Copyright 2026 Matt Pocock），允许复制、修改、再分发。
- **无网络/命令执行**：纯对话 Skill，不写文件、不执行命令、不访问网络。
- **已设置 `disable-model-invocation`**：Agent 不会自动触发，只有用户显式调用。

## 本地改写要点

1. **上游 SKILL.md 太薄**（仅 8 行），需注入本仓上下文：路由到 `engineering.grilling`、说明 stateless/any-subject/fresh-conversation 定位。
2. **从上游 `docs/productivity/grill-me.md` 提取关键概念**：前端决策、grillable vs ungrillable、什么时候停、失败模式。
3. **与 `engineering.grilling` 建立清晰的路由关系**：grill-me 是入口，grilling 是引擎。

## 处理结果

**已晋级为 `skills/engineering/grill-me/`。**