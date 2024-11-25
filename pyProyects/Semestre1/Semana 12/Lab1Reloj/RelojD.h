//
// Created by admin on 04/11/2024.
//

#ifndef RELOJD_H
#define RELOJD_H

class RelojD {
private:
    int hour, minute;
public:
    //Constructores
    RelojD();
    RelojD(int _hour, int _minute);
    //Destructor
    ~RelojD();

    void setHour(int _hour);
    void setMinute(int _minute);
    int getHour();
    int getMinute();
    void showTime();
    void addMinute(int _minute);
};

#endif //RELOJD_H
