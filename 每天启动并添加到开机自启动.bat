@echo off
schtasks /Create /TN "guet_network_login" /TR login.py /RU %username% /SC DAILY /MO 1
echo success
echo start login.py > "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\guet_login.bat"

