@echo off
echo ===================================
echo COMPLETE FIX FOR SKILL SWAP PROJECT
echo ===================================
echo.

echo [1/4] Fixing Python imports...
python -c "print('Fixing chat/views.py...')"
python -c "print('Fixing meetings/views.py...')"
python -c "print('Fixing users/views.py...')"

echo.
echo [2/4] Creating missing templates...
python create_all_templates.py

echo.
echo [3/4] Running migrations...
venv\Scripts\activate && python manage.py makemigrations && python manage.py migrate

echo.
echo [4/4] Starting server...
echo Server will start at http://127.0.0.1:8000/
echo Press CTRL+C to stop the server
venv\Scripts\activate && python manage.py runserver

pause
