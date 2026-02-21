@echo off
color 0A
title Skill Swap Platform - Installation

echo.
echo ================================================================
echo                    SKILL SWAP PLATFORM
echo                    Installation Wizard
echo ================================================================
echo.
echo This will set up your complete skill exchange platform with:
echo   - User Authentication
echo   - Skill Management
echo   - Real-time Chat
echo   - Video Calling
echo   - Dark Theme UI
echo.
echo ================================================================
echo.

pause

echo.
echo [1/7] Building project structure...
echo ================================================================
python build_project.py
if errorlevel 1 (
    color 0C
    echo ERROR: Failed to build project structure
    pause
    exit /b 1
)
echo ✓ Project structure created
echo.

echo [2/7] Creating HTML templates...
echo ================================================================
python build_templates.py
if errorlevel 1 (
    color 0C
    echo ERROR: Failed to create templates
    pause
    exit /b 1
)
echo ✓ Templates created
echo.

echo [3/7] Activating virtual environment...
echo ================================================================
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated
echo.

echo [4/7] Installing Django and dependencies...
echo ================================================================
echo This may take a few minutes...
pip install -q Django djangorestframework channels daphne pillow
if errorlevel 1 (
    color 0C
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed
echo.

echo [5/7] Creating database migrations...
echo ================================================================
python manage.py makemigrations users dashboard chat video
if errorlevel 1 (
    color 0C
    echo ERROR: Failed to create migrations
    pause
    exit /b 1
)
echo ✓ Migrations created
echo.

echo [6/7] Applying migrations to database...
echo ================================================================
python manage.py migrate
if errorlevel 1 (
    color 0C
    echo ERROR: Failed to apply migrations
    pause
    exit /b 1
)
echo ✓ Database initialized
echo.

echo [7/7] Collecting static files...
echo ================================================================
python manage.py collectstatic --noinput
echo ✓ Static files ready
echo.

color 0A
echo.
echo ================================================================
echo                    INSTALLATION COMPLETE!
echo ================================================================
echo.
echo Your Skill Swap platform is ready to use!
echo.
echo 📝 Next Steps:
echo.
echo   1. Create an admin account:
echo      python manage.py createsuperuser
echo.
echo   2. Start the development server:
echo      python manage.py runserver
echo.
echo   3. Open your browser and visit:
echo      http://127.0.0.1:8000/
echo.
echo   4. Access admin panel at:
echo      http://127.0.0.1:8000/admin/
echo.
echo ================================================================
echo.
echo 💡 Quick Commands:
echo    - Start server: python manage.py runserver
echo    - Create user:  python manage.py createsuperuser
echo    - Shell:        python manage.py shell
echo.
echo 📚 Documentation:
echo    - See SETUP_GUIDE.md for detailed information
echo    - See PROJECT_SUMMARY.md for feature overview
echo.
echo ================================================================
echo.

set /p create_admin="Would you like to create an admin account now? (y/n): "
if /i "%create_admin%"=="y" (
    echo.
    python manage.py createsuperuser
)

echo.
set /p start_server="Would you like to start the server now? (y/n): "
if /i "%start_server%"=="y" (
    echo.
    echo Starting development server...
    echo Press Ctrl+C to stop the server
    echo.
    python manage.py runserver
) else (
    echo.
    echo When ready, run: python manage.py runserver
    echo.
)

pause
