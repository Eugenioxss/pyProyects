def recibirlista(lista,mini,toro):
    listitafinal=[i for i in lista if i >= mini and i <= toro]
    return(listitafinal)

def main():
    listitacompleta=[]
    cant=int(input("Ingresa la cantidad de elementos que quieres en tu lista: "))

    for i in range (cant):
        listitacompleta.append(int(input(f"Dame el valor {i+1}: ")))

    toromin=int(input("Dame el valor minimo: "))
    toromax=int(input("Dame el valor maximo: "))
    listitafinal=recibirlista(listitacompleta,toromin,toromax)
    print(listitacompleta)
    print(listitafinal)

main()