@echo off
chcp 65001 >nul 2>&1
echo ========================================
echo Cleanup Old Scheduled Task
echo ========================================
echo.

echo Checking for old task "AI新闻订阅"...
schtasks /Query /TN "AI新闻订阅" >nul 2>&1
if errorlevel 1 (
    echo Old task not found or already deleted.
) else (
    echo Found old task. Deleting...
    schtasks /Delete /TN "AI新闻订阅" /F
    if errorlevel 1 (
        echo Error: Failed to delete old task. Please run as Administrator.
    ) else (
        echo Old task deleted successfully.
    )
)

echo.
echo Checking for task "AI_News_Feed"...
schtasks /Query /TN "AI_News_Feed" >nul 2>&1
if errorlevel 1 (
    echo Task "AI_News_Feed" does not exist yet.
    echo You can create it by running: scripts\schedule_task.bat
) else (
    echo Task "AI_News_Feed" already exists.
)

echo.
pause

