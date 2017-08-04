@echo off
call Scripts\activate.bat
set FLASK_APP=source\mainApp.py
flask run
pause
