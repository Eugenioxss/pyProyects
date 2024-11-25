//
// Created by admin on 07/11/2024.
//
#include <iostream>

using namespace std;

int main() {
    int num;
    cout << "Tabla de multiplicar " << endl;
    cout << "Dame el numero de tablas a multiplicar: ";
    cin >> num;

    int i = 1;
    int j = 1;

    while (j<11){
        cout << i << " x " << j << " = " << j * i << endl;
        j++;
    }
    i++;
    while (i<=num) {
        cout << i << " x " << j << " = " << j * i << endl;
        i++;
    }
    return 0;
}
