hora=int(input("Dime la hora en formato 24 horas"))
minutes=int(input("Dime los minutos en formato 24 horas"))

if hora >=12 and hora<24:
    letras="PM"
elif hora==24:
    letras =""
else:
    letras="AM"

if hora==0:
    hora_nueva = 12
elif (hora<=12):
    hora_nueva=hora
elif (hora >12 and hora<24):
    hora_nueva=hora-12
elif hora>23 or hora<0 or minutes>59 or minutes<0:
    hora_nueva=""
    minutes=""
    print("Hora Invalida")

print(hora_nueva, ":", minutes, letras)