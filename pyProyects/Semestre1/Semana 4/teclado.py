def main():
    total=0
    cantnum=0
    
    while(total<=1000):
        n1=int(input("Type a number: "))
        cantnum+=1
        total+=n1
    print("Suma = ",total)
    print("Cantidad de numeros = ",cantnum)

main()