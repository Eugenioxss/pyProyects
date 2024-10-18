#Eugenio Moreno v
#a01723720
#Proyecto Integrador

#Play in fullscreen, for help or testing of the game, the matrix with answers is printed once every 2 
#turns in the terminal, being "0" the pairs already turned

import math as math
import turtle
import random
import time

def paint_begin(TAM,screen):

    turtletable=turtle.Turtle()

    turtletable.hideturtle()
    screen.bgcolor("tan")
    screen.tracer(0)

    turtletable.hideturtle()
    turtletable.pensize(10)
    turtletable.pu()
    turtletable.goto(-TAM // 2, TAM // 2)   
    
    turtletable.pd()
    turtletable.goto(TAM // 2, TAM // 2)
    turtletable.goto(TAM // 2, -TAM // 2)
    turtletable.goto(-TAM // 2, -TAM // 2)
    turtletable.goto(-TAM // 2, TAM // 2)
    turtletable.pu()

    screen.update()

    str_casi=turtle.textinput("Numero de Casillas", "Easy(4x4), Normal(6x6) or Hard(8x8)? (type the word)")

    while str_casi is None or str_casi not in ("easy","normal","hard"):
        str_casi=turtle.textinput("Numero de Casillas", "Easy(4x4), Normal(6x6) or Hard(8x8)? (type the word)")
        str_casi=str_casi.replace(" ","")
        str_casi=str_casi.lower()
        if str_casi is None:
            turtle.bye()

    str_casi=str_casi.replace(" ","")
    str_casi=str_casi.lower()

    ncasi=0
    match str_casi:
        case "easy":
            ncasi=16
        case "normal":
            ncasi=36
        case "hard":
            ncasi=64

    anchlarg_casi=TAM//int(math.sqrt(ncasi))
    counti=0
        
    screen.tracer(0)
    for i in range (-TAM//2+anchlarg_casi,TAM//2+1,anchlarg_casi):
        turtletable.goto(i-(anchlarg_casi//2),TAM // 2 + 17)
        turtletable.write(counti, align='center', font=('Arial', 20, 'normal'))
        turtletable.pensize(5)
        turtletable.goto(i,TAM // 2)
        turtletable.pd()
        turtletable.goto(i,-TAM // 2)
        turtletable.pu()
        counti+=1

    countj=int(math.sqrt(ncasi))-1
    for j in range (-TAM//2+anchlarg_casi,TAM//2+1,anchlarg_casi):
        turtletable.goto(-TAM // 2 - 24, j - (anchlarg_casi * 0.6))
        turtletable.write(countj, align='center', font=('Arial', 20, 'normal'))
        turtletable.pensize(5)
        turtletable.goto(TAM // 2,j)
        turtletable.pd()
        turtletable.goto(-TAM // 2,j)
        turtletable.pu()
        countj-=1
        
    screen.update()

    pairs=ncasi//2
    casi=[]

    colortable=turtle.Turtle()
    colortable.hideturtle()

    for i in range(-TAM // 2, TAM//2,anchlarg_casi):
        for j in range (-TAM // 2, TAM//2,anchlarg_casi):
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

    turtletable.goto(TAM//2+80,0)
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

def show_names(name1,name2,TAM):
    turtlename1=turtle.Turtle()
    turtlename2=turtle.Turtle()

    turtlename1.pu()
    turtlename2.pu()

    turtlename1.hideturtle()
    turtlename2.hideturtle()

    dist_from_y_bellow=TAM//8
    turtlename1.goto(-TAM//2+(dist_from_y_bellow*1.5),-TAM // 2 - dist_from_y_bellow)
    turtlename1.write(name1, align='left', font=('Arial', 25, 'normal'))
    turtlename2.goto(TAM//2-(dist_from_y_bellow*1.5),-TAM // 2 - dist_from_y_bellow)
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

def turnone(screen, name1, dist_from_y_bellow, TAM, ncasi, anchlarg_casi, memoramation, leftpairs,pairsone,pairsrisen,multiplesof5,bonus1):
    modifyname1=turtle.Turtle()
    modifyname1.hideturtle()
    modifyname1.pu()

    modifyname1.color("green")
    modifyname1.goto(-TAM//2+(dist_from_y_bellow*1.5),-TAM // 2 - dist_from_y_bellow)
    modifyname1.write(name1, align='left', font=('Arial', 25, 'normal'))
    modifyname1.color("black")

    valuesel1=0
    valuesel2=0

    stopfrombutton=False

    while valuesel1==0 and stopfrombutton==False:
        valuesel1,stopfrombutton,columne1,row1=valuesection1andsection2(screen,TAM,anchlarg_casi,modifyname1,memoramation)
        #Handles the click, and returns the columne and row of the selection
    
    while valuesel2==0 and stopfrombutton==False:
        valuesel2,stopfrombutton,columne2,row2=valuesection1andsection2(screen,TAM,anchlarg_casi,modifyname1,memoramation)
        if columne1==columne2 and row1==row2:
            print("Click repetido")
            valuesel2=0
        elif stopfrombutton==True:
            print()
        else:
            #Handles the click, and returns the columne and row of the selection if the row and columne are different
            if valuesel1==valuesel2 and valuesel1!=0:
                memoramation[columne1][row1]=0
                memoramation[columne2][row2]=0
                leftpairs-=1
                pairsone+=1
                pairsrisen+=1
                if pairsrisen in multiplesof5:
                    multiplesof5.remove(pairsrisen)
                    bonus1+=1
            else:
                time.sleep(1)
                modifyname1.clear()

    modifyname1.goto(-TAM//2+(dist_from_y_bellow*1.5),-TAM // 2 - dist_from_y_bellow)
    modifyname1.write(name1, align='left', font=('Arial', 25, 'normal'))
    return leftpairs,stopfrombutton,pairsone,pairsrisen,bonus1

def turntwo(screen, name2, dist_from_y_bellow, TAM, ncasi, anchlarg_casi, memoramation, leftpairs,pairstwo,pairsrisen,multiplesof5,bonus2):

    modifyname2=turtle.Turtle()
    modifyname2.hideturtle()
    modifyname2.pu()

    modifyname2.color("green")
    modifyname2.goto(TAM//2-(dist_from_y_bellow*1.5),-TAM // 2 - dist_from_y_bellow)
    modifyname2.write(name2, align='right', font=('Arial', 25, 'normal'))
    modifyname2.color("black")
    valuesel1=0
    valuesel2=0

    stopfrombutton=False

    while valuesel1 == 0 and stopfrombutton==False:
        valuesel1,stopfrombutton,columne1,row1=valuesection1andsection2(screen,TAM,anchlarg_casi,modifyname2,memoramation)

    while valuesel2==0 and stopfrombutton==False:
        valuesel2,stopfrombutton,columne2,row2=valuesection1andsection2(screen,TAM,anchlarg_casi,modifyname2,memoramation)
        if columne1==columne2 and row1==row2:
            print("Click repetido")
            valuesel2=0
        else:
            #Handles the click, and returns the columne and row of the selection if the row and columne are different
            if valuesel1==valuesel2 and valuesel1!=0:
                memoramation[columne1][row1]=0
                memoramation[columne2][row2]=0
                leftpairs-=1
                pairstwo+=1
                pairsrisen+=1
                if pairsrisen in multiplesof5:
                    multiplesof5.remove(pairsrisen)
                    bonus2+=1
            else:
                time.sleep(1)
                modifyname2.clear()

    modifyname2.goto(TAM//2-(dist_from_y_bellow*1.5),-TAM // 2 - dist_from_y_bellow)
    modifyname2.write(name2, align='right', font=('Arial', 25, 'normal'))
    return leftpairs,stopfrombutton,pairstwo,pairsrisen,bonus2

def valuesection1andsection2(screen,TAM,anchlarg_casi,turtlename,memoramation):
    def handle_click(x, y):#Handles the click, and returns the x and y value of the click
        xandy.append((x, y))
        flagclicked[0] = True 
        print("Clic registrado:", xandy)

    xandy = []
    flagclicked = [False] 

    screen.onscreenclick(handle_click)

    while not flagclicked[0]:
        screen.update()
    
    x, y = xandy[0]
    stopfrombutton = exit_button(x, y,screen)

    if -TAM // 2 <= x <= TAM // 2 and -TAM // 2 <= y <= TAM // 2 and not stopfrombutton:
        columne = int((x + TAM // 2) // anchlarg_casi)
        row = int((-y + TAM // 2) // anchlarg_casi)
        valueselection = memoramation[columne][row]

        if valueselection != 0:
            gotox = (int(-TAM // 2)) + (columne * anchlarg_casi) + (int(anchlarg_casi // 2))
            gotoy = ((int(TAM // 2)) - (row * anchlarg_casi) - (int(anchlarg_casi // 2)))

            turtlename.goto(gotox - int(anchlarg_casi // 2), gotoy + int(anchlarg_casi // 2))
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
    elif stopfrombutton==True:
        valueselection=0
        columne=0
        row=0
    else:
        valueselection=0
        columne=0
        row=0
    flagclicked = [False] 
    return valueselection,stopfrombutton,columne,row

def exit_button(x,y,screen):
    hitbox_width = 80
    hitbox_height = 40
    TAM=600

    hitbox_center_x = TAM // 2 + 40
    hitbox_center_y = 0

    hitbox_x1 = hitbox_center_x - (hitbox_width / 2)
    hitbox_y1 = hitbox_center_y - (hitbox_height / 2)

    hitbox_x2 = hitbox_center_x + (hitbox_width / 2)
    hitbox_y2 = hitbox_center_y + (hitbox_height / 2)

    if hitbox_x1 <= x <= hitbox_x2 and hitbox_y1 <= y <= hitbox_y2:
        stopfrombutton=True
        print("Bye Bye!")
    else:
        stopfrombutton=False

    return stopfrombutton

def second_exit(screen,TAM):
    def handle_click(x, y):
        xandysecondexit.append((x, y))
        secondexitflag[0] = True 
        print("Clic registrado:", xandysecondexit)

    xandysecondexit = []
    secondexitflag = [False] 
    screen.onscreenclick(handle_click)
    stopfrombutton2=False

    while not secondexitflag[0]:
        screen.update()
        if xandysecondexit:
            x, y = xandysecondexit[0]
            stopfrombutton2 = exit_button(x, y,screen)
        if stopfrombutton2==True:
            secondexitflag = [True]

    return stopfrombutton2

def show_stats(TAM,leftpairs,pairsone,pairstwo,screen,bonus1,bonus2):
    showstats=turtle.Turtle()
    showstats.hideturtle()
    showstats.pu()

    showstats.goto(-TAM//2,TAM//2)
    showstats.begin_fill()
    showstats.fillcolor("grey")
    screen.update()

    for k in range(4):
        showstats.forward(TAM)
        showstats.right(90)
        screen.update()

    showstats.end_fill()
    screen.update()
    showstats.goto(0,TAM//2)
    showstats.pensize(10)
    showstats.pd()
    showstats.goto(0,-TAM//2)
    showstats.pu()

    if bonus1 != 0:
        totalpoints1=(pairsone*100)+(pairsone*bonus1*1000)
    else:
        totalpoints1=pairsone*100

    if bonus2 != 0:
        totalpoints2=(pairstwo*100)+(pairstwo*bonus2*1000)
    else:
        totalpoints2=pairstwo*100
    showstats.color("black")
    if leftpairs==0:
        showstats.goto(-150,200)
        showstats.write("GAME", align='center', font=('Arial', 40, 'normal'))
        showstats.goto(150,200)
        showstats.write("OVER", align='center', font=('Arial', 40, 'normal'))
        showstats.goto(-150,0)
        showstats.write("Total Poins: "+str(totalpoints1), align='center', font=('Arial', 25, 'normal'))
        showstats.goto(150,0)
        showstats.write("Total Poins: "+str(totalpoints2), align='center', font=('Arial', 25, 'normal'))
        if totalpoints1>totalpoints2:
            showstats.goto(-150,-200)
            showstats.color("green")
            showstats.write("Winner :)", align='center', font=('Arial', 30, 'normal'))
            showstats.goto(150,-200)
            showstats.color("red")
            showstats.write("Loser :(", align='center', font=('Arial', 30, 'normal'))
        else:
            showstats.goto(150,-200)
            showstats.color("green")
            showstats.write("Winner :)", align='center', font=('Arial', 30, 'normal'))
            showstats.goto(-150,-200)
            showstats.color("red")
            showstats.write("Loser :(", align='center', font=('Arial', 30, 'normal'))

    else:
        showstats.goto(-150,100)
        showstats.write("Pairs: "+str(pairsone), align='center', font=('Arial', 25, 'normal'))
        showstats.goto(150,100)
        showstats.write("Pairs: "+str(pairstwo), align='center', font=('Arial', 25, 'normal'))
        showstats.goto(-150,-50)
        showstats.write("Bonus points: "+str(bonus1), align='center', font=('Arial', 25, 'normal'))
        showstats.goto(150,-50)
        showstats.write("Bonus points: "+str(bonus2), align='center', font=('Arial', 25, 'normal'))
        showstats.goto(-150,-200)
        showstats.write("Total points: "+str(totalpoints1), align='center', font=('Arial', 25, 'normal'))
        showstats.goto(150,-200)
        showstats.write("Total points: "+str(totalpoints2), align='center', font=('Arial', 25, 'normal'))

    stopfrombutton2=second_exit(screen,TAM)
    return stopfrombutton2

def main():
    screen=turtle.Screen()
    screen.title("Memorama de Eugenio")
    name1,name2=generales() #Asks the name of both players
    TAM=600
    ncasi,anchlarg_casi,=paint_begin(TAM,screen) #Draws all the initial visuals of the screen
    memoramation=create_matrix(ncasi) #Create and shuffles the matrix
    dist_from_y_bellow,turtlename1,turtlename2=show_names(name1,name2,TAM) #Shows the names in the turtle screen
    totalpairs=int(ncasi//2)
    leftpairs=totalpairs
    stopfrombutton=False
    pairsone=0
    pairstwo=0
    pairsrisen=0
    multiplesof5=[5,10,15,20,25,30,35]
    bonus1=0
    bonus2=0

    while(stopfrombutton==False and leftpairs>0):
        
        for i in range (len(memoramation)):
            for j in range(len(memoramation[0])):
                print(f'{memoramation[j][i]:3}', end="")
            print()

        leftpairs,stopfrombutton,pairsone,pairsrisen,bonus1=turnone(screen,name1,dist_from_y_bellow,TAM,ncasi,anchlarg_casi,memoramation,leftpairs,pairsone,pairsrisen,multiplesof5,bonus1)
        #Handles the click for player 1, and updates the corresponding variables if the turned pair is correct

        if stopfrombutton==False and leftpairs!=0:
            leftpairs,stopfrombutton,pairstwo,pairsrisen,bonus2=turntwo(screen,name2,dist_from_y_bellow,TAM,ncasi,anchlarg_casi,memoramation,leftpairs,pairstwo,pairsrisen,multiplesof5,bonus2)
            #Handles the click for player 2, and updates the corresponding variables if the turned pair is correct
            print("Left pairs: ",leftpairs)
            print("Pairs player 1: ",pairsone)
            print("Pairs player 2: ",pairstwo)
        if stopfrombutton==True:
            leftpairs==0
            
    stopfrombutton2=show_stats(TAM,leftpairs,pairsone,pairstwo,screen,bonus1,bonus2) #Calculates and show the stats in the turtle screen
    if stopfrombutton2==True:
        screen.bye()

main()