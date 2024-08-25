import time
import sys

def barra_de_carga(total, prefix='', suffix='', length=50, fill='█', print_end="\r"):
    """
    Crea una barra de carga en la terminal.
    
    total: El número total de iteraciones.
    prefix: Texto que precede a la barra de carga.
    suffix: Texto que sigue a la barra de carga.
    length: Longitud de la barra de carga.
    fill: Carácter de relleno para la barra.
    print_end: Carácter al final de la impresión, por defecto "\r" (sobreescribe la línea).
    """
    for i in range(total + 1):
        # Calcula el porcentaje de completado
        percent = ("{0:.1f}").format(100 * (i / float(total)))
        # Calcula el número de caracteres de relleno
        filled_length = int(length * i // total)
        # Construye la barra de carga
        bar = fill * filled_length + '-' * (length - filled_length)
        # Imprime la barra de carga
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
        # Simula una carga lenta
        time.sleep(0.1)
    # Al finalizar, imprime una nueva línea
    print()

# Ejemplo de uso:
total_items = 100
barra_de_carga(total_items, prefix='Cargando:', suffix='Completado', length=50)
