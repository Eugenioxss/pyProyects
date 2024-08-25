def price(h,m):
    if(h>=0 and m>=0 and m<=59): #verification of values
        if(h>=3 and (h<16 and m>0) and (h!=15 and m>=0)):
            if(m>=0):
                return "Costo =", 30+5*(h-3)+5
            elif(m==0):
                return "Costo =", 30+5*(h-3)
        elif(h<3):
            if(m>=0):
                return "Costo = 35"
            if(m==0):
                return "Costo = 30"
        else:
            return "Costo = 100"
    else:
        return "Valores no validos"

def main():
    hours=int(input("Dime las horas "))
    minutes=int(input("Dime los minutos (0-59) "))
    print(price(hours,minutes))

main()