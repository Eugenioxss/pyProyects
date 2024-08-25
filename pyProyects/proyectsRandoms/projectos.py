import subprocess
import os

directorio_proyectos = 'C:/Users/admin/Desktop/ProyectosProgra/pyProyects/'

def ejecutar_proyecto(opcion):
    comandos = {
        1: 'calculadora_simple.py',
        2: 'numeros_primos.py',
        3: 'palindromo.py',
        4: 'proyecto4.py',
        5: 'proyecto5.py',
        6: 'proyecto6.py',
        7: 'proyecto7.py',
        8: 'proyecto8.py',
        9: 'proyecto9.py',
        10: 'proyecto10.py',
    }

    archivo = comandos.get(opcion)
    if archivo:
        ruta_completa = os.path.join(directorio_proyectos, archivo)
        print(f"Ejecutando archivo: {ruta_completa}") 
        subprocess.run(['python', ruta_completa])
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 10.")

def mostrar_opciones():
    print("Selecciona el proyecto a ejecutar:")
    print("""
        1: calculadora_simple.py
        2: numeros_primos.py
        3: palindromo.py
        4: proyecto4.py
        5: proyecto5.py
        6: proyecto6.py
        7: proyecto7.py
        8: proyecto8.py
        9: proyecto9.py
        10: proyecto10.py""")

if __name__ == "__main__":
    mostrar_opciones()
    try:
        opcion = int(input("Introduce el número del proyecto a ejecutar: "))
        ejecutar_proyecto(opcion)
    except ValueError:
        print("Por favor, ingresa un número válido.")



"""Nivel 1: Básico
Calculadora Simple
Descripción: Crea una calculadora que realice operaciones básicas (suma, resta, multiplicación, división).
Input/Output:
Entrada: 3, +, 5
Salida: 8
Recurso: Terminal."""

"""Nivel 2: Básico
Números Primos
Descripción: Escribe un programa que verifique si un número es primo.
Input/Output:
Entrada: 29
Salida: 29 es un número primo.
Recurso: Terminal."""


"""Nivel 3: Intermedio
Palíndromo
Descripción: Verifica si una palabra o frase es un palíndromo.
Input/Output:
Entrada: anilina
Salida: "anilina" es un palíndromo.
Recurso: Terminal."""


"""Nivel 4: Intermedio
Generador de Contraseñas
Descripción: Crea un programa que genere contraseñas seguras y aleatorias.
Input/Output:
Entrada: longitud: 12
Salida: tu contraseña generada: A4f$8gK@2Lm3
Recurso: Terminal."""


"""Nivel 5: Intermedio
Adivina el Número
Descripción: Un juego en el que la computadora genera un número aleatorio y el usuario debe adivinarlo.
Input/Output:
Entrada: Intento 1: 50
Salida: Muy alto.
Entrada: Intento 2: 30
Salida: ¡Correcto! El número era 30.
Recurso: Terminal."""


"""Nivel 6: Avanzado
Fibonacci Recursivo
Descripción: Implementa una función recursiva que calcule el n-ésimo número de Fibonacci.
Input/Output:
Entrada: n = 7
Salida: 13
Recurso: Terminal."""


"""Nivel 7: Avanzado
Analizador de Texto
Descripción: Lee un archivo de texto y devuelve estadísticas como el número de palabras y las más comunes.
Input/Output:
Entrada: Texto en archivo: "hola mundo hola"
Salida:
Número de palabras: 3
Palabra más común: hola
Recurso: Terminal, necesitarás un archivo de texto."""


"""Nivel 8: Avanzado
Juego del Ahorcado
Descripción: Implementa el juego del ahorcado con palabras predefinidas.
Input/Output:
Entrada: Intento 1: A
Salida: Letras correctas: _ _ _ A _
Entrada: Intento 2: R
Salida: ¡Felicidades, ganaste! La palabra era "PARCA".
Recurso: Terminal."""


"""Nivel 9: Experto
Simulador de Vida Artificial (Conway's Game of Life)
Descripción: Implementa el juego de la vida de Conway.
Input/Output:
Entrada: Matriz inicial
Salida: Matriz en tiempo real mostrando la evolución del sistema.
Recurso: Preferiblemente en terminal, aunque puede usarse un recurso visual simple como matplotlib."""


"""Nivel 10: Experto
Clasificador de Imágenes con Machine Learning
Descripción: Construye un clasificador de imágenes utilizando un dataset como MNIST.
Input/Output:
Entrada: Imagen de un dígito escrito a mano (dataset MNIST).
Salida: Predicción: 5
Recurso: Uso de bibliotecas como TensorFlow o PyTorch. Necesitarás un entorno gráfico para mostrar las imágenes (Jupyter Notebook o un script con matplotlib)."""