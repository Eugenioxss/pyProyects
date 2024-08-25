"""Nivel 2: Básico
Números Primos
Descripción: Escribe un programa que verifique si un número es primo.
Input/Output:
Entrada: 29
Salida: 29 es un número primo.
Recurso: Terminal."""

import math

def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso
primo = int(input("Introduce un número para verificar si es primo: "))
if checkPrime(primo):
    print(f"{primo} es un número primo.")
else:
    print(f"{primo} no es un número primo.")
