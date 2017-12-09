@echo off
set searchq=%1%2
echo Opening Facebook...
if "%searchq%" == "" (chrome https://www.facebook.com/) else (chrome https://www.facebook.com/search/top/?q="%1 %2")

