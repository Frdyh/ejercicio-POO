import sys
import os

# Redirigir al directorio padre para ejecutar el main principal del ejercicio 1
directorio_ejercicio_1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, directorio_ejercicio_1)

from main import ejecutar_sistema_nomina

if __name__ == "__main__":
    ejecutar_sistema_nomina()
