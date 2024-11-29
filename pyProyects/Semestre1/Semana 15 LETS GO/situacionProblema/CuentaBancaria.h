//
// Created by admin on 28/11/2024.
//
#include <string>
using namespace std;

#ifndef CUENTABANCARIA_H
#define CUENTABANCARIA_H



class CuentaBancaria {
protected:
  string numCuenta;
  string nombreCuenta;
  float saldo;
  string nombreClave;

public:
  CuentaBancaria(string _nombreCuenta, float _saldo);

  void setNombreClave(string _nombreClave);
  string getNombreClave();

  string getNumCuenta();
  void setNumCuenta(string numCuenta);
  string getNombreCuenta();
  void setNombreCuenta(string nombreCuenta);
  float getSaldo();
  void setSaldo(float saldo);


  void depositar(float _cantidad);
  void retirar(float _cantidad);
  void mostrarSaldo();

  virtual ~CuentaBancaria();
};


class CuentaDebito : public CuentaBancaria {
private:
  int comisionApertura = 3000;
  float comisionMensual;
  string tipoDebito;
public:
  CuentaDebito(string _nombreCuenta, float _saldo) : CuentaBancaria(_nombreCuenta, _saldo) {
    comisionMensual = saldo * 0.02;
  }
  void asignarTipoDebito();
  void showComisionMensual();
  void cobrarComision();

  ~CuentaDebito();
};


class CuentaCredito : public CuentaBancaria {
private:
  int limiteCredito = 10000;
  string fechaCorte = "15/12/2024";
  float tasaMensual = 0.04;
  string recompensas = "Puntos";
public:
  CuentaCredito(string _nombreCuenta, float _saldo) : CuentaBancaria(_nombreCuenta, _saldo) {}

  void mostrarSaldo();

  ~CuentaCredito();
};


class CuentaInversion : public CuentaBancaria {
private:
  float tasaInteres = 0.12;
  string riesgoInversion;
  int gananciasEnInversiones;
  string estrategiaInversion = "Crecimiento";
public:
  CuentaInversion(string _nombreCuenta, float _saldo) : CuentaBancaria(_nombreCuenta, _saldo) {}

  void definirRiesgoInversion();
  void invertir(float _cantidad);
  void mostrarInversiones();

  ~CuentaInversion();
};


class CuentaHipotecario : public CuentaBancaria {
private:
  int plazoMeses = 240;
  int pagoMensual;
  string fechaCorte = "28/11/2044";
  string tipoPropiedad = "Casa";
public:
  CuentaHipotecario(string _nombreCuenta, float _saldo) : CuentaBancaria(_nombreCuenta, _saldo) {}

  void mostrarDeuda();
  void abonarMensualidad(int _meses);

  ~CuentaHipotecario();
};


#endif //CUENTABANCARIA_H
