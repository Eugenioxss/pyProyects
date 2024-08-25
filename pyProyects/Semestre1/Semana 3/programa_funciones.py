def area_rect(largo, ancho):
    area=largo*ancho
    return area

def perimetro_rect(largo, ancho):
    perimetro=largo*2+ancho*2
    return perimetro

def main():


    inplargo=int(input("Dame el largo del rectangulo "))
    inpancho=int(input("Dame el ancho del rectangulo "))
    loopie="y"
    while(loopie=="y" and loopie!="n"):
        eleccion=input("Qué vas a calcular? (a = area, p = perimetro) ")

        if(eleccion=="a"):
            area_fin=area_rect(inplargo, inpancho)
            print("Tu área es: ", area_fin)
        elif(eleccion=="p"):
            perimetro_fin=perimetro_rect(inplargo, inpancho)
            print("Tu perímetro es: ", perimetro_fin)
        else:
            print("Valor Inválido")
        loopie = input("¿Quieres calcular algo más? y/n: ").lower()
        while loopie != "y" and loopie != "n":
            print("Valor Inválido")
            loopie = input("¿Quieres calcular algo más? y/n: ").lower()

    if loopie == "n":
        print("Ciao")

main()