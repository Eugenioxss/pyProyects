#include <iostream>
#include "RelojD.h"
// Eugenio Moreno Vargas
// A01723720
// 04/11/2024

using namespace std;

int main() {
    RelojD r1;
    int option, hour, minute;

    cout << "1.SetHour\n"
            "2.SetMinute\n"
            "3.GetHour\n"
            "4.GetMinute\n"
            "5.ShowTime\n"
            "6.Exit\n";

    cin >> option;

    while(option != 6){
        switch(option){
            case 1:
                cout << "Enter hour: " << endl;
                cin >> hour;
                r1.setHour(hour);
                break;
            case 2:
                cout << "Enter minute: " << endl;
                cin >> minute;
                r1.setMinute(minute);
                break;
            case 3:
                cout << "Hour: " << r1.getHour() << endl;
                break;
            case 4:
                cout << "Minute: " << r1.getMinute() << endl;
                break;
            case 5:
                r1.showTime();
                break;
            default:
                cout << "Invalid option" << endl;
        }
        cout << "1.SetHour\n"
                "2.SetMinute\n"
                "3.GetHour\n"
                "4.GetMinute\n"
                "5.ShowTime\n"
                "7.Exit\n";
        cin >> option;
    }
    cout << "Goodbye!" << endl;
    return 0;
}