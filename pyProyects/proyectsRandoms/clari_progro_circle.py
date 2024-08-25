import math

radius=float(input("Type circle's radius:  "))
cenx=float(input("Type circle's center loc x:  "))
ceny=float(input("Type circle's center loc y:  "))
x1=float(input("Type point to evaluate x:  "))
y1=float(input("Type point to evaluate y:  "))

distance=math.sqrt((x1-cenx)**2+(y1-ceny)**2)

if(distance<radius):
    print("The point is inside the circle")
elif(distance>radius):
    print("The point is outside the circle")
elif(distance==radius):
    print("The point is on the circumference")