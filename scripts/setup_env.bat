@echo off
chcp 65001 >nul
echo ========================================
echo 快速设置Python虚拟环境
echo ========================================
echo.

REM 切换到项目根目录（如果脚本在scripts文件夹中）
cd /d %~dp0..
set PROJECT_DIR=%CD%

REM 检查是否已存在虚拟环境
if exist "%PROJECT_DIR%\venv" (
    echo 虚拟环境已存在！
    echo.
    echo 激活虚拟环境：
    echo   PowerShell: %PROJECT_DIR%\venv\Scripts\Activate.ps1
    echo   CMD: %PROJECT_DIR%\venv\Scripts\activate.bat
    echo.
    pause
    exit /b 0
)

echo 项目目录: %PROJECT_DIR%
echo 正在创建虚拟环境...
echo.

REM 尝试不同的Python命令
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo 使用 python 命令创建虚拟环境...
    python -m venv "%PROJECT_DIR%\venv"
    if %errorlevel% equ 0 goto :success
)

python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo 使用 python3 命令创建虚拟环境...
    python3 -m venv "%PROJECT_DIR%\venv"
    if %errorlevel% equ 0 goto :success
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo 使用 py 命令创建虚拟环境...
    py -m venv "%PROJECT_DIR%\venv"
    if %errorlevel% equ 0 goto :success
)

echo.
echo ========================================
echo 错误：未找到Python！
echo ========================================
echo.
echo 请先安装Python：
echo 1. 访问 https://www.python.org/downloads/
echo 2. 下载Python 3.7或更高版本
echo 3. 安装时务必勾选 "Add Python to PATH"
echo 4. 安装完成后重新运行此脚本
echo.
pause
exit /b 1

:success
if not exist "%PROJECT_DIR%\venv" (
    echo.
    echo 错误：虚拟环境创建失败！
    pause
    exit /b 1
)

echo.
echo ========================================
echo 虚拟环境创建成功！
echo ========================================
echo.

REM 激活虚拟环境并安装依赖
echo 正在激活虚拟环境并安装依赖包...
call "%PROJECT_DIR%\venv\Scripts\activate.bat"

if %errorlevel% equ 0 (
    echo.
    echo 虚拟环境已激活
    echo 正在安装依赖包...
    pip install --upgrade pip
    pip install -r requirements.txt
    
    if %errorlevel% equ 0 (
        echo.
        echo ========================================
        echo 安装完成！
        echo ========================================
        echo.
        echo 现在可以运行程序了：
        echo   cd %PROJECT_DIR%
        echo   python main.py
        echo.
        echo 或者激活虚拟环境后运行：
        echo   %PROJECT_DIR%\venv\Scripts\activate.bat
        echo   python main.py
    ) else (
        echo.
        echo 警告：依赖包安装可能有问题
        echo 请手动运行: pip install -r requirements.txt
    )
) else (
    echo.
    echo 无法自动激活虚拟环境
    echo 请手动激活：
    echo   venv\Scripts\activate.bat
    echo 然后运行: pip install -r requirements.txt
)

echo.
pause

