@echo off
echo ========================================
echo    Lancement du Bot Controleur
echo ========================================
echo.

echo Verification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe!
    echo.
    echo Veuillez installer Python depuis https://www.python.org/downloads/
    echo IMPORTANT: Cochez "Add Python to PATH" lors de l'installation
    echo.
    pause
    exit /b 1
)

echo Python detecte avec succes!
echo.

echo Lancement du bot...
python bot_controller.py

if errorlevel 1 (
    echo.
    echo ERREUR: Impossible de lancer le bot
    echo.
    echo Verifiez que toutes les dependances sont installees:
    echo pip install -r requirements.txt
    echo.
    pause
)

