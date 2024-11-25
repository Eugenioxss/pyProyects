//
// Created by admin on 04/11/2024.
//
#include "RelojD.h"
#include <iostream>

RelojD::RelojD(){
    hour = 0;
    minute = 0;
}

RelojD::RelojD(int _hour, int _minute){
    hour = _hour;
    minute = _minute;
}

RelojD::~RelojD(){
    hour = 0;
    minute = 0;
}

void RelojD::setHour(int _hour){
    hour = _hour;
}

void RelojD::setMinute(int _minute){
    minute = _minute;
}

int RelojD::getHour(){
    return hour;
}

int RelojD::getMinute(){
    return minute;
}

void RelojD::showTime(){
    if (hour >= 24 || hour < 0){
        hour = hour % 24;
        if (hour < 0){
            hour += 24;
        }
    }
    if (minute >= 60 || minute < 0) {
        hour += minute / 60;
        minute = minute % 60;
    }
    std::cout << hour << ":" << minute << std::endl;
}

void RelojD::addMinute(int _minute){ // No se usa
    minute += _minute;
}
