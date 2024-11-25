//
// Created by admin on 11/11/2024.
//
#include <iostream>

using namespace std;

int main(){
    char letras[] = {'a','b','c','d','e','f'};
    char letras2[] = {'g','h','i','j','k','l'};
    char letras3[12];

    cout << "Hello World!" << endl;

    for (int i=0; i<6; i++){
        letras3[i] = letras[i];
        letras3[i+6] = letras2[i];
    }
    for (int l=0; l<12; l++){
        cout << "Indice " << l << ": "<< letras3[l] << endl;
    }

    int sizeito;
    cout << "Ingrese el tamaño del array ";
    cin >> sizeito;

    int numeros[sizeito];

    for (int j=0; j<sizeito; j++) {
        cout << "Ingrese valores int ";
        cin >> numeros[j];
    }

    for (int k=0; k<sizeito; k++){
        cout << "\nValores Ingresados " << numeros[k];
    }

    return 0;
}