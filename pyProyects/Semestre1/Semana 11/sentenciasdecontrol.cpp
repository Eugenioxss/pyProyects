#include <iostream>
using namespace std;

int main()
{
    double saldo, interes;
    char tipo;

    cout << "Saldo de la tarjeta: ";
    cin >> saldo;
    cout << "Tipo de tarjeta (B-Basica, O-Oro, P-Platinum): ";
    cin >> tipo;

    if (tipo == 'B'){
        interes = saldo * 0.10;
    } else if (tipo == 'O'){
        interes = saldo * 0.15;
    } else {
        interes = saldo * 0.20;
    }

    cout << "Interes: " << interes;

}