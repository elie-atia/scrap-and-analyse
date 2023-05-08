@echo off
set WAIT_TIME=1
cd "C:\Program Files\NordVPN\"
nordvpn -d
@REM echo deconnect
@REM timeout /t %WAIT_TIME% >nul  