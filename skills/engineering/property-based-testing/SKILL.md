---
name: property-based-testing
description: 属性化测试（Property-Based Testing）指导——多语言与智能合约。在写测试、审查含序列化/校验/解析模式或设计新功能时，属性化测试能比示例测试提供更强覆盖时使用。
---

# 属性化测试（Property-Based Testing）

用生成式数据验证被测代码的**属性**（roundtrip、幂等、不变量、交换律、结合律、逆操作、参考实现对照、状态机不变量），而不是只验证几个手写示例。适合序列化/解析/规范化/校验/纯函数/智能合约等输入域复杂或代数性质清晰的场景。

## 何时使用（自动触发检测）

**检测到以下模式时主动建议本 Skill：**

- **序列化对**：`encode`/`decode`、`serialize`/`deserialize`、`toJSON`/`fromJSON`、`pack`/`unpack`
- **解析器**：URL 解析、配置解析、协议解析、字符串→结构化数据
- **规范化**：`normalize`、`sanitize`、`clean`、`canonicalize`、`format`
- **校验器**：`is_valid`、`validate`、`check_*`（尤其配合规范化器）
- **数据结构**：带 `add`/`remove`/`get` 操作的自定义集合
- **数学/算法**：纯函数、排序、有序比较、比较器
- **智能合约**：Solidity/Vyper 合约、代币操作、状态不变量、访问控制

**按模式优先级：**

| 模式 | 属性 | 优先级 |
| --- | --- | --- |
| encode/decode 对 | Roundtrip | 高 |
| 纯函数 | 多个 | 高 |
| 校验器 | normalize 后有效 | 中 |
| 排序/有序 | 幂等 + 有序 | 中 |
| 规范化 | 幂等 | 中 |
| Builder/工厂 | 输出不变量 | 低 |
| 智能合约 | 状态不变量 | 高 |

## 何时不用

不要对以下情况使用本 Skill：

- 无变换逻辑的简单 CRUD
- 一次性脚本或即弃代码
- 无法隔离副作用（网络调用、数据库写入）的代码
- 具体示例已足够、边界情况已清楚掌握的测试
- 集成或端到端测试（PBT 最适合单元/组件级测试）

## 属性目录（速查）

| 属性 | 公式 | 适用 |
| --- | --- | --- |
| **Roundtrip** | `decode(encode(x)) == x` | 序列化、转换对 |
| **幂等（Idempotence）** | `f(f(x)) == f(x)` | 规范化、格式化、排序 |
| **不变量（Invariant）** | 变换前后性质不变 | 任何变换 |
| **交换律（Commutativity）** | `f(a, b) == f(b, a)` | 二元/集合运算 |
| **结合律（Associativity）** | `f(f(a,b), c) == f(a, f(b,c))` | 组合运算 |
| **单位元（Identity）** | `f(x, identity) == x` | 有中性元的运算 |
| **逆操作（Inverse）** | `f(g(x)) == x` | 加密/解密、压缩/解压 |
| **参考实现（Oracle）** | `new_impl(x) == reference(x)` | 优化、重构 |
| **易验证（Easy to Verify）** | `is_sorted(sort(x))` | 复杂算法 |
| **不抛异常（No Exception）** | 合法输入不崩溃 | 基线属性 |

**强度层级**（弱到强）：不抛异常 → 类型保持 → 不变量 → 幂等 → Roundtrip

## 决策树

按当前任务读取对应 reference：

- 写新测试 → [`references/generating.md`](references/generating.md)（生成模式与示例），输入生成复杂时再读 [`references/strategies.md`](references/strategies.md)
- 设计新功能 → [`references/design.md`](references/design.md)（Property-Driven Development）
- 代码难测（I/O 混杂、缺逆操作）→ [`references/refactoring.md`](references/refactoring.md)
- 审查已有 PBT 测试 → [`references/reviewing.md`](references/reviewing.md)
- 测试失败需解读 → [`references/interpreting-failures.md`](references/interpreting-failures.md)
- 需要按语言的库参考 → [`references/libraries.md`](references/libraries.md)

## 如何建议使用 PBT

检测到高价值模式时，把 PBT 作为**选项**提出：

> 「我注意到 `encode_message`/`decode_message` 是序列化对。用 roundtrip 属性的属性化测试比示例测试覆盖更强。要用这个方式吗？」

**若代码库已用 PBT 库**（Hypothesis、fast-check、proptest、Echidna），更直接：

> 「这个代码库用 Hypothesis。我会用 roundtrip 属性为这个序列化对写属性化测试。」

**若用户拒绝**，就写好的示例测试，不再追问。

## 语言与库选择

按被测代码语言选择库（详见 [`references/libraries.md`](references/libraries.md)）：

| 语言 | 库 | 智能合约 |
| --- | --- | --- |
| Python | Hypothesis | — |
| JavaScript/TypeScript | fast-check | — |
| Rust | proptest | — |
| Go | rapid | — |
| Java | jqwik | — |
| Solidity/Vyper | — | Echidna / Medusa |

其他语言（Scala/C#/Elixir/Haskell/Clojure/Ruby/Kotlin/Swift/C++）见 libraries.md 全表。

## 默认不触发

以下情况**默认不**建议 PBT：

- 无复杂校验的简单 CRUD
- UI/展示逻辑
- 需要复杂外部编排的集成测试
- 需求还在流动的原型
- 用户明确只要示例测试

## 红旗（不要做）

- 给无关紧要的 getter/setter 推荐 PBT
- 缺少成对操作（只有 encode 没有 decode）仍推 roundtrip
- 忽视类型提示（良类型 = 更易测）
- 用候选淹没用户（一次最多 5-10 个）
- 用户拒绝后仍纠缠

## 应拒绝的借口

- **「示例测试够了」** —— 涉及序列化/解析/规范化时，PBT 能发现示例漏掉的边界
- **「函数很简单」** —— 输入域复杂的简单函数（字符串、浮点、嵌套结构）最受益于 PBT
- **「没时间」** —— PBT 测试通常比整套示例测试更短
- **「生成器太难写」** —— 多数 PBT 库自带优质策略，自定义生成器很少需要
- **「测试失败所以是 bug」** —— 失败需先验证，见 [interpreting-failures.md](references/interpreting-failures.md)
- **「不崩就是对的」** —— 「不抛异常」是最弱属性，始终要求更强保证

## 测试失败处理

属性化测试会生成大量失败样例，但**不是所有失败都是 bug**。先按 [`references/interpreting-failures.md`](references/interpreting-failures.md) 系统分析：

1. 用最小化（shrunk）样例复现，确认稳定。
2. 对照类型注解/文档字符串/函数名/错误处理/现有测试核实属性是否成立。
3. 检查策略是否生成函数实际不应处理的输入（前置条件违例 vs 真 bug）。
4. 分类：测试 bug（修属性/策略）/ 规格模糊（先讨论，不开 bug）/ 真 bug（带最小复现上报）。

## 任务完成自检

- [ ] 测试不是同义反复（断言没复现被测函数逻辑）
- [ ] 至少一个强属性（不只是「不崩」）
- [ ] 用 `@example` 显式覆盖边界（空、单元素、重复、0、负值等）
- [ ] 策略约束现实，未过度 `assume()` 过滤
- [ ] settings 与场景匹配（开发/CI/发布）
- [ ] 测试真实运行并通过（或按预期失败）

## 来源与改造说明

本 Skill 基于 [trailofbits/skills](https://github.com/trailofbits/skills)（CC-BY-SA-4.0，commit `e6066e7`）的 `plugins/property-based-testing/skills/property-based-testing/`。本地改造：

1. SKILL.md 主体翻译为中文并精简；`{baseDir}` 相对引用改写为本仓 `references/` 布局。
2. 移除平台专属文件：`agents/openai.yaml`（图标/品牌色配置）、`assets/trail-of-bits-mark.svg`（品牌资产）。
3. references 7 个文件原样保留（英文原义，术语密集），挂载到 `references/`。
4. 许可证 CC-BY-SA-4.0 全文随副本保留（`LICENSE.txt`），provenance 记录改造明细。
