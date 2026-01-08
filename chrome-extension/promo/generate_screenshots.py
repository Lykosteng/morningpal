#!/usr/bin/env python3
"""
生成 Chrome Web Store 截图
运行: python3 generate_screenshots.py
"""
from PIL import Image, ImageDraw
import os

# 创建 1280x800 的截图
width, height = 1280, 800

def create_gradient(w, h, color1, color2):
    """创建渐变背景"""
    img = Image.new('RGB', (w, h))
    for y in range(h):
        r = int(color1[0] + (color2[0] - color1[0]) * y / h)
        g = int(color1[1] + (color2[1] - color1[1]) * y / h)
        b = int(color1[2] + (color2[2] - color1[2]) * y / h)
        for x in range(w):
            img.putpixel((x, y), (r, g, b))
    return img

def draw_rounded_rect(draw, coords, radius, fill):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = coords
    # 处理透明度 (如果有)
    if isinstance(fill, tuple) and len(fill) == 4:
        fill = fill[:3]  # 去掉 alpha
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius], fill=fill)
    draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius], fill=fill)
    draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2], fill=fill)
    draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2], fill=fill)

print("🎨 正在生成 Chrome Web Store 截图...")

# ========== 截图1 - 主界面 ==========
img1 = create_gradient(width, height, (12, 25, 41), (26, 54, 93))
draw1 = ImageDraw.Draw(img1)

# 左侧文字
draw1.text((120, 250), "🧭", fill=(255, 255, 255))
draw1.text((180, 250), "MorningPal", fill=(255, 255, 255))
draw1.text((120, 320), "每天早上", fill=(255, 255, 255))
draw1.text((120, 370), "找到你的工作节奏", fill=(255, 255, 255))
draw1.text((120, 450), "AI 早安教练「小航」", fill=(148, 163, 184))
draw1.text((120, 490), "根据你每天不同的状态", fill=(148, 163, 184))
draw1.text((120, 530), "给出个性化建议", fill=(148, 163, 184))

# 功能标签
draw_rounded_rect(draw1, (120, 600, 230, 640), 15, (14, 80, 120))
draw1.text((135, 612), "⏰ 定时提醒", fill=(125, 211, 252))

draw_rounded_rect(draw1, (250, 600, 360, 640), 15, (14, 80, 120))
draw1.text((265, 612), "💬 AI 对话", fill=(125, 211, 252))

draw_rounded_rect(draw1, (380, 600, 500, 640), 15, (14, 80, 120))
draw1.text((395, 612), "🔥 连续打卡", fill=(125, 211, 252))

# 右侧模拟弹窗
draw_rounded_rect(draw1, (680, 120, 1160, 680), 20, (30, 41, 59))

# 弹窗头部
draw_rounded_rect(draw1, (680, 120, 1160, 200), 20, (12, 74, 110))
draw1.ellipse([710, 140, 770, 200], fill=(14, 165, 233))
draw1.text((730, 155), "🧭", fill=(255, 255, 255))
draw1.text((790, 145), "小航", fill=(255, 255, 255))
draw1.text((790, 175), "你的早安领航员", fill=(125, 211, 252))

# 连续天数
draw_rounded_rect(draw1, (1050, 145, 1140, 175), 12, (100, 80, 20))
draw1.text((1060, 152), "🔥 7天", fill=(252, 211, 77))

# 对话消息
draw_rounded_rect(draw1, (700, 230, 1050, 310), 16, (20, 50, 80))
draw1.text((720, 250), "早上好呀！今天感觉", fill=(226, 232, 240))
draw1.text((720, 275), "怎么样？😊", fill=(226, 232, 240))

draw_rounded_rect(draw1, (850, 340, 1140, 400), 16, (14, 165, 233))
draw1.text((870, 360), "感觉不错，准备开工！", fill=(255, 255, 255))

draw_rounded_rect(draw1, (700, 430, 1100, 530), 16, (20, 50, 80))
draw1.text((720, 450), "太好了！💪 精力充沛的时候", fill=(226, 232, 240))
draw1.text((720, 475), "正适合挑战重要任务。", fill=(226, 232, 240))
draw1.text((720, 500), "今天打算先做什么？", fill=(226, 232, 240))

# 输入框
draw_rounded_rect(draw1, (700, 560, 1060, 610), 12, (51, 65, 85))
draw1.text((720, 577), "输入消息...", fill=(100, 116, 139))

draw_rounded_rect(draw1, (1080, 560, 1140, 610), 12, (14, 165, 233))
draw1.text((1100, 577), "→", fill=(255, 255, 255))

img1.save('screenshot-1.png', 'PNG')
print("✅ screenshot-1.png")

# ========== 截图2 - 设置页面 ==========
img2 = create_gradient(width, height, (12, 25, 41), (26, 54, 93))
draw2 = ImageDraw.Draw(img2)

# 左侧说明
draw2.text((100, 250), "⚙️", fill=(255, 255, 255))
draw2.text((100, 320), "个性化你的", fill=(255, 255, 255))
draw2.text((100, 370), "早安体验", fill=(255, 255, 255))

draw2.text((100, 450), "⏰ 灵活的提醒时间", fill=(148, 163, 184))
draw2.text((100, 490), "🌴 周末可以休息", fill=(148, 163, 184))
draw2.text((100, 530), "🔔 桌面通知提醒", fill=(148, 163, 184))

# 设置卡片
draw_rounded_rect(draw2, (500, 100, 1180, 700), 20, (30, 41, 59))

# 头部
draw_rounded_rect(draw2, (500, 100, 1180, 180), 20, (12, 74, 110))
draw2.text((540, 130), "⚙️ MorningPal 设置", fill=(255, 255, 255))

# 提醒时间
draw_rounded_rect(draw2, (530, 210, 1150, 290), 12, (51, 65, 85))
draw2.text((560, 230), "⏰ 每日提醒时间", fill=(255, 255, 255))
draw2.text((560, 258), "设置你希望收到提醒的时间", fill=(100, 116, 139))
draw_rounded_rect(draw2, (1040, 235, 1120, 275), 8, (14, 165, 233))
draw2.text((1055, 247), "09:00", fill=(255, 255, 255))

# 周末提醒
draw_rounded_rect(draw2, (530, 310, 1150, 390), 12, (51, 65, 85))
draw2.text((560, 330), "📅 周末提醒", fill=(255, 255, 255))
draw2.text((560, 358), "周六周日也发送提醒", fill=(100, 116, 139))
draw_rounded_rect(draw2, (1060, 340, 1120, 370), 15, (71, 85, 105))
draw2.ellipse([1062, 342, 1088, 368], fill=(200, 200, 200))

# 桌面通知
draw_rounded_rect(draw2, (530, 410, 1150, 490), 12, (51, 65, 85))
draw2.text((560, 430), "🔔 桌面通知", fill=(255, 255, 255))
draw2.text((560, 458), "启用浏览器通知", fill=(100, 116, 139))
draw_rounded_rect(draw2, (1060, 440, 1120, 470), 15, (34, 197, 94))
draw2.ellipse([1090, 442, 1116, 468], fill=(255, 255, 255))

# 账户
draw_rounded_rect(draw2, (530, 510, 1150, 590), 12, (51, 65, 85))
draw2.text((560, 530), "👤 captain@example.com", fill=(255, 255, 255))
draw2.text((560, 558), "已登录", fill=(100, 116, 139))

# 保存按钮
draw_rounded_rect(draw2, (530, 620, 1150, 680), 12, (14, 165, 233))
draw2.text((790, 642), "💾 保存设置", fill=(255, 255, 255))

img2.save('screenshot-2.png', 'PNG')
print("✅ screenshot-2.png")

# ========== 截图3 - 功能亮点 ==========
img3 = create_gradient(width, height, (12, 25, 41), (26, 54, 93))
draw3 = ImageDraw.Draw(img3)

# 标题
draw3.text((530, 60), "🧭 MorningPal", fill=(255, 255, 255))
draw3.text((480, 110), "根据你的状态，给出个性化建议", fill=(148, 163, 184))

# 功能卡片
features = [
    (100, "⏰", "定时提醒", "每天设定时间", "收到温馨提醒"),
    (380, "🤖", "AI 对话", "自然聊天", "不是冷冰冰模板"),
    (660, "🔥", "连续打卡", "可视化坚持", "保持动力"),
    (940, "🔒", "隐私优先", "数据安全", "只属于你"),
]

for x, emoji, title, desc1, desc2 in features:
    draw_rounded_rect(draw3, (x, 180, x + 230, 420), 16, (30, 41, 59))
    draw3.ellipse([x + 70, 210, x + 160, 300], fill=(20, 60, 100))
    draw3.text((x + 100, 235), emoji, fill=(255, 255, 255))
    draw3.text((x + 75, 320), title, fill=(255, 255, 255))
    draw3.text((x + 50, 360), desc1, fill=(100, 116, 139))
    draw3.text((x + 40, 390), desc2, fill=(100, 116, 139))

# 状态说明
draw3.text((430, 470), "小航会根据你的状态调整建议", fill=(148, 163, 184))

states = [
    (100, "😊", "精力充沛", "→ 挑战重要任务"),
    (380, "😴", "疲惫不堪", "→ 从简单开始"),
    (660, "😰", "焦虑迷茫", "→ 拆解任务"),
    (940, "😑", "拖延症", "→ 找开始方法"),
]

for x, emoji, title, action in states:
    draw_rounded_rect(draw3, (x, 520, x + 230, 620), 12, (30, 41, 59))
    draw3.text((x + 20, 545), emoji, fill=(255, 255, 255))
    draw3.text((x + 60, 545), title, fill=(255, 255, 255))
    draw3.text((x + 40, 580), action, fill=(14, 165, 233))

# 底部
draw3.text((450, 700), "让每个早晨都充满方向感 ⛵✨", fill=(148, 163, 184))

img3.save('screenshot-3.png', 'PNG')
print("✅ screenshot-3.png")

print("\n🎉 完成！截图已保存到当前目录:")
print("   - screenshot-1.png (主界面)")
print("   - screenshot-2.png (设置页面)")
print("   - screenshot-3.png (功能亮点)")
print("\n📐 尺寸: 1280x800 PNG (无透明度)")
