import numpy as np

# Definir el perfil exterior del vaso
def perfil_externo(x):
    return 0.00025 * x**4 - 0.012 * x**3 + 0.2 * x**2 - 1.291 * x - 2.06

# Definir el perfil interior del vaso
def perfil_interno(x, grosor_lateral):
    return perfil_externo(x) - 2 * grosor_lateral

# Calcular el volumen del vaso
def volumen_vaso(altura, grosor_lateral, base_grosor):
    # Definir el número de puntos para la integración
    n = 1000
    x = np.linspace(0, altura, n)
    
    # Calcular el perfil exterior e interior
    y_exterior = perfil_externo(x)
    y_interior = perfil_interno(x, grosor_lateral)
    
    # Asegurarse de que el perfil interior no tenga valores negativos
    y_interior[y_interior < 0] = 0
    
    # Calcular el volumen exterior e interior usando integración numérica
    volumen_exterior = np.pi * np.trapezoid(y_exterior**2, x)
    volumen_interior = np.pi * np.trapezoid(y_interior**2, x)
    
    # Calcular el volumen del cuerpo del vaso
    volumen_cuerpo = volumen_exterior - volumen_interior
    
    # Calcular el volumen de la base
    y_exterior_base = perfil_externo(0)
    y_interior_base = perfil_interno(0, grosor_lateral)
    volumen_base = np.pi * (y_exterior_base**2 - y_interior_base**2) * base_grosor
    
    # Calcular el volumen total del vaso
    volumen_total = volumen_cuerpo + volumen_base
    
    return volumen_total

# Template para ingresar valores
altura_vaso = 19.59  # Altura del vaso en cm
grosor_lateral_vaso = 1  # Grosor lateral del vaso en cm
base_grosor_vaso = 2  # Grosor de la base del vaso en cm

# Calcular el volumen del vaso
volumen = volumen_vaso(altura_vaso, grosor_lateral_vaso, base_grosor_vaso)

print(f"El volumen del vaso es {volumen:.2f} cm³")