//
// Created by admin on 25/11/2024.
//
#include <iostream>

using namespace std;

class Complex{
  private:
    double real = 0.0;
    double imag = 0.0;
  public:
      //Constructos por defecto y con parametros
      Complex() = default;
      Complex(double r, double i) : real(r), imag(i) {
        real = r;
        imag = i;
       }
       //Sobrecarga de operadores +
        Complex operator + (const Complex& other)const{
          return Complex(real + other.real, imag + other.imag);
        }
        //Mostrar numero complejo
        void display () const{
          if (imag < 0)
          cout << real << " + i" << imag << endl;
        }

 };
 int main(){
   Complex c1, c2, result;
   cout << "Enter real and imaginary parts of first complex number: ";
   cin >> c1;
   cout << "Enter real and imaginary parts of second complex number: ";
   cin >> c2;
   result = c1 + c2;
   cout << "Sum = " << result;
   return 0;
 }