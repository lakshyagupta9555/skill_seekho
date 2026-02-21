@echo off
echo ================================================================
echo             SKILLSWAP - COMPLETE FIX SCRIPT
echo ================================================================
echo.

cd /d %~dp0

echo [1/4] Fixing profile template...
call FIX_PROFILE.bat >nul 2>&1

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Checking for missing migrations...
python manage.py makemigrations

echo [4/4] Applying migrations...
python manage.py migrate

echo.
echo ================================================================
echo                     ALL FIXES COMPLETE!
echo ================================================================
echo.
echo Your SkillSwap application is ready to run.
echo.
echo Starting the development server...
echo.
python manage.py runserver
