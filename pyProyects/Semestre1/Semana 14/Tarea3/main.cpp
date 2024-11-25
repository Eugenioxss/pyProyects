//
// Created by ArbolHojaSaltoLuz on 24/11/2024.
//
#include "Vehicles.h"
#include <iostream>

using namespace std;

int main() {
    Car myCar;
        myCar.setName("myCar");
        myCar.setType("Car");
        myCar.setMaxSpeed(200);
        myCar.setSize(4);
        myCar.setLaunchDate(2015);
        myCar.setWheels(4);
        myCar.setFuelType("Gasoline");
        myCar.setMilesPerGallon(25.5);

        //print all the atributes and do methods
        cout << "Name: " << myCar.getName() << endl;
        cout << "Type: " << myCar.getType() << endl;
        cout << "Max Speed: " << myCar.getMaxSpeed() << endl;
        cout << "Size: " << myCar.getSize() << endl;
        cout << "Launch Date: " << myCar.getLaunchDate() << endl;
        cout << "Wheels: " << myCar.getWheels() << endl;
        cout << "Fuel Type: " << myCar.getFuelType() << endl;
        cout << "Miles Per Gallon: " << myCar.getMilesPerGallon() << endl;
        myCar.move(100, 'N');
        myCar.stop();
        myCar.honk();
        cout << endl;

    Boat myBoat;
        myBoat.setName("myBoat");
        myBoat.setType("Boat");
        myBoat.setMaxSpeed(50);
        myBoat.setSize(20);
        myBoat.setLaunchDate(2010);
        myBoat.setHullLength(30.5);
        myBoat.setBoatType("Sailboat");
        myBoat.setIsMotorized(false);

        //print all the atributes and do methods
        cout << "Name: " << myBoat.getName() << endl;
        cout << "Type: " << myBoat.getType() << endl;
        cout << "Max Speed: " << myBoat.getMaxSpeed() << endl;
        cout << "Size: " << myBoat.getSize() << endl;
        cout << "Launch Date: " << myBoat.getLaunchDate() << endl;
        cout << "Hull Length: " << myBoat.getHullLength() << endl;
        cout << "Boat Type: " << myBoat.getBoatType() << endl;
        cout << "Is Motorized: " << myBoat.getIsMotorized() << endl;
        myBoat.move(10, 'E');
        myBoat.stop();
        myBoat.dock();
        cout << endl;


    Plane myPlane;
        myPlane.setName("myPlane");
        myPlane.setType("Plane");
        myPlane.setMaxSpeed(500);
        myPlane.setSize(200);
        myPlane.setLaunchDate(2020);
        myPlane.setWingspan(150);
        myPlane.setIsBoeing(true);
        myPlane.setMaxAltitude(30000);

        //print all the atributes and do methods
        cout << "Name: " << myPlane.getName() << endl;
        cout << "Type: " << myPlane.getType() << endl;
        cout << "Max Speed: " << myPlane.getMaxSpeed() << endl;
        cout << "Size: " << myPlane.getSize() << endl;
        cout << "Launch Date: " << myPlane.getLaunchDate() << endl;
        cout << "Wingspan: " << myPlane.getWingspan() << endl;
        cout << "Is Boeing: " << myPlane.getIsBoeing() << endl;
        cout << "Max Altitude: " << myPlane.getMaxAltitude() << endl;
        myPlane.move(500, 'S');
        myPlane.stop();
        myPlane.takeOff();
        cout << endl;


    Rocket myRocket;
        myRocket.setName("myRocket");
        myRocket.setType("Rocket");
        myRocket.setMaxSpeed(1000);
        myRocket.setSize(50);
        myRocket.setLaunchDate(2021);
        myRocket.setStages(3);
        myRocket.setPayloadCapacity(1000);
        myRocket.setFuelAmount(500);

        //print all the atributes and do methods
        cout << "Name: " << myRocket.getName() << endl;
        cout << "Type: " << myRocket.getType() << endl;
        cout << "Max Speed: " << myRocket.getMaxSpeed() << endl;
        cout << "Size: " << myRocket.getSize() << endl;
        cout << "Launch Date: " << myRocket.getLaunchDate() << endl;
        cout << "Stages: " << myRocket.getStages() << endl;
        cout << "Payload Capacity: " << myRocket.getPayloadCapacity() << endl;
        cout << "Fuel Amount: " << myRocket.getFuelAmount() << endl;
        myRocket.move(1000, 'W');
        myRocket.stop();
        myRocket.launch();
        cout << endl;


    Bycicle myBycicle;
        myBycicle.setName("myBycicle");
        myBycicle.setType("Bycicle");
        myBycicle.setMaxSpeed(30);
        myBycicle.setSize(1);
        myBycicle.setLaunchDate(2019);
        myBycicle.setGears(10);
        myBycicle.setHasBell(true);
        myBycicle.setHasLight(true);


        //print all the atributes and do methods
        cout << "Name: " << myBycicle.getName() << endl;
        cout << "Type: " << myBycicle.getType() << endl;
        cout << "Max Speed: " << myBycicle.getMaxSpeed() << endl;
        cout << "Size: " << myBycicle.getSize() << endl;
        cout << "Launch Date: " << myBycicle.getLaunchDate() << endl;
        cout << "Gears: " << myBycicle.getGears() << endl;
        cout << "Has Bell: " << myBycicle.getHasBell() << endl;
        cout << "Has Light: " << myBycicle.getHasLight() << endl;
        myBycicle.move(10, 'N');
        myBycicle.stop();
        myBycicle.ringBell();
        myBycicle.turnLightOn();
        myBycicle.turnLightOn();
        cout << endl;

    cout << "Type anything + enter to end the program" << endl;
    string intup;
    cin >> intup;


    return 0;
}