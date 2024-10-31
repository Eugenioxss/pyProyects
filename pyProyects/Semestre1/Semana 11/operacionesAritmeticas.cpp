#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float n1, n2;

    cout << "Numero 1: ";
    cin >> n1;
    cout << "Numero 2: ";
    cin >> n2;

    cout << "El resultado de "<< "sumar " << n1 << " y " << n2 << " es igual a " << n1 + n2 << endl;
    cout << "El resultado de "<< "restar " << n1 << " y " << n2 << " es igual a " << n1 - n2 << endl;
    cout << "El resultado de "<< "multiplicar " << n1 << " y " << n2 << " es igual a " << n1 * n2 << endl;
    cout << "El resultado de "<< "dividir " << n1 << " y " << n2 << " es igual a " << n1 / n2 << endl;
    cout << "El residuo de la división de " << n1 << " y " << n2 << " es igual a " << fmod(n1,n2) << endl;
    return 0;
}