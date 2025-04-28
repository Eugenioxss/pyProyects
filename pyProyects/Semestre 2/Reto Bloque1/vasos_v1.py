import numpy as np

# Creamos una lista con los puntos asignados
lista_valores = [[0,1.35],[1.25,2.189],[8,2.14],[5,2],[3,2.12],[6.52,2.03],[0.47,1.75],[2.01,2.17],[4.07,2.03],[5.8,1.98],[7.26,2.06],[7.72,2.10]]
X = len(lista_valores)
# Creamos dos matrices, una para la eje de las x y otro para el eje de las y
A = np.zeros((X,X))
B = np.zeros(X)

# Iteramos una primera vez para acceder al indice de los puntos
for i in range(len(lista_valores)):
    # Reemplazamos los valores de la matriz B por y de los puntos
    b = lista_valores[i][1]
    B[i] = b
    for j in range(len(lista_valores)):
        # elevamos x a la potencia correspondiente
        # Reemplazamos los valor de la matriz A por el resultado de x de los puntos
        a = lista_valores[i][0] ** j
        A[i][j] = a

# Calculamos el producto de la inversa de la matriz A por la matriz B
producto = np.linalg.inv(A) @ B
print("\n a = {}".format(producto)) 







