@echo off
REM Windows定时任务创建脚本
REM 使用方法：以管理员身份运行此脚本

echo ========================================
echo 创建自动化新闻订阅定时任务
echo ========================================

REM 获取当前脚本所在目录（scripts文件夹）
set SCRIPT_DIR=%~dp0
REM 获取项目根目录（上一级目录）
set PROJECT_DIR=%SCRIPT_DIR%..
set PYTHON_PATH=python
set SCRIPT_PATH=%PROJECT_DIR%\main.py

REM 检查Python是否可用
%PYTHON_PATH% --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未找到Python，请确保Python已安装并添加到PATH
    pause
    exit /b 1
)

REM 检查main.py是否存在
if not exist "%SCRIPT_PATH%" (
    echo 错误：未找到main.py文件
    pause
    exit /b 1
)

echo.
echo 脚本路径: %SCRIPT_PATH%
echo Python路径: %PYTHON_PATH%
echo.

REM 创建任务计划（每天上午9点执行）
schtasks /Create /TN "AI新闻订阅" /TR "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" /SC DAILY /ST 09:00 /F

if errorlevel 1 (
    echo.
    echo 错误：创建任务失败
    echo 请确保以管理员身份运行此脚本
    pause
    exit /b 1
)

echo.
echo ========================================
echo 任务创建成功！
echo ========================================
echo.
echo 任务名称: AI新闻订阅
echo 执行时间: 每天 09:00
echo 执行命令: %PYTHON_PATH% %SCRIPT_PATH%
echo.
echo 如需修改执行时间，请使用以下命令：
echo schtasks /Change /TN "AI新闻订阅" /ST 新时间（格式：HH:MM）
echo.
echo 如需删除任务，请使用以下命令：
echo schtasks /Delete /TN "AI新闻订阅" /F
echo.
pause

