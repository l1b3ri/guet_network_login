@echo off
schtasks /Create /TN "guet_network_login" /TR login.py /RU %username% /SC DAILY
echo success
echo start login.py > "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\guet_login.bat"

