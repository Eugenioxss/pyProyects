//
// Created by admin on 04/11/2024.
//

#include <iostream>
#include "Triangle.h"
#include "Rectangle.h"

using namespace std;

int main() {
    double baset1, heightt1;
    Triangle t1;
    cout << "Enter base for t1: " << endl;
    cin >> baset1;
    cout << "Enter height for t1: " << endl;
    cin >> heightt1;
    t1.setBase(baset1);
    t1.setHeight(heightt1);
    cout << "Base: " << t1.getBase() << endl;
    cout << "Height: " << t1.getHeight() << endl;
    cout << "Area: " << t1.getArea() << endl;

    double baser1, heightr1;
    Rectangle r1;
    cout << "Enter base for r1: " << endl;
    cin >> baser1;
    cout << "Enter height for r1: " << endl;
    cin >> heightr1;
    r1.setBase(baser1);
    r1.setHeight(heightr1);
    cout << "Base: " << r1.getBase() << endl;
    cout << "Height: " << r1.getHeight() << endl;
    cout << "Area: " << r1.getArea() << endl;
    return 0;

}