# 📘 Instrucciones: Ejecutar el Notebook en Google Colab

## ⚠️ Problema Actual en VS Code

Tu sistema Windows tiene restricciones de seguridad (AppLocker) que bloquean las DLLs de pandas. **La mejor solución es usar Google Colab**, que está optimizado para notebooks Jupyter sin estas limitaciones.

---

## ✅ OPCIÓN 1: Usar Google Colab (Recomendado)

### Paso 1: Subir el notebook a Google Drive

1. Abre [Google Drive](https://drive.google.com)
2. Sube el archivo `Fase1_EDA_Preprocesamiento.ipynb` a una carpeta (clic derecho → Subir archivos)

### Paso 2: Abrir en Google Colab

1. Haz clic derecho en el archivo subido
2. Selecciona: **"Abrir con" → "Google Colaboratory"**
3. Si no aparece, instala la app: 
   - Busca "Colaboratory" en Google Workspace Marketplace
   - Instálala

### Paso 3: Ejecutar el notebook

1. En la celda 1 (importaciones), descomenta la línea:
   ```python
   !pip install pandas numpy matplotlib seaborn scikit-learn -q
   ```

2. Ejecuta la celda presionando **Ctrl+Enter** o el botón ▶

3. Ejecuta todas las demás celdas secuencialmente

### Ventajas de Google Colab:
✅ Sin restricciones de seguridad de Windows
✅ GPU disponible gratuitamente
✅ Todas las librerías preinstaladas
✅ Perfecta para ciencia de datos
✅ Sincronización automática con Google Drive

---

## ❌ OPCIÓN 2: Solución Local en Windows

Si prefieres trabajar localmente, necesitarás:

### A. Crear ambiente virtual (Recomendado)
```powershell
# En PowerShell, en la carpeta del proyecto
python -m venv env_colab
.\env_colab\Scripts\Activate.ps1
pip install pandas numpy matplotlib seaborn scikit-learn
```

### B. O usar Anaconda
```powershell
conda create -n colab_env python=3.11
conda activate colab_env
conda install pandas numpy matplotlib seaborn scikit-learn
```

### C. Abrir en VS Code con el environment correcto
1. Abre VS Code
2. Ctrl+Shift+P → "Python: Select Interpreter"
3. Elige el environment que creaste (env_colab o colab_env)
4. Recarga la ventana

---

## 🎯 Mejor Recomendación: Google Colab

Para este proyecto, **Google Colab es la opción ideal** porque:

1. **Instalación instantánea**: Sin problemas de compatibilidad
2. **Recursos gratuitos**: GPU/TPU disponibles
3. **Almacenamiento**: Integración con Google Drive
4. **Colaboración**: Comparte links fácilmente con tu profesor
5. **Entorno controlado**: Todas las versiones compatibles

---

## 📋 Próximos pasos

### Si eliges Google Colab:
1. Sube el archivo a Drive
2. Abre con Colab
3. Descomenta `!pip install...` en celda 1
4. Ejecuta el notebook completo

### Si eliges Local (con environment):
1. Crea el environment virtual
2. Selecciona ese interpreter en VS Code
3. Abre el notebook
4. Ejecuta las celdas

---

**¿Necesitas ayuda?** Tengo scripts listos para cualquiera de estas opciones. 🚀
