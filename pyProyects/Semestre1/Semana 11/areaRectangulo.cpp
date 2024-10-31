#include <iostream>
using namespace std;

double calcArea(double _base, double _alt){
    double _area;
    _area = _base * _alt;
    return _area;
}

int main()
{
    double base, altura, area;

    cout << "Base: ";
    cin >> base;
    cout << "Altura: ";
    cin >> altura;
    area = calcArea(base, altura);
    cout << "Area:" << area;
}