//
// Created by ArbolHojaSaltoLuz on 24/11/2024.
//

#include "Vehicles.h"
#include <iostream>
#include <string>
using namespace std;

Vehicles::Vehicles() {
    Type = "TBD";
    maxSpeed = 0;
    Size = 0;
    LaunchDate = 0;
}

void Vehicles::setName(string _Name) {
    name = _Name;
}

string Vehicles::getName() {
    return name;
}

void Vehicles::setType(string _Type) {
    Type = _Type;
}

string Vehicles::getType() {
    return Type;
}

void Vehicles::setMaxSpeed(int _MaxSpeed) {
    maxSpeed = _MaxSpeed;
}

int Vehicles::getMaxSpeed() {
    return maxSpeed;
}

void Vehicles::setSize(int _Size) {
    Size = _Size;
}

int Vehicles::getSize() {
    return Size;
}

void Vehicles::setLaunchDate(int _LaunchDate) {
    LaunchDate = _LaunchDate;
}

int Vehicles::getLaunchDate() {
    return LaunchDate;
}

Vehicles::~Vehicles() {
    cout << "Vehicle destroyed" << endl;
}

void Vehicles::move(double speed, char direction) {
    cout << "Vehicle is moving at " << speed << " in direction " << direction << endl;
}

void Vehicles::stop() {
    cout << "Vehicle has stopped" << endl;
}

void Car::setWheels(int _Wheels) {
    wheels = _Wheels;
}

int Car::getWheels() {
    return wheels;
}

void Car::setFuelType(string _FuelType) {
    fuelType = _FuelType;
}

string Car::getFuelType() {
    return fuelType;
}

void Car::setMilesPerGallon(float _MilesPerGallon) {
    milesPerGallon = _MilesPerGallon;
}

float Car::getMilesPerGallon() {
    return milesPerGallon;
}

void Car::honk() {
    cout << "Honk Honk" << endl;
}

void Boat::setHullLength(double _HullLength) {
    hullLength = _HullLength;
}

double Boat::getHullLength() {
    return hullLength;
}

void Boat::setBoatType(string _BoatType) {
    boatType = _BoatType;
}

string Boat::getBoatType() {
    return boatType;
}

void Boat::setIsMotorized(bool _IsMotorized) {
    isMotorized = _IsMotorized;
}

bool Boat::getIsMotorized() {
    return isMotorized;
}

void Boat::dock() {
    cout << "Boat is docked" << endl;
}

void Plane::setWingspan(int _Wingspan) {
    wingspan = _Wingspan;
}

int Plane::getWingspan() {
    return wingspan;
}

void Plane::setIsBoeing(bool _IsBoeing) {
    isBoeing = _IsBoeing;
}

bool Plane::getIsBoeing() {
    return isBoeing;
}

void Plane::setMaxAltitude(double _MaxAltitude) {
    maxAltitude = _MaxAltitude;
}

double Plane::getMaxAltitude() {
    return maxAltitude;
}

void Plane::takeOff() {
    cout << "Plane is taking off" << endl;
}

void Plane::land() {
    cout << "Plane is landing" << endl;
}

void Rocket::setStages(int _Stages) {
    stages = _Stages;
}

int Rocket::getStages() {
    return stages;
}

void Rocket::setPayloadCapacity(double _PayloadCapacity) {
    payloadCapacity = _PayloadCapacity;
}

double Rocket::getPayloadCapacity() {
    return payloadCapacity;
}

void Rocket::setFuelAmount(double _FuelAmount) {
    fuelAmount = _FuelAmount;
}

double Rocket::getFuelAmount() {
    return fuelAmount;
}

void Rocket::launch() {
    cout << "Rocket is launching" << endl;
}

void Rocket::detachStage() {
    cout << "Rocket is detaching stage" << endl;
}

void Bycicle::setGears(int _Gears) {
    gears = _Gears;
}

int Bycicle::getGears() {
    return gears;
}

void Bycicle::setHasBell(bool _HasBell) {
    hasBell = _HasBell;
}

bool Bycicle::getHasBell() {
    return hasBell;
}

void Bycicle::setHasLight(bool _HasLight) {
    hasLight = _HasLight;
}

bool Bycicle::getHasLight() {
    return hasLight;
}

void Bycicle::ringBell() {
    cout << "Ring Ring" << endl;
}

void Bycicle::turnLightOn() {
    cout << "Light is on" << endl;
}

void Bycicle::turnLightOff() {
    cout << "Light is off" << endl;
}

void Bycicle::changeGear(int gear) {
    cout << "Gear changed to " << gear << endl;
}

