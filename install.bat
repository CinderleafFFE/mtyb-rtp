@echo off
set guid=%random%%random%-%random%-%random%-%random%-%random%%random%%random%

mkdir %WINDIR%\%guid%>nul 2>&1
rmdir %WINDIR%\%guid%>nul 2>&1

IF %ERRORLEVEL% neq 0 (
    echo ��Ҫ�Թ���Ա���С�
    pause
    exit /b
)
set rtp_path="%ProgramFiles(x86)%\RPG Maker XP\RGSS"
echo ���밲װħ�� RTP ��λ�á�Ĭ���� Standard ͬĿ¼��
set /p rtp_path=
reg add HKLM\SOFTWARE\Enterbrain\RGSS\RTP /v Oksh_mtyb /d %rtp_path%\Oksh_mtyb\ /reg:32
robocopy /e "%~dp0\Oksh_mtyb.assets" %rtp_path%\Oksh_mtyb
pause
