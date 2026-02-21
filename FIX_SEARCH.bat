@echo off
echo Fixing empty template files...

cd /d "%~dp0"

del templates\users\search.html 2>nul
copy templates\users\search_new.html templates\users\search.html

echo.
echo Template fixed!
echo.
pause
