@echo off
setlocal
echo ========================================================
echo   Multi-Scale Artifact Reduction - Setup ^& Launch
echo ========================================================
echo.

:: 1. Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not added to your PATH.
    echo Please install Python 3.8+ from python.org and check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

:: 2. Create virtual environment if it doesn't exist
IF NOT EXIST ".venv" (
    echo [1/3] Creating Python virtual environment ^(.venv^)...
    python -m venv .venv
    IF %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
) ELSE (
    echo [1/3] Virtual environment already exists.
)

:: 3. Activate the virtual environment
call .venv\Scripts\activate.bat

:: 4. Install requirements
echo [2/3] Installing/verifying dependencies...
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

:: 5. Run the application
echo.
echo [3/3] Launching Streamlit Application...
echo.

streamlit run app.py

:: 6. Keep the terminal open if the app crashes
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Application closed unexpectedly.
    pause
)
