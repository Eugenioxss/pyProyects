#include <iostream>

using namespace std;

class Persona{
private:
    string nombre;
    int edad;
public:
    Persona(){
        nombre="Default";
        edad=20;
    }
    void setNombre(string _nombre){
        nombre = _nombre;
    }
    void setEdad(int _edad){
        edad = _edad;
    }
    string getNombre(){
        return nombre;
    }
    int getEdad(){
        return edad;
    }
    virtual void mostrar() const{
        cout << "\nNombre: " << nombre << " \nEdad:" << edad;
    }
    virtual ~Persona()=default;
};


class Alumno : public Persona{
private:
    string matricula;
public:
    void leer(){
        cout << "\nAlumno Leyendo...";
    }

    virtual void mostrar() const{
        cout << "\n Mostrar del Alumno";
    }
};

class Profesor : public Persona{
private:
    string materia;
public:
    void ensenar(){
        cout << "\nProfesor en clase...";
    }

    virtual void mostrar() const{
        cout << "\n Mostrar del Profesor\n";
    }
};

int main()
{
    cout << "Herencia" << endl;

    Persona per1;
    per1.setNombre("Jorge");
    per1.setEdad(40);
    per1.mostrar();

    Alumno alu1;
    alu1.setNombre("Ramon");
    alu1.setEdad(20);
    alu1.leer();
    alu1.mostrar();

    Profesor pro1;
    pro1.setNombre("David");
    pro1.setEdad(50);
    pro1.ensenar();
    pro1.mostrar();

    return 0;
}
