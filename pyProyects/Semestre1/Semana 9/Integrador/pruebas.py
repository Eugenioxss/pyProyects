import math
import random
import turtle as t

ncasi=16

lengthfullmemorama=int(math.sqrt(ncasi))

incompletedpairs=list(range(1,int(ncasi//2+1)))
shufflednumbers = incompletedpairs*2
random.shuffle(shufflednumbers)

memoramation=[]

for i in range(lengthfullmemorama):
    row=shufflednumbers[i*lengthfullmemorama:(i+1)*lengthfullmemorama]
    memoramation.append(row)

print(memoramation)


#_____________________________________________________________________________________________________________________________________________________________


# Tamaño de la cuadrícula
tam = 300
casillas = 4  # Una cuadrícula 4x4

anchura_casilla = tam // casillas
selecciones = []  # Lista para almacenar selecciones de casillas

# Función que se ejecutará en clic, determinar casilla
def handle_click(x, y):
    # Verificar si el clic está dentro de la cuadrícula
    if -tam//2 <= x <= tam//2 and -tam//2 <= y <= tam//2:
        # Convertir coordenadas a índices de la cuadrícula
        col = int((x + tam // 2) // anchura_casilla)
        row = int((y + tam // 2) // anchura_casilla)
        
        # Comprobar si ya se ha seleccionado esta casilla
        if (row, col) not in selecciones:
            # Almacenar la selección
            selecciones.append((row, col))
            t.goto(x, y)
            t.write(f"({row}, {col})", align="center", font=("Arial", 12, "normal"))
            print(f"Casilla seleccionada: ({row}, {col})")
            
            # Comprobar si se han seleccionado dos casillas
            if len(selecciones) == 2:
                print(f"Pares seleccionados: {selecciones}")
                # Aquí puedes agregar la lógica para comparar las dos selecciones
                # Reiniciar las selecciones después de un breve tiempo
                t.ontimer(limpiar_selecciones, 2000)  # Limpia después de 2 segundos
    else:
        # Manejar clic fuera de la cuadrícula
        t.goto(0, 0)  # Ir a una posición central
        t.write("Clic fuera de la cuadrícula.", align="center", font=("Arial", 12, "normal"))

def limpiar_selecciones():
    global selecciones
    selecciones = []
    t.clear()  # Limpiar la pantalla
    
# Registrar el evento de clic en la pantalla
t.onscreenclick(handle_click)

# Mantener la ventana abierta
t.mainloop()


import turtle as t

def main_function(extra_arg1, extra_arg2):
    def handle_click(x, y):
        print(f"Clic en: ({x}, {y})")
        print(f"Argumento extra 1: {extra_arg1}")
        print(f"Argumento extra 2: {extra_arg2}")

    # Registrar la función de clic
    t.onscreenclick(handle_click)

# Llama a la función principal con argumentos adicionales
main_function("Hola", 42)

# Mantener la ventana abierta
t.mainloop()
