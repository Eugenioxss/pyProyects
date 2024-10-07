import math
import turtle as t
import random

def paint_begin(tam):
    t.hideturtle()
    t.bgcolor("tan")
    t.tracer(0)

    turtletable = t.Turtle()
    turtletable.hideturtle()
    turtletable.pensize(10)
    turtletable.penup()
    turtletable.goto(-tam // 2, tam // 2)
    turtletable.pendown()
    for _ in range(4):
        turtletable.forward(tam)
        turtletable.right(90)
    turtletable.penup()

    t.update()

    strcasi = t.textinput("Numero de Casillas", "Easy, Normal or Hard? ")
    if strcasi:
        strcasi = strcasi.replace(" ", "").lower()

    while not strcasi or strcasi not in ("easy", "normal", "hard"):
        strcasi = t.textinput("Numero de Casillas", "Easy, Normal or Hard? ")
        if strcasi is None:
            t.bye()
            return

    ncasi = {"easy": 16, "normal": 36, "hard": 64}.get(strcasi, 16)
    anchlarg_casi = tam // int(math.sqrt(ncasi))
    counti = 0

    turtletable.pensize(5)
    # Dibujar líneas verticales y etiquetas
    for i in range(1, int(math.sqrt(ncasi))):
        x = -tam // 2 + i * anchlarg_casi
        turtletable.goto(x, tam // 2)
        turtletable.pendown()
        turtletable.goto(x, -tam // 2)
        turtletable.penup()
        # Escribir etiqueta superior
        turtletable.goto(x - anchlarg_casi//2, tam // 2 + 17)
        turtletable.write(counti, align='center', font=('Arial', 20, 'normal'))
        counti += 1

    # Dibujar líneas horizontales y etiquetas
    countj = int(math.sqrt(ncasi)) - 1
    for j in range(1, int(math.sqrt(ncasi))):
        y = tam // 2 - j * anchlarg_casi
        turtletable.goto(-tam // 2, y)
        turtletable.pendown()
        turtletable.goto(tam // 2, y)
        turtletable.penup()
        # Escribir etiqueta lateral
        turtletable.goto(-tam // 2 - 24, y - (anchlarg_casi * 0.6))
        turtletable.write(countj, align='center', font=('Arial', 20, 'normal'))
        countj -= 1

    # Color de casillas
    colortable = t.Turtle()
    colortable.hideturtle()
    colortable.pensize(1)

    for row in range(int(math.sqrt(ncasi))):
        for col in range(int(math.sqrt(ncasi))):
            x = -tam // 2 + col * anchlarg_casi
            y = tam // 2 - row * anchlarg_casi
            colortable.penup()
            colortable.goto(x, y)
            colortable.pendown()

            if (row + col) % 2 == 0:
                colortable.fillcolor("olive")
            else:
                colortable.fillcolor("khaki")
            
            colortable.begin_fill()
            for _ in range(4):
                colortable.forward(anchlarg_casi)
                colortable.right(90)
            colortable.end_fill()

    # Mostrar botón de salida
    turtletable.goto(tam//2 + 10, 0)
    turtletable.color("red")
    turtletable.write("EXIT", align='right', font=('Arial', 20, 'bold'))
    t.update()

    return ncasi, anchlarg_casi

def generales():
    name1 = t.textinput("Players", "Name of first player: ")
    while not name1:
        name1 = t.textinput("Invalid Blank Name, try again!", "Name of first player: ")
        if name1 is None:
            t.bye()
            return None, None

    name2 = t.textinput("Players", "Name of second player: ")
    while not name2:
        name2 = t.textinput("Invalid Blank Name, try again!", "Name of second player: ")
        if name2 is None:
            t.bye()
            return None, None

    return name1, name2

def show_names(name1, name2, tam):
    turtlename1 = t.Turtle()
    turtlename2 = t.Turtle()

    turtlename1.penup()
    turtlename2.penup()
    turtlename1.hideturtle()
    turtlename2.hideturtle()

    dist_from_y_bellow = tam // 8
    turtlename1.goto(-tam//2 + (dist_from_y_bellow * 1.5), -tam // 2 - dist_from_y_bellow)
    turtlename1.write(name1, align='left', font=('Arial', 25, 'normal'))
    turtlename2.goto(tam//2 - (dist_from_y_bellow * 1.5), -tam // 2 - dist_from_y_bellow)
    turtlename2.write(name2, align='right', font=('Arial', 25, 'normal'))

    return dist_from_y_bellow, turtlename1, turtlename2

def create_matrix(ncasi):
    lengthfullmemorama = int(math.sqrt(ncasi))
    incompletedpairs = list(range(1, (ncasi//2) + 1))
    shufflednumbers = incompletedpairs * 2
    random.shuffle(shufflednumbers)

    memoramation = []
    for i in range(lengthfullmemorama):
        row = shufflednumbers[i * lengthfullmemorama:(i + 1) * lengthfullmemorama]
        memoramation.append(row)

    return memoramation

def undo_multiple(turtle_obj, times):
    for _ in range(times):
        turtle_obj.undo()

def exit_button(x, y, tam):
    # Dimensiones del hitbox
    hitbox_width = 68
    hitbox_height = 40

    # Centro del hitbox
    hitbox_center_x = tam // 2 + 10
    hitbox_center_y = 0
    # Coordenadas de la esquina inferior izquierda del hitbox
    hitbox_x1 = hitbox_center_x - (hitbox_width / 2)
    hitbox_y1 = hitbox_center_y - (hitbox_height / 2)

    # Coordenadas de la esquina superior derecha del hitbox
    hitbox_x2 = hitbox_center_x + (hitbox_width / 2)
    hitbox_y2 = hitbox_center_y + (hitbox_height / 2)

    if hitbox_x1 <= x <= hitbox_x2 and hitbox_y1 <= y <= hitbox_y2:
        print("Bye Bye!")
        t.bye()  # Cierra la ventana de Turtle
        return True
    return False

def main():
    name1, name2 = generales()
    if not name1 or not name2:
        return  # Cierra si los nombres no son válidos

    tam = 600
    ncasi, anchlarg_casi = paint_begin(tam)
    memoramation = create_matrix(ncasi)
    dist_from_y_bellow, turtlename1, turtlename2 = show_names(name1, name2, tam)

    totalpairs = ncasi // 2
    leftpairs = totalpairs
    current_player = 1  # 1 para player1, 2 para player2
    stopfrombutton = False

    # Crear un diccionario para almacenar el estado del juego
    state = {
        "selection": [],  # Almacena las coordenadas de las selecciones actuales
        "leftpairs": leftpairs,
        "current_player": current_player,
        "memoramation": memoramation,
        "tam": tam,
        "anchlarg_casi": anchlarg_casi,
        "stop": False
    }

    # Crear tortugas para mostrar mensajes
    message_turtle = t.Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()

    def update_message():
        message_turtle.clear()
        if state["current_player"] == 1:
            message_turtle.goto(0, tam//2 + 40)
            message_turtle.write(f"Turno de {name1}", align='center', font=('Arial', 20, 'normal'))
        else:
            message_turtle.goto(0, tam//2 + 40)
            message_turtle.write(f"Turno de {name2}", align='center', font=('Arial', 20, 'normal'))

    def reveal_cell(row, col):
        # Calcular posición
        x = -tam // 2 + col * anchlarg_casi
        y = tam // 2 - row * anchlarg_casi
        value = memoramation[row][col]

        reveal_turtle = t.Turtle()
        reveal_turtle.hideturtle()
        reveal_turtle.penup()
        reveal_turtle.goto(x + anchlarg_casi//2, y - anchlarg_casi//2 - 10)
        reveal_turtle.write(value, align='center', font=('Arial', 15, 'normal'))
        reveal_turtle.showturtle()
        t.update()
        return reveal_turtle

    def hide_cell(reveal_turtle, row, col):
        # Calcular posición
        x = -tam // 2 + col * anchlarg_casi
        y = tam // 2 - row * anchlarg_casi
        color = "olive" if (row + col) % 2 == 0 else "khaki"

        reveal_turtle.clear()
        reveal_turtle.penup()
        reveal_turtle.goto(x, y)
        reveal_turtle.fillcolor(color)
        reveal_turtle.begin_fill()
        for _ in range(4):
            reveal_turtle.forward(anchlarg_casi)
            reveal_turtle.right(90)
        reveal_turtle.end_fill()
        t.update()

    def handle_match():
        if len(state["selection"]) == 2:
            (row1, col1), (row2, col2) = state["selection"]
            val1 = memoramation[row1][col1]
            val2 = memoramation[row2][col2]

            if val1 == val2:
                print(f"Player {state['current_player']} encontró un par: {val1}")
                # Marcar las casillas como encontradas
                memoramation[row1][col1] = 0
                memoramation[row2][col2] = 0
                state["leftpairs"] -= 1
            else:
                print(f"Player {state['current_player']} no encontró un par.")
                # Esperar un momento y ocultar las casillas
                t.ontimer(lambda: hide_selected_cells(), 1000)
                # Cambiar de jugador
                state["current_player"] = 2 if state["current_player"] == 1 else 1

            state["selection"] = []
            update_message()

            if state["leftpairs"] == 0:
                message_turtle.goto(0, 0)
                message_turtle.write("¡Juego Terminado!", align='center', font=('Arial', 25, 'bold'))
                state["stop"] = True

    def hide_selected_cells():
        for reveal_turtle, (row, col) in state["selection"]:
            hide_cell(reveal_turtle, row, col)

    def on_click(x, y):
        if state["stop"]:
            return

        # Verificar si se hizo clic en el botón EXIT
        if exit_button(x, y, state["tam"]):
            state["stop"] = True
            return

        # Calcular la fila y columna basadas en las coordenadas
        if -tam // 2 <= x < tam // 2 and -tam // 2 <= y < tam // 2:
            col = int((x + tam // 2) // anchlarg_casi)
            row = int((tam // 2 - y) // anchlarg_casi)

            # Validar si la casilla ya ha sido encontrada
            if state["memoramation"][row][col] == 0:
                return

            # Validar si ya está seleccionada en este turno
            for _, (sel_row, sel_col) in state["selection"]:
                if sel_row == row and sel_col == col:
                    return

            # Revelar la casilla
            reveal_turtle = reveal_cell(row, col)
            state["selection"].append((reveal_turtle, (row, col)))

            if len(state["selection"]) == 2:
                handle_match()

    # Inicializar mensaje de turno
    update_message()

    # Configurar la detección de clics
    t.onscreenclick(on_click)

    t.mainloop()

main()
