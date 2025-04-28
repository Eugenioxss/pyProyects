import numpy as np
import math
import matplotlib.pyplot as plt


def main():
    #Static Variables
    g = 9.81 #m/s2
    airD = 1.29 #kg/m3
    oilD = 860 #kg/m3
    platesD = 0.009 #m
    airV = 1.83*np.power(10.0,-5) #pas
    U = 4000 #V
    mHeightSpray = .1 #m 
    n = int(input("Number of simulations to run: "))
    chargesList = np.empty(n)

    e = 1.602e-19

    for i in range (0,n):

        #Gauss Bell for generation of radii (maybe a bit overcomplicated, we know 😁)
        mu = math.log(math.sqrt(10**-6 * 10**-5)) #ln(hypotenuse bwetween our orders of magnitud), approximately -12.664
        sigma = 0.4 #Standard Deviation
        while True:
            r = np.random.lognormal(mu, sigma)
            #print(r)
            if 0.000001 <= r <= 0.00001: 
                break

        vDrop = (4/3) * np.pi * (r**3)
        mDrop = vDrop * oilD #Drop's mass
        fgDrop = mDrop * g #Gravitational Force ejerced by the Oil Drop
        bfDrop = vDrop * airD * g #Bouyancy Force
        netForce = fgDrop - bfDrop
        vMax = netForce / (6 * np.pi * airV * r)  # Terminal Velocity
        
        electricCamp = U / platesD
        qDrop = netForce / electricCamp
        k = np.random.randint(1, 10)  # Calculates a random multiple of e between 1 and 9
        qDrop_emultiple = k * e #Assigns the multiple

        chargesList[i] = qDrop_emultiple
        print(i)

        # Only for the first droplet
        if i == 0:
            time_list = []
            position_list = []
            velocity_list = []

            t = 0
            dt = 0.00001
            max_time = 2

            current_height = platesD / 2
            current_velocity = vMax
            previous_velocity = current_velocity

            while current_height > -platesD / 2 and t < max_time:
                electricForce = qDrop_emultiple * electricCamp
                drag_force = 6 * np.pi * airV * r * current_velocity
                net_force_total = fgDrop - bfDrop + electricForce - np.sign(current_velocity) * abs(drag_force)
                acceleration = net_force_total / mDrop

                current_velocity += acceleration * dt
                current_height += current_velocity * dt

                time_list.append(t)
                position_list.append(current_height)
                velocity_list.append(current_velocity)

                if abs(acceleration) < 1e-6 and abs(current_velocity - previous_velocity) < 1e-6:
                    break

                previous_velocity = current_velocity
                t += dt



    nonzero_charges = chargesList[chargesList != 0] #If generated drops with charge 0
    sorted_charges = np.sort(nonzero_charges) #Lower to higher
    differences = np.abs(np.diff(sorted_charges)) #Difference between consecutives charges

    differences = differences[differences > 1e-21] #Gets rid of non-useful data

    e_estimated = np.min(differences) #The difference will be in multiples of e (1e, 2e, 3e, 4e), so we just want the 1e difference, which is the lowest

    qdropcharges = np.mean(nonzero_charges)
    print("Average charge of droplets without zeros: ", qdropcharges, " C") #A bit useless

    print("Estimated charge of e: ", e_estimated)


    #Visual Stuff
    time_array = np.array(time_list)
    position_array = np.array(position_list)
    velocity_array = np.array(velocity_list)

    # 1) Calcula desplazamiento relativo arrancando en cero:
    rel_disp = position_array - position_array[0]

    # 2) (Opcional) pasa a micrómetros para verlo más claro:
    rel_disp_um = rel_disp * 1e6  # 1 m = 1e6 μm

    # Gráfica desplazamiento vs tiempo sin las placas:
    plt.figure()
    plt.plot(time_array, rel_disp_um, label='Desplazamiento de la gota')
    plt.title('Desplazamiento vs Tiempo')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Desplazamiento (μm)')
    plt.grid(True)
    plt.legend()

    # Gráfica velocidad vs tiempo
    plt.figure()
    plt.plot(time_array, velocity_array)
    plt.title('Velocidad vs Tiempo (caída)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.grid(True)

    plt.show()

main()