# Test-Driven Development（测试驱动开发）

## 一句话定位

在写任何实现代码之前先写失败测试，走 Red-Green-Refactor 循环，确保每行代码都有测试证明其行为正确。

## 适用场景

- 实现新功能。
- 修复 bug（先写复现测试）。
- 重构（有测试保护）。
- 改变行为。

**例外（需用户确认）**：一次性原型、生成代码、配置文件。

## 不适用场景

- 纯探索/调研——不需要 TDD，但探索代码应扔掉，不要进入生产。
- 已经在 `engineering.brainstorming` 阶段——先完成设计再进 TDD。

## 执行前需要的信息

- 要实现的规格或 bug 描述。
- 项目的测试框架和命令。

## 执行流程

1. **RED**：写一个最小失败测试。
2. **验证 RED**：跑测试，确认失败原因正确。
3. **GREEN**：写刚好通过测试的最小代码。
4. **验证 GREEN**：跑测试，确认通过且其他测试全绿。
5. **REFACTOR**：全绿后清理代码，保持绿。
6. 重复直到功能完成。
7. **路由**：实现完成后按工作领域路由到对应的领域 Skill 验证。

## 交付结果

- 通过测试的生产代码。
- 测试先失败过的证据（Red-Green 循环记录）。
- 后续路由建议（前端验证 / 后端审查 / 排障）。

## 默认边界

- **读文件**：是。
- **写文件**：是（写测试和生产代码）。
- **执行命令**：是（跑测试、lint、build）。
- **网络**：否。
- **先写测试再写实现**：不可协商。

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `web.frontend-testing` | TDD 是**方法论**（怎么测）；frontend-testing 是**领域测试**（浏览器、UI 流程） |
| `backend.backend-implementation` | TDD 保证正确性；backend-implementation 提供领域架构 |
| `engineering.verification-before-completion` | TDD 在开发阶段；verification 在声称完成之前 |

## 行为案例

### 案例 1：典型成功场景（新功能）

**输入**：「实现一个 `retryOperation` 函数，失败时重试 3 次」。

**预期行为**：
1. 先写测试：`test('retries failed operations 3 times', ...)`。
2. 跑测试 → FAIL（函数不存在）。
3. 写最小实现（for 循环，3 次重试）。
4. 跑测试 → PASS。
5. 清理（提取常量等）。
6. 路由到 `engineering.verification-before-completion` 做最终验证。

### 案例 2：边界/违规场景

**输入**：开发者先写了 50 行实现代码才意识到没写测试。

**预期行为**：
1. Skill 识别违反铁律（代码在测试之前）。
2. 坚决要求删掉代码（不保留"参考"、不"改编"）。
3. 从 RED 步骤重新开始。
4. **不得**接受"已经花了时间"或"这次特殊"等合理化借口。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `test-driven-development` Skill（MIT License），做了本仓适配改造。
