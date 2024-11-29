//
//  SituacionProblema.cpp
//
//  Created by Irasema Alvarez
//
#include <iostream>
#include "SituacionProblema.h"
using namespace std;

int main(){
    CuentaBancaria* cuenta[MAX_CUENTAS];
    int numCuentas = 0;
    int opcion;

    do {
        cout << "\nMenu:\n";
        cout << "1. Leer Nueva Cuenta\n";
        cout << "2. Mostrar Saldo\n";
        cout << "3. Mostrar Cuentas\n";
        cout << "4. Depositar Dinero\n";
        cout << "5. Retirar Dinero\n";
        cout << "6. Salir\n";
        cout << "Elija una opcion: ";
        cin >> opcion;
        cin.ignore();

        switch (opcion){
            case 1: {
                int tipoCuenta;
                cout << "\nSeleccione el tipo de cuenta:\n";
                cout << "1. Cuenta de Debito\n";
                cout << "2. Cuenta de Credito\n";
                cout << "3. Cuenta de Inversion\n";
                cout << "4. Cuenta Hipotecario\n";
                cout << "Elija una opcion: ";
                cin >> tipoCuenta;
                cin.ignore();

                CuentaBancaria* nuevaCuenta = nullptr;
                switch (tipoCuenta) {
                    case 1:
                        nuevaCuenta = new CuentaDebito(0, "", "", 0.0);
                        break;
                    case 2: nuevaCuenta = new CuentaCredito(0, "", "", 0.0);
                        break;
                    case 3: nuevaCuenta = new CuentaInversion(0, "", "", 0.0);
                        break;
                    case 4: { CuentaHipotecario* cuentaHipotecario = new CuentaHipotecario(0, "", "", 0.0);
                        cuentaHipotecario->abonoMensual();
                        nuevaCuenta = cuentaHipotecario;
                        break;
                    }
                    default:
                        cout << "Opcion de cuenta no valida." << endl; continue;
                }
                if (nuevaCuenta != nullptr) {
                    nuevaCuenta->leerNumCuenta();
                    nuevaCuenta->leerNombre();
                    nuevaCuenta->leerApellido();
                    nuevaCuenta->leerSaldo();
                    cuenta[numCuentas++] = nuevaCuenta; }
                break;
            }
            case 2: {
                int cuentaSeleccionada;
                cout << "Introduce el numero de cuenta a consultar: ";
                cin >> cuentaSeleccionada;
                cin.ignore();
                bool encontrada = false;
                for (int i = 0; i < numCuentas; ++i) {
                    if (cuenta[i]->getNumCuenta() == cuentaSeleccionada) {
                        cuenta[i]->mostrarSaldo();
                        encontrada = true;
                        break;
                    }
                }
                if (!encontrada) {
                    cout << "Cuenta no encontrada." << endl;
                }
                break;
            }
            case 3:
                for (int i = 0; i < numCuentas; ++i) {
                    cuenta[i]->mostrar();
                    cout << endl; }
                break;
            case 4: {
                int cuentaSeleccionada;
                cout << "Introduce el numero de cuenta para depositar dinero: ";
                cin >> cuentaSeleccionada;
                cin.ignore();
                bool encontrada = false;
                for (int i = 0; i < numCuentas; ++i) {
                    if (cuenta[i]->getNumCuenta() == cuentaSeleccionada) {
                        cuenta[i]->depositar();
                        encontrada = true;
                        break;
                    }
                }
                if (!encontrada) {
                    cout << "Cuenta no encontrada." << endl;
                }
                break;
            }
            case 5: {
                int cuentaSeleccionada;
                cout << "Introduce el numero de cuenta para retirar dinero: ";
                cin >> cuentaSeleccionada;
                cin.ignore();
                bool encontrada = false;
                for (int i = 0; i < numCuentas; ++i) {
                    if (cuenta[i]->getNumCuenta() == cuentaSeleccionada) {
                        cuenta[i]->retirar();
                        encontrada = true;
                        break;
                    }
                }
                if (!encontrada) {
                    cout << "Cuenta no encontrada." << endl;
                }
                break;
            }
            case 6:
                cout << "Saliendo..." << endl;
                break;
            default: cout << "Opción no válida. Intente de nuevo." << endl; }

        } while (opcion != 4);
        for (int i = 0; i < numCuentas; ++i) {
            delete cuenta[i];
        }

        return 0;
    }
