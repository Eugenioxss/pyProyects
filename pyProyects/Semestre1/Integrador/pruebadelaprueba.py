
import math as math
import turtle
import random
import time

def paint_begin(tam,screen):

    turtletable=turtle.Turtle()

    turtletable.hideturtle()
    screen.bgcolor("tan")
    screen.tracer(0)

    turtletable.hideturtle()
    turtletable.pensize(10)
    turtletable.pu()
    turtletable.goto(-tam // 2, tam // 2)
    turtletable.pd()
    turtletable.goto(tam // 2, tam // 2)
    turtletable.goto(tam // 2, -tam // 2)
    turtletable.goto(-tam // 2, -tam // 2)
    turtletable.goto(-tam // 2, tam // 2)
    turtletable.pu()

    screen.update()

    strcasi=turtle.textinput("Numero de Casillas", "Easy(4x4), Normal(6x6) or Hard(8x8)? (type the word)")
    strcasi=strcasi.replace(" ","").lower()

    while strcasi is None or strcasi not in ("easy","normal","hard"):
        strcasi=turtle.textinput("Numero de Casillas", "Easy(4x4), Normal(6x6) or Hard(8x8)? (type the word)")
        if strcasi is None:
            turtle.bye()

    ncasi=0
    match strcasi:
        case "easy":
            ncasi=16
        case "normal":
            ncasi=36
        case "hard":
            ncasi=64

    anchlarg_casi=tam//int(math.sqrt(ncasi))
    counti=0
        
    screen.tracer(0)
    for i in range (-tam//2+anchlarg_casi,tam//2+1,anchlarg_casi):
        turtletable.goto(i-(anchlarg_casi//2),tam // 2 + 17)
        turtletable.write(counti, align='center', font=('Arial', 20, 'normal'))
        turtletable.pensize(5)
        turtletable.goto(i,tam // 2)
        turtletable.pd()
        turtletable.goto(i,-tam // 2)
        turtletable.pu()
        counti+=1

    countj=int(math.sqrt(ncasi))-1
    for j in range (-tam//2+anchlarg_casi,tam//2+1,anchlarg_casi):
        turtletable.goto(-tam // 2 - 24, j - (anchlarg_casi * 0.6))
        turtletable.write(countj, align='center', font=('Arial', 20, 'normal'))
        turtletable.pensize(5)
        turtletable.goto(tam // 2,j)
        turtletable.pd()
        turtletable.goto(-tam // 2,j)
        turtletable.pu()
        countj-=1
    screen.update()

    pairs=ncasi//2
    casi=[]

    colortable=turtle.Turtle()
    colortable.hideturtle()

    for i in range(-tam // 2, tam//2,anchlarg_casi):
        for j in range (-tam // 2, tam//2,anchlarg_casi):
            colortable.pu()
            colortable.goto(i,j+anchlarg_casi)
            colortable.pd()

            if (((i // anchlarg_casi) + (j // anchlarg_casi)) % 2 == 0):
                colortable.fillcolor("olive")
            else:
                colortable.fillcolor("khaki")
            
            colortable.begin_fill()
            for k in range(4):
                colortable.forward(anchlarg_casi)
                colortable.right(90)
            colortable.end_fill()
            screen.update()

    turtletable.goto(tam//2+80,0)
    turtletable.color("red")
    turtletable.write("EXIT", align='right', font=('Arial', 20, 'bold'))
    screen.update()

    return ncasi,anchlarg_casi

def generales():
    name1=turtle.textinput("Players", "Name of first player: ")
    
    while name1 is None or name1 == "":
        name1=turtle.textinput("Invalid Blank Name, try again!", "Name of first player: ")
        if name1 is None:
            turtle.bye()

    name2=turtle.textinput("Players", "Name of second player: ")

    while name2 is None or name2 == "":
        name2=turtle.textinput("Invalid Blank Name, try again!", "Name of second player: ")
        if name2 is None:
            turtle.bye()

    return name1,name2

def show_names(name1,name2,tam):
    turtlename1=turtle.Turtle()
    turtlename2=turtle.Turtle()

    turtlename1.pu()
    turtlename2.pu()

    turtlename1.hideturtle()
    turtlename2.hideturtle()

    dist_from_y_bellow=tam//8
    turtlename1.goto(-tam//2+(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    turtlename1.write(name1, align='left', font=('Arial', 25, 'normal'))
    turtlename2.goto(tam//2-(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    turtlename2.write(name2, align='right', font=('Arial', 25, 'normal'))

    return dist_from_y_bellow,turtlename1,turtlename2

def create_matrix(ncasi):

    lengthfullmemorama=int(math.sqrt(ncasi))

    incompletedpairs=list(range(1,int(ncasi//2+1)))
    shufflednumbers = incompletedpairs*2
    random.shuffle(shufflednumbers)

    memoramation=[]

    for i in range(lengthfullmemorama):
        row=shufflednumbers[i*lengthfullmemorama:(i+1)*lengthfullmemorama]
        memoramation.append(row)

    return memoramation

def turnone(screen, name1, dist_from_y_bellow, tam, ncasi, anchlarg_casi, memoramation, leftpairs,pairsone):
    modifyname1=turtle.Turtle()
    modifyname1.hideturtle()
    modifyname1.pu()

    print("turn one")
    modifyname1.color("green")
    modifyname1.goto(-tam//2+(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    modifyname1.write(name1, align='left', font=('Arial', 25, 'normal'))
    modifyname1.color("black")

    valuesel1=0
    valuesel2=0

    print(memoramation)
    stopfrombutton=False

    while valuesel1==0 and stopfrombutton==False:
        valuesel1,stopfrombutton,columne1,row1=valuesection1andsection2(screen,tam,anchlarg_casi,modifyname1,memoramation)
    
    while valuesel2==0 and stopfrombutton==False:
            valuesel2,stopfrombutton,columne2,row2=valuesection1andsection2(screen,tam,anchlarg_casi,modifyname1,memoramation)
            if valuesel1==valuesel2 and valuesel1!=0:
                memoramation[columne1][row1]=0
                memoramation[columne2][row2]=0
                leftpairs-=1
                pairsone+=1
            else:
                time.sleep(1)
                modifyname1.clear()
    modifyname1.goto(-tam//2+(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    modifyname1.write(name1, align='left', font=('Arial', 25, 'normal'))
    return leftpairs,stopfrombutton,pairsone

def turntwo(screen, name2, dist_from_y_bellow, tam, ncasi, anchlarg_casi, memoramation, leftpairs,pairstwo):

    modifyname2=turtle.Turtle()
    modifyname2.hideturtle()
    modifyname2.pu()

    print("turn two")
    modifyname2.color("green")
    modifyname2.goto(tam//2-(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    modifyname2.write(name2, align='right', font=('Arial', 25, 'normal'))
    modifyname2.color("black")
    valuesel1=0
    valuesel2=0

    print(memoramation)
    stopfrombutton=False

    while valuesel1 == 0 and stopfrombutton==False:
        valuesel1,stopfrombutton,columne1,row1=valuesection1andsection2(screen,tam,anchlarg_casi,modifyname2,memoramation)

    while valuesel2==0 and stopfrombutton==False:
        valuesel2,stopfrombutton,columne2,row2=valuesection1andsection2(screen,tam,anchlarg_casi,modifyname2,memoramation)
        if valuesel1 != 0:
            if valuesel1==valuesel2:
                memoramation[columne1][row1]=0
                memoramation[columne2][row2]=0
                leftpairs-=1
                pairstwo+=1
            else:
                time.sleep(1)
                modifyname2.clear()
    modifyname2.goto(tam//2-(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    modifyname2.write(name2, align='right', font=('Arial', 25, 'normal'))
    return leftpairs,stopfrombutton,pairstwo

def valuesection1andsection2(screen,tam,anchlarg_casi,turtlename,memoramation):
    def handle_click(x, y):
        xandy.append((x, y))
        flagclicked[0] = True 
        print("Clic registrado:", xandy)

    xandy = []
    flagclicked = [False] 

    screen.onscreenclick(handle_click)

    while not flagclicked[0]:# Espera a que se haga clic
        screen.update()  # Actualiza la pantalla para seguir capturando eventos
    
    x, y = xandy[0]
    stopfrombutton = exit_button(x, y,screen)

    if -tam // 2 <= x <= tam // 2 and -tam // 2 <= y <= tam // 2 and not stopfrombutton:
        columne = int((x + tam // 2) // anchlarg_casi)
        row = int((-y + tam // 2) // anchlarg_casi)
        valueselection = memoramation[columne][row]

        if valueselection != 0:
            print("if valueselection != 0:")
            gotox = (int(-tam // 2)) + (columne * anchlarg_casi) + (int(anchlarg_casi // 2))
            gotoy = ((int(tam // 2)) - (row * anchlarg_casi) - (int(anchlarg_casi // 2)))

            turtlename.goto(gotox - int(anchlarg_casi // 2), gotoy + int(anchlarg_casi // 2))  # top left
            turtlename.begin_fill()
            turtlename.fillcolor("grey")
            for k in range(4):
                turtlename.forward(anchlarg_casi)
                turtlename.right(90)
                screen.update()
            turtlename.end_fill()
            screen.update()
            turtlename.goto(gotox, gotoy)
            turtlename.write(valueselection, align='center', font=('Arial', 15, 'normal'))
            screen.update()
    else:
        valueselection=0
        columne=0
        row=0
    return valueselection,stopfrombutton,columne,row

def exit_button(x,y,screen):

    # Dimensiones del hitbox
    stopfrombutton=False
    hitbox_width = 100
    hitbox_height = 40
    tam=600

    # Centro del hitbox
    hitbox_center_x = tam // 2 + 80
    hitbox_center_y = 0
    # Coordenadas de la esquina inferior izquierda del hitbox
    hitbox_x1 = hitbox_center_x - (hitbox_width / 2)
    hitbox_y1 = hitbox_center_y - (hitbox_height / 2)

    # Coordenadas de la esquina superior derecha del hitbox
    hitbox_x2 = hitbox_center_x + (hitbox_width / 2)
    hitbox_y2 = hitbox_center_y + (hitbox_height / 2)

    if hitbox_x1 <= x <= hitbox_x2 and hitbox_y1 <= y <= hitbox_y2:
        stopfrombutton=True
        print("Bye Bye!")

    return stopfrombutton

def main():
    screen=turtle.Screen()
    screen.title("Memorama de Eugenio M")
    name1,name2=generales()
    tam=600
    ncasi,anchlarg_casi,=paint_begin(tam,screen)
    memoramation=create_matrix(ncasi)
    dist_from_y_bellow,turtlename1,turtlename2=show_names(name1,name2,tam)
    totalpairs=int(ncasi//2)
    leftpairs=totalpairs
    stopfrombutton=False
    pairsone=0
    pairstwo=0
    while(stopfrombutton==False and leftpairs>0):
        leftpairs,stopfrombutton,pairsone=turnone(screen,name1,dist_from_y_bellow,tam,ncasi,anchlarg_casi,memoramation,leftpairs,pairsone)
        if stopfrombutton==False:
            leftpairs,stopfrombutton,pairstwo=turntwo(screen,name2,dist_from_y_bellow,tam,ncasi,anchlarg_casi,memoramation,leftpairs,pairstwo)
            print("Left pairs:",leftpairs)
        elif leftpairs==0:
            #display stats de la partida\
            print()
    screen.bye()
main()

"""
To do:

done show names on screen, and show which player is on turn
done make random matrix
semi-done handle clicks in a loop
done if that works, show end button
show at the end or if finished the stats with bonus points and stuff

"""