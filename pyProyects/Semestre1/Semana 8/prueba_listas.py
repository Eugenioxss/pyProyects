def main():
    cant=int(input("Ingresa la cantidad de elementos que quieres en tu lista: "))
    listita=[]
    suma=0

    if cant<=0:
        cant=int(input("Ingresa un entero mayor a 0: "))
    else:
        for i in range (cant):
            listita.append(int(input("Dime el valor")))
        for j in range (cant):
            print(f'lista[{j}]={listita[j]}')
            suma+=listita[j]
        print(listita[-1])
        print(suma)
        print(suma/cant)


main()