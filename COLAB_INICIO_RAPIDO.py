# COPIA ESTE CÓDIGO EN GOOGLE COLAB

# ============================================================
# PASO 0: INSTALAR TODAS LAS DEPENDENCIAS (Ejecutar primero)
# ============================================================

!pip install pandas numpy matplotlib seaborn scikit-learn -q

print("✓ Todas las dependencias instaladas correctamente")

# ============================================================
# PASO 1: IMPORTAR LIBRERÍAS REQUERIDAS
# ============================================================

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import json
import urllib.request
import os

# Configurar estilos de visualización
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10
warnings.filterwarnings('ignore')

print("✓ Todas las librerías importadas exitosamente")
print(f"✓ Versión de Pandas: {pd.__version__}")
print(f"✓ Versión de NumPy: {np.__version__}")
print(f"✓ Versión de Matplotlib: {matplotlib.__version__}")
print(f"✓ Versión de Seaborn: {sns.__version__}")

# ============================================================
# PASO 2: DESCARGAR ARCHIVOS DEL REPOSITORIO UCI
# ============================================================

# Definir las URLs de los archivos
url_train = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
url_test = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"

# Descargar los archivos con manejo de errores
print("\n" + "="*80)
print("DESCARGANDO ARCHIVOS DEL REPOSITORIO UCI")
print("="*80)
print("\nEsto puede tomar unos minutos...\n")

try:
    print("Descargando archivo de entrenamiento (adult.data)...")
    urllib.request.urlretrieve(url_train, "adult_train.data")
    print("✓ adult.data descargado exitosamente")
except Exception as e:
    print(f"⚠ Error al descargar adult.data: {e}")
    print("  Continuando...")

try:
    print("\nDescargando archivo de prueba (adult.test)...")
    urllib.request.urlretrieve(url_test, "adult_test.data")
    print("✓ adult.test descargado exitosamente")
except Exception as e:
    print(f"⚠ Error al descargar adult.test: {e}")
    print("  Continuando...")

# ============================================================
# PASO 3: ASIGNAR NOMBRES DE COLUMNAS Y CARGAR DATOS
# ============================================================

# Definir los nombres de las 15 columnas del dataset
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

print("\n" + "="*80)
print("CARGANDO ARCHIVOS CON PANDAS")
print("="*80)

# Cargar archivo de entrenamiento
print("\nCargando archivo de entrenamiento...")
df_train = pd.read_csv(
    "adult_train.data",
    header=None,
    names=column_names,
    skipinitialspace=True,
    na_values=' ?'
)

# Cargar archivo de prueba
print("Cargando archivo de prueba...")
df_test = pd.read_csv(
    "adult_test.data",
    header=None,
    names=column_names,
    skiprows=1,
    skipinitialspace=True,
    na_values=' ?'
)

# Normalizar la columna 'income'
df_test['income'] = df_test['income'].str.replace('.', '', regex=False)

print("\n✓ Archivos cargados exitosamente")
print(f"  Entrenamiento: {df_train.shape}")
print(f"  Prueba: {df_test.shape}")

# ============================================================
# PASO 4: CONSOLIDAR DATASETS
# ============================================================

df = pd.concat([df_train, df_test], axis=0, ignore_index=True)

print("\n" + "="*80)
print("DATASET CONSOLIDADO")
print("="*80)
print(f"\nDimensiones: {df.shape}")
print(f"  - Filas: {df.shape[0]:,}")
print(f"  - Columnas: {df.shape[1]}")

print("\nPrimeras 5 filas:")
print(df.head())

print("\nÚltimas 5 filas:")
print(df.tail())

print("\nTipos de datos:")
print(df.dtypes)

# ============================================================
# INFORMACIÓN COMPLETA DEL DATASET
# ============================================================

print("\n" + "="*80)
print("INFORMACIÓN GENERAL DEL DATASET")
print("="*80)

print(f"\nTotal de filas: {len(df):,}")
print(f"Total de columnas: {df.shape[1]}")
print(f"Variables numéricas: {df.select_dtypes(include=[np.number]).shape[1]}")
print(f"Variables categóricas: {df.select_dtypes(include=['object']).shape[1]}")

print("\n✓ ¡PARTE 1 COMPLETADA!")
print("\nEste es el código básico. Para obtener el análisis completo,")
print("copia el contenido del archivo Fase1_EDA_Preprocesamiento.ipynb")
print("en Google Colab y ejecuta celda por celda.")
