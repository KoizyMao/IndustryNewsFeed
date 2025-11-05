# 项目结构说明

## 目录结构

```
IndustryNewsFeed/
│
├── 📄 核心代码文件
│   ├── main.py                 # 主程序入口
│   ├── config.py              # 配置文件（包含敏感信息，不提交到Git）
│   ├── config.py.example      # 配置文件模板（不含敏感信息）
│   ├── news_collector.py      # 新闻收集模块（RSS + API）
│   ├── email_sender.py        # 邮件发送模块
│   └── utils.py               # 工具函数（去重、筛选等）
│
├── 📦 配置文件
│   ├── requirements.txt       # Python依赖包列表
│   └── .gitignore             # Git忽略文件配置
│
├── 📚 文档
│   ├── README.md              # 项目主文档（必读）
│   └── docs/                  # 详细文档文件夹
│       ├── QUICK_START.md     # 快速开始指南
│       └── SECURITY.md        # 安全配置指南
│
├── 🔧 脚本工具
│   └── scripts/               # 辅助脚本文件夹
│       ├── setup_env.bat      # 一键设置虚拟环境
│       └── schedule_task.bat  # 创建Windows定时任务
│
└── 💾 运行时文件（自动生成，不提交到Git）
    ├── venv/                  # Python虚拟环境
    ├── news_feed.log          # 程序运行日志
    └── news_cache.json        # 新闻去重缓存
```

## 文件说明

### 核心代码

- **main.py**: 程序入口，整合所有模块
- **config.py**: 配置文件，包含邮箱、授权码等敏感信息
- **news_collector.py**: 从RSS源和API收集新闻
- **email_sender.py**: 生成HTML邮件并发送
- **utils.py**: 工具函数，包括去重、筛选等

### 脚本工具

- **setup_env.bat**: 自动创建虚拟环境并安装依赖
- **schedule_task.bat**: 创建Windows定时任务

### 文档

- **README.md**: 项目主文档，包含快速开始和基本使用说明
- **docs/QUICK_START.md**: 详细的安装和配置步骤
- **docs/SECURITY.md**: 如何保护个人信息和配置安全

## 使用流程

1. **首次使用**：
   - 运行 `scripts\setup_env.bat` 设置环境
   - 复制 `config.py.example` 为 `config.py`
   - 编辑 `config.py` 填写您的信息
   - 运行 `python main.py` 测试

2. **设置定时任务**：
   - 以管理员身份运行 `scripts\schedule_task.bat`

## 注意事项

- ✅ `config.py` 包含敏感信息，不会被提交到Git
- ✅ 日志和缓存文件会自动生成，不需要手动创建
- ✅ 所有脚本都可以从项目根目录运行
- ✅ 虚拟环境文件夹 `venv/` 不应提交到Git

