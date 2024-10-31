#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    float ladoa, ladob, hypotenuse;

    cout << "Lado A: ";
    cin >> ladoa;
    cout << "Lado B: ";
    cin >> ladob;
    hypotenuse = sqrt(pow(ladoa, 2) + pow(ladob, 2));
    cout << "Hipotenusa: " << hypotenuse << endl;

    return 0;
}