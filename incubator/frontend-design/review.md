# Frontend Design 审核报告

> 审核日期：2026-08-04
> 来源：`incubator/frontend-design/source.yaml`
> 审核人：skygazer42（Agent 辅助）

## 一、概况

`anthropics/skills` 的 `frontend-design`，Anthropic 官方设计 Skill，生态安装量第一（约 277K）。核心理念：像小工作室的设计主管一样，拒绝模板化默认，给每个 brief 一个独一无二、无法与他人混淆的视觉身份。

原文 55 行，密集但完整。无附属脚本、无网络依赖。Apache 2.0 许可。

## 二、检查（AGENTS.md §8.2）

| 检查项 | 结论 |
| --- | --- |
| 解决真实工作流问题 | ✅ 是——本仓最缺「做出好看的 UI」。现有 `web.frontend-implementation` 管功能和无障碍，不管审美 |
| 与现有 Skill 重复 | ⚠️ 与 `web.frontend-implementation` 相邻但不重复——design 管视觉方向和审美，implementation 管功能落地和正确性。需在 README 明确边界 |
| 隐式提交/推送/删除 | ✅ 无 |
| 密钥/隐私/内部地址 | ✅ 无 |
| 下载执行远程脚本 | ✅ 无 |
| 网络行为/遥测 | ✅ 无 |
| 平台绑定 | ✅ 平台中立（提到"截图如果环境支持"，可选降级） |
| 强制署名/外链/上传 | ✅ 无 |
| License 允许复制修改 | ✅ Apache 2.0——允许，但需保留 LICENSE 和版权声明 |

## 三、规范化决策

1. **分类**：`web`（前端设计）。ID `web.frontend-design`。
2. **中文化**：正文译为中文，保留关键设计术语首现英文（hero / signature / display face 等）和 hex 值示例。
3. **注入本仓上下文**：新增与 `web.frontend-implementation` 的边界说明和路由——设计方向定了之后，交给 implementation 落地。
4. **License 保留**：Apache 2.0 要求保留声明，`LICENSE.txt` 随 Skill 一起保存，`provenance.yaml` 记录 `identifier: Apache-2.0` / `file: LICENSE.txt`。
5. **权限**：读文件、写文件（生成 UI 代码）、执行命令（可选截图预览）。

## 四、状态

**审核通过。** 已规范化到 `skills/web/frontend-design/`。
