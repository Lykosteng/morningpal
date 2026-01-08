#!/bin/bash
# MorningPal CLI 启动脚本

cd "$(dirname "$0")"

# 设置 API Key（请替换为你的密钥）
export STEPFUN_API_KEY="3jksrNI2ub5ksoQN0OomkHcIHZBgULzxe3Bv7evhlWwvmdZll1XR9tWfZFOo4dnfa"

python3 morningpal.py
