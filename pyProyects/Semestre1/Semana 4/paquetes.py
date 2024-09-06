import math

def main():
    repetir="s"
    tot_ventas=0
    precio=0
    
    while(repetir=="s"):
        tot_ventas=tot_ventas+precio
        precio=calculo()
        repetir=input(f"El precio es: ${precio} deseas enviar otro paquete? (s/n)").lower()
    print("El total de ventas es:", tot_ventas)

def calculo():
    peso=float(input("Escribe el peso del paquete: "))
    peso=math.ceil(peso)
    precio=peso*4.50
    
    return precio
    

main()