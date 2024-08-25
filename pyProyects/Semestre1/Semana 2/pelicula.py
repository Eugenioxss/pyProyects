name=input(("Dime el nombre de una película"))
totalesMin=int(input(("Dime la duración de la película en minutos")))
horas=totalesMin//60
restantesMin=totalesMin%60
print("La película de", name, "dura", horas, "horas y", restantesMin, "minutos")