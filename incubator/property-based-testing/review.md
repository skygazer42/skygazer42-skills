# 审核：property-based-testing（trailofbits/skills）

## 概况

| 项 | 值 |
| --- | --- |
| 来源仓库 | https://github.com/trailofbits/skills |
| 固定 revision | `e6066e7db1fd57cb35f9a534781ceec595327feb`（克隆 HEAD 已核对一致） |
| 原路径 | `plugins/property-based-testing/skills/property-based-testing/` |
| 许可证 | CC-BY-SA-4.0（仓库顶层 LICENSE 全文随副本保留） |
| 作者 | Trail of Bits |
| 建议 skill 名 | `engineering.property-based-testing` |
| 版本/状态 | `0.1.0` / `beta` |

## 检查表（§8.2）

| 检查项 | 结论 | 说明 |
| --- | --- | --- |
| 解决个人工作流真实问题 | ✅ | 序列化/解析/规范化/校验/纯函数/智能合约场景下，生成式测试比示例测试覆盖面更强，是本仓工程测试能力的缺口 |
| 与现有 Skill 重复 | ⚠️ 不重复 | `engineering.test-driven-development` 管理开发节奏（Red-Green-Refactor）；本 Skill 只判定「哪些属性值得用生成式数据验证」，职责划分清晰 |
| 隐式提交/推送/发消息/PR/发布/删除/生产写入 | ✅ 无 | 只生成测试代码与运行 pytest 等测试命令，无任何外部副作用 |
| 读取/输出密钥、个人数据、内部地址、敏感日志 | ✅ 无 | 只读被测源码与测试 |
| 下载执行远程脚本/未声明网络/遥测 | ✅ 无 | `network: false` |
| 脚本读写路径/命令/失败安全性 | ✅ 安全 | 只建议 `pytest`、`rg`、`pip install hypothesis` 等测试侧命令 |
| 绑定单一平台/未装工具/专属 Skill/不存在的环境变量 | ✅ 无 | 库参考覆盖 Python/JS/Rust/Go/Java/Scala/C#/Elixir/Haskell/Clojure/Ruby/Kotlin/Swift/C++；工具依赖为可选 |
| 强制署名/外链/上传案例/对外创建状态 | ✅ 无 | 不强制任何对外动作 |
| License 允许复制修改 + 版权声明随副本 | ✅ | CC-BY-SA-4.0：保留署名 + 相同方式共享；本仓以同许可保留 LICENSE.txt |
| README 宣传是否由指令支撑 | ✅ | 检测模式、属性目录、决策树、库参考均有实体文件支撑 |

## 规范化决策

1. **保留**：SKILL.md 核心（检测模式、属性目录、决策树、PBT 建议话术、红旗清单）+ 7 个 references 文件（design/generating/interpreting-failures/libraries/refactoring/reviewing/strategies）。
2. **移除**：
   - `agents/openai.yaml`（平台图标/品牌色配置，非行为内容）。
   - `assets/trail-of-bits-mark.svg`（上游品牌资产，非执行所需）。
   - README 中「Claude 激活」等平台专属描述改写为通用表述。
3. **改写**：SKILL.md 中 `{baseDir}` 相对引用在本仓布局下改为 `references/<file>.md`；`name` frontmatter 保留 `property-based-testing`；补中文说明。
4. **中文化**：SKILL.md 主体翻译为中文并精简；references 保留英文原义（术语密集，避免翻译失真）——按 writing-skills 的先例（原版附属文件移入 references/ 保留英文）。
5. **许可证**：CC-BY-SA-4.0 全文 `LICENSE.txt` 随正式 Skill 保存；provenance 记录 identifier `CC-BY-SA-4.0` + file `LICENSE.txt`。
6. **权限**：`network: false`、`read_files: true`、`write_files: true`（生成测试文件）、`execute_commands: true`（pytest 等）。
7. **依赖**：无本仓 skill 依赖；commands 空（库按语言可选）。

## 状态

✅ 审核通过，可以规范化发布为 `engineering.property-based-testing@0.1.0-beta`。
