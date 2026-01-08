#!/usr/bin/env python3
"""
MorningPal CLI - 小航终端版
每天早上帮你找到工作节奏的AI助手 ⛵
"""

import os
import json
from datetime import datetime
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

# 加载环境变量
load_dotenv()

console = Console()

# 配置
STEPFUN_API_KEY = os.getenv("STEPFUN_API_KEY", "")
HISTORY_FILE = Path.home() / ".morningpal_history.json"

# 系统提示词
SYSTEM_PROMPT = """你是小航，一个温暖、专业的AI早安教练。你的任务是：

1. 每天早上用温暖的问候开始对话
2. 了解用户今天的心情和状态
3. 帮助用户规划今天最重要的1-3件事
4. 提供积极的鼓励和建议
5. 用简洁有力的话语激励用户开始新的一天

风格要求：
- 亲切友好，像朋友一样交谈
- 简洁明了，不要太长篇大论
- 适当使用emoji增加亲和力
- 关注用户的感受，给予情感支持

记住：你的目标是帮助用户以积极的心态开始新的一天！"""


def load_history():
    """加载历史记录"""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"conversations": [], "streak": 0, "last_date": None}


def save_history(history):
    """保存历史记录"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def update_streak(history):
    """更新连续打卡天数"""
    today = datetime.now().strftime("%Y-%m-%d")
    last = history.get("last_date")
    
    if last == today:
        return history["streak"]
    
    yesterday = (datetime.now().replace(hour=0, minute=0, second=0) 
                 - __import__("datetime").timedelta(days=1)).strftime("%Y-%m-%d")
    
    if last == yesterday:
        history["streak"] += 1
    elif last != today:
        history["streak"] = 1
    
    history["last_date"] = today
    save_history(history)
    return history["streak"]


def chat(client, messages):
    """与AI对话"""
    try:
        response = client.chat.completions.create(
            model="step-1-8k",
            messages=messages,
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 出错了: {str(e)}"


def main():
    # 检查 API Key
    if not STEPFUN_API_KEY:
        console.print(Panel(
            "[red]请先设置 STEPFUN_API_KEY 环境变量！[/red]\n\n"
            "方法1: 在 cli 目录创建 .env 文件:\n"
            "[cyan]STEPFUN_API_KEY=你的API密钥[/cyan]\n\n"
            "方法2: 直接导出环境变量:\n"
            "[cyan]export STEPFUN_API_KEY=你的API密钥[/cyan]",
            title="⚠️ 配置缺失"
        ))
        return
    
    # 初始化客户端
    client = OpenAI(api_key=STEPFUN_API_KEY, base_url="https://api.stepfun.com/v1")
    
    # 加载历史
    history = load_history()
    streak = update_streak(history)
    
    # 显示欢迎信息
    hour = datetime.now().hour
    if hour < 12:
        greeting = "早上好"
    elif hour < 18:
        greeting = "下午好"
    else:
        greeting = "晚上好"
    
    console.print()
    console.print(Panel(
        f"[bold cyan]🧭 MorningPal - 小航[/bold cyan]\n"
        f"[dim]你的早安领航员[/dim]\n\n"
        f"[yellow]🔥 连续打卡: {streak} 天[/yellow]",
        title=f"⛵ {greeting}！",
        border_style="cyan"
    ))
    console.print()
    
    # 初始化对话
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # 获取AI问候
    console.print("[dim]小航正在准备...[/dim]")
    greeting_msg = chat(client, messages + [{"role": "user", "content": "请用温暖的方式问候我，开始今天的早安对话"}])
    messages.append({"role": "assistant", "content": greeting_msg})
    
    console.print()
    console.print(Panel(Markdown(greeting_msg), title="🧭 小航", border_style="blue"))
    
    # 对话循环
    console.print("\n[dim]输入消息与小航聊天，输入 'q' 或 'quit' 退出[/dim]\n")
    
    while True:
        try:
            user_input = console.input("[bold green]你:[/bold green] ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['q', 'quit', 'exit', '退出']:
                console.print("\n[cyan]小航:[/cyan] 今天也要加油哦！明天见 👋✨\n")
                break
            
            messages.append({"role": "user", "content": user_input})
            
            console.print("[dim]思考中...[/dim]")
            response = chat(client, messages)
            messages.append({"role": "assistant", "content": response})
            
            console.print()
            console.print(Panel(Markdown(response), title="🧭 小航", border_style="blue"))
            console.print()
            
        except KeyboardInterrupt:
            console.print("\n\n[cyan]小航:[/cyan] 再见！明天见 👋\n")
            break
    
    # 保存对话到历史
    if len(messages) > 2:
        history["conversations"].append({
            "date": datetime.now().isoformat(),
            "messages": messages[1:]  # 不保存系统提示
        })
        # 只保留最近30天的对话
        history["conversations"] = history["conversations"][-30:]
        save_history(history)


if __name__ == "__main__":
    main()
