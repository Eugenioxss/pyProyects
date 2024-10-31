#include <iostream>
using namespace std;

int main()
{
    double n1, n2, intermed;

    cout << "Dame el primer valor: ";
    cin >> n1;
    cout << "Dame el segundo valor: ";
    cin >> n2;

    intermed = n2;
    n2 = n1;
    n1 = intermed;

    cout << "Valor 1 es: " << n1 << endl;
    cout << "Valor 2 es: " << n2 << endl;

    return 0;
}