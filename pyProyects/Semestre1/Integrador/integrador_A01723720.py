#Eugenio Moreno v
#a01723720
#Proyecto Integrador

import math as math
import turtle as t
import random

def pintar_begin(tam):
    t.tracer(0)
    t.pensize(7)
    t.pu()
    t.goto(-tam // 2, tam // 2)
    t.pd()
    t.goto(tam // 2, tam // 2)
    t.goto(tam // 2, -tam // 2)
    t.goto(-tam // 2, -tam // 2)
    t.goto(-tam // 2, tam // 2)
    t.pu()
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

    anchlarg_casi=tam//math.sqrt(ncasi)

    for i in range (int((-tam//2)+anchlarg_casi),int((tam//2)-anchlarg_casi),int(anchlarg_casi)):
        t.tracer(0)
        t.pensize(7)
        t.goto(i,tam // 2)
        t.pd()
        t.goto(i,-tam // 2)
        t.pu()
        t.update()

    for j in range(int((-tam//2)+anchlarg_casi),int((tam//2)-anchlarg_casi),int(anchlarg_casi)):
        t.tracer(0)
        t.pensize(7)
        t.goto(tam // 2,j)
        t.pd()
        t.goto(-tam // 2,j)
        t.pu()
        t.update()

    pairs=ncasi//2
    casi=[]


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


def main():
    name1,name2=generales()
    tam=700
    ncasi,anchlarg_casi,=pintar_begin(tam)


main()