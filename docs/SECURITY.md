# 安全配置指南

## 个人信息保护

本项目已配置保护您的个人信息，但请确保正确设置。

## 保护措施

### 1. 配置文件保护

`config.py` 文件包含敏感信息（邮箱、授权码），请妥善保管，**不要分享给他人**。

### 2. 敏感文件清单

以下文件包含敏感信息，请妥善保管：
- `config.py` - 配置文件（包含邮箱和授权码）
- `news_feed.log` - 日志文件（可能包含邮箱地址）
- `news_cache.json` - 缓存文件

### 3. 配置文件模板

项目包含 `config.py.example` 作为模板，**不包含任何敏感信息**，可以安全分享。

## 配置您的个人信息

### 方法1：直接编辑 config.py（推荐用于本地开发）

1. 复制 `config.py.example` 为 `config.py`（如果还没有）
2. 编辑 `config.py`，填写您的信息：
   ```python
   SMTP_USERNAME = 'your_email@163.com'  # 您的163邮箱
   SMTP_PASSWORD = 'your_auth_code'      # 163邮箱授权码
   RECIPIENT_EMAIL = 'recipient@example.com'  # 收件人邮箱
   ```

### 方法2：使用环境变量（推荐用于生产环境）

在Windows PowerShell中：
```powershell
$env:SMTP_USERNAME="your_email@163.com"
$env:SMTP_PASSWORD="your_auth_code"
$env:RECIPIENT_EMAIL="recipient@example.com"
```

在Windows CMD中：
```cmd
set SMTP_USERNAME=your_email@163.com
set SMTP_PASSWORD=your_auth_code
set RECIPIENT_EMAIL=recipient@example.com
```

## 安全配置检查清单

✅ **配置前请确保**：

1. **确认 config.py 包含敏感信息**
   - 配置文件包含邮箱和授权码
   - 不要将 `config.py` 分享给他人
   - 使用 `config.py.example` 作为模板

2. **清除日志文件**（如果包含个人信息）
   - 定期清理 `news_feed.log`（如果包含邮箱地址）
   - 日志文件会自动生成，包含运行信息

3. **环境变量方式更安全**
   - 推荐使用环境变量存储敏感信息
   - 避免在代码中硬编码密码

## 如果敏感信息泄露

### 立即采取措施：

1. **更改所有暴露的密码/授权码**
   - 163邮箱：立即重新生成授权码
   - 其他服务：立即更改密码

2. **检查并更新配置**
   - 更新 `config.py` 中的敏感信息
   - 或使用新的环境变量

## 最佳实践

1. ✅ **使用环境变量**存储敏感信息
2. ✅ **永远不要分享**包含真实密码/密钥的文件
3. ✅ **妥善保管**配置文件，不要上传到公共平台
4. ✅ **定期检查**日志文件是否包含敏感信息
5. ✅ **使用配置文件模板**（如 `config.py.example`）分享给他人

## 获取163邮箱授权码

1. 登录163邮箱
2. 进入"设置" → "POP3/SMTP/IMAP"
3. 开启"POP3/SMTP服务"
4. 点击"生成授权码"
5. 将授权码保存到环境变量或 `config.py`（本地）

## 需要帮助？

如果发现任何安全问题，请：
1. 立即更改所有相关密码和授权码
2. 检查配置文件是否泄露
3. 更新所有敏感信息

