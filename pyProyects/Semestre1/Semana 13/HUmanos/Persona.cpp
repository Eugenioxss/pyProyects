//
// Created by admin on 14/11/2024.
//
#include <iostream>
#include "Persona.h"
#include <string>

Persona::Persona(std::string _nombre, int _edad) {
    nombre = _nombre;
    edad = _edad;
}

void Persona::mostrar() {
    std::cout << "Nombre: " << nombre << " con edad: " << edad << std::endl;
}

void Persona::setNombre(std::string _nombre) {
    nombre = _nombre;
}

std::string Persona::getNombre() {
    return nombre;
}

void Persona::setEdad(int _edad) {
    edad = _edad;
}

int Persona::getEdad() {
    return edad;
}

void Persona::showName() {
    std::cout << "Nombre: " << nombre << std::endl;
}

void Persona::showAge() {
    std::cout << "Edad: " << edad << std::endl;
}

void Persona::showNameAndAge() {
    std::cout << "Nombre: " << nombre << " con edad: " << edad << std::endl;
}



Alumno::Alumno(std::string _nombre, int _edad, float _calificacion) : Persona(_nombre, _edad) {
    calificacion = _calificacion;
}

void Alumno::mostrar(){
    Persona::mostrar();
    std::cout << "Calificacion: " << calificacion << std::endl;
}




Profesor::Profesor(std::string _nombre, int _edad, std::string _materia) : Persona(_nombre, _edad) {
    materia = _materia;
}

void Profesor::leer() {
    std::cout << "Leyendo" << std::endl;
}

void Profesor::mostrar(){
    Persona::mostrar();
    std::cout << "Materia: " << materia << std::endl;
}