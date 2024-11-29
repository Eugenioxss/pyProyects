#include "CuentaBancaria.h"

// Constructor Base
CuentaBancaria::CuentaBancaria(string _nombreCliente, float _saldo) {
    nombreCliente = _nombreCliente;
    nombreClave = _nombreCliente;
    saldo = _saldo;
    numeroCuenta = "XXXX-XXXX-XXXX";
}

string CuentaBancaria::getNombreClave() const {
    return nombreClave;
}

void CuentaBancaria::mostrarSaldo() {
    cout << "Saldo actual: $" << saldo << endl;
}

void CuentaBancaria::depositar(float cantidad) {
    saldo += cantidad;
    cout << "Depósito realizado. Nuevo saldo: $" << saldo << endl;
}

void CuentaBancaria::retirar(float cantidad) {
    if (cantidad > saldo) {
        cout << "Saldo insuficiente." << endl;
    } else {
        saldo -= cantidad;
        cout << "Retiro realizado. Nuevo saldo: $" << saldo << endl;
    }
}

// CuentaDebito
CuentaDebito::CuentaDebito(string _nombreCliente, float _saldo, string _CLABE)
    : CuentaBancaria(_nombreCliente, _saldo - comisionApertura), CLABE(_CLABE) {}

void CuentaDebito::mostrarSaldo() {
    saldo -= saldo * comisionMensual;
    cout << "Saldo con comisión: $" << saldo << endl;
}

// CuentaCredito
CuentaCredito::CuentaCredito(string _nombreCliente, float _saldo, float _limiteCredito, string _fechaCorte, string _tipoPlastico)
    : CuentaBancaria(_nombreCliente, _saldo), limiteCredito(_limiteCredito), fechaCorte(_fechaCorte), tipoPlastico(_tipoPlastico) {}

void CuentaCredito::mostrarSaldo() {
    saldo -= saldo * tasaAnual;
    cout << "Saldo después de aplicar tasa: $" << saldo << endl;
}

// CuentaInversion
CuentaInversion::CuentaInversion(string _nombreCliente, float _saldo, string _tipoRiesgo, string _apellidoCliente)
    : CuentaBancaria(_nombreCliente, _saldo), tipoRiesgo(_tipoRiesgo), apellidoCliente(_apellidoCliente) {}

void CuentaInversion::mostrarSaldo() {
    saldo += saldo * tasaInteres;
    cout << "Saldo con interés: $" << saldo << endl;
}

// CuentaHipotecario
CuentaHipotecario::CuentaHipotecario(string _nombreCliente, float _saldo, float _pagoMensual, string _numPlastico)
    : CuentaBancaria(_nombreCliente, _saldo), pagoMensual(_pagoMensual), numPlastico(_numPlastico) {}

void CuentaHipotecario::mostrarSaldo() {
    cout << "Saldo actual: $" << saldo << endl;
    cout << "Pago mensual: $" << pagoMensual << endl;
}
