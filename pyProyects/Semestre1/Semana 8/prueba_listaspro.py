def main():
    listita=[]
    valor=int(input("Dime un entero (-1 para detener): "))
    while valor!=-1:
        listita.append(valor)
        valor=int(input("Dime un entero (-1 para detener): "))
    print(listita)
    print(listita[::-1])

main()