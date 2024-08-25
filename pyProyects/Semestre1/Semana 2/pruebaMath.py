import math
deg=float(input("Dame los grados del triángulo"))
hyp=float(input("Dame la hipotenusa"))
adj=float(input("Dame el cateto adjacente"))
rad=math.radians(deg)
opp=math.sin(rad)*hyp
print("El cateto opuesto es", rad)