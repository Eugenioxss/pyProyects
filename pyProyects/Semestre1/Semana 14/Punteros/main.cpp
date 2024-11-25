#include <iostream>
using namespace std;
int main() {
    int numero = 7;
    int *pNum = &numero;

    numero = 9;

    cout << *pNum << endl;

    std::cout << "Hello, World!" << std::endl;
    return 0;
}
