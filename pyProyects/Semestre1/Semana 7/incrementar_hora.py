def main():
    hora=int(input("Dime la hora: "))
    minu=int(input("Dime los minutos: "))
    parar=input("Clave? ")
    while(parar != "t"):
        minu+=1
        if minu==60:
            minu=0
            hora+=1
            if(hora==24):
                hora=0
        print(hora,":",minu)
        parar=input("Clave? ")

main()