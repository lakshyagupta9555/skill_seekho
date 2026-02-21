@echo off
echo ========================================
echo SkillSwap - Complete Fix and Run
echo ========================================
echo.

cd /d "%~dp0"

echo Step 1: Checking virtual environment...
if not exist venv\Scripts\python.exe (
    echo ERROR: Virtual environment not found!
    echo Please run SETUP_PROJECT.bat first to create virtual environment
    pause
    exit /b 1
)

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat

echo Step 3: Checking Django installation...
python -c "import django; print('Django version:', django.get_version())" 2>nul
if errorlevel 1 (
    echo ERROR: Django not installed!
    echo Installing required packages...
    python -m pip install --quiet --upgrade pip
    python -m pip install --quiet -r requirements.txt
)

echo Step 4: Verifying project structure...
python manage.py check --deploy 2>nul
if errorlevel 1 (
    echo Running basic check...
    python manage.py check
)

echo.
echo Step 5: Database migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo ========================================
echo Setup complete! Starting server...
echo ========================================
echo.
echo Server will be available at: http://127.0.0.1:8000/
echo.
echo Login page: http://127.0.0.1:8000/users/login/
echo Register page: http://127.0.0.1:8000/users/register/
echo.
echo Press CTRL+C to stop the server
echo.

python manage.py runserver

pause
