def producir_matriz(lon):
    matriz=[]
    for i in range(lon):
        lista=[]
        for j in range(lon):
            lista.append(0)
        matriz.append(lista)
    for k in range (lon):
        matriz[k][k]=1
    return matriz

def lucir_matriz(matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            print(f'{matriz[i][j]:3}', end="")
        print()

def main():
    lon=0
    while lon<2:
        lon=int(input("Dame el numero de renglones: "))
        if lon>=2:
            matriz=producir_matriz(lon)
    lucir_matriz(matriz)


main()