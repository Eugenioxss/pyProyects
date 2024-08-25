"""Nivel 1: Básico
Calculadora Simple
Descripción: Crea una calculadora que realice operaciones básicas (suma, resta, multiplicación, división).
Input/Output:
Entrada: 3, +, 5
Salida: 8
Recurso: Terminal."""

num1=float(input("num1 "))
opr=input("operador (+,-,*,/) ")
num2=float(input("num2 "))

operador = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

resultado = operador[opr](num1,num2)
print(resultado)
