#Eugenio Moreno v
#a01723720
#Proyecto Integrador

import math as math
import turtle as t
import random

def paint_begin(tam):
    t.hideturtle()
    t.bgcolor("tan")
    t.tracer(0)

    turtletable=t.Turtle()

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

    t.update()

    strcasi=t.textinput("Numero de Casillas", "Easy, Normal or Hard? ")
    strcasi=strcasi.replace(" ","").lower()

    while strcasi is None or strcasi not in ("easy","normal","hard"):
        strcasi=t.textinput("Numero de Casillas", "Easy, Normal or Hard? ")
        if strcasi is None:
            t.bye()

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
        
    t.tracer(0)
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
    t.update()

    pairs=ncasi//2
    casi=[]

    colortable=t.Turtle()
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
            t.update()

    turtletable.goto(tam//2+40,0)
    turtletable.color("red")
    turtletable.write("EXIT", align='right', font=('Arial', 20, 'bold'))
    t.update()

    return ncasi,anchlarg_casi

def generales():
    name1=t.textinput("Players", "Name of first player: ")
    
    while name1 is None or name1 == "":
        name1=t.textinput("Invalid Blank Name, try again!", "Name of first player: ")
        if name1 is None:
            t.bye()

    name2=t.textinput("Players", "Name of second player: ")

    while name2 is None or name2 == "":
        name2=t.textinput("Invalid Blank Name, try again!", "Name of second player: ")
        if name2 is None:
            t.bye()

    return name1,name2

def show_names(name1,name2,tam):
    turtlename1=t.Turtle()
    turtlename2=t.Turtle()


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

def turnone(name1,turtlename1,dist_from_y_bellow,tam,ncasi,anchlarg_casi,memoramation,leftpairs):
    turtlename1.color("green")
    turtlename1.goto(-tam//2+(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    turtlename1.write(name1, align='left', font=('Arial', 25, 'normal'))
    stopfrombutton=False
    selection1=0
    selection2=0
    turtlename1.color("black")
    while selection1==0:
        selection1,valueselection1=t.onscreenclick(handle_click)

        def handle_click(x,y):
            if -tam//2 <= x <= tam//2 and -tam//2 <= y <= tam//2:

                columne = int((x + tam // 2) // anchlarg_casi)
                row = int((y + tam // 2) // anchlarg_casi)
                valueselection1=memoramation[columne][row]

                if valueselection1!=0:
                    gotox=(int(-tam//2))+(columne*anchlarg_casi)+(int(anchlarg_casi//2))
                    gotoy=(int(tam//2))-(row*anchlarg_casi)-(int(anchlarg_casi//2))
                    turtlename1.goto(gotox-int(anchlarg_casi//2),gotoy+int(anchlarg_casi//2)) #top left
                    turtlename1.begin_fill()
                    for k in range(4):
                        turtlename1.fillcolor("grey")
                        turtlename1.forward(anchlarg_casi)
                        turtlename1.right(90)
                        turtlename1.end_fill()
                        turtlename1.goto(gotox,gotoy)
                        turtlename1.write(valueselection1, align='left', font=('Arial', 15, 'normal'))
                        t.update()
                selection1=1
            stopfrombutton=exit_button(x,y)
            return selection1,valueselection1,stopfrombutton
    
    while selection2==0:
        selection2,valueselection2=t.onscreenclick(handle_click)

        def handle_click(x,y):
            if -tam//2 <= x <= tam//2 and -tam//2 <= y <= tam//2:

                columne = int((x + tam // 2) // anchlarg_casi)
                row = int((y + tam // 2) // anchlarg_casi)
                valueselection2=memoramation[columne][row]

                if valueselection2!=0:
                    gotox=(int(-tam//2))+(columne*anchlarg_casi)+(int(anchlarg_casi//2))
                    gotoy=(int(tam//2))-(row*anchlarg_casi)-(int(anchlarg_casi//2))
                    turtlename1.goto(gotox-int(anchlarg_casi//2),gotoy+int(anchlarg_casi//2)) #top left
                    turtlename1.begin_fill()
                    for k in range(4):
                        turtlename1.fillcolor("grey")
                        turtlename1.forward(anchlarg_casi)
                        turtlename1.right(90)
                    turtlename1.end_fill()
                    turtlename1.goto(gotox,gotoy)
                    turtlename1.write(valueselection2, align='left', font=('Arial', 15, 'normal'))
                    t.update()
                selection2=1
            stopfrombutton=exit_button(x,y)
            return selection2,valueselection2

    if valueselection1==valueselection2:
        leftpairs-=1
    else:
        undo_multiple(turtlename1,2)

    turtlename1.undo()
    return leftpairs,stopfrombutton

def turntwo(name2,turtlename2,dist_from_y_bellow,tam,ncasi,anchlarg_casi,memoramation):
    turtlename2.color("green")
    turtlename2.goto(tam//2-(dist_from_y_bellow*1.5),-tam // 2 - dist_from_y_bellow)
    turtlename2.write(name2, align='right', font=('Arial', 25, 'normal'))

    ##interaccion

    turtlename2.undo()

def undo_multiple(turtle, times):
    for i in range (times):
        turtle.undo()

def exit_button(x,y):
    # Dimensiones del hitbox
    hitbox_width = 68
    hitbox_height = 40
    tam=600

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
        stopfrombutton=True
        print("Bye Bye!")

    return stopfrombutton

def main():
    name1,name2=generales()
    tam=600
    ncasi,anchlarg_casi,=paint_begin(tam)
    memoramation=create_matrix(ncasi)
    dist_from_y_bellow,turtlename1,turtlename2=show_names(name1,name2,tam)
    totalpairs=int(ncasi//2)
    leftpairs=totalpairs
    stopfrombutton=False
    while(not stopfrombutton or leftpairs!=0):
        leftpairs,stopfrombutton=turnone(name1,turtlename1,dist_from_y_bellow,tam,ncasi,anchlarg_casi,memoramation,leftpairs)
        turntwo(name2,turtlename2,dist_from_y_bellow,tam,ncasi,anchlarg_casi,memoramation,leftpairs)

    t.mainloop()
    
main()

"""
To do:

done show names on screen, and show which player is on turn
done make random matrix

handle clicks in a for
if that works, show end button
show at the end or if finished the stats with bonus points and stuff

"""