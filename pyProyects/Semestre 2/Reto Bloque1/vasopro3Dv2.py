import matplotlib.pyplot as plt
import numpy as np

n = 501  # Número de puntos y dominio
x1 = np.linspace(0, 19.59, n)  # Altura del vaso

def perfil_externo(x):
    return 0.00025 * x**4 - 0.012 * x**3 + 0.2 * x**2 - 1.291 * x - 2.06

y1 = perfil_externo(x1)  # Perfil exterior

grosor_lateral = 0.5
base_grosor = 1.1

# Perfil interno
x2 = x1[x1 >= base_grosor]
y2 = perfil_externo(x2) - grosor_lateral

y2[y2 < 0] = 0  # Evitar radios negativos

# Configuración de la gráfica
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')

# Dibujar el perfil 2D del vaso
ax1.plot(y1, x1, color='r', label="Interior")
ax1.plot(-y1, x1, color='r')

# Grosor en la base
ax1.hlines(base_grosor, -perfil_externo(base_grosor), perfil_externo(base_grosor), color='r', linestyle='--')
ax1.hlines(0, -perfil_externo(0), perfil_externo(0), color='r', linestyle='--')

# Eliminar la línea vertical y crear una línea paralela e idéntica a la línea roja original con un grosor de 0.3
ax1.plot(perfil_externo(x1) - grosor_lateral, x1, color='b',label="Exterior",)
ax1.plot(-(perfil_externo(x1) - grosor_lateral), x1, color='b')

ax1.set_xlim([-10, 10])
ax1.set_ylim([0, 20])
ax1.set_title("Perfil del Vaso")
ax1.set_xlabel("Radio")
ax1.set_ylabel("Altura")
ax1.legend()

# Vector de rotación para el 3D
t = np.linspace(0, np.pi * 2, n)
xn = np.outer(y1, np.sin(t))
yn = np.outer(y1, np.cos(t))
zn = np.zeros_like(yn)
for i in range(len(x1)):
    zn[i:i+1, :] = np.full_like(zn[0, :], x1[i])
ax2.plot_surface(yn, xn, zn, color='b', alpha=0.6)
ax2.set_xlim([-10, 10])
ax2.set_ylim([-10, 10])
ax2.set_zlim([0, 20])
ax2.set_title("Vista 3D del Vaso")

plt.show()