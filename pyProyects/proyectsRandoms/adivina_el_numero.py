import random

def main():
    mini=int(input("Dime el rango mínimo: "))
    toro=int(input("Dime el rango máximo: "))
    num=random.randint(mini,toro)
    guess=0
    while(guess!=num):
        guess=int(input("Dime tu número: "))
        if(guess>num):
            print("Muy alto")
        elif(guess<num):
            print("Muy bajo")
    print("Lo adivinaste, el número era ",num)
main()