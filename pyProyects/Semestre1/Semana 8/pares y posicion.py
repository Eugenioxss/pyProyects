listitacompleta=[]
cant=int(input("Ingresa la cantidad de elementos que quieres en tu lista: "))
for i in range (cant):
    listitacompleta.append(int(input(f"Dame el valor {i+1}: ")))

for i in listitacompleta:
    if i % 2==0:
        print("pos",listitacompleta.index(i),"valor",i)