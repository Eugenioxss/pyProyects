def main():
    parar="s"
    cantlujo=0
    while(parar!="t"):
        silla=input("Escriba su tipo de silla (basica/estandar/lujo): ").lower()
        cliente=input("Tipo de cliente(normal/frecuente) ").lower()
        cantidad=int(input('Cual es la cantidad de sillas a comprar? '))
        if (silla in ["basica","estandar","lujo"]) or (cliente in ["frecuente","normal"]):
            if silla == "lujo":
                cantlujo=cantlujo+cantidad

            if(cliente=="normal"):
                precio,sindesc=normal(silla,cantidad)
            else:
                precio,sindesc=frecuente(silla,cantidad)
            print("Precio sin descuento: ",sindesc)
            print("Descuento de -",sindesc-precio)
            print("Total a pagar con descuento: ", precio)
        else:
            print("Valores Invalidos")
        parar=input("Otro cliente? (t para parar)").lower()
    print("Se vendieron", cantlujo, "sillas de lujo")
    print("El total fue de $", cantlujo, "pesos")

def normal(silla,cantidad):
    sindesc=0
    precio=0
    if(silla=="basica"):
        sindesc=cantidad*700
    elif(silla=="estandar"):
        sindesc=cantidad*900
    else:
        sindesc=cantidad*900

    if(precio>=10000 and precio<20000):
        precio=sindesc*0.90
    elif(precio>=20000):
        precio=sindesc*0.85
    return precio,sindesc

def frecuente(silla,cantidad):
    precio=0
    sindesc=0
    if(silla=="basica"):
        sindesc=cantidad*700
    elif(silla=="estandar"):
        sindesc=cantidad*900
    else:
        sindesc=cantidad*900
    precio=sindesc*0.80
    return precio,sindesc

main()