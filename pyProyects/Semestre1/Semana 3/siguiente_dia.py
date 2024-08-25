year=int(input("Type the year (number)"))
month=int(input("Type the month (number)"))
day=int(input("Type the day (number)"))

if day>32 or day<1 or month>12 or month<1 or year<0:
    print("Fecha invalida")

if (day not in [28,29] and month==2) or (day not in [30,31]):
    day+=1

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    bisiesto=True
else:
    bisiesto=False

if month==2 and bisiesto==True and day==28:
    day += 1
elif month==2 and bisiesto==True and day==28:
    day = 1
    month = 3
elif month==2 and bisiesto==False and day==29:
    day = 1
    month = 3
elif month == 2 and (day>29 or (bisiesto==False and day==29)):
    print("Fecha invalida")

if month==12 and day==31:
    year +=1
    month =1
    day=1

if month in [1,3,5,7,8,10] and day==31:
    day=1
    month+=1
elif month in [4,6,9,11] and day==30:
    day=1
    month+=1
elif month in [4,6,9,11] and day==31:
    print("Fecha invalida")

print(day,",",month,",",year)