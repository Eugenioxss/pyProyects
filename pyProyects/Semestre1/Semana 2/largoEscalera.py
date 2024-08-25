import math
hCasa=float(input("Dame la altura de la casa"))
degEscalera=int(input("Dame la inclinación de la escalera en grados"))
largo=hCasa/math.sin(math.radians(degEscalera))
largoBueno=math.ceil(largo)
print("El largo mínimo de la escalera es:", largoBueno)