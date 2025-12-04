@echo off
REM This script should be run AFTER restarting your computer
REM It will build the Tauri desktop application

echo.
echo ========================================
echo Astron RPA - Desktop App Build
echo ========================================
echo.

REM Set up environment with all required tools
setlocal enabledelayedexpansion
set "SWIG_PATH=C:\Users\Admin\AppData\Local\Microsoft\WinGet\Packages\SWIG.SWIG_Microsoft.Winget.Source_8wekyb3d8bbwe\swigwin-4.4.0"
set "PATH=%PATH%;!SWIG_PATH!"

REM Verify tools are available
echo Checking required tools...
cargo --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Cargo not found. Rust may not be installed.
    exit /b 1
)
echo ✓ Cargo is available

link.exe >nul 2>&1
if errorlevel 1 (
    echo ERROR: link.exe not found. Visual Studio C++ tools not installed.
    echo Please ensure Visual Studio Build Tools with C++ workload is installed.
    exit /b 1
)
echo ✓ MSVC linker (link.exe) is available

echo ✓ All tools ready
echo.

REM Start the build
echo Starting Tauri desktop app build...
echo.

cd /d E:\astron-rpa\frontend
pnpm build:tauri-debug

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo Installer location:
echo E:\astron-rpa\frontend\packages\tauri-app\src-tauri\target\release\bundle\msi\
echo.
pause
