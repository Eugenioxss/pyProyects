//
// Created by admin on 04/11/2024.
//

#include "Rectangle.h"

void Rectangle::setBase(double _base){
    base = _base;
}

void Rectangle::setHeight(double _height){
    height = _height;
}

double Rectangle::getBase(){
    return base;
}

double Rectangle::getHeight(){
    return height;
}

double Rectangle::getArea(){
    return base * height;
}