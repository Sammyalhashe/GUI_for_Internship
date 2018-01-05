


@ECHO off
::set searchq=%1%2
set /P prompt= Want main page? [y/n]
::GOTO:EOF
IF "%prompt%"=="y" (GOTO:MAIN) ELSE GOTO:PERSON

:MAIN
ECHO Opening Facebook...
(chrome https://www.facebook.com/)
GOTO END

:PERSON
ECHO Opening Facebook Search...
set /P search= Search Person:
(chrome https://www.facebook.com/search/top/?q="%search%")

:END

