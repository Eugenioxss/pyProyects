import numpy as np

def main():

    """
    polynomialGrade = int(input("Escribe el grado del polinomio"))

    arrayBegin= np.array = []

    for i in range (0,polynomialGrade):
        print("Coeficiente grado ",polynomialGrade-i)
        arrayBegin.append(int(input()))
        print()

    print(arrayBegin)
    """

    # Puntos
    arrayPoints = np.array([
        (0.34, -0.63),
        (0.95, -1.4),
        (2.53, -1.81),
        (4.38, -1.57),
        (4.94, -1.398)
    ])

    # y = a0 + a1x + a2x2 + a3x3 + a4x4 + a5x5
    n = len(arrayPoints)
    a = np.zeros((n,n))
    b = np.zeros(n)

    for i in range(n):
        x,y = arrayPoints[i]
        b[i] = y
        for j in range(n):
            a[i, j] = x ** j

    A = np.matrix(a)
    coefficients = np.linalg.inv(A) @ b
    print(np.flip(coefficients))
    #Se voltean para que aparezcan de mayor grado a menor grado



main()