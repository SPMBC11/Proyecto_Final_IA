@echo off
REM ============================================================
REM Script para crear environment virtual y instalar paquetes
REM ============================================================
REM Ejecuta este archivo (.bat) en PowerShell o Command Prompt

echo.
echo ============================================================
echo CREAR ENVIRONMENT VIRTUAL PARA EL NOTEBOOK
echo ============================================================
echo.

REM Crear environment virtual
echo Creando environment virtual...
python -m venv env_colab

REM Activar environment
echo Activando environment...
call env_colab\Scripts\activate.bat

REM Instalar paquetes
echo.
echo Instalando paquetes necesarios...
echo (Esto puede tomar unos minutos)
echo.

pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel -q

REM Registrar kernel para Jupyter
python -m ipykernel install --user --name env_colab --display-name "Python (Colab Project)"

echo.
echo ============================================================
echo ✓ ¡Environment creado exitosamente!
echo ============================================================
echo.
echo Próximos pasos:
echo.
echo 1. ABRIR JUPYTER NOTEBOOK
echo    Ejecuta:  jupyter notebook
echo.
echo 2. O usa este environment en VS Code:
echo    - Ctrl+Shift+P
echo    - Escribe: "Python: Select Interpreter"
echo    - Elige: "env_colab"
echo.
echo 3. ACTIVAR ENVIRONMENT MANUALMENTE (si necesitas)
echo    En Command Prompt:  env_colab\Scripts\activate.bat
echo    En PowerShell:      .\env_colab\Scripts\Activate.ps1
echo.
echo ============================================================
pause
