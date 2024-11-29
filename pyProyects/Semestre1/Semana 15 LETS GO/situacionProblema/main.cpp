#include <iostream>
#include <iomanip>
#include "CuentaBancaria.h"

using namespace std;

int main() {
    string nombreUsuario;
    float saldoTotal;

    cout << "Bienvenido al Banco\n";
    cout << "Introduce el nombre de usuario: " << endl;
    cin >> nombreUsuario;
    cout << "Bienvenido " << nombreUsuario << endl;
    cout << "Introduce tu saldo total (tip: escribe un numero grande)" << endl;
    cin >> saldoTotal;
    CuentaBancaria cuentaBase(nombreUsuario, saldoTotal);
    cout << fixed << setprecision(4);


    const int MAX_CUENTAS = 30;
    CuentaBancaria* personas[MAX_CUENTAS];
    int numCuentas = 0;
    int opcion1;

    do {
        cout << "\nMenu:\n";
        cout << "*****************************" << endl;
        cout << "1. Crear Cuenta\n";
        cout << "2. Acciones en Cuentas\n";
        cout << "3. Lista de Cuentas\n";
        cout << "0. Salir\n";
        cout << "*****************************" << endl;

        cout << "Elija una opcion: ";
        cin >> opcion1;
        cin.ignore();

        switch (opcion1) {
            case 1: {
                if (numCuentas < MAX_CUENTAS) {
                    int opcion2;
                    do {
                        cout << "\nTipo de Cuentas:\n";
                        cout << "*****************************" << endl;
                        cout << "1. Cuenta de Debito\n";
                        cout << "2. Cuenta de Credito\n";
                        cout << "3. Cuenta de Inversion\n";
                        cout << "4. Cuenta de Hipoteca\n";
                        cout << "*****************************" << endl;

                        cout << "Elija una opcion: ";
                        cin >> opcion2;
                        cin.ignore();
                    } while (opcion2 < 1 || opcion2 > 4);

                    string nombreClave;
                    cout << "Ingrese un nombreclave para identificar esta cuenta: ";
                    getline(cin, nombreClave);

                    switch (opcion2) {
                        case 1: {
                            CuentaDebito* cuentaDebito = new CuentaDebito("", 0);
                            cuentaDebito->setNombreClave(nombreClave);
                            cuentaDebito->asignarTipoDebito();
                            personas[numCuentas++] = cuentaDebito;
                            break;
                        }
                        case 2: {
                            CuentaCredito* cuentaCredito = new CuentaCredito("", 0);
                            cuentaCredito->setNombreClave(nombreClave);
                            personas[numCuentas++] = cuentaCredito;
                            break;
                        }
                        case 3: {
                            CuentaInversion* cuentaInversion = new CuentaInversion("", 0);
                            cuentaInversion->setNombreClave(nombreClave);
                            cuentaInversion->definirRiesgoInversion();
                            personas[numCuentas++] = cuentaInversion;
                            break;
                        }
                        case 4: {
                            CuentaHipotecario* cuentaHipotecario = new CuentaHipotecario("", 0);
                            cuentaHipotecario->setNombreClave(nombreClave);
                            personas[numCuentas++] = cuentaHipotecario;
                            break;
                        }
                    }

                } else {
                    cout << "Capacidad maxima alcanzada.\n";
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
        cout << i + 1 << ". NombreClave: " << personas[i]->getNombreClave()
             << " | Tipo: " << typeid(*personas[i]).name() << endl;
    }

    int seleccion;
    cout << "Seleccione el número de la cuenta para realizar acciones (0 para volver al menú principal): ";
    cin >> seleccion;

    if (seleccion <= 0 || seleccion > numCuentas) {
        cout << "Selección no válida. Regresando al menú principal.\n";
        break;
    }

    seleccion -= 1;

    if (auto* cuentaDebito = dynamic_cast<CuentaDebito*>(personas[seleccion])) {
        int accion6;
        do {
            cout << "\nMenú Cuenta Débito:\n";
            cout << "1. Mostrar Tipo de Débito\n";
            cout << "2. Mostrar Comisión Mensual\n";
            cout << "3. Cobrar Comisión\n";
            cout << "0. Volver al menú principal\n";
            cout << "Seleccione una acción: ";
            cin >> accion6;

            switch (accion6) {
                case 1:
                    cout << "Tipo de Débito: Clásica/Oro/Platino\n"; // Placeholder, puedes personalizar
                    break;
                case 2:
                    cuentaDebito->showComisionMensual();
                    break;
                case 3:
                    cuentaDebito->cobrarComision();
                    break;
                case 0:
                    cout << "Regresando al menú principal.\n";
                    break;
                default:
                    cout << "Opción no válida. Intente de nuevo.\n";
            }
        } while (accion6 != 0);

    } else if (auto* cuentaCredito = dynamic_cast<CuentaCredito*>(personas[seleccion])) {
        // Submenú para Cuenta Crédito
        int accion;
        do {
            cout << "\nMenú Cuenta Crédito:\n";
            cout << "1. Mostrar Saldo\n";
            cout << "2. Mostrar Recompensas\n";
            cout << "0. Volver al menú principal\n";
            cout << "Seleccione una acción: ";
            cin >> accion;

            switch (accion) {
                case 1:
                    cuentaCredito->mostrarSaldo();
                    break;
                case 2:
                    cout << "Recompensas: Puntos acumulados.\n"; // Placeholder
                    break;
                case 0:
                    cout << "Regresando al menu principal.\n";
                    break;
                default:
                    cout << "Opción no valida. Intente de nuevo.\n";
            }
        } while (accion != 0);

    } else if (auto* cuentaInversion = dynamic_cast<CuentaInversion*>(personas[seleccion])) {
        // Submenú para Cuenta Inversión
        int accion;
        do {
            cout << "\nMenú Cuenta Inversion:\n";
            cout << "1. Mostrar Inversiones\n";
            cout << "2. Invertir Dinero\n";
            cout << "3. Definir Riesgo\n";
            cout << "0. Volver al menu principal\n";
            cout << "Seleccione una acción: ";
            cin >> accion;

            switch (accion) {
                case 1:
                    cuentaInversion->mostrarInversiones();
                    break;
                case 2: {
                    float cantidad;
                    cout << "Ingrese la cantidad a invertir: ";
                    cin >> cantidad;
                    cuentaInversion->invertir(cantidad);
                    break;
                }
                case 3:
                    cuentaInversion->definirRiesgoInversion();
                    break;
                case 0:
                    cout << "Regresando al menu principal.\n";
                    break;
                default:
                    cout << "Opcion no válida. Intente de nuevo.\n";
            }
        } while (accion != 0);

    } else if (auto* cuentaHipoteca = dynamic_cast<CuentaHipotecario*>(personas[seleccion])) {
        // Submenú para Cuenta Hipotecaria
        int accion;
        do {
            cout << "\nMenú Cuenta Hipotecaria:\n";
            cout << "1. Mostrar Deuda\n";
            cout << "2. Abonar Mensualidad\n";
            cout << "0. Volver al menu principal\n";
            cout << "Seleccione una accion: ";
            cin >> accion;

            switch (accion) {
                case 1:
                    cuentaHipoteca->mostrarDeuda();
                    break;
                case 2: {
                    int meses;
                    cout << "Ingrese el numero de meses a abonar: ";
                    cin >> meses;
                    cuentaHipoteca->abonarMensualidad(meses);
                    break;
                }
                case 0:
                    cout << "Regresando al menu principal.\n";
                    break;
                default:
                    cout << "Opcion no válida. Intente de nuevo.\n";
            }
        } while (accion != 0);
    }

    break;
            }
            case 3:
                cout << "Lista de Cuentas:\n";
            for (int i = 0; i < numCuentas; ++i) {
                personas[i]->mostrarSaldo();
            }
            break;
            case 0:
                cout << "Saliendo del programa...\n";
            break;
            default:
                cout << "Opcion no valida. Por favor, intente de nuevo.\n";
        }
    } while (opcion1 != 0);

    // Liberar memoria
    for (int i = 0; i < numCuentas; ++i) {
        delete personas[i];
    }

    return 0;
}
