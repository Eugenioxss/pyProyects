num=int(input("Escribe un entero positivo: "))

while(num<=0):
    num=int(input("Escribe un entero positivo: "))

for i in range (1,num+1):
    print(i, end=", ")
for i in range (num-1, 1,-1):
    print(i, end=", ")
print("1")