import math
porPintar=float(input("Dame el área por pintar en metros cuadrados"))
sqMetrosLitro=float(input("Dame el área que rinde un litro de pintura en metros cuadrados"))
porPintar/sqMetrosLitro
print("La cantidad de cubetas que necesitas son", math.ceil(porPintar/sqMetrosLitro))