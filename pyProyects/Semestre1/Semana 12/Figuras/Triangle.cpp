//
// Created by admin on 04/11/2024.
//

#include "Triangle.h"

void Triangle::setBase(double _base){
    base = _base;
}

void Triangle::setHeight(double _height){
    height = _height;
}

double Triangle::getBase(){
    return base;
}

double Triangle::getHeight(){
    return height;
}

double Triangle::getArea(){
    return base * height / 2;
}