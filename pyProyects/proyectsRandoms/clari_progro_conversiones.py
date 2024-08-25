import math
mscm=int(input("Type distance in cm:  "))

if (mscm>0 and mscm<100):
    print(mscm, "cm")
elif (mscm>=100 and mscm<100000 and mscm>0):
    print(math.floor(mscm//100), "m")
    if((mscm%100)!=0):
            print(math.floor(mscm%100), "cm")
elif(mscm>=100000):
    print(math.floor(mscm//100000), "km")
    if((mscm%100000)>0 and (mscm%100000//100!=0)):
        print(math.floor(mscm%100000//100), "m")
        if((mscm%100)!=0):
            print(math.floor(mscm%100), "cm")
    elif((mscm%100000)%100!=0):
            print(math.floor(mscm%100), "cm")    
