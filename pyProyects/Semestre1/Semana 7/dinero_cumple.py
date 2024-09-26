def main():
    edad=int(input("Dime la edad actual: "))
    dinero=10
    while(dinero<=1000):
        dinero=dinero*2
        edad+=1
    print(edad,dinero)

main()