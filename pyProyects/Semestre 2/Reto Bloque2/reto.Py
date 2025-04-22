import numpy as np

def main():
    g = 9.81 #m/s2
    airD = 1.29 #kg/m3
    oilD = 860 #kg/m3
    platesD = 0.1 #m
    airV = 1.83*np.power(10.0,-5) #pas
    U = 280 #V
    mHeightSpray = .1 #m 

    r = np.random.uniform(0.000000437, 0.00000164) #generador de radios de gota de aceite

    a = 0

    while a != 0:
        print(a)

main()