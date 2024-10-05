def main():
    pala=input("Escribe tu string: ")
    palanew=""
    for letra in pala:
        if letra in "eéEÉ":
            palanew+="3"
        elif letra in "aáAÁ":
            palanew+="4"
        elif letra in "oOóÓ":
            palanew+="h"
        else:
            palanew+=letra
    print(palanew)


main()