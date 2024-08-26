def area(base,altura,fondo):
    resultado=base*altura+2*(altura*fondo)+2*(fondo*base)
    return resultado

def main():
    base=float(input("Dame la base de la base de la alberca: "))
    altura=float(input("Dame el altura de la base de la alberca: "))
    profundidad=float(input("Dame la profunidad: "))
    medida=input("Que medida estas usando? ")
    print(area(base,altura,profundidad), medida)
    
main()
