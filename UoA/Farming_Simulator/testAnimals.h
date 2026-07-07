#include <iostream>
#include "Animals.h"  // Assuming Animals.h is the header file for the Animals class

class AnimalsTest {
public:
    void runTests() {
        testDefaultConstructor();
        testParameterizedConstructor();
        testSetValuePerDay();
        // Add other test methods here
    }

private:
    void testDefaultConstructor() {
        Animals animal;

        if (animal.getName() != "" || animal.getCostPerDay() != 0 ||
            animal.getSellingPrice() != 0 || animal.getBuyingPrice() != 0 ||
            animal.getValuePerDay() != 0) {
            std::cout << "Default Constructor Test Failed: One or more attributes are not initialized correctly!" << std::endl;
        }
        // Add more assertions if needed
    }

    void testParameterizedConstructor() {
        Animals animal("TestAnimal", 5, 10, 7, 3);

        if (animal.getName() != "TestAnimal" || animal.getCostPerDay() != 5 ||
            animal.getSellingPrice() != 10 || animal.getBuyingPrice() != 7 ||
            animal.getValuePerDay() != 3) {
            std::cout << "Parameterized Constructor Test Failed: One or more attributes are not initialized correctly!" << std::endl;
        }
        // Add more assertions if needed
    }

    void testSetValuePerDay() {
        Animals animal("TestAnimal", 5, 10, 7, 3);

        animal.setValuePerDay(2);

        if (animal.getValuePerDay() != 5) {
            std::cout << "setValuePerDay Test Failed: Value per day is not set correctly!" << std::endl;
        }
        // Add more assertions if needed
    }

    // Add other test functions here
};
