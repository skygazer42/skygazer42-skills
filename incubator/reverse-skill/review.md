# Review: reverse-skill

## 结论

**部分内化**。上游是大型安全/逆向/CTF 技能集合（515 文件 / 84 SKILL.md / 40+ 模块），
按仓库所有者要求只选定 6 个核心自包含模块，固化为候选。晋级到 `skills/` 前仍需逐模块规范化。

## 保留理由

- 覆盖个人工作流中真实存在的授权逆向 / 移动 / 恶意样本 / API 审计需求。
- 与现有仓库能力（web/backend/engineering/design）互补，无重叠。
- 模块自包含度高：核心逻辑都在 `SKILL.md` + `references/`，无强制重型平台依赖。

## 纳入的模块

| 模块 | 说明 | 状态 |
| --- | --- | --- |
| reverse-engineering | 通用逆向 + dsl-vm 子模块 | 核心 |
| apk-reverse | Android APK 逆向（jadx/frida/重打包） | 核心 |
| mobile-reverse | Android+iOS 动态插桩、MAS test | 核心 |
| malware-analysis | 样本分析、YARA/Sigma、沙箱 | 核心 |
| api-security | REST/GraphQL/WebSocket 协议安全 | 核心 |
| code-audit | 源码白盒审计（Semgrep/CodeQL） | 核心 |

另保留最小共享运行时：`field-journal/`（案例库）、`ops/`（scope/证据链契约）、
`references/`、`MASTER-ROUTING.md`、`routing.md`、`LICENSE`。

## 未纳入（有意省略）

- `CTF-Sandbox-Orchestrator/`（41 个 CTF 子技能 + 总控编排，规模过大）
- `kali/`、`burp-mcp-full/`、`ida-reverse`（重型平台 / MCP 依赖）
- `attack-chain`、`pwn-chain`、`edr-bypass-re`、`patch-diff-exploit`（偏攻击侧，超出本次授权研究范围）
- `docs/reports/scripts` 等辅助目录

## 安全与 License 检查

- **License**：MIT（Copyright c 2026 zhaoxuya520），允许复制、修改、再分发；LICENSE 已随候选保留。
- **授权门闩**：`ops/scope-contract.md` 要求 auth 未 granted 禁止对目标 ACT；`field-journal` 记录授权先例。
- **网络行为**：核心模块以本地工具（gdb/frida/jadx/semgrep 等）为主；`tool-index.md` 为模板，未内嵌自动下载执行远程脚本。
- **敏感数据**：`api-security` 中 `../../etc/passwd` 为文本示例（路径穿越测试用例），非真实加载。
- **无隐式对外写操作**：未发现提交/推送/发布/发消息等隐式外部状态修改。

## 需要修改的内容（晋级前）

1. **断链**：`apk-reverse/scripts/*.sh` 引用 `../../../kali/scripts/bootstrap-reverse.sh`（未纳入）；
   `reverse-engineering/languages-compiled.md` 引用 `../dotnet-reverse/`（未纳入）。需中立化或补对应依赖说明。
2. **契约补全**：按 `templates/skill/` 为每个模块补 `manifest.yaml`、中文 `README.md`、`provenance.yaml`、`tests/cases.yaml`。
3. **权限申明**：按第 9 节逐模块书写最坏路径权限，不全部置 true。
4. **命名/分类**：映射到本仓库分类（建议 `security.*` 或 `reverse-engineering.*`），ID=分类=物理目录名对齐。
5. **脚本平台**：`*.ps1` 为 Windows 优先，需在 README 标注或提供降级说明。

## 处理结果

当前状态：**孵化候选**。已固化 source.yaml + candidate。晋级 `skills/` 需仓库所有者确认后逐模块规范化。
本候选未进入 `registry.yaml`（孵化区不参与索引）。