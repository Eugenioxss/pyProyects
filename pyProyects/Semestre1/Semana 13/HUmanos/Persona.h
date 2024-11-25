//
// Created by admin on 14/11/2024.
//

#ifndef PERSONA_H
#define PERSONA_H
#include <string>

class Persona {
    private:
        std::string nombre;
        int edad;
    public:
        Persona() = default;
        Persona (std::string, int );
        void setEdad(int);
        int getEdad();
        void setNombre(std::string);
        std::string getNombre();
        void showName();
        void showAge();
        void showNameAndAge();
        virtual void mostrar();
};

class Alumno : public Persona {
    private:
        float calificacion;
    public:
    Alumno() = default;
        Alumno(std::string , int, float);
        void estudiar();
        void mostrar();
};

class Profesor : public Persona {
private:
    std::string materia;
public:
    Profesor() = default;
    Profesor (std::string, int, std::string);
    void leer();
    void calificar();
    void mostrar();
};

#endif //PERSONA_H
