@echo off
echo Opening Google Chrome...
set arg1=%*
if not "%arg1%" == "" (
    set input="%arg1%"
    goto :PROCESS
)
set /P input= Please enter an input:
::set arg1=%1
:PROCESS
chrome https://www.google.com/search?q="%input%"
