@echo off
set WAIT_TIME=20
cd "C:\Program Files\NordVPN\"
set vpn_group=%1
echo connect %vpn_group%

nordvpn -c -g %vpn_group%
@REM timeout /t %WAIT_TIME% >nul  