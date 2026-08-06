# Mobile Reverse Engineering（移动端逆向）

## 一句话定位

Android + iOS 统一逆向方法论，覆盖 Frida/Objection 动态插桩、SSL Pinning 绕过、Root/越狱检测绕过和 OWASP MASTG 渗透测试。

## 适用场景

- Android APK 和 iOS IPA 的逆向与安全测试
- 运行时动态插桩（Frida/Objection）
- SSL Pinning / Root 检测 / 越狱检测绕过
- 移动端加密算法提取（AES/RSA/HMAC）
- OWASP MASTG 合规测试
- 非 Root/越狱环境下的应用测试（Frida Gadget）

## 不适用场景

- 纯 APK 静态分析（jadx/smali/重打包）→ 转 `security.apk-reverse` 更高效
- 通用二进制逆向（.so/Mach-O 深度分析）→ 转 `security.reverse-engineering`
- 恶意样本分析 → 转 `security.malware-analysis`

## 执行前需要的信息

- 移动应用文件（APK/IPA）
- 目标平台（Android/iOS/双平台）
- 测试设备或模拟器
- 授权状态

## 执行流程

1. Phase 1: 信息收集（Manifest/Info.plist 分析、加固检测）
2. Phase 2: 静态分析（JADX/Ghidra/Hopper/class-dump）
3. Phase 3: 动态分析（Frida Hook + Objection REPL）
4. Phase 4: 网络分析（Burp/mitmproxy/SSL Pinning 绕过）

## 交付结果

- 四阶段分析报告
- 加密算法位置和密钥提取
- 绕过方案（SSL Pinning/Root/反调试）
- 可复现的 Frida/Objection 脚本

## 默认边界

- **读文件**：是
- **写文件**：否（仅在 case 工作空间副本上操作）
- **执行命令**：是（frida/objection/jadx 等）
- **网络**：否（除非需要网络分析阶段）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `security.apk-reverse` | 专精 APK 静态全链路（jadx/smali/重打包），本 Skill 覆盖双平台动态插桩 |
| `security.reverse-engineering` | 通用二进制逆向，本 Skill 专注移动端特有的检测绕过和 MASTG |

## 行为案例

### 案例 1：典型移动端安全测试

**输入**：用户提供 `app.apk` 和测试设备，要求"做完整的移动安全测试"。

**预期行为**：
1. 分析 Manifest 权限和导出组件
2. 静态分析 Java 层业务逻辑
3. Objection 禁用 SSL Pinning 和 root 检测
4. Frida Hook 提取加密密钥
5. Burp 拦截网络流量
6. 产出 MASTG 合规报告

### 案例 2：无设备环境

**输入**：用户要求"帮我分析这个 IPA 的安全问题"但没有 iOS 测试设备。

**预期行为**：
1. 告知动态分析需要设备
2. 先做静态分析（class-dump/Info.plist/Ghidra）
3. 列出需要设备验证的发现项
4. 不编造动态分析结果

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `mobile-reverse` 模块（MIT License），做了本仓适配改造（见 `provenance.yaml`）。