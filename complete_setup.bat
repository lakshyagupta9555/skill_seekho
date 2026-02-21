@echo off
echo ========================================
echo   Skill Swap Platform - Complete Setup
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Step 1: Creating project structure...
python build_project.py
if errorlevel 1 (
    echo ERROR: Failed to create project structure
    pause
    exit /b 1
)
echo.

echo Step 2: Creating templates...
python build_templates.py
if errorlevel 1 (
    echo ERROR: Failed to create templates
    pause
    exit /b 1
)
echo.

echo Step 3: Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo WARNING: Could not activate virtual environment
)
echo.

echo Step 4: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo Step 5: Creating migrations...
python manage.py makemigrations
if errorlevel 1 (
    echo ERROR: Failed to create migrations
    pause
    exit /b 1
)
echo.

echo Step 6: Running migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)
echo.

echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a superuser: python manage.py createsuperuser
echo 2. Run the server: python manage.py runserver
echo 3. Visit: http://127.0.0.1:8000/
echo.
echo For more information, see SETUP_GUIDE.md
echo.
pause
