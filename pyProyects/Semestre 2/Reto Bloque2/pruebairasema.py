import numpy as np

def main():
    g = 9.81  # m/s²
    airD = 1.29  # kg/m³
    oilD = 860  # kg/m³
    platesD = 0.1  # m
    airV = 1.83e-5  # Pa·s (viscosidad del aire)
    U = 280  # V
    mHeightSpray = 0.1  # m
    e_charge = 1.602e-19  # C (carga elemental)

    r = np.random.uniform(4.37e-7, 1.64e-6)  # Radio de la gota en metros
    V = (4/3) * np.pi * (r*3)  # Volumen de la gota
    m = V * oilD  # Masa de la gota
    Fg = m * g  # Fuerza gravitacional
    Fb = V * airD * g  # Fuerza de flotación
    Feq = Fg - Fb  # Fuerza neta actuante
    v = Feq / (6 * np.pi * airV * r)  # Velocidad límite

#Cálculo de la carga en equilibrio con el campo eléctrico
    E = U / platesD  # Campo eléctrico
    q = Feq / E  # Carga de la gota
    n_electrons = round(q / e_charge)  # Número entero de cargas elementales

    print(f"Radio de la gota: {r:.2e} m")
    print(f"Velocidad límite: {v:.2e} m/s")
    print(f"Carga de la gota: {q:.2e} C")
    print(f"Número de electrones en la gota: {n_electrons}")

if name == "main":
    main()
