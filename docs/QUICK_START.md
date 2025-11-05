# 快速开始指南

## 第一步：安装Python（如果还没有）

1. 访问 [Python官网](https://www.python.org/downloads/)
2. 下载 Python 3.7 或更高版本（推荐最新稳定版）
3. **重要**：安装时务必勾选 ✅ **"Add Python to PATH"**
4. 点击"Install Now"完成安装

## 第二步：创建虚拟环境并安装依赖

### 方法1：使用自动脚本（最简单）

直接双击运行 `setup_env.bat`，脚本会自动：
- 创建虚拟环境
- 安装所有依赖包

### 方法2：手动创建

打开命令提示符（CMD）或PowerShell，进入项目目录：

```bash
cd D:\IndustryNewsFeed

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

## 第三步：配置邮箱信息

编辑 `config.py` 文件，确保以下信息已配置：
- `SMTP_USERNAME`: 163邮箱地址
- `SMTP_PASSWORD`: 163邮箱授权码
- `RECIPIENT_EMAIL`: 收件人邮箱

## 第四步：测试运行

激活虚拟环境后运行：

```bash
python main.py
```

程序会：
1. 收集AI/AIGC相关新闻
2. 筛选并去重
3. 发送邮件到指定邮箱

## 第五步：设置定时任务（可选）

双击运行 `schedule_task.bat`（需要管理员权限），会自动创建每天定时执行的任务。

## 常见问题

### Q: 找不到python命令？
A: 确保安装Python时勾选了"Add Python to PATH"，或重新安装Python。

### Q: PowerShell无法激活虚拟环境？
A: 运行以下命令允许脚本执行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Q: 依赖安装失败？
A: 确保网络连接正常，或使用国内镜像：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q: 邮件发送失败？
A: 检查 `config.py` 中的SMTP配置，确保：
- 163邮箱已开启SMTP服务
- 使用的是授权码（不是登录密码）
- 收件人邮箱地址正确

## 查看日志

程序运行日志保存在 `news_feed.log` 文件中，可以查看详细执行信息。

