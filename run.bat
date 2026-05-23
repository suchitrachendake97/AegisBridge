@echo off
title AegisBridge
color 0A
cls
echo.
echo  =====================================================
echo   AEGISBRIDGE  -  AI Bridge Health Monitor
echo  =====================================================
echo.

:: Check Python
where python >nul 2>&1
if %errorlevel%==0 (
    python --version 2>&1 | findstr "Python 3" >nul
    if %errorlevel%==0 ( set PY=python & goto :run )
)
where py >nul 2>&1
if %errorlevel%==0 ( set PY=py & goto :run )

echo  [ERROR] Python 3 is not installed!
echo.
echo  Install it FREE from: https://www.python.org/downloads/
echo  During install: tick "Add Python to PATH" checkbox.
echo.
pause
exit /b 1

:run
if not exist "%~dp0server.py" (
    echo  [ERROR] server.py missing from this folder!
    pause & exit /b 1
)
if not exist "%~dp0AegisBridge.html" (
    echo  [ERROR] AegisBridge.html missing from this folder!
    pause & exit /b 1
)
echo  [OK] Python found
echo  [OK] All files found
echo.
echo  Starting at http://localhost:5000
echo  Browser will open automatically.
echo.
echo  !! DO NOT CLOSE THIS WINDOW !!
echo  Press Ctrl+C to stop when done.
echo  ─────────────────────────────────────────────────────
cd /d "%~dp0"
%PY% server.py
echo.
echo  Server stopped. Press any key to close.
pause >nul
