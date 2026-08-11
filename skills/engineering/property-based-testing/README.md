# 属性化测试（Property-Based Testing）

## 一句话定位

用**生成式数据**验证被测代码的**属性**——roundtrip、幂等、不变量、交换律、结合律、逆操作、参考实现对照、状态机不变量——而不是只验证几个手写示例。适合序列化/解析/规范化/校验/纯函数/智能合约等输入域复杂或代数性质清晰的场景。

## 适用场景

- 写测试时发现序列化对（encode/decode、serialize/deserialize）、解析器、规范化器、校验器、纯函数
- 代码已用 PBT 库（Hypothesis/fast-check/proptest/Echidna），需要按库惯例写属性化测试
- 审查已有属性化测试的质量（同义反复/空洞/弱断言/过度过滤/缺边界）
- 用属性先行（Property-Driven Development）设计新功能，实现前定义可执行规格
- 函数难测（I/O 混杂、缺逆操作）时，用可测性重构解锁更强属性
- 属性化测试失败时，判定是真 bug、测试 bug 还是规格模糊

## 不适用场景

- 无变换逻辑的简单 CRUD、一次性脚本、无法隔离副作用的代码
- 具体示例已足够且边界情况清楚的测试
- 集成/端到端测试（PBT 最适合单元/组件级）
- 需求未稳定的原型
- 用户明确只要示例测试（此时写好的示例测试，不纠缠）

## 执行前需要的信息

- 被测代码与语言栈（决定选 Hypothesis/fast-check/proptest 等）
- 目标函数/模块的签名、类型、文档与既有示例测试
- 是否已存在 PBT 库依赖（决定建议的直白程度）

## 执行流程

1. **检测模式**：按 SKILL.md 的触发列表识别序列化对/解析器/规范化器/校验器/纯函数/智能合约模式
2. **按优先级路由**：roundtrip > 幂等/有序 > 不变量 > builder 输出 > 状态不变量，读对应 reference
3. **设计策略**：把约束建进策略（`min_value`/`max_size`/`st.builds`），而非 `assume()` 过滤
4. **选属性**：从属性目录挑至少一个强属性（roundtrip/幂等/不变量/参考实现对照），弱属性只作基线
5. **生成测试**：带说明 docstring、`@example` 边界、与场景匹配的 `@settings`（开发/CI/发布）
6. **审查**（已有测试时）：检查同义反复/空洞/弱断言/复现函数/过度过滤/缺边界/设置不当
7. **失败解读**：用最小化样例复现 → 对照文档/类型核实 → 分类真 bug/测试 bug/规格模糊

## 交付结果

- 属性化测试代码（按语言库惯例，含边界示例与 settings）
- 测试质量审查结论（按强度/覆盖/断言/设置四维评分）
- 失败分类与处置建议（真 bug 带最小复现上报 / 测试 bug 修属性 / 规格模糊先讨论）
- 按需的可测性重构建议（提取纯核心、补逆操作、注入依赖等）

## 默认边界

- **读文件**：是（被测源码与测试）
- **写文件**：是（生成/修改测试文件）
- **执行命令**：是（pytest 等测试运行）
- **网络**：否
- **事实边界不可越**：不装库、不跑 CI、不改生产代码；只在用户要求且已授权的范围内写测试并运行

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.test-driven-development` | TDD 管理开发节奏（Red-Green-Refactor）；本 Skill 只判定「哪些属性值得用生成式数据验证」，是测试方式的决策，不重复 TDD 流程 |
| `engineering.writing-plans` | 实现计划编排；本 Skill 是具体测试方法的生成与审查 |
| `engineering.architecture-review` | 架构层深化；本 Skill 聚焦单个函数的代数属性与测试质量 |

## 行为案例

### 案例 1：序列化对 → roundtrip 属性

**输入**：`encode_message`/`decode_message` 序列化对，代码库用 Hypothesis。

**预期行为**：
1. 识别为序列化对，HIGH 优先级
2. 用 `st.builds` 构造 `Message` 策略（id/content/priority/tags）
3. 写 roundtrip 属性 `decode(encode(msg)) == msg` + 确定性 `encode(msg) == encode(msg)` + 类型保持 + 非法输入不崩
4. 补 `@example` 边界与 CI 级 `@settings(max_examples=200)`
5. 运行 pytest 验证通过

### 案例 2：规范函数 → 幂等属性

**输入**：`normalize(s)` 字符串规范化函数。

**预期行为**：
1. 识别为规范化器，MEDIUM 优先级
2. 写幂等属性 `normalize(normalize(s)) == normalize(s)`
3. 对照文档核实输入域（如「任意 unicode」）
4. 策略用 `st.text()` 而非过度过滤

### 案例 3：用户拒绝 PBT

**输入**：用户说「这个函数简单，写示例测试就行」。

**预期行为**：
1. 一次提议后用户仍拒绝 → 尊重选择，写高质量示例测试
2. 不纠缠、不重复推销
3. 若检测到强模式（序列化/解析），可简短说明收益，但最终按用户决定执行

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [trailofbits/skills](https://github.com/trailofbits/skills)（CC-BY-SA-4.0，commit `e6066e7`）的 `plugins/property-based-testing/skills/property-based-testing/`。详见 `provenance.yaml`。
