# 自动化行业新闻订阅系统

一个自动化的AI/AIGC行业新闻订阅系统，每天自动收集最新的AI和AIGC相关新闻，并通过邮件发送到指定邮箱。

## 功能特性

- 📰 **多源新闻收集**：支持RSS订阅源和新闻API两种方式
- 🤖 **智能筛选**：自动筛选AI/AIGC相关内容
- 🔄 **自动去重**：避免重复新闻
- 📧 **邮件发送**：生成精美的HTML格式邮件
- ⏰ **定时任务**：支持Windows任务计划程序自动执行

## 项目结构

```
IndustryNewsFeed/
├── main.py                 # 主程序入口
├── config.py              # 配置文件（需要您自己创建，包含敏感信息）
├── config.py.example      # 配置文件模板（不含敏感信息）
├── news_collector.py      # 新闻收集模块
├── email_sender.py        # 邮件发送模块
├── utils.py               # 工具函数
├── requirements.txt       # Python依赖包
├── README.md              # 项目说明文档
│
├── scripts/               # 辅助脚本
│   ├── setup_env.bat      # 一键设置虚拟环境
│   └── schedule_task.bat  # 创建Windows定时任务
│
└── docs/                  # 文档
    ├── QUICK_START.md     # 快速开始指南
    └── SECURITY.md        # 安全配置指南
```

## 快速开始

### 1. 安装Python

确保您的系统已安装Python 3.7或更高版本。访问 [Python官网](https://www.python.org/downloads/) 下载。

### 2. 设置环境

**方法1：使用自动脚本（推荐）**

双击运行 `scripts\setup_env.bat`，脚本会自动：
- 创建虚拟环境
- 安装所有依赖包

**方法2：手动设置**

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# PowerShell:
venv\Scripts\Activate.ps1
# 或 CMD:
venv\Scripts\activate.bat

# 安装依赖
pip install -r requirements.txt
```

### 3. 配置系统

复制 `config.py.example` 为 `config.py`，然后编辑 `config.py` 填写您的信息：

```python
SMTP_USERNAME = 'your_email@163.com'  # 您的163邮箱地址
SMTP_PASSWORD = 'your_auth_code'      # 163邮箱授权码（不是登录密码）
RECIPIENT_EMAIL = 'recipient@example.com'  # 收件人邮箱
```

**获取163邮箱授权码：**
1. 登录163邮箱
2. 进入"设置" → "POP3/SMTP/IMAP"
3. 开启"POP3/SMTP服务"
4. 点击"生成授权码"

### 4. 测试运行

```bash
python main.py
```

程序会：
1. 收集AI/AIGC相关新闻
2. 筛选并去重
3. 发送邮件到指定邮箱

## 设置定时任务

以管理员身份运行 `scripts\schedule_task.bat`，脚本会自动创建每天上午9点执行的任务。

或手动创建任务：
1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器为"每天"
4. 程序路径：`python`
5. 参数：`D:\IndustryNewsFeed\main.py`（请改为您的实际路径）

## 配置文件说明

### config.py 主要配置项

- `SMTP_HOST`: SMTP服务器地址（默认：smtp.163.com）
- `SMTP_PORT`: SMTP端口（默认：465）
- `SMTP_USERNAME`: 163邮箱账号
- `SMTP_PASSWORD`: 163邮箱授权码
- `RECIPIENT_EMAIL`: 收件人邮箱地址
- `NEWS_API_KEY`: NewsAPI密钥（可选）
- `RSS_FEEDS`: RSS订阅源列表（可自定义）
- `AI_KEYWORDS`: AI/AIGC相关关键词列表（可自定义）

## 日志和缓存

- **日志文件**：`news_feed.log`（程序运行日志）
- **缓存文件**：`news_cache.json`（新闻去重记录，自动清理30天前的记录）

## 故障排除

### 邮件发送失败
- 检查SMTP配置是否正确
- 确认使用的是授权码（不是登录密码）
- 查看 `news_feed.log` 日志文件

### 未收集到新闻
- 检查网络连接
- 某些RSS源可能暂时不可用
- 查看日志文件了解详情

### 定时任务未执行
- 确认任务已创建并启用
- 检查Python路径是否正确
- 查看任务计划程序中的执行历史

## 更多文档

- 📖 [快速开始指南](docs/QUICK_START.md) - 详细的安装和配置步骤
- 🔒 [安全配置指南](docs/SECURITY.md) - 如何保护您的个人信息

## 自定义和扩展

### 添加新的RSS源

在 `config.py` 的 `RSS_FEEDS` 列表中添加新的RSS URL。

### 修改关键词

在 `config.py` 的 `AI_KEYWORDS` 列表中添加或删除关键词。

### 修改邮件模板

编辑 `email_sender.py` 中的 `generate_email_html()` 函数来自定义邮件样式。

## 许可证

本项目仅供个人学习和使用。

## 支持

如有问题或建议，请查看日志文件或联系开发者。
