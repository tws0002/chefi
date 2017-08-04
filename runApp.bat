@echo off
call Scripts\activate.bat
set FLASK_APP=mainApp.py
flask run
pause
