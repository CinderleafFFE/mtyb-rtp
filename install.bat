@echo off
set guid=%random%%random%-%random%-%random%-%random%-%random%%random%%random%

mkdir %WINDIR%\%guid%>nul 2>&1
rmdir %WINDIR%\%guid%>nul 2>&1

IF %ERRORLEVEL% neq 0 (
    echo 需要以管理员运行。
    pause
    exit /b
)
set rtp_path="%ProgramFiles(x86)%\RPG Maker XP\RGSS"
echo 输入安装魔塔 RTP 的位置。默认与 Standard 同目录。
set /p rtp_path=
reg add HKLM\SOFTWARE\Enterbrain\RGSS\RTP /v Oksh_mtyb /d %rtp_path%\Oksh_mtyb\ /reg:32
robocopy /e "%~dp0\Oksh_mtyb.assets" %rtp_path%\Oksh_mtyb
pause
