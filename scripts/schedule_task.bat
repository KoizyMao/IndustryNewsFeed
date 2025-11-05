@echo off
chcp 65001 >nul 2>&1
REM Windows定时任务创建脚本
REM 使用方法：以管理员身份运行此脚本

echo ========================================
echo Create Scheduled Task for News Feed
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
    echo Error: Python not found. Please ensure Python is installed and added to PATH
    pause
    exit /b 1
)

REM 检查main.py是否存在
if not exist "%SCRIPT_PATH%" (
    echo Error: main.py file not found
    pause
    exit /b 1
)

echo.
echo Script Path: %SCRIPT_PATH%
echo Python Path: %PYTHON_PATH%
echo.

REM 创建任务计划（每天上午9点执行）
schtasks /Create /TN "AI_News_Feed" /TR "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" /SC DAILY /ST 09:00 /F

if errorlevel 1 (
    echo.
    echo Error: Failed to create scheduled task
    echo Please run this script as Administrator
    pause
    exit /b 1
)

echo.
echo ========================================
echo Task Created Successfully!
echo ========================================
echo.
echo Task Name: AI_News_Feed
echo Schedule: Daily at 09:00
echo Command: %PYTHON_PATH% %SCRIPT_PATH%
echo.
echo To change the schedule time, use:
echo   schtasks /Change /TN "AI_News_Feed" /ST HH:MM
echo.
echo To delete the task, use:
echo   schtasks /Delete /TN "AI_News_Feed" /F
echo.
pause

