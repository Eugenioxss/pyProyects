import numpy as np

def main():

    arrayPoints = np.array([
        (0.76, -2.93),
        (1.67, -3.71),
        (3.84, -4.69),
        (12.56, -4.46),
        (19.59, -4.7)
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