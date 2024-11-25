#include <iostream>
#include "Persona.h"

using namespace std;

int main() {
    Persona * vector[3];

    vector[0] = new Alumno("Jorge",20,9.8);
    vector[0] -> mostrar();

    vector[1] = new Alumno("Ramon",19,9.5);
    vector[1] -> mostrar();

    vector[2] = new Profesor("Jorge",40,"POO");
    vector[2] -> mostrar();

    cout << endl;
    cout << "PERSONA:\n";

    Persona persona1;
    persona1.setNombre("Persona");
    persona1.setEdad(13);
    persona1.mostrar();

    cout << "ALUMNO:\n";
    Alumno alu1;
    alu1.setNombre("Eugenio");
    alu1.setEdad(18);
    alu1.mostrar();

    cout << "PROFESOR:\n";
    Alumno pro1;
    pro1.setNombre("Jorge");
    pro1.setEdad(40);
    pro1.mostrar();


    return 0;
}
