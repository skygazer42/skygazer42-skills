---
name: code-audit
description: 授权源码安全审计和 SAST 工作流。覆盖 Semgrep/CodeQL 模式、危险 API 扫描、鉴权审查和修复验证。
---

# 源码安全审计

## 使用前确认

1. 确认有**源码/仓库访问权限**（无源码二进制 → 转 `security.reverse-engineering`）。
2. 明确语言栈与范围（目录/服务/PR diff）。
3. 确认是授权审计，不是未授权攻击。

## 适用场景

- 白盒审计、PR/差分安全审查
- Semgrep / CodeQL / Bandit / gosec 等 SAST
- 危险 API、注入点、鉴权缺失、加密误用
- 自有代码逻辑审计（非依赖/供应链扫描，后者应走独立供应链分析流程）

## 工作流

### 1. 范围与威胁模型

- 信任边界：用户输入、文件、反序列化、SSRF、鉴权中间件
- 高价值资产：鉴权、支付、管理端、密钥处理

### 2. 自动扫描

```bash
semgrep --config auto .
# 或项目规则包
semgrep --config p/owasp-top-ten .
```

### 3. 人工验证（MUST）

- 每个 SAST 命中：可达性？可利用性？误报？
- 鉴权：IDOR/越权、缺校验、错误的多租户隔离
- 注入：SQL/命令/模板/LDAP
- 加密：硬编码密钥、ECB、自定义 crypto

### 4. 产出

```
Finding：位置 + 数据流 + PoC + 修复建议
可选 ATT&CK / CWE 编号
```

## 工具链

| 工具 | 语言/场景 |
|------|-----------|
| Semgrep | 多语言快速规则 |
| CodeQL | 深数据流（GitHub） |
| Bandit | Python |
| gosec / staticcheck | Go |
| SpotBugs / FindSecBugs | Java |

## 补充参考

`references/` 目录包含：
- `sast-review-checklist.md` — SAST 审查清单

## 与相邻 Skill 的关系

- 依赖漏洞扫描 → 供应链安全分析（独立流程）
- 运行时验证 → 渗透测试工具
- API 安全审计 → 可联动 `security.api-security`
- 无源码的目标 → 转 `security.reverse-engineering`

## 任务完成自检

- [ ] 是否人工验证而非只贴扫描器输出？
- [ ] 是否含修复建议？
- [ ] 是否限定在授权仓库范围？
- [ ] 是否完成了 Checklist？

## 来源与改造说明

本 Skill 基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `code-audit` 模块（MIT License，commit `d8bf345`）。本地改造：

1. 删除对共享运行时（`field-journal`、`tool-index`、`ops`、`MASTER-ROUTING`）的交叉引用。
2. 删除对未纳入模块（`supply-chain-security`、`llm-security`）的引用。
3. 中文化 + 按本仓库 `SKILL.md` 惯例重写。
4. 保留 `references/`（1 个文件）。