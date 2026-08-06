# Reverse Engineering（逆向工程）

## 一句话定位

逆向工程通用技能，覆盖二进制、APK、WASM、固件、自定义 VM、字节码等目标的静态/动态分析方法论和工具链。

## 适用场景

- 本地 CTF 逆向题目（crackme、wargame、培训目标）
- 沙盒环境中的二进制分析
- 授权安全测试中的逆向需求
- 需要理解编译/混淆/打包/虚拟化目标的内部逻辑
- 反调试/反分析逻辑的绕过研究

## 不适用场景

- 漏洞已知且只需利用的场景（这是 pwn/exploit 的职责）
- 纯 Web 工作流（除非逆向 JS 是实现瓶颈，此时转 `security.js-reverse`）
- 日志/磁盘取证（转 `security.digital-forensics`）
- 独立密码学问题（除非逆向实现是真正瓶颈）
- 未授权或生产目标（必须先确认授权）

## 执行前需要的信息

- 目标文件（二进制/APK/WASM 等）
- 目标平台和架构信息
- 授权状态（CTF/沙盒/授权测试）
- 已知约束（如"不能修改原始文件""只能静态分析"等）

## 执行流程

1. 确认授权和沙盒上下文
2. 快速上手：strings → ltrace/strace → Frida hook → angr → Qiling
3. 初步分析：file、checksec、架构识别
4. 按需深入：静态分析（Ghidra/radare2/IDA）或动态分析（Frida/GDB/angr）
5. 在每个阶段结束时提供下一步菜单，让用户保持控制
6. 产出可复现证据和报告

## 交付结果

- 可复现的分析命令/脚本
- 目标逻辑的逆向理解（控制流、数据流、加密算法等）
- 对于 CTF：flag 提取脚本或证据
- 对于分析任务：结构化报告

## 默认边界

- **读文件**：是
- **写文件**：否（除非在 case 工作空间副本上操作）
- **执行命令**：是（gdb/radare2/python 等工具）
- **网络**：否（默认离线分析，除非用户明确选择外部交互分支）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `security.apk-reverse` | 专精 Android APK 层（jadx/smali/重打包），本 Skill 处理 .so 层及通用逆向 |
| `security.mobile-reverse` | 覆盖 Android+iOS 动态插桩，本 Skill 侧重二进制分析 |
| `security.malware-analysis` | 专精恶意样本六阶段分析，本 Skill 侧重一般逆向 |
| `security.code-audit` | 源码白盒审计，本 Skill 是黑盒/灰盒逆向 |

## 行为案例

### 案例 1：典型 CTF 逆向

**输入**：用户提供 `challenge.elf`，要求"帮我分析这个 CTF 逆向题"。

**预期行为**：
1. 确认是 CTF/沙盒环境
2. strings → ltrace 快速上手
3. 如未命中，用 radare2/Ghidra 做静态分析
4. 如需要，用 Frida/angr 做动态分析
5. 产出 flag 并附带可复现命令

### 案例 2：授权不明确

**输入**：用户要求"帮我逆向这个生产环境的 APK"。

**预期行为**：
1. 询问授权状态或沙盒确认
2. 在授权不明时拒绝执行
3. 不假设"用户说了就算"

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `reverse-engineering` 模块（MIT License），做了本仓适配改造（见 `provenance.yaml` 和 SKILL.md 末尾"来源与改造说明"）。