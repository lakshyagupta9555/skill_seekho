@echo off
echo Setting up Django Skill Swap Platform...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install required packages
echo Installing Django and dependencies...
pip install django djangorestframework channels daphne pillow

REM Create directory structure
echo Creating directory structure...
python create_structure.py

REM Create Django apps
echo Creating Django apps...
python manage.py startapp users
python manage.py startapp dashboard
python manage.py startapp chat
python manage.py startapp video

echo.
echo Setup complete! Next steps:
echo 1. Run: python manage.py makemigrations
echo 2. Run: python manage.py migrate
echo 3. Run: python manage.py createsuperuser
echo 4. Run: python manage.py runserver
pause
