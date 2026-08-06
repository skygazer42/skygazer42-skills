# Source Code Security Audit（源码安全审计）

## 一句话定位

授权源码安全审计和 SAST 工作流，用 Semgrep/CodeQL 等工具做白盒安全审查，人工验证每项发现。

## 适用场景

- 白盒审计、PR/差分安全审查
- Semgrep / CodeQL / Bandit / gosec 等 SAST 工具
- 危险 API、注入点、鉴权缺失、加密误用
- 自有代码逻辑审计

## 不适用场景

- 依赖或供应链安全扫描（独立流程）
- 无源码的二进制分析 → 转 `security.reverse-engineering`
- 黑盒渗透测试 → 转 `security.api-security`
- 恶意样本分析 → 转 `security.malware-analysis`

## 执行前需要的信息

- 源码仓库访问权限
- 语言栈和审计范围（目录/服务/PR diff）
- 授权审计确认

## 执行流程

1. 范围与威胁模型：明确信任边界和高价值资产
2. 自动扫描：semgrep --config auto / CodeQL 分析
3. 人工验证（MUST）：每个 SAST 命中都要验证可达性和可利用性
4. 产出：Finding（位置 + 数据流 + PoC + 修复建议）

## 交付结果

- 按严重度排序的审计发现
- 每个发现含：位置 + 数据流 + PoC + 修复建议
- 可选 ATT&CK / CWE 编号

## 默认边界

- **读文件**：是
- **写文件**：否
- **执行命令**：是（semgrep/codeql 等工具）
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `security.api-security` | 黑盒 API 测试，本 Skill 是白盒源码审计 |
| `security.reverse-engineering` | 无源码的二进制逆向，本 Skill 需要源码访问 |

## 行为案例

### 案例 1：典型 PR 安全审查

**输入**：用户提供 PR diff，要求"审查这个 PR 的安全问题"。

**预期行为**：
1. 确认授权范围（PR diff 涉及的服务）
2. 运行 semgrep 自动扫描
3. 人工验证每个命中（可达性/可利用性）
4. 按严重度排序发现
5. 产出修复建议

### 案例 2：无源码

**输入**：用户要求"审计这个 API 的安全性"但只有二进制文件。

**预期行为**：
1. 告知本 Skill 需要源码访问
2. 建议转 `security.reverse-engineering` 做二进制逆向分析
3. 不编造源码审计结果

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `code-audit` 模块（MIT License），做了本仓适配改造（见 `provenance.yaml`）。