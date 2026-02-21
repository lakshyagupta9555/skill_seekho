@echo off
echo ========================================
echo    FIXING MANAGE.PY AND STARTING SERVER
echo ========================================
echo.

echo Step 1: Backing up old manage.py...
if exist manage.py (
    copy manage.py manage_backup.py.old >nul 2>&1
    echo Old manage.py backed up
)

echo Step 2: Replacing manage.py...
copy /Y manage_new.py manage.py >nul 2>&1
echo manage.py has been fixed!

echo.
echo Step 3: Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Step 4: Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo Step 5: Starting Django development server...
echo.
echo ========================================
echo Server will start at http://127.0.0.1:8000/
echo Press CTRL+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause
