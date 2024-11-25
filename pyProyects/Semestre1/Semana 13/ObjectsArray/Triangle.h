//
// Created by admin on 11/11/2024.
//

#ifndef TRIANGLE_H
#define TRIANGLE_H

class Triangle {
private:
    double base;
    double height;
public:
    Triangle();
    Triangle(double _base, double _height);
    double getBase() const;
    void setBase(double _base);
    double getHeight() const;
    void setHeight(double _height);

#endif //TRIANGLE_H
