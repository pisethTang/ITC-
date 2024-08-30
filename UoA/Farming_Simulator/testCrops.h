#ifndef TESTCROPS_H
#define TESTCROPS_H

#include <iostream>
#include "Crops.h"

class CropsUnitTest {
private:
    void testConstructors(){
        testDefaultConstructor();
        testParameterizedConstructor();
    }
    void testDefaultConstructor() {
        Crops crops;

        if (crops.getGrowthStage() != 0) {
            std::cout << "Default Constructor Test Failed: Growth stage is not initialized correctly!" << std::endl;
        }
        // Add more assertions if needed
    }

    void testParameterizedConstructor() {
        Crops crops("TestCrop", 5, 10, 7);

        if (crops.getName() != "TestCrop" || crops.getCostPerDay() != 5 ||
            crops.getSellingPrice() != 10 || crops.getBuyingPrice() != 7 ||
            crops.getGrowthStage() != 0) {
            std::cout << "Parameterized Constructor Test Failed: One or more attributes are not initialized correctly!" << std::endl;
        }
        // Add more assertions if needed
    }

    void testGetGrowthStage() {
        Crops crops;

        if (crops.getGrowthStage() != 0) {
            std::cout << "getGrowthStage Test Failed: Initial growth stage is not 0!" << std::endl;
        }
        // Add more assertions if needed
    }

    void testSetGrowthStage() {
        Crops crops;

        crops.setGrowthStage(5);

        if (crops.getGrowthStage() != 5) {
            std::cout << "setGrowthStage Test Failed: Growth stage is not set correctly!" << std::endl;
        }
        // Add more assertions if needed
    }
    public:
    void runTests() {
        testConstructors();
        testGetGrowthStage();
        testSetGrowthStage();
    }

};

#endif