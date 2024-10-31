#include <iostream>
using namespace std;

int main()
{
  string nombre, saldo;
  int edad;

  cout << "Nombre del Cliente:";
  cin >> nombre;
  cout << "Saldo del Cliente:";
  cin >> saldo;
  cout << "Edad del Cliente:";
  cin >> edad;
  cout << "Cliente: " << nombre << " con Saldo: " << saldo << " con Edad: " << edad;

}