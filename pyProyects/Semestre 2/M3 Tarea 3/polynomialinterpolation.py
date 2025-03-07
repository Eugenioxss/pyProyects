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

    #puntos
    arrayPoints = np.array([
        (0.55, -1.1),
        (1.3, -1.4),
        (3, -1.8),
        (2.5, -1.8),
        (5.5, -1.5),
        (4, -1.7)
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




main()