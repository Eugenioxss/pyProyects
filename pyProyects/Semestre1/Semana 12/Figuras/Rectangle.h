//
// Created by admin on 04/11/2024.
//

#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
private:
    double base, height;
public:
    void setBase(double _base);
    void setHeight(double _height);
    double getBase();
    double getHeight();
    double getArea();
};

#endif //RECTANGLE_H
