<<<<<<< HEAD
@echo off
set arg1=%1
chrome https://www.google.com/search?q=%arg1%
=======
@echo off
echo Opening Google Chrome...
set /P input= Please enter an input:
::set arg1=%1
chrome https://www.google.com/search?q="%input%"
>>>>>>> 3baf57ceecff4eee51d0142a2791cab22e0a7317
