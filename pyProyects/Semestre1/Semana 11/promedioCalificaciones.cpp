#include <iostream>
using namespace std;

int main()
{

    double c1, c2, c3, promedio;
    string nombre;

    cout << "Dame el nombre del alumno: ";
    cin >> nombre;
    cout << "Dame la primera calificacion: ";
    cin >> c1;
    cout << "Dame la segunda calificacion: ";
    cin >> c2;
    cout << "Dame la primera calificacion: ";
    cin >> c3;

    promedio = (c1 + c2 + c3) / 3;

    cout << "El promedio de " << nombre << " es: " << promedio << endl;
    return 0;
}