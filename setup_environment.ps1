# ============================================================
# Script PowerShell para crear environment virtual
# ============================================================
# Ejecuta este archivo en PowerShell con:
# powershell -ExecutionPolicy Bypass -File setup_environment.ps1

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "CREAR ENVIRONMENT VIRTUAL PARA EL NOTEBOOK" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Crear environment virtual
Write-Host "📦 Creando environment virtual..." -ForegroundColor Yellow
python -m venv env_colab

# Activar environment
Write-Host "🔧 Activando environment..." -ForegroundColor Yellow
& .\env_colab\Scripts\Activate.ps1

# Instalar paquetes
Write-Host ""
Write-Host "📥 Instalando paquetes necesarios..." -ForegroundColor Yellow
Write-Host "   (Esto puede tomar unos minutos)" -ForegroundColor Gray
Write-Host ""

pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel -q

# Registrar kernel para Jupyter
Write-Host ""
Write-Host "📝 Registrando kernel para Jupyter..." -ForegroundColor Yellow
python -m ipykernel install --user --name env_colab --display-name "Python (Colab Project)"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "✓ ¡Environment creado exitosamente!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""

Write-Host "Próximos pasos:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1️⃣ OPCIÓN A: Abrir Jupyter Notebook" -ForegroundColor White
Write-Host "   Ejecuta en PowerShell:  jupyter notebook" -ForegroundColor Gray
Write-Host ""
Write-Host "2️⃣ OPCIÓN B: Usar environment en VS Code" -ForegroundColor White
Write-Host "   - Presiona: Ctrl+Shift+P" -ForegroundColor Gray
Write-Host "   - Escribe: 'Python: Select Interpreter'" -ForegroundColor Gray
Write-Host "   - Elige: 'env_colab'" -ForegroundColor Gray
Write-Host ""
Write-Host "3️⃣ ACTIVAR ENVIRONMENT MANUALMENTE" -ForegroundColor White
Write-Host "   Ejecuta:  .\env_colab\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Read-Host "Presiona Enter para cerrar esta ventana"
