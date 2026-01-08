# 🧭 MorningPal - 小航

> 每天早上帮你找到工作节奏的 AI 助手 ⛵

[![Chrome Web Store](https://img.shields.io/badge/Chrome-Extension-4285F4?logo=googlechrome&logoColor=white)](https://chrome.google.com/webstore)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## ✨ 什么是 MorningPal？

**MorningPal（小航）** 是一个智能早安教练，帮助你：

- 🌅 每天早上以积极的心态开始新的一天
- 📝 规划今天最重要的 1-3 件事
- 💪 建立持续的早起习惯，记录连续打卡天数
- 🧠 通过 AI 对话获得个性化的建议和鼓励

## 🚀 两种使用方式

### 1️⃣ 命令行版本（CLI）（推荐）

适合喜欢在终端工作的开发者。

```bash
# 安装依赖
cd cli
pip3 install -r requirements.txt

# 设置 API Key 并运行
export STEPFUN_API_KEY="你的API密钥"
python3 morningpal.py

# 或者直接运行启动脚本（需要先编辑 start.sh 填入 API Key）
./start.sh
```

### 2️⃣ Chrome 扩展（实验中暂时不推荐）

适合喜欢在浏览器中使用的用户，支持定时提醒。

```
chrome-extension/
├── manifest.json      # 扩展配置
├── popup.html/js      # 弹出窗口
├── options.html/js    # 设置页面
├── background.js      # 后台服务（提醒功能）
└── icons/             # 图标
```

**安装方法：**
1. 打开 Chrome，访问 `chrome://extensions/`
2. 开启「开发者模式」
3. 点击「加载已解压的扩展程序」
4. 选择 `chrome-extension` 文件夹

## 🔧 配置

### 获取 API Key

MorningPal 使用 [Stepfun](https://platform.stepfun.com/) 的 AI 服务。你需要：

1. 访问 [Stepfun 平台](https://platform.stepfun.com/)
2. 注册账号并创建 API Key
3. 将 API Key 配置到扩展设置或环境变量中

### Chrome 扩展配置

1. 点击扩展图标
2. 登录或注册账户
3. 在设置页面配置提醒时间

### CLI 配置

在 `cli` 目录创建 `.env` 文件：

```env
STEPFUN_API_KEY=你的API密钥
```


## 📁 项目结构

```
morningpal/
├── chrome-extension/   # Chrome 扩展
│   ├── icons/         # 扩展图标
│   ├── styles/        # 样式文件
│   └── promo/         # 商店截图
├── cli/               # 命令行版本
│   ├── morningpal.py  # 主程序
│   ├── requirements.txt
│   └── start.sh       # 启动脚本
├── docs/              # 文档
│   ├── privacy-policy.md
│   └── privacy-policy.html
└── README.md
```

## 🔒 隐私政策

MorningPal 尊重你的隐私：

- 所有对话数据存储在本地
- 仅在与 AI 交互时发送必要的消息内容
- 不收集任何个人身份信息

详见 [隐私政策](docs/privacy-policy.md)

## 🛠️ 技术栈

- **Chrome 扩展**: Manifest V3, Vanilla JS
- **CLI**: Python 3.9+, Rich, OpenAI SDK
- **AI 服务**: Stepfun API

## 📄 开源协议

MIT License © 2026 [Lykosteng](https://github.com/Lykosteng)

---

<p align="center">
  <b>每一个美好的早晨，都从和小航的对话开始 🌅</b>
</p>
