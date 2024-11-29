#include <string>
#include <iostream>
using namespace std;

#ifndef CUENTA_BANCARIA_H
#define CUENTA_BANCARIA_H

class CuentaBancaria {
protected:
  string numeroCuenta;
  string nombreCliente;
  float saldo;
  string nombreClave;

public:
  CuentaBancaria(string _nombreCliente, float _saldo);

  virtual void mostrarSaldo();
  void depositar(float cantidad);
  virtual void retirar(float cantidad);

  string getNombreClave() const;

  virtual ~CuentaBancaria() {}
};

class CuentaDebito : public CuentaBancaria {
private:
  const float comisionApertura = 50.0;
  const float comisionMensual = 0.02;
  string CLABE;  // Nuevo atributo
public:
  CuentaDebito(string _nombreCliente, float _saldo, string _CLABE);
  void mostrarSaldo() override;
  ~CuentaDebito() {}
};

class CuentaCredito : public CuentaBancaria {
private:
  float limiteCredito;
  string fechaCorte;
  const float tasaAnual = 0.04;
  string tipoPlastico;  // Nuevo atributo (VISA, MASTERCARD)
public:
  CuentaCredito(string _nombreCliente, float _saldo, float _limiteCredito, string _fechaCorte, string _tipoPlastico);
  void mostrarSaldo() override;
  ~CuentaCredito() {}
};

class CuentaInversion : public CuentaBancaria {
private:
  const float tasaInteres = 0.12;
  string tipoRiesgo;
  string apellidoCliente;  // Nuevo atributo
public:
  CuentaInversion(string _nombreCliente, float _saldo, string _tipoRiesgo, string _apellidoCliente);
  void mostrarSaldo() override;
  ~CuentaInversion() {}
};

class CuentaHipotecario : public CuentaBancaria {
private:
  const int plazoMeses = 240;
  float pagoMensual;
  string numPlastico;  // Nuevo atributo
public:
  CuentaHipotecario(string _nombreCliente, float _saldo, float _pagoMensual, string _numPlastico);
  void mostrarSaldo() override;
  ~CuentaHipotecario() {}
};

#endif // CUENTA_BANCARIA_H
