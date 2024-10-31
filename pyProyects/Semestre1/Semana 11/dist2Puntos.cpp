#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double x1, x2, y1, y2, distancia;
    cout << "Ingrese las coordenadas del primer punto (x1, y1): ";
    cin >> x1 >> y1;
    cout << "Ingrese las coordenadas del segundo punto (x2, y2): ";
    cin >> x2 >> y2;
    distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    cout << "La distancia entre los dos puntos es: " << distancia << endl;
}