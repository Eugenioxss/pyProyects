//
// Created by ArbolHojaSaltoLuz on 24/11/2024.
//

#include <string>
using namespace std;

#ifndef VEHICLES_H
#define VEHICLES_H



class Vehicles {
private:
    string name;
    string Type;
    int maxSpeed;
    int Size;
    int LaunchDate;

public:
    Vehicles();
    void setName(string _Name);
    string getName();
    void setType(string _Type);
    string getType();
    void setMaxSpeed(int _MaxSpeed);
    int getMaxSpeed();
    void setSize(int _Size);
    int getSize();
    void setLaunchDate(int _LaunchDate);
    int getLaunchDate();
    ~Vehicles();

    void move(double speed, char direction);
    void stop();
};

class Car : public Vehicles {
private:
    int wheels;
    string fuelType;
    float milesPerGallon;
public:
    void setWheels(int _Wheels);
    int getWheels();
    void setFuelType(string _FuelType);
    string getFuelType();
    void setMilesPerGallon(float _MilesPerGallon);
    float getMilesPerGallon();
    void honk();
};

class Boat : public Vehicles {
private:
    double hullLength;
    string boatType;
    bool isMotorized;

public:
    void setHullLength(double _HullLength);
    double getHullLength();
    void setBoatType(string _BoatType);
    string getBoatType();
    void setIsMotorized(bool _IsMotorized);
    bool getIsMotorized();
    void dock();
};

class Plane : public Vehicles {
private:
    int wingspan;
    bool isBoeing;
    double maxAltitude;
public:
    void setWingspan(int _Wingspan);
    int getWingspan();
    void setIsBoeing(bool _IsBoeing);
    bool getIsBoeing();
    void setMaxAltitude(double _MaxAltitude);
    double getMaxAltitude();
    void takeOff();
    void land();
};

class Rocket : public Vehicles {
private:
    int stages;
    double payloadCapacity;
    double fuelAmount;
public:
    void setStages(int _Stages);
    int getStages();
    void setPayloadCapacity(double _PayloadCapacity);
    double getPayloadCapacity();
    void setFuelAmount(double _FuelAmount);
    double getFuelAmount();
    void launch();
    void detachStage();
};

class Bycicle : public Vehicles {
    int gears;
    bool hasBell;
    bool hasLight;
public:
    void setGears(int _Gears);
    int getGears();
    void setHasBell(bool _HasBell);
    bool getHasBell();
    void setHasLight(bool _HasLight);
    bool getHasLight();
    void ringBell();
    void turnLightOn();
    void turnLightOff();
    void changeGear(int gear);
};

#endif //VEHICLES_H
