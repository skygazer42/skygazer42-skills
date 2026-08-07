#!/usr/bin/env bash
# skygazer42-skills 一键环境配置
# 安装依赖工具 + 交互式安装 Skill
set -euo pipefail

echo "=================================="
echo " skygazer42-skills 环境配置"
echo "=================================="
echo ""

# ---------- FastCtx ----------
echo "→ 检查 FastCtx（高性能 MCP 文件/搜索/命令工具）..."

if command -v fastctx &>/dev/null; then
    echo "  ✓ 已安装: $(fastctx --version 2>/dev/null || echo 'ok')"
else
    echo "  ⚠ 未检测到 fastctx，正在安装..."
    if command -v npm &>/dev/null; then
        npm install --global fastctx
        echo "  ✓ fastctx 安装完成"
        echo ""
        echo "  ℹ 接下来请运行 fastctx 进入控制终端，在 Apply 页面确认配置后重启 AI 会话。"
    else
        echo "  ✗ 未检测到 npm，请先安装 Node.js 18+，然后手动运行:"
        echo "    npm install --global fastctx"
    fi
fi

echo ""

# ---------- Skills ----------
echo "→ 安装 Skills..."
if command -v npx &>/dev/null; then
    npx skills@latest add skygazer42/skygazer42-skills
else
    echo "  ⚠ 未检测到 npx，跳过。请手动安装 Skill:"
    echo "    npx skills@latest add skygazer42/skygazer42-skills"
fi

echo ""
echo "=================================="
echo " 配置完成！"
echo "=================================="
echo ""
echo "快速验证:"
echo "  fastctx status    # 检查 FastCtx 是否正常"
echo ""
