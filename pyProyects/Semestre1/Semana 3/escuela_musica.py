def evclave(n):
    if(n>=0):
        if(n<10):
            return "NO CLASIFICA"
        elif(n>=10 and n<=20):
            return "A"
        else:
            return "B"
    else:
        return "Valor no valido"

def main():
    points=int(input("Escribe la cantidad de puntos "))
    print(evclave(points))

main()