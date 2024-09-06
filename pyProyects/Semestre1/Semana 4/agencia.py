def param(numnoches,paq):
    reg=0
    hotelm3=0
    if (paq=="a"):
        if(numnoches>=5):
            reg=1
    elif(paq=="h"):
        if(numnoches>=3):
            reg=1
        else:
            hotelm3=1
    else:
        print("Paquete inválido.")
    return reg,hotelm3

def main():
    otro="s"
    nochesgratis=0
    hotelm3dias=0
    while (otro!="n"):
        numnoches=int(input("Numero de noches: "))
        paq=input("Selecciona el paquete (A/H)").lower()
        regalo, hotelm3=param(numnoches,paq)
        nochesgratis+=regalo
        hotelm3dias+=hotelm3
        otro=input("Otro cliente (S/N)").lower()
    print("Noches gratis", nochesgratis)
    print("Sólo hotel menos de 3 días:", hotelm3dias)

main()