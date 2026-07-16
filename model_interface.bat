@echo off
cd /d "%~dp0"

:: Set python path to use the virtual environment
set PYTHON_EXE=.venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

if "%1"=="" (
    "%PYTHON_EXE%" interactive_menu.py
) else if "%1"=="menu" (
    "%PYTHON_EXE%" interactive_menu.py
) else if "%1"=="help" (
    "%PYTHON_EXE%" -m src.model_cli --help
) else if "%1"=="train" (
    shift
    "%PYTHON_EXE%" -m src.model_cli train %*
) else if "%1"=="validate" (
    shift
    "%PYTHON_EXE%" -m src.model_cli validate %*
) else if "%1"=="test-single" (
    shift
    "%PYTHON_EXE%" -m src.model_cli test-single %*
) else if "%1"=="test-batch" (
    shift
    "%PYTHON_EXE%" -m src.model_cli test-batch %*
) else if "%1"=="config" (
    shift
    "%PYTHON_EXE%" -m src.model_cli config %*
) else if "%1"=="benchmark" (
    shift
    "%PYTHON_EXE%" -m src.model_cli benchmark %*
) else if "%1"=="test" (
    "%PYTHON_EXE%" -m src.test_model_interface
) else (
    "%PYTHON_EXE%" -m src.model_cli %*
)
