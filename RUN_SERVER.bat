@echo off
echo ========================================
echo Starting SkillSwap Development Server
echo ========================================
echo.

cd /d "%~dp0"

if not exist venv\Scripts\python.exe (
    echo ERROR: Virtual environment not found!
    echo Please run SETUP_PROJECT.bat first
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Django development server...
echo Server will be available at: http://127.0.0.1:8000/
echo Press CTRL+C to stop the server
echo.

python manage.py runserver

pause
