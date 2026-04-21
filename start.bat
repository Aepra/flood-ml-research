@echo off
REM ============================================================
REM   Flood ML Research - One Command Setup
REM   Simply run: start.bat
REM ============================================================

echo.
echo ============================================================
echo         FLOOD ML RESEARCH - Starting Docker
echo ============================================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker Desktop not found!
    echo.
    echo Please install Docker Desktop from:
    echo   https://www.docker.com/products/docker-desktop
    echo.
    pause
    exit /b 1
)

REM Start Docker Compose
echo Starting container... (this may take a few minutes on first run)
echo.

docker-compose up

echo.
echo ============================================================
echo         Container stopped
echo ============================================================
echo.

pause
