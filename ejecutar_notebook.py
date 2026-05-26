#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para ejecutar el notebook Fase2_Redes_Neuronales.ipynb
"""

import subprocess
import sys

def ejecutar_notebook():
    """Ejecuta el notebook usando nbconvert"""
    try:
        # Ejecutar nbconvert para convertir y ejecutar el notebook
        resultado = subprocess.run(
            [
                sys.executable, 
                '-m', 
                'nbconvert', 
                '--to', 
                'notebook', 
                '--execute', 
                'Fase2_Redes_Neuronales.ipynb', 
                '--output', 
                'Fase2_Redes_Neuronales_EJECUTADO.ipynb',
                '--ExecutePreprocessor.timeout=600'
            ],
            cwd=r'c:\Users\santi\OneDrive\Desktop\Trabajos\IA\Proyecto',
            capture_output=True,
            text=True,
            timeout=900
        )
        
        print("STDOUT:", resultado.stdout)
        print("STDERR:", resultado.stderr)
        print("Return code:", resultado.returncode)
        
        if resultado.returncode == 0:
            print("\n✓ Notebook ejecutado exitosamente")
            print("Archivo guardado: Fase2_Redes_Neuronales_EJECUTADO.ipynb")
        else:
            print("\n✗ Error durante la ejecución del notebook")
            
    except subprocess.TimeoutExpired:
        print("Error: El notebook tardó demasiado en ejecutarse (> 900s)")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    ejecutar_notebook()
