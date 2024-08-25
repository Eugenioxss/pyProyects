import math
ancho=float(input("Dame el ancho del rectangulo"))
largo=float(input("Dame el largo del rectangulo"))
diag=math.hypot(ancho,largo)
print("La diagonal del rectangulo es:", diag)