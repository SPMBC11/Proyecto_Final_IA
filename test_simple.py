#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

print("Script iniciado")
sys.stdout.flush()

# Cambiar a directorio correcto
os.chdir(r'c:\Users\santi\OneDrive\Desktop\Trabajos\IA\Proyecto')
print("Directorio: " + os.getcwd())
sys.stdout.flush()

# Cargar librerías
print("Importando numpy...")
sys.stdout.flush()
import numpy as np
print("NumPy importado OK")
sys.stdout.flush()

# Cargar datos
print("Cargando datos...")
sys.stdout.flush()
X_train = np.load('X_train.npy')
print(f"X_train cargado: {X_train.shape}")
sys.stdout.flush()

X_test = np.load('X_test.npy')
print(f"X_test cargado: {X_test.shape}")
sys.stdout.flush()

y_train = np.load('y_train.npy')
print(f"y_train cargado: {y_train.shape}")
sys.stdout.flush()

y_test = np.load('y_test.npy')
print(f"y_test cargado: {y_test.shape}")
sys.stdout.flush()

n_features = X_train.shape[1]
print(f"Características: {n_features}")
sys.stdout.flush()

# Importar TensorFlow
print("Importando TensorFlow...")
sys.stdout.flush()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Reducir verbosidad de TF
import tensorflow as tf
print(f"TensorFlow {tf.__version__} importado OK")
sys.stdout.flush()

from tensorflow.keras import layers, Sequential

# Modelo A
print("\n=== MODELO A ===")
print("Creando modelo...")
sys.stdout.flush()

model_A = Sequential([
    layers.Dense(1, activation='sigmoid', use_bias=True, input_shape=(n_features,))
])
model_A.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("Modelo A creado. Entrenando...")
sys.stdout.flush()

hist_A = model_A.fit(X_train, y_train, epochs=5, batch_size=32,
                     validation_split=0.1, verbose=1)

print("✓ Modelo A entrenado")
sys.stdout.flush()

y_pred_A = (model_A.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
print(f"Predicciones shape: {y_pred_A.shape}")
sys.stdout.flush()

# Importar sklearn
print("Importando scikit-learn...")
sys.stdout.flush()
from sklearn.metrics import f1_score
f1_A = f1_score(y_test, y_pred_A, average='macro')
print(f"F1-score Modelo A: {f1_A:.4f}")
sys.stdout.flush()

print("\n✓ Script completado exitosamente")
sys.stdout.flush()
