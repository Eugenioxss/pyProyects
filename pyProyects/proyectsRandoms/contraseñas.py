
"""Nivel 4: Intermedio
Generador de Contraseñas
Descripción: Crea un programa que genere contraseñas seguras y aleatorias.
Input/Output:
Entrada: longitud: 12
Salida: tu contraseña generada: A4f$8gK@2Lm3
Recurso: Terminal."""

import random
sequence = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKL0123456789012345678901234567890123456789MNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()')
sequence_list = list(sequence)
random.shuffle(sequence_list)
num_car=int(input("How many characters do you want?"))
print("".join(sequence_list[:num_car]))