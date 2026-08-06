# API Security Testing（API 安全测试）

## 一句话定位

授权 API 安全测试，覆盖 REST/GraphQL/WebSocket/SOAP 全协议，从发现到 CI/CD 集成的 10 阶段方法论。

## 适用场景

- REST API 安全测试（OpenAPI/Swagger 驱动或盲测）
- GraphQL 安全审计（内省/批查询/别名过载）
- WebSocket 安全测试
- JWT / OAuth 2.0 认证测试
- BOLA/IDOR/BFLA 授权漏洞检测
- API 限速绕过与 DoS 测试

## 不适用场景

- 源码安全审计（SAST）→ 转 `security.code-audit`
- 移动端 API 逆向（需要先解包 APK）→ 转 `security.apk-reverse`
- 未授权目标（必须先确认授权）

## 执行前需要的信息

- API 端点（URL/域名）
- 认证凭证或测试 token
- OpenAPI/GraphQL 规范（如可用）
- 授权测试范围（哪些端点、什么时间段）

## 执行流程

1. Phase 1: API 发现与侦察（Vespasian/Entropy/Kiterunner）
2. Phase 2: 认证测试（JWT 分析/OAuth 2.0 攻击）
3. Phase 3: 授权测试（BOLA/IDOR/BFLA）
4. Phase 4: GraphQL 专项（内省/别名过载/批查询/CSRF）
5. Phase 5: REST 输入验证（方法切换/NoSQL 注入/SSRF/参数污染）
6. Phase 6: 业务逻辑与差分测试
7. Phase 7: WebSocket 测试
8. Phase 8: 限速与 DoS
9. Phase 9: 数据暴露
10. Phase 10: CI/CD 集成

## 交付结果

- 按严重度排序的漏洞发现
- 每个发现含：位置 + 数据流 + PoC + 修复建议
- 可选 ATT&CK / CWE 编号

## 默认边界

- **读文件**：是
- **写文件**：否
- **执行命令**：是（curl/jwt_tool/python 等工具）
- **网络**：是（API 测试需要访问目标端点，限授权范围）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `security.code-audit` | 源码白盒审计，本 Skill 是黑盒/灰盒 API 测试 |
| `security.reverse-engineering` | 二进制逆向，本 Skill 是 Web API 协议层测试 |

## 行为案例

### 案例 1：典型 REST API 安全测试

**输入**：用户提供 `https://api.example.com` 的 OpenAPI 规范和测试 token，要求"做完整的安全测试"。

**预期行为**：
1. 确认授权范围
2. 从 OpenAPI 规范发现所有端点
3. 逐阶段测试：认证、授权、输入验证、限速
4. 对每个发现做 PoC 验证
5. 产出漏洞报告和修复建议

### 案例 2：未授权目标

**输入**：用户要求"帮我测试一下这个第三方 API 有没有漏洞"但未提供授权证明。

**预期行为**：
1. 拒绝执行
2. 要求提供书面授权
3. 不执行任何测试请求

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `api-security` 模块（MIT License），做了本仓适配改造（见 `provenance.yaml`）。