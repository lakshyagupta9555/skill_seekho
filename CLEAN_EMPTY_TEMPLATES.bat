@echo off
echo ================================================
echo Fixing All Empty Template Files
echo ================================================
echo.

cd /d "%~dp0"

echo Removing empty template files...
del /F /Q templates\users\profile.html 2>nul
del /F /Q templates\users\edit_profile.html 2>nul
del /F /Q templates\users\add_skill.html 2>nul
del /F /Q templates\users\add_interest.html 2>nul
del /F /Q templates\users\search.html 2>nul
del /F /Q templates\skills\exchange_list.html 2>nul
del /F /Q templates\skills\exchange_detail.html 2>nul
del /F /Q templates\skills\create_exchange.html 2>nul
del /F /Q templates\chat\chat_list.html 2>nul
del /F /Q templates\chat\chat_room.html 2>nul
del /F /Q templates\meetings\meeting_list.html 2>nul
del /F /Q templates\meetings\meeting_detail.html 2>nul
del /F /Q templates\meetings\create_meeting.html 2>nul

echo.
echo Renaming profile_new.html to profile.html...
move /Y templates\users\profile_new.html templates\users\profile.html 2>nul

echo.
echo ================================================
echo Template cleanup complete!
echo.
echo Now run COMPLETE_FIX_AND_RUN.bat to create
echo all missing templates and start the server.
echo ================================================
pause
