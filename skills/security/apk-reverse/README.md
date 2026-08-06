# APK Reverse Engineering（APK 逆向）

## 一句话定位

在 CLI 环境下做 Android APK 逆向，覆盖解包、Java 反编译、smali 修改、重打包和 Frida 动态 Hook 全链路。

## 适用场景

- 分析 APK 的 Java 业务逻辑（登录/签名/风控）
- 定位 root 检测、证书校验、SSL Pinning 等安全机制
- 修改 smali 做 patch 并重打包
- Frida 动态 Hook Java/native 层
- 授权移动应用安全测试中的 APK 分析

## 不适用场景

- iOS 应用逆向（转 `security.mobile-reverse`）
- 纯 .so 深层次逆向（转 `security.reverse-engineering`）
- 未授权或生产环境 APK（必须先确认授权）

## 执行前需要的信息

- APK 文件
- 授权状态（CTF/沙盒/授权测试）
- 分析目标（如"定位签名算法""绕过 root 检测""分析登录流程"）

## 执行流程

1. Triage：jadx 反编译 Java + apktool 解包 smali
2. Java 逻辑观察：定位 MainActivity、登录/加密/风控类
3. Smali 与资源确认：查看 AndroidManifest.xml、strings.xml、patch 关键点
4. 动态 Hook：Frida 注入，先 Java 后 native
5. 重建与安装：apktool b + 签名 + adb install
6. Native 分流：遇到 .so 核心逻辑时转通用逆向

## 交付结果

- 入口组件与关键类识别
- 关键逻辑位置（Java/smali/.so）
- 敏感点清单（登录/签名/root/SSL/WebView/JNI）
- 如做 patch/Hook，说明修改了什么

## 默认边界

- **读文件**：是
- **写文件**：否（仅在 case 工作空间副本上操作）
- **执行命令**：是（jadx/apktool/frida/adb）
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `security.reverse-engineering` | 通用二进制逆向，本 Skill 专精 APK 层（Java/smali/重打包） |
| `security.mobile-reverse` | 覆盖 Android+iOS 动态插桩，本 Skill 侧重 APK 静态+动态全链路 |

## 行为案例

### 案例 1：典型 APK 逆向

**输入**：用户提供 `app.apk`，要求"分析这个 APK 的签名算法"。

**预期行为**：
1. jadx 反编译 → 搜索 `sign`/`encrypt`/`token` 等关键词
2. apktool 解包查看 smali 和 manifest
3. 定位签名逻辑（Java 层或 .so 层）
4. 如需动态验证，写 Frida Hook 脚本
5. 产出分析报告和可复现步骤

### 案例 2：授权不明确

**输入**：用户要求"帮我逆向这个生产环境的 APK 看看有没有后门"。

**预期行为**：
1. 询问授权状态
2. 在授权不明时拒绝执行
3. 不假设"用户说了就算"

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `apk-reverse` 模块（MIT License），做了本仓适配改造（见 `provenance.yaml`）。