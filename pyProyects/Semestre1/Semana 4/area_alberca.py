def area(base,altura,fondo):
    resultado=base*altura+2*(altura*fondo)+2*(fondo*base)
    print("holaaa")
    #return resultado

def main():
    base=float(input("Dame la base de la base de la alberca: "))
    altura=float(input("Dame el altura de la base de la alberca: "))
    profundidad=float(input("Dame la profunidad: "))
    medida=input("Que medida estas usando? ")
    area(1,2,3)
    #print(area(base,altura,profundidad), medida)
    
main()
