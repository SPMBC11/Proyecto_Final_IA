#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fase 2 - Redes Neuronales - Versión optimizada para CPU
"""
import os
import sys

# Configurar antes de importar TensorFlow
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Forzar CPU
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'    # Reducir verbosidad
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'   # Desactivar oneDNN

import warnings
warnings.filterwarnings('ignore')

print("\n" + "="*70)
print("FASE 2: REDES NEURONALES (CPU Mode)")
print("="*70)

import numpy as np
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from tensorflow.keras import layers, Sequential
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd
import random

# Cambiar directorio
os.chdir(r'c:\Users\santi\OneDrive\Desktop\Trabajos\IA\Proyecto')

# Fijar semilla
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)
random.seed(SEED)

print(f"\n✓ Semilla: {SEED}")

# Cargar datos
print("Cargando datos...")
X_train = np.load('X_train.npy')
X_test = np.load('X_test.npy')
y_train = np.load('y_train.npy')
y_test = np.load('y_test.npy')
n_features = X_train.shape[1]

print(f"X_train: {X_train.shape}, X_test: {X_test.shape}")
print(f"y_train: {y_train.shape}, y_test: {y_test.shape}")
print(f"Características: {n_features}")

# Contar clases
unique, counts = np.unique(y_train, return_counts=True)
for u, c in zip(unique, counts):
    pct = 100 * c / len(y_train)
    clase_label = '<=50K' if u == 0 else '>50K'
    print(f"  Clase {u} ({clase_label}): {c} ({pct:.1f}%)")

print("\n" + "="*70)
print("MODELO A: PERCEPTRÓN")
print("="*70)

model_A = Sequential([layers.Dense(1, activation='sigmoid', use_bias=True, input_shape=(n_features,))])
model_A.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("Entrenando Modelo A...")
hist_A = model_A.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)
y_pred_A = (model_A.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
accuracy_A = accuracy_score(y_test, y_pred_A)
precision_A_macro = precision_score(y_test, y_pred_A, average='macro')
recall_A_macro = recall_score(y_test, y_pred_A, average='macro')
f1_A_macro = f1_score(y_test, y_pred_A, average='macro')
cm_A = confusion_matrix(y_test, y_pred_A)
metricas_A = {'accuracy': accuracy_A, 'precision': precision_A_macro, 'recall': recall_A_macro, 'f1': f1_A_macro}
print(f"✓ Modelo A: Accuracy={accuracy_A:.4f}, F1={f1_A_macro:.4f}")

print("\n" + "="*70)
print("MODELO B: RED CON 1 CAPA OCULTA")
print("="*70)

model_B = Sequential([
    layers.Dense(n_features, activation='sigmoid', use_bias=True, input_shape=(n_features,)),
    layers.Dense(1, activation='sigmoid', use_bias=True)
])
model_B.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("Entrenando Modelo B...")
hist_B = model_B.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)
y_pred_B = (model_B.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
accuracy_B = accuracy_score(y_test, y_pred_B)
precision_B_macro = precision_score(y_test, y_pred_B, average='macro')
recall_B_macro = recall_score(y_test, y_pred_B, average='macro')
f1_B_macro = f1_score(y_test, y_pred_B, average='macro')
cm_B = confusion_matrix(y_test, y_pred_B)
metricas_B = {'accuracy': accuracy_B, 'precision': precision_B_macro, 'recall': recall_B_macro, 'f1': f1_B_macro}
print(f"✓ Modelo B: Accuracy={accuracy_B:.4f}, F1={f1_B_macro:.4f}")

print("\n" + "="*70)
print("MODELO C: RED CON 2 CAPAS OCULTAS (BOTTLENECK)")
print("="*70)

model_C = Sequential([
    layers.Dense(2, activation='sigmoid', use_bias=True, input_shape=(n_features,)),
    layers.Dense(2, activation='sigmoid', use_bias=True),
    layers.Dense(1, activation='sigmoid', use_bias=True)
])
model_C.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
print("Entrenando Modelo C...")
hist_C = model_C.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)
y_pred_C = (model_C.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
accuracy_C = accuracy_score(y_test, y_pred_C)
precision_C_macro = precision_score(y_test, y_pred_C, average='macro')
recall_C_macro = recall_score(y_test, y_pred_C, average='macro')
f1_C_macro = f1_score(y_test, y_pred_C, average='macro')
cm_C = confusion_matrix(y_test, y_pred_C)
metricas_C = {'accuracy': accuracy_C, 'precision': precision_C_macro, 'recall': recall_C_macro, 'f1': f1_C_macro}
print(f"✓ Modelo C: Accuracy={accuracy_C:.4f}, F1={f1_C_macro:.4f}")

print("\n" + "="*70)
print("COMPARATIVA")
print("="*70)

comparativa = pd.DataFrame({
    'Modelo': ['A — Perceptrón', 'B — 1 capa oculta', 'C — 2 capas ocultas'],
    'Accuracy': [metricas_A['accuracy'], metricas_B['accuracy'], metricas_C['accuracy']],
    'Precisión': [metricas_A['precision'], metricas_B['precision'], metricas_C['precision']],
    'Recall': [metricas_A['recall'], metricas_B['recall'], metricas_C['recall']],
    'F1-score': [metricas_A['f1'], metricas_B['f1'], metricas_C['f1']],
})

print("\n" + comparativa.to_string(index=False))

f1_scores = {'A': metricas_A['f1'], 'B': metricas_B['f1'], 'C': metricas_C['f1']}
mejor_modelo = max(f1_scores, key=f1_scores.get)
print(f"\n✓ Mejor modelo: Modelo {mejor_modelo} (F1={f1_scores[mejor_modelo]:.4f})")

# Análisis de hiperparámetros
print("\n" + "="*70)
print("ANÁLISIS DE SENSIBILIDAD")
print("="*70)

modelos_dict = {'A': model_A, 'B': model_B, 'C': model_C}
mejor_model = modelos_dict[mejor_modelo]

# Epochs
print("\nVariando epochs...")
epochs_list = [20, 50, 100]
f1_scores_epochs = []
for num_epochs in epochs_list:
    if mejor_modelo == 'A':
        model_temp = Sequential([layers.Dense(1, activation='sigmoid', use_bias=True, input_shape=(n_features,))])
    elif mejor_modelo == 'B':
        model_temp = Sequential([
            layers.Dense(n_features, activation='sigmoid', use_bias=True, input_shape=(n_features,)),
            layers.Dense(1, activation='sigmoid', use_bias=True)
        ])
    else:
        model_temp = Sequential([
            layers.Dense(2, activation='sigmoid', use_bias=True, input_shape=(n_features,)),
            layers.Dense(2, activation='sigmoid', use_bias=True),
            layers.Dense(1, activation='sigmoid', use_bias=True)
        ])
    model_temp.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model_temp.fit(X_train, y_train, epochs=num_epochs, batch_size=32, validation_split=0.1, verbose=0)
    y_pred_temp = (model_temp.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
    f1_temp = f1_score(y_test, y_pred_temp, average='macro')
    f1_scores_epochs.append(f1_temp)
    print(f"  Epochs={num_epochs}: F1={f1_temp:.4f}")

# Batch size
print("\nVariando batch_size...")
batch_sizes = [16, 32, 64, 128]
f1_scores_batch = []
for batch_sz in batch_sizes:
    if mejor_modelo == 'A':
        model_temp = Sequential([layers.Dense(1, activation='sigmoid', use_bias=True, input_shape=(n_features,))])
    elif mejor_modelo == 'B':
        model_temp = Sequential([
            layers.Dense(n_features, activation='sigmoid', use_bias=True, input_shape=(n_features,)),
            layers.Dense(1, activation='sigmoid', use_bias=True)
        ])
    else:
        model_temp = Sequential([
            layers.Dense(2, activation='sigmoid', use_bias=True, input_shape=(n_features,)),
            layers.Dense(2, activation='sigmoid', use_bias=True),
            layers.Dense(1, activation='sigmoid', use_bias=True)
        ])
    model_temp.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model_temp.fit(X_train, y_train, epochs=50, batch_size=batch_sz, validation_split=0.1, verbose=0)
    y_pred_temp = (model_temp.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
    f1_temp = f1_score(y_test, y_pred_temp, average='macro')
    f1_scores_batch.append(f1_temp)
    print(f"  Batch_size={batch_sz}: F1={f1_temp:.4f}")

print("\n" + "="*70)
print("EXPORTACIÓN DE ARTEFACTOS")
print("="*70)

y_pred_mejor_prob = mejor_model.predict(X_test, verbose=0)
y_pred_mejor = (y_pred_mejor_prob > 0.5).astype(int).flatten()

mejor_model.save('mejor_modelo_fase2.h5')
print("✓ Modelo guardado: mejor_modelo_fase2.h5")

comparativa.to_csv('metricas_fase2.csv', index=False)
print("✓ Métricas guardadas: metricas_fase2.csv")

np.save('y_pred_mejor.npy', y_pred_mejor)
print("✓ Predicciones guardadas: y_pred_mejor.npy")

print("\n" + "="*70)
print("✓ FASE 2 COMPLETADA EXITOSAMENTE")
print("="*70)
print(f"\nTensorFlow: {tf.__version__}")
print(f"Mejor modelo guardado: Modelo {mejor_modelo}")
print("\nArtefactos disponibles para Fase 3")
