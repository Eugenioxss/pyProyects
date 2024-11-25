#include <iostream>
using namespace std;

void cargaArreglo(int arr[10], int &size) {
    cout << "Cuantos datos tiene el arreglo " << endl;
    cin >> size;

    for (int cont = 0; cont < size; cont++) {
        cout << "Dato[" << cont << "] = ";
        cin >> arr[cont];
    }
}

void sumaArreglo(int arroz[10], int &size) {
    int suma = 0, numerito;

    cout << "Cuantos datos tiene el arreglo " << endl;
    cin >> size;

    for (int cont = 0; cont < size; cont++) {
        cout << "Dato[" << cont << "] = ";
        cin >> numerito;
        arroz[cont] = numerito;
            if (numerito % 2 == 0) {
                suma += numerito;
            }
    }
    cout << "El arreglo es: ";
    for (int cont = 0; cont < size; cont++) {
        cout << arroz[cont] << " ";
    }
    cout << endl;
    cout << "La suma de los pares es: " << suma << endl;
}


int main() {
    int arregloA[10];
    int tamA;

    // Llama a la función para cargar datos al arreglo A
    cargaArreglo(arregloA, tamA);
    sumaArreglo(arregloA, tamA);

    return 0;
}