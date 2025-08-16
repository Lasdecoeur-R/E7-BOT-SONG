@echo off
echo ========================================
echo    Installation du Bot Controleur
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

echo Installation des dependances...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERREUR: Impossible d'installer les dependances
    echo.
    echo Essayez cette commande a la place:
    echo python -m pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo    Installation terminee avec succes!
echo ========================================
echo.
echo Pour lancer le bot, tapez:
echo python bot_controller.py
echo.
echo Ou double-cliquez sur "lancer_bot.bat"
echo.
pause

