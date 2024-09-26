def diagonal(mat):
    diagonal=[]
    for i in range(len(mat)):
        diagonal.append[i][i]
    print(diagonal)

def crear_matriz(ren,col):
    matriz=[]
    for i in range(ren):
        renglon=[]
        for j in range(col):
            renglon.append(int(input("Dame un valor: ")))
        matriz.append(renglon)
    return matriz

def main():
    matriz=[]
    ren=int(input("Dame el numero de renglones: "))
    col=int(input("Dame el numero de columnas: "))
    if ren!=col:
        print("No es cuadrada :(")
    else:
        matriz=crear_matriz(ren,col)
        diagonal(matriz)

main()