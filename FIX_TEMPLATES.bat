@echo off
echo Fixing all templates and views...
echo.

cd /d "%~dp0"

REM Copy the new exchange_detail template
if exist "templates\skills\exchange_detail_new.html" (
    copy /Y "templates\skills\exchange_detail_new.html" "templates\skills\exchange_detail.html"
    echo Fixed exchange_detail.html
)

echo.
echo All fixes applied!
echo.
echo You can now run: python manage.py runserver
pause
