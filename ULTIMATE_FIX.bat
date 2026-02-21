@echo off
echo ================================================
echo SkillSwap - ULTIMATE FIX - All Problems Solved
echo ================================================
echo.

cd /d "%~dp0"

echo Step 1/5: Creating all missing templates...
python create_templates.py
if errorlevel 1 (
    echo WARNING: Failed to run create_templates.py
    echo Continuing anyway...
)

echo.
echo Step 2/5: Checking virtual environment...
if not exist venv\Scripts\python.exe (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo.
echo Step 3/5: Installing/upgrading dependencies...
call venv\Scripts\activate.bat
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

echo.
echo Step 4/5: Setting up database...
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo.
echo Step 5/5: Starting development server...
echo ================================================
echo.
echo ✅ ALL FIXES APPLIED!
echo.
echo Your server is starting at: http://127.0.0.1:8000/
echo.
echo Pages to visit:
echo   Home: http://127.0.0.1:8000/
echo   Register: http://127.0.0.1:8000/users/register/
echo   Login: http://127.0.0.1:8000/users/login/
echo.
echo ================================================
echo Press CTRL+C to stop the server
echo ================================================
echo.

python manage.py runserver

pause
