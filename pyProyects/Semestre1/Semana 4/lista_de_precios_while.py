def main():
    parar=None
    total=0
    print("""
    Menú:
    A 120
    B 250
    C 360
          
    Type letter to add an item, or X to exit
    """)
    while(parar!="X"):
        parar=input()
        if(parar=="A"):
            total+=120
        elif(parar=="B"):
            total+=250
        elif(parar=="C"):
            total+=360
        elif (parar != "X"):
            print("Valor invalido, introduzca uno nuevo")
        
    print("Total = ",total)
    print("Gracias")

main()