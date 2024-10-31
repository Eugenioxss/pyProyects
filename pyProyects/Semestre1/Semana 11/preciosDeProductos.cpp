#include <iostream>
using namespace std;

int main()
{
    double precio, impuesto;

    cout << "Precio del producto: ";
    cin >> precio;
    cout << "Porcentaje de impuesto añadido: ";
    cin >> impuesto;

    cout << "El precio del producto con el " << impuesto << " de iva es: " << (impuesto/100 + 1) * precio;

}