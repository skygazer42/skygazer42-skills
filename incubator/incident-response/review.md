# 审核：incident-response（anthropics/knowledge-work-plugins）

## 概况

| 项 | 值 |
| --- | --- |
| 来源仓库 | https://github.com/anthropics/knowledge-work-plugins |
| 固定 revision | `2cf42948f0b79c5492bb38981752b815fc6788ec`（克隆 HEAD 已核对一致） |
| 原路径 | `engineering/skills/incident-response/` |
| 许可证 | Apache-2.0（212 行原文中 203-212 行含非标准附加文本，按 202 行标准文本裁剪随副本保留） |
| 作者 | anthropics |
| 建议 skill 名 | `operations.incident-response` |
| 版本/状态 | `0.1.0` / `beta` |

## 检查表（§8.2）

| 检查项 | 结论 | 说明 |
| --- | --- | --- |
| 解决个人工作流真实问题 | ✅ | 生产事故从检测到复盘的全生命周期管理（triage/沟通/缓解/复盘），是运维侧真实缺口 |
| 与现有 Skill 重复 | ⚠️ 不重复 | `backend.backend-debugging` 定位代码根因、影响范围与修复建议；本 Skill 管理整个生产事故生命周期（严重级别/影响/时间线/缓解验证/状态草稿/无责备复盘），并新增 `operations` 分类 |
| 隐式提交/推送/发消息/PR/发布/删除/生产写入 | ⚠️ 需改写 | 原文「If Connectors Available」含 ~~monitoring/~~incident management（PagerDuty/Opsgenie paging）/~~chat 自动写入分支 → 全部移除，外部通知只生成草稿 |
| 读取/输出密钥、个人数据、内部地址、敏感日志 | ✅ 无 | 只处理用户提供的事故描述与证据 |
| 下载执行远程脚本/未声明网络/遥测 | ✅ 无 | `network: false` |
| 脚本读写路径/命令/失败安全性 | ✅ 安全 | 只读证据文件，写复盘文档草稿，运行只读诊断命令 |
| 绑定单一平台/未装工具/专属 Skill/不存在的环境变量 | ✅ 无 | 无平台绑定，无必需外部工具 |
| 强制署名/外链/上传案例/对外创建状态 | ✅ 无 | 不强制任何对外动作 |
| License 允许复制修改 + 版权声明随副本 | ✅ | Apache-2.0 允许复制修改，保留许可证全文随副本 |
| README 宣传是否由指令支撑 | ✅ | 严重级别/沟通/输出模板均有 SKILL.md 支撑 |

## 规范化决策

1. **保留**：四阶段流程（Triage/Communicate/Mitigate/Postmortem）、SEV1-4 严重级别分类、沟通指导、状态更新模板、复盘模板、5 Whys、无责备原则、Tips。
2. **移除**：
   - 「If Connectors Available」整节（PagerDuty/Opsgenie paging、聊天频道/战情室、监控拉取自动写入）。
   - 顶部 CONNECTORS.md 指引行。
   - `/incident-response` 斜杠命令格式改为通用「模式」表述。
3. **改写**：外部通知一律只生成**草稿**，不自动发送；重启/回滚/部署/paging/发消息等动作需**分别独立授权**。
4. **事实边界**：不依据模糊描述编造影响人数、根因、恢复时间或责任人；证据不足时明确标注「未知」，并给出下一步取证动作。
5. **中文化**：SKILL.md 主体翻译为中文并精简，按本仓惯例补 5 件套。
6. **许可证**：Apache-2.0 全文（202 行标准文本）`LICENSE.txt` 随正式 Skill 保存。
7. **权限**：`network: false`、`read_files: true`、`write_files: false`（复盘文档草稿由用户落盘）、`execute_commands: true`（只读诊断命令）。
8. **依赖**：无本仓 skill 依赖，无必需命令。

## 状态

✅ 审核通过，可以规范化发布为 `operations.incident-response@0.1.0-beta`。
