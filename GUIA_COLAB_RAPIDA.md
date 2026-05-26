# 🚀 GUÍA RÁPIDA: EJECUTAR EN GOOGLE COLAB

## ⭐ 3 PASOS SIMPLES

### PASO 1: Abre Google Colab
1. Ve a: https://colab.research.google.com
2. Haz clic en "Nuevo notebook"

### PASO 2: Copia y pega ESTO en la primera celda

```python
# Instalar dependencias
import subprocess
import sys

packages = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'scikit-learn']
for pkg in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

# Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import urllib.request
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("✓ ¡Todo instalado y listo!")
```

### PASO 3: Ejecuta la celda
- Presiona **Ctrl+Enter** o el botón ▶
- Espera a que termine (1-2 minutos)

---

## ✅ DESPUÉS DE INSTALAR

Ya tienes pandas, numpy, etc. listo. Ahora puedes ejecutar el resto del código.

### Descargar datos:
```python
url_train = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
url_test = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"

urllib.request.urlretrieve(url_train, "adult_train.data")
urllib.request.urlretrieve(url_test, "adult_test.data")

print("✓ Archivos descargados")
```

### Cargar datos:
```python
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

df_train = pd.read_csv("adult_train.data", header=None, names=column_names, 
                       skipinitialspace=True, na_values=' ?')
df_test = pd.read_csv("adult_test.data", header=None, names=column_names,
                      skiprows=1, skipinitialspace=True, na_values=' ?')

df_test['income'] = df_test['income'].str.replace('.', '', regex=False)

df = pd.concat([df_train, df_test], axis=0, ignore_index=True)

print(f"Dataset: {df.shape}")
print(df.head())
```

---

## 🎯 OPCIÓN ALTERNATIVA: Usar el Notebook Completo

Si quieres el análisis COMPLETO con todas las visualizaciones:

1. **Descarga** `Fase1_EDA_Preprocesamiento.ipynb`
2. **Sube a Google Drive** (Drag & drop)
3. **Abre con Colab** (Click derecho → "Abrir con" → Colaboratory)
4. **Ejecuta todas las celdas** (Runtime → Run all)

---

## ❓ ¿Qué elegir?

| Opción | Tiempo | Complejidad |
|--------|--------|-------------|
| **Este script rápido** | 5 min | Básico |
| **Notebook completo** | 20 min | Completo (con 20+ gráficos) |

**Recomendación**: Empieza con este script para verificar que todo funciona, luego usa el notebook completo.

---

## 🆘 Si Algo Falla

**Error: "ModuleNotFoundError"**
- Vuelve a ejecutar la celda de instalación (PASO 2)
- Presiona Ctrl+Enter dos veces

**Error al descargar datos**
- Los servidores de UCI pueden ser lentos
- Espera 1-2 minutos y reintenta

**Nada de eso funciona**
- Abre una celda nueva en Colab
- Ejecuta: `!pip install --upgrade pip pandas numpy`
- Luego vuelve a intentar

---

**¡Listo! Ya puedes trabajar con los datos.** 🎓
