def promedio(list):
    promedio=sum(list)/len(list)
    return promedio

def main():
    listones=[]
    cant=int(input("Ingresa la cantidad de elementos que quieres en tu lista: "))
    for i in range (cant):
        listones.append(float(input(f"Dame el valor {i+1}: ")))
    prom=promedio(listones)
    for i in listones:
        if i > prom:
            print(i)

main()