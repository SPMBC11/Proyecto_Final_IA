# 📊 Fase 1: EDA & Preprocesamiento - Dataset Adult

**Proyecto Final — Introducción a la Inteligencia Artificial**  
**Pontificia Universidad Javeriana**

---

## 🎯 Objetivo

Realizar análisis exploratorio y preprocesamiento completo del dataset Adult (Census Income) de UCI para construir un pipeline robusto de ciencia de datos.

---

## 📁 Archivos en esta carpeta

```
adult/                              # Archivos de datos originales
├── adult.data
├── adult.test
├── adult.names
└── Index

Fase1_EDA_Preprocesamiento.ipynb   # ← NOTEBOOK PRINCIPAL

INSTRUCCIONES_GOOGLE_COLAB.md      # ← LEER ESTO PRIMERO
setup_environment.bat              # Windows: Crear environment local
setup_environment.ps1              # PowerShell: Crear environment local
README.md                          # Este archivo
```

---

## ⚡ INICIO RÁPIDO (3 opciones)

### OPCIÓN 1: Google Colab ⭐ (RECOMENDADO)

**Ventajas**: Sin instalar nada, perfecto para ciencia de datos.

1. Ve a [Google Drive](https://drive.google.com)
2. Sube `Fase1_EDA_Preprocesamiento.ipynb`
3. Click derecho → **Abrir con → Google Colaboratory**
4. En celda 1, descomenta: `!pip install pandas numpy matplotlib seaborn scikit-learn -q`
5. Ejecuta con **Ctrl+Enter**

**Documento detallado**: Lee `INSTRUCCIONES_GOOGLE_COLAB.md`

---

### OPCIÓN 2: Local con Script (Automático)

**Windows - Command Prompt:**
```cmd
setup_environment.bat
```

**Windows - PowerShell:**
```powershell
powershell -ExecutionPolicy Bypass -File setup_environment.ps1
```

Esto crea automáticamente:
- Environment virtual: `env_colab/`
- Instala todas las librerías necesarias
- Registra kernel en Jupyter

Luego abre en VS Code y selecciona el interpreter `env_colab`.

---

### OPCIÓN 3: Manual (Control total)

```powershell
# Crear environment
python -m venv env_colab

# Activar (Windows PowerShell)
.\env_colab\Scripts\Activate.ps1

# Activar (Windows Command Prompt)
env_colab\Scripts\activate.bat

# Instalar paquetes
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

# Abrir Jupyter
jupyter notebook
```

---

## 📋 Requisitos Técnicos

### Opción Colab: ✓ Nada (todo preinstalado)

### Opción Local:
- Python 3.8+ (recomendado: 3.11 o 3.10)
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- jupyter (opcional, si usas Jupyter local)

---

## 🚀 Una vez esté listo el Environment

### En Google Colab:
1. Abre el notebook
2. Ejecuta celdas secuencialmente (Ctrl+Enter)
3. Los datos se descargan automáticamente desde UCI

### En VS Code / Jupyter Local:
1. Selecciona kernel `env_colab`
2. Abre `Fase1_EDA_Preprocesamiento.ipynb`
3. Ejecuta: Cell → Run All
4. Los datos se descargan automáticamente

---

## 📊 Contenido del Notebook

| Sección | Descripción |
|---------|------------|
| **PASO 1** | Descarga y consolidación del dataset |
| **PASO 2** | Análisis exploratorio de datos (EDA) |
| **PASO 3** | Tratamiento de nulos y outliers |
| **PASO 4** | Dummificación y normalización |
| **PASO 5** | Particionamiento train-test |
| **PASO 6** | Exportación de artefactos |

---

## 📥 Artefactos Generados

Después de ejecutar el notebook, se crean:

```
X_train.npy          # Características de entrenamiento (39,073 × 64)
X_test.npy           # Características de prueba (9,769 × 64)
y_train.npy          # Labels de entrenamiento (39,073,)
y_test.npy           # Labels de prueba (9,769,)
config_fase1.json    # Metadatos (número de features, etc)
```

Estos archivos son necesarios para la **Fase 2** (modelado).

---

## ⚠️ Resolución de Problemas

### Error: "DLL load failed" en Windows Local
**Causa**: Restricciones de seguridad del sistema  
**Solución**: Usa Google Colab (recomendado) o crea un environment virtual

### Error: "ModuleNotFoundError: pandas"
**Causa**: Environment no activado  
**Solución**: Asegúrate de activar el environment antes de ejecutar

### Error: "No module named jupyter"
**Causa**: Jupyter no instalado  
**Solución**: `pip install jupyter` en el environment

### El notebook descarga lentamente
**Causa**: Conexión a UCI  
**Solución**: Normal la primera vez. Paciencia ~2 minutos

---

## 📖 Documentación en el Notebook

Cada sección del notebook incluye:
- ✅ Código comentado y limpio
- ✅ Interpretaciones técnicas (mín. 3 oraciones)
- ✅ Justificaciones de decisiones
- ✅ Visualizaciones profesionales (20+ gráficos)
- ✅ Conclusiones con conclusiones en Markdown

---

## 🎓 Estructura ICONTEC

El notebook cumple con formato ICONTEC NTC-1486 para generación de PDF:
- Portada
- Tabla de contenido (auto-generada en Colab)
- Introducción
- Desarrollo (6 secciones)
- Conclusiones
- Referencias

**Para exportar como PDF:**
- **Colab**: File → Download → PDF
- **Jupyter**: File → Export As → PDF

---

## 🤝 Preguntas Frecuentes

**P: ¿Debo ejecutar todas las celdas?**  
R: Sí, secuencialmente de arriba a abajo. Cada celda depende de las anteriores.

**P: ¿Puedo correr solo algunas celdas?**  
R: No recomendado. Sigue el orden para evitar errores de variables no definidas.

**P: ¿Cuánto tarda en ejecutarse?**  
R: ~15-20 minutos en Colab (primera vez, con descargas). ~5-10 minutos local.

**P: ¿Los archivos .npy son necesarios?**  
R: Sí, para la Fase 2. Guárdalos en la misma carpeta que el notebook.

**P: ¿Puedo usar Python 3.14?**  
R: Colab usa 3.10. Local: recomendado 3.10-3.11 para compatibilidad.

---

## 📞 Soporte

Si tienes problemas:
1. Lee `INSTRUCCIONES_GOOGLE_COLAB.md` (soluciones específicas)
2. Verifica los requisitos técnicos
3. Intenta con Google Colab primero (más fácil)
4. Si aún falla, revisa el setup_environment script

---

**Última actualización**: Mayo 2026  
**Versión**: 1.0  
**Estado**: ✅ Listo para usar

¡Buena suerte con tu proyecto! 🚀
