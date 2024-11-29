//
// Created by admin on 28/11/2024.
//
#include <string>
#include <iostream>
#include <random>
#include "CuentaBancaria.h"

using namespace std;

CuentaBancaria::CuentaBancaria(string _nombreCuenta, float _saldo) {
    nombreCuenta = _nombreCuenta;
    saldo = _saldo;

    //Generar numero aleatorio con formato XXXX-XXXX-XXXX-XXXX
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 9);

    string numero = "";
    for (int i = 0; i < 16; ++i) {
        numero += to_string(dis(gen));
        if (i % 4 == 3 && i < 15) {
            numero += '-';
        }
    }
    numCuenta = numero;
}

void CuentaBancaria::setNombreClave(string _nombreClave) {
    nombreClave = _nombreClave;
}

string CuentaBancaria::getNombreClave() {
    return nombreClave;
}

string CuentaBancaria::getNumCuenta() {
    return numCuenta;
}

void CuentaBancaria::setNumCuenta(string _numCuenta) {
    numCuenta = _numCuenta;
}

string CuentaBancaria::getNombreCuenta() {
    return nombreCuenta;
}

void CuentaBancaria::setNombreCuenta(string _nombreCuenta) {
    nombreCuenta = _nombreCuenta;
}

float CuentaBancaria::getSaldo() {
    return saldo;
}

void CuentaBancaria::setSaldo(float _saldo) {
    saldo = _saldo;
}

void CuentaBancaria::depositar(float _cantidad) {
    saldo += _cantidad;
}

void CuentaBancaria::retirar(float _cantidad) {
    if (_cantidad > saldo) {
        cout << "Saldo insuficiente" << endl;
    } else {
        saldo -= _cantidad;
        cout << _cantidad << " retirada exitosamente" << endl;
    }
}

void CuentaBancaria::mostrarSaldo() {
    cout << "Cuenta: " << nombreClave << endl;
}

CuentaBancaria::~CuentaBancaria() {
    // Destructor virtual para que funcione dynamic_cast
}


void CuentaDebito::asignarTipoDebito() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 3);

    int numRandom = dis(gen);

    if (numRandom == 1) {
        tipoDebito = "Clasica";
    } else if (numRandom == 2) {
        tipoDebito = "Oro";
    } else {
        tipoDebito = "Platino";
    }
}

void CuentaDebito::showComisionMensual() {
    comisionMensual = saldo*0.02;
    cout << "Comision mensual: " << comisionMensual << endl;
}

void CuentaDebito::cobrarComision() {
    saldo -= comisionMensual;
    cout << "Comision cobrada" << endl;
    comisionMensual = saldo*0.02;
}





void CuentaCredito::mostrarSaldo() {
    cout << "Saldo: $" << saldo << endl;
    cout << "Limite de credito: $" << limiteCredito << endl;
    cout << "Fecha de corte: " << fechaCorte << endl;
    cout << "Tasa mensual: " << tasaMensual << endl;
    cout << "Recompensas: " << recompensas << endl;
}



void CuentaInversion::definirRiesgoInversion() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 3);

    int numRandom = dis(gen);

    if (numRandom == 1) {
        riesgoInversion = "Bajo";
    } else if (numRandom == 2) {
        riesgoInversion = "Medio";
    } else {
        riesgoInversion = "Alto";
    }

    gananciasEnInversiones = 0;
}

void CuentaInversion::invertir(float _cantidad) {
    saldo += _cantidad*tasaInteres;
    gananciasEnInversiones++;
    cout << "Inversion de $" << _cantidad << "realizada con exito." << endl;
}

void CuentaInversion::mostrarInversiones() {
    cout << "Saldo: $" << saldo << endl;
    cout << "Tasa de interes: " << tasaInteres << endl;
    cout << "Riesgo de inversion: " << riesgoInversion << endl;
    cout << "Cantidad de inversiones: " << gananciasEnInversiones << endl;
    cout << "Estrategia de inversion: " << estrategiaInversion << endl;
}



void CuentaHipotecario::mostrarDeuda() {
    cout << "Saldo: $" << saldo << endl;
    cout << "Plazo de Meses: $" << plazoMeses << endl;
    cout << "Fecha de corte: " << fechaCorte << endl;
    cout << "Pago mensual: $" << pagoMensual << endl;
    cout << "Deuda total: $" << plazoMeses*pagoMensual << endl;
    cout << "Tipo de propiedad: " << tipoPropiedad << endl;
}

void CuentaHipotecario::abonarMensualidad(int _meses) {
    saldo -= _meses*pagoMensual;
    cout << "Abono realizado con exito" << endl;
    plazoMeses = plazoMeses - _meses;
}



//Destructores
CuentaDebito::~CuentaDebito() {
    cout << "Destructor de CuentaDebito llamado." << endl;
}

CuentaCredito::~CuentaCredito() {
    cout << "Destructor de CuentaCredito llamado." << endl;
}

CuentaInversion::~CuentaInversion() {
    cout << "Destructor de CuentaInversion llamado." << endl;
}

CuentaHipotecario::~CuentaHipotecario() {
    cout << "Destructor de CuentaHipotecario llamado." << endl;
}