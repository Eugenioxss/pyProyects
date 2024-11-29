cmake_minimum_required(VERSION 3.29)
project(situacionProblema)

set(CMAKE_CXX_STANDARD 20)

add_executable(situacionProblema main.cpp
        CuentaBancaria.h
        CuentaBancaria.cpp)
