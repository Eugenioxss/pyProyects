//By Eugenio Moreno Vargas 28/11/2024 with support of github copilot in C Lion for structure and clarity

#include <iostream>
#include <string>
#include "CuentaBancaria.h"

using namespace std;

const int MAX_CUENTAS = 30;
CuentaBancaria* personas[MAX_CUENTAS];
int numCuentas = 0;

int main() {
    int opcion1;
    string nombre;
    float saldo;

    do {
        cout << "\nMenú:\n";
        cout << "*****************************" << endl;
        cout << "1. Crear Cuenta\n";
        cout << "2. Lista de Cuentas\n";
        cout << "0. Salir\n";
        cout << "*****************************" << endl;
        cout << "Elija una opcion: ";
        cin >> opcion1;
        cin.ignore();

        switch (opcion1) {
            case 1: {
                if (numCuentas < MAX_CUENTAS) {
                    int opcion2;
                    cout << "\nTipo de Cuentas:\n";
                    cout << "1. Cuenta de Débito\n";
                    cout << "2. Cuenta de Crédito\n";
                    cout << "3. Cuenta de Inversión\n";
                    cout << "4. Cuenta Hipotecaria\n";
                    cout << "Elija una opción: ";
                    cin >> opcion2;
                    cin.ignore();

                    cout << "Ingrese el nombre del cliente: ";
                    getline(cin, nombre);
                    cout << "Ingrese el saldo inicial: ";
                    cin >> saldo;

                    switch (opcion2) {
                        case 1: {
                            string CLABE;
                            cout << "Ingrese la CLABE: ";
                            cin >> CLABE;
                            personas[numCuentas++] = new CuentaDebito(nombre, saldo, CLABE);
                            break;
                        }
                        case 2: {
                            float limiteCredito;
                            string fechaCorte, tipoPlastico;
                            cout << "Ingrese el límite de crédito: ";
                            cin >> limiteCredito;
                            cout << "Ingrese la fecha de corte: ";
                            cin >> fechaCorte;
                            cout << "Ingrese el tipo de plástico (VISA/MASTERCARD): ";
                            cin >> tipoPlastico;
                            personas[numCuentas++] = new CuentaCredito(nombre, saldo, limiteCredito, fechaCorte, tipoPlastico);
                            break;
                        }
                        case 3: {
                            string riesgo, apellido;
                            cout << "Ingrese el tipo de riesgo (bajo, medio, alto): ";
                            cin >> riesgo;
                            cout << "Ingrese el apellido del cliente: ";
                            cin >> apellido;
                            personas[numCuentas++] = new CuentaInversion(nombre, saldo, riesgo, apellido);
                            break;
                        }
                        case 4: {
                            float pagoMensual;
                            string numPlastico;
                            cout << "Ingrese el pago mensual: ";
                            cin >> pagoMensual;
                            cout << "Ingrese el número de plástico: ";
                            cin >> numPlastico;
                            personas[numCuentas++] = new CuentaHipotecario(nombre, saldo, pagoMensual, numPlastico);
                            break;
                        }
                    }
                } else {
                    cout << "Capacidad máxima alcanzada.\n";
                }
                break;
            }

            case 2: {
                if (numCuentas == 0) {
                    cout << "No hay cuentas disponibles.\n";
                    break;
                }

                cout << "\nLista de Cuentas:\n";
                for (int i = 0; i < numCuentas; ++i) {
                    cout << i + 1 << ". Nombre: " << personas[i]->getNombreClave() << " | ";
                    personas[i]->mostrarSaldo();
                }
                break;
            }

            case 0:
                cout << "Saliendo...\n";
                break;

            default:
                cout << "Opción no válida. Intente nuevamente.\n";
                break;
        }

    } while (opcion1 != 0);

    for (int i = 0; i < numCuentas; ++i) {
        delete personas[i];
    }

    return 0;
}
