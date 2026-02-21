@echo off
cls
echo ╔═══════════════════════════════════════════════════════════╗
echo ║         SKILL SWAP - COMPLETE FIX AND RUN                ║
echo ║              All Errors Fixed - Ready to Go!              ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

echo [Step 1/3] Creating all missing templates...
python create_all_templates.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to create templates!
    pause
    exit /b 1
)
echo ✓ Templates created successfully!
echo.

echo [Step 2/3] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)
echo ✓ Virtual environment activated!
echo.

echo [Step 3/3] Starting Django server...
echo.
echo ═══════════════════════════════════════════════════════════
echo   Server will start at: http://127.0.0.1:8000/
echo   Press CTRL+C to stop the server
echo ═══════════════════════════════════════════════════════════
echo.
echo Ready URLs:
echo  • Home:       http://127.0.0.1:8000/
echo  • Register:   http://127.0.0.1:8000/users/register/
echo  • Login:      http://127.0.0.1:8000/users/login/
echo  • Dashboard:  http://127.0.0.1:8000/users/dashboard/
echo  • Search:     http://127.0.0.1:8000/users/search/
echo.
python manage.py runserver
