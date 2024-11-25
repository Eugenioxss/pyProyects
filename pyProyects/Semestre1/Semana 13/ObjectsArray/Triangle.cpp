//
// Created by admin on 11/11/2024.
//

#include "Triangle.h"
Triangle::Triangle() {
    base = 0;
    height = 0;
}

Triangle::Triangle(double _base, double _height) {
    base = _base;
    height = _height;
}

double Triangle::getBase() const{
    return base;
}

void Triangle::setBase(double _base){
    base = _base;
}

double Triangle::getHeight() const{
    return height;
}

void Triangle::setHeight(double _height){
    height = _height;
}

double Triangle::getArea() const{
    return base * height / 2;
}
