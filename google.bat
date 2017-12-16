@echo off
echo Opening Google Chrome...
set /P input= Please enter an input:
::set arg1=%1
chrome https://www.google.com/search?q="%input%"