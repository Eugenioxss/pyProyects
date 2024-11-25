//
// Created by admin on 04/11/2024.
//

#ifndef TRIANGLE_H
#define TRIANGLE_H

class Triangle {
private:
    double base, height;
public:
    void setBase(double _base);
    void setHeight(double _height);
    double getBase();
    double getHeight();
    double getArea();
};

#endif //TRIANGLE_H
