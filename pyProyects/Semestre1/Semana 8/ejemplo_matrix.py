def producir_matriz(ren,col):
    matriz=[]
    for i in range(ren):
        renglon=[]
        for j in range(col):
            renglon.append("777")
        matriz.append(renglon)
    return matriz

def main():
    ren=0
    col=0
    while ren<2 or col<2:
        ren=int(input("Dame el numero de renglones: "))
        col=int(input("Dame el numero de columnas: "))
        if ren>=2 and col>=2:
            matriz=producir_matriz(ren,col)
            for renglon in matriz:
                print(" ".join(renglon))


main()