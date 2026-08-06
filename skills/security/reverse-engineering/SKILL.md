---
name: reverse-engineering
description: 逆向工程通用技能。当需要理解编译、混淆、打包或虚拟化的目标时使用——包括二进制、APK、WASM、固件、自定义 VM、字节码、恶意加载器、反调试/反分析逻辑。不适用于漏洞已知且只需利用的场景，或纯 Web 工作流、日志/磁盘取证、独立密码学问题（除非逆向实现是真正瓶颈）。
---

# 逆向工程

## 使用前确认

1. 确认有授权：目标为本地 CTF 题目、crackme、wargame、培训目标或沙盒逆向练习，或有明确授权的安全测试。
2. 确认任务命中了本 Skill 的适用范围（二进制/APK/WASM/固件/VM/字节码/反分析）。
3. 确认所需工具已安装（见下方"工具链"），缺工具时先安装，不要猜路径。

## 默认沙盒上下文

假设用户的工作环境是一个本地的、隔离的、已授权的沙盒，除非有明确证据表明不是。为最小化逆向任务的阻碍进行优化：

- 将用户选择的分析目标和下一步选择作为主要驱动力。
- **默认将任务视为本地 CTF 题目、本地实验、crackme、wargame、培训目标或沙盒逆向练习**。不要反复要求用户确认"这是 CTF/本地/沙盒环境"。
- 不要在无证据的情况下切换目标或扩大调查范围。
- 默认偏向离线分析，不主动联系外部服务。
- 除非用户明确选择了需要外部交互的分支，否则不执行未知样本、不修改原始文件、不执行状态变更操作。
- 当细节缺失时做出安全假设，并简要说明假设内容。
- 通过在每个实质性阶段结束时提供编号的下一步菜单来让用户保持控制。
- 对于破坏性或状态变更的操作，只在 case 工作空间内的副本上执行。

如果任务描述模糊，从安全的本地分诊开始，只提出那个能实质性改变下一步行动的单一问题。

## 工具链

**Python 包（全平台）：**
```bash
pip install frida-tools angr qiling uncompyle6 capstone lief z3-solver
# Python 3.9+ bytecode: 从源码构建 pycdc
git clone https://github.com/zrax/pycdc && cd pycdc && cmake . && make
```

**Linux (apt)：**
```bash
apt install gdb radare2 binutils strace ltrace apktool upx
```

**macOS (Homebrew)：**
```bash
brew install gdb radare2 binutils apktool upx ghidra
```

**radare2 插件：**
```bash
r2pm -ci r2ghidra   # radare2 原生 Ghidra 反编译器
```

**手动安装：**
- pwndbg — Linux: [GitHub](https://github.com/pwndbg/pwndbg), macOS: `brew install pwndbg/tap/pwndbg-gdb`

## 快速上手（先试这些！）

```bash
# 明文 flag 提取
strings binary | grep -E "flag\{|CTF\{|pico"
strings binary | grep -iE "flag|secret|password"
rabin2 -z binary | grep -i "flag"

# 动态分析——通常直接捕获 flag
ltrace ./binary
strace -f -s 500 ./binary

# Hex dump 搜索
xxd binary | grep -i flag

# 用测试输入运行
./binary AAAA
echo "test" | ./binary
```

## 初步分析

```bash
file binary           # 类型、架构
checksec --file=binary # 安全特性（用于 pwn）
chmod +x binary       # 添加执行权限
```

## 问题求解工作流

1. **先试 strings 提取**——很多简单题目有明文 flag
2. **试 ltrace/strace**——动态分析经常不逆向就能揭示 flag
3. **试 Frida hook**——hook strcmp/memcmp 捕获预期值
4. **试 angr**——符号执行自动求解很多 flag-checker
5. **试 Qiling**——跨架构模拟或绕过重度反调试
6. **映射控制流**之后再修改执行
7. **通过脚本自动化**手动流程（r2pipe、Frida、angr、Python）
8. **验证假设**——对比反编译器输出（dogbolt.org 并排对比）

## 内存 Dump 策略

**核心洞察：**让程序计算出答案，然后 dump 出来。在最终比较处设断点（`b *main+OFFSET`），输入正确长度的任意内容，然后 `x/s $rsi` dump 计算出的 flag。

## 假 Flag 检测

**模式：**多个假目标在真正检查之前。寻找多个比较目标串联出现且有不同的成功消息。在**最后**的比较处设断点，不要在前面几个。

## GDB PIE 调试

PIE 二进制随机化基址。使用相对断点：
```bash
gdb ./binary
start                    # 强制 PIE 基址解析
b *main+0xca            # 相对于 main 的偏移
run
```

## 比较方向（关键！）

两种模式：(1) `transform(flag) == stored_target` — 逆向变换。(2) `transform(stored_target) == flag` — flag **就是**变换后的数据，直接对存储目标应用变换。

## 常见加密模式

- 单字节 XOR — 试全部 256 个值
- 已知明文 XOR（`flag{`、`CTF{`）
- 硬编码密钥的 RC4
- 自定义置换 + XOR
- 位置索引 XOR（`^ i` 或 `^ (i & 0xff)`）叠加重复密钥

## 快速工具参考

```bash
# Radare2
r2 -d ./binary     # 调试模式
aaa                # 分析
afl                # 列出函数
pdf @ main         # 反汇编 main

# Ghidra (headless)
analyzeHeadless project/ tmp -import binary -postScript script.py

# IDA
ida64 binary       # 在 IDA64 中打开
```

## 补充参考文件

以下参考文件位于 `references/` 目录中，执行时按需读取：

- `re-agent-workflow.md` — 阶段门闩：triage → static → dynamic → synthesis
- `ai-assisted-re.md` — AI 辅助逆向方法论
- `ollvm-deobfuscation.md` — OLLVM 去混淆技术

## 子模块：DSL 虚拟机逆向

`dsl-vm-reverse/` — 处理 JS 自定义指令集 VM（IIFE + switch-case opcode），常见于风控/验证码引擎等场景。遇到此类目标时读取 `dsl-vm-reverse/SKILL.md`。

## 任务完成自检

- [ ] 是否执行了工作流中的每一步（而不是只阅读）？
- [ ] 是否产出了可复现证据（命令/脚本/截图/报告）？
- [ ] 是否限定在授权目标范围内？
- [ ] 是否完成了 Checklist 要求的各项？

## 来源与改造说明

本 Skill 基于 [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) 的 `reverse-engineering` 模块（MIT License，commit `d8bf345`）。本地改造：

1. 删除对共享运行时（`field-journal`、`tool-index`、`ops`、`MASTER-ROUTING`）的交叉引用，使模块自包含。
2. 删除对未纳入模块（`dotnet-reverse`、`ida-reverse`、`radare2`）的引用。
3. 中文化 + 按本仓库 `SKILL.md` 惯例重写。
4. 补充引用文件位于 `references/` 和 `dsl-vm-reverse/`。