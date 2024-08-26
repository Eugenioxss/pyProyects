def evclave(n):
    if(n>=0):
        if(n<10):
            return "N"
        elif(n>=10 and n<=20):
            return "A"
        else:
            return "B"
    else:
        return "Valor no válido"

def main():
    points=int(input("Escribe la cantidad de puntos "))
    calif=evclave(points)
    if calif == "N":
        print("NO CLASIFICA")
    else:
        print(calif)
main()