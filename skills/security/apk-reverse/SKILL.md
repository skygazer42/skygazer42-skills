---
name: apk-reverse
description: 在 CLI 环境下做 Android APK 逆向时使用。适用于 APK 解包、Java 反编译、smali 修改、重打包、Frida 动态 Hook，以及按需切换到 so/native 分析。
---

# APK 逆向

## 使用前确认

1. 确认有授权：目标为本地 CTF 题目、沙盒实验或已授权测试的 APK。
2. 确认任务命中了本 Skill 的适用范围（APK 解包/Java 反编译/smali 修改/重打包/Frida Hook）。
3. 确认所需工具已安装（jadx/apktool/frida/adb），缺工具时先安装，不要猜路径。

## 适用范围

当任务属于以下场景时优先使用本 Skill：

- 分析 APK 的 Java 业务逻辑
- 定位登录、签名、风控、证书校验、root 检测
- 查看与修改 `AndroidManifest.xml`
- 查看与修改 smali
- 重打包 APK
- 用 Frida 做 Java/native 动态 Hook
- APK 内含 `.so` 时切到 native 分析

## 工具分工

### `jadx`

用于 Java 反编译阅读、包名/类名/方法名搜索、从高层逻辑理解 APK。

```bash
jadx -d jadx_out app.apk
jadx --single-class com.example.LoginActivity -d jadx_out app.apk
jadx --deobf -d jadx_out app.apk
```

### `apktool`

用于解包 APK、查看和修改 `AndroidManifest.xml`/smali、重建 APK。

```bash
apktool d app.apk -o apktool_out
apktool b apktool_out -o rebuilt.apk
```

### `frida`

用于动态观察 Java 方法调用、Hook native 导出函数、绕过 root 检测/证书校验/调试检测。

```bash
frida-ps -U
frida -U -f com.example.app -l hook.js
frida-trace -U -f com.example.app -j '*!*certificate*'
```

### `adb`

用于设备连接、安装 APK、查看日志、拉取文件。

```bash
adb devices
adb install -r app.apk
adb shell pm list packages
adb logcat
adb pull /data/local/tmp/file .
```

## 推荐工作流

### 1. Triage

先确定 APK 大致构成，不急着改包或 Hook：

1. 用 `jadx -d jadx_out app.apk` 导出 Java 代码
2. 用 `apktool d app.apk -o apktool_out` 导出 smali 和资源
3. 先看：`AndroidManifest.xml`、主 package、`application`/`activity`/`service`/`receiver`、`lib/` 目录是否有 `.so`

### 2. Java 逻辑观察

优先从 `jadx_out` 读：`MainActivity`、`Application`、登录/网络/加密/风控相关类、第三方 SDK 初始化类。

常见关键词：`login`、`sign`、`encrypt`、`cipher`、`token`、`root`、`certificate`、`trust`、`okhttp`、`retrofit`、`webview`

如果 Java 代码可读，先在这里定位业务逻辑。

### 3. Smali 与资源层确认

当 `jadx` 结果不完整、混淆重、或需要实际 patch 时，切到 `apktool_out`：
- 看 `smali*/`、`res/values/strings.xml`、`AndroidManifest.xml`
- 优先 patch：`android:exported`、调试标记、root 检测返回值、登录验证逻辑、证书校验分支

### 4. 重建与安装

```bash
apktool b apktool_out -o rebuilt.apk
```

本 Skill 只保证 `apktool` 重建链路。若后续需要正式安装到设备，通常还需要签名流程（`apksigner` / `zipalign`）。

### 5. 动态 Hook

静态分析不足时，用 Frida：
- Hook 登录函数、`OkHttp`/`Retrofit`/`WebView` 关键点
- Hook `javax.crypto`、`MessageDigest`
- Hook root 检测函数、SSL pinning 逻辑

原则：先 Hook Java 层，再看是否需要 native Hook；先打印参数与返回值，再决定是否主动修改返回值。

### 6. Native `.so` 分流

如果 APK 中包含关键 `.so`：
- 用 `apktool` 或 `jadx` 找到 `lib/**/*.so`
- 若只是导出符号、字符串、快速 triage，可用 `radare2`
- 若需长期深入分析，转 `security.reverse-engineering`

遇到这些信号要尽快切 native：
- Java 层只是 JNI 包装
- 核心签名逻辑不在 Java
- `System.loadLibrary()` 后关键逻辑消失
- 证书校验/风控在 `.so` 中

## 输出要求

最终至少说明：
- 入口组件与关键类
- 关键逻辑在 Java、smali 还是 `.so`
- 已确认的敏感点：登录、签名、root、SSL、WebView、JNI
- 如果做了 patch，说明改了什么
- 如果做了 Hook，说明 Hook 了哪个类/方法/导出函数

## 禁止事项

- 不要一开始就盲目改 smali
- 不要在没看 manifest 和主入口前就写 Hook
- 不要把 Java 反编译不完整直接等同于"逻辑不可分析"
- 不要在 `.so` 明显承载核心逻辑时继续死磕 Java 层

## 自带脚本

以下脚本位于 `scripts/` 目录，用于高频流程自动化：

- `scripts/decode.ps1` / `decode.sh` — 统一跑 jadx+apktool 落盘并产出摘要
- `scripts/frida-run.ps1` / `frida-run.sh` — Frida 设备检查、进程列举、spawn/attach 注入
- `scripts/rebuild-sign-install.ps1` / `rebuild-sign-install.sh` — 重建、对齐、签名、安装 APK
- `scripts/manifest-summary.ps1` — 快速抽取 Manifest 关键组件与权限

> 注意：`.ps1` 脚本为 Windows 优先（PowerShell），`.sh` 脚本为 Linux/macOS。脚本中可能引用 Kali 自举工具路径，本仓库未纳入 Kali 基础设施，请在相应平台手动安装依赖工具。

## 快速命令备忘

```bash
# 反编译 Java
jadx -d jadx_out app.apk
# 解包 APK
apktool d app.apk -o apktool_out
# 重建 APK
apktool b apktool_out -o rebuilt.apk
# 设备与进程
adb devices
frida-ps -U
# 启动并注入
frida -U -f com.example.app -l hook.js
```

## 补充参考

`references/` 目录包含：
- `frida-cookbook.md` — Frida Hook 常用配方
- `apk-security-checklist.md` — APK 安全检查清单
- `frida-bypass-kit.md` — Frida 绕过套件（root/SSL/反调试）
- `android-advanced.md` — Android 逆向进阶

## 任务完成自检

- [ ] 是否执行了工作流中的每一步（而不是只阅读）？
- [ ] 是否产出了可复现证据（命令/脚本/截图/报告）？
- [ ] 是否限定在授权目标范围内？

## 来源与改造说明

本 Skill 基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `apk-reverse` 模块（MIT License，commit `d8bf345`）。本地改造：

1. 删除对共享运行时（`field-journal`、`tool-index`、`ops`、`MASTER-ROUTING`）的交叉引用。
2. 删除对未纳入模块（`ida-reverse`、`radare2`）的引用。
3. 中文化 + 按本仓库 `SKILL.md` 惯例重写。
4. 保留 `references/`（4 个文件）和 `scripts/`（7 个脚本，标注平台限制）。