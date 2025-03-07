import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Función para crear un vaso con bordes que se estrechan a la mitad
def twisted_glass(height=10, base_radius=3, segments=6):
    theta = np.linspace(0, 2 * np.pi, segments + 1)
    z_levels = np.linspace(0, height, 20)

    x_coords, y_coords, z_coords = [], [], []

    for z in z_levels:
        # Reducir radio hacia la mitad y expandir de nuevo
        radius = base_radius * (1 - 0.3 * np.sin((z / height) * np.pi))
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(np.full_like(x, z))

    return x_coords, y_coords, z_coords


# Visualizar el vaso en 3D
def plot_glass(x_coords, y_coords, z_coords):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar las paredes laterales
    for i in range(len(z_coords) - 1):
        for j in range(len(x_coords[i]) - 1):
            verts_side = [
                [x_coords[i][j], y_coords[i][j], z_coords[i][j]],
                [x_coords[i][j + 1], y_coords[i][j + 1], z_coords[i][j + 1]],
                [x_coords[i + 1][j + 1], y_coords[i + 1][j + 1], z_coords[i + 1][j + 1]],
                [x_coords[i + 1][j], y_coords[i + 1][j], z_coords[i + 1][j]]
            ]
            ax.add_collection3d(Poly3DCollection([verts_side], color='cyan', alpha=0.4))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


# Crear y visualizar el vaso con los bordes ajustados
x_coords, y_coords, z_coords = twisted_glass()
plot_glass(x_coords, y_coords, z_coords)

# ¿Te gustaría ajustar más la forma o probar con otra curvatura? 🚀
