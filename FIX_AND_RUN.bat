@echo off
echo ========================================
echo Fixing Import Error and Running Server
echo ========================================
echo.

cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Django development server...
echo.
python manage.py runserver

pause
