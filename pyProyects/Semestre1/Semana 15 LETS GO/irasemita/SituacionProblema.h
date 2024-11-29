//
//  SituacionProblema.h
//
//  Created by Irasema Alvarez on 28/11/24.
//
using namespace std;

const int MAX_CUENTAS = 30;

class CuentaBancaria{
private:
    int numCuenta;
    string nombre;
    string apellido;
    double saldo;
public:
    CuentaBancaria(int numCuenta, const string &nombre, const string &apellido, double saldo) : numCuenta(numCuenta), nombre(nombre), apellido(apellido), saldo(saldo) {}
    
    void setNumCuenta(int numCuenta) {
        this->numCuenta = numCuenta;
    }
    void setNombre (const string &nombre) {
        this->nombre = nombre;
    }
    void setApellido (const string &apellido) {
        this->apellido = apellido;
    }
    void setSaldo(const double &saldo) {
        this->saldo = saldo;
    }
    int getNumCuenta() const {
        return numCuenta;
    }
    string getNombre() const {
        return nombre;
    }
    string getApellido() const {
        return apellido;
    }
    double getSaldo() const {
        return saldo;
    }
    void leerNumCuenta() {
        cout << "Introduce el numero de cuenta: ";
        cin >> numCuenta;
        cin.ignore();
    }
    void leerNombre() {
        cout << "Introduce el nombre: ";
        getline(cin, nombre);
    }
    void leerApellido() {
        cout << "Introduce el apellido: ";
        getline(cin, apellido);
    }
    void leerSaldo() {
        cout << "Introduce el saldo: ";
        cin >> saldo;
        cin.ignore();
    }
    void depositar(){
        double cantidad;
        cout << "Introduce la cantidad a depositar: ";
        cin >> cantidad;
        saldo += cantidad;
        cout << "Deposito realizado." << endl;
    }
    void retirar(){
        double cantidad;
        cout << "Introduce la cantidad a retirar: ";
        cin >> cantidad;
        if (cantidad <= saldo) {
            saldo -= cantidad;
            cout << "Retiro realizado."<< endl;
        }
        else {
            cout << "Fondos insuficientes." << endl;
        }
        cin.ignore(); 
    }
    virtual void mostrar() const {
        cout << "Número de cuenta: " << numCuenta << endl;
        cout << "Nombre: " << nombre << endl;
        cout << "Apellido: " << apellido << endl;
        cout << "Saldo: " << saldo << endl;
    }
    void mostrarSaldo(){
        cout << "Saldo actual: " << saldo << endl;
    }
    virtual ~CuentaBancaria() = default;
};

class CuentaDebito : public CuentaBancaria{
public:
    CuentaDebito(int numCuenta, const string &nombre, const string &apellido, double saldo) : CuentaBancaria(numCuenta, nombre, apellido, saldo) {}
    
    void nuevoSaldo() {
        setSaldo(getSaldo() * 0.98);
    }
    void mostrar() const override {
            cout << "Cuenta de Debito" << endl;
            CuentaBancaria::mostrar();
        }
};

class CuentaCredito : public CuentaBancaria{
public:
    CuentaCredito(int numCuenta, const string &nombre, const string &apellido, double saldo) : CuentaBancaria(numCuenta, nombre, apellido, saldo) {}
    
    void nuevoSaldo() {
        setSaldo(getSaldo() * 0.96);
    }
    void mostrar() const override {
        cout << "Cuenta de Credito" << endl;
            CuentaBancaria::mostrar();
        }
};

class CuentaInversion : public CuentaBancaria{
public:
    CuentaInversion(int numCuenta, const string &nombre, const string &apellido, double saldo) : CuentaBancaria(numCuenta, nombre, apellido, saldo) {}
    
    void nuevoSaldo() {
        setSaldo(getSaldo() * 1.12);
    }
    void mostrar() const override {
            cout << "Cuenta de Inversion" << endl;
            CuentaBancaria::mostrar();
        }
};

class CuentaHipotecario : public CuentaBancaria{
private:
    double abono;
public:
    void setAbono(const double &abono) {
        this->abono = abono;
    }
    int getAbono() const {
        return abono;
    }
    CuentaHipotecario(int numCuenta, const string &nombre, const string &apellido, double saldo) : CuentaBancaria(numCuenta, nombre, apellido, saldo) {}
    
    void abonoMensual(){
        cout << "Introduce el monto a depositar mensualmente: ";
        cin >> abono;
        cin.ignore();
    }
    void mostrar() const override {
        cout << "Cuenta de Hipotecario" << endl;
        CuentaBancaria::mostrar();
        cout << "Monto de abono mensual: " << abono << endl;
    }
    void nuevoSaldo() {
        setSaldo(getSaldo() - abono*240);
    }
};
