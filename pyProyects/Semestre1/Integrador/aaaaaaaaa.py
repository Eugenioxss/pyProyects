import turtle

# Crear una ventana de turtle
screen = turtle.Screen()
screen.title("Almacena Coordenadas de Clics")

# Crear una tortuga (cursor de dibujo)
t = turtle.Turtle()
t.penup()  # Levantar el lápiz para no dibujar líneas al mover la tortuga

# Lista para almacenar las coordenadas de los clics
coordenadas = []

def store_coordinates(x, y):
    """Almacena las coordenadas (x, y) en la lista y dibuja un punto."""
    coordenadas.append((x, y))  # Agregar las coordenadas a la lista
    print(f"Clic en: ({x}, {y})")  # Imprimir coordenadas en la consola
    t.goto(x, y)  # Mover la tortuga a la posición del clic
    t.dot(5, "red")  # Dibujar un punto rojo en la posición del clic
    print(coordenadas)

# Asignar la función de manejo de clics a la pantalla
screen.onscreenclick(store_coordinates)

# Mantener la ventana abierta hasta que el usuario la cierre
screen.mainloop()

# Al finalizar, las coordenadas estarán en la lista
print("Coordenadas almacenadas:", coordenadas)
