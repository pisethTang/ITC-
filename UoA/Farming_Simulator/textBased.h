#ifndef TEXTBASED_H
#define TEXTBASED_H

#include <SFML/Window/Keyboard.hpp>
#include <iostream>
#include "Farm.h"




class textBased {
private:
    Farm* farm;
    Land* land;
    std::string title;

public:
    // Constructor with a title parameter
    textBased(const std::string& title) : title(title) {
        // declaring all the game entiies
        farm = new Farm("Team 40's Farm", 10);
        land = new Land(true, true);
        

    }
    // Function to display the menu
    void displayMenu() {
        std::cout << "-----------------------------\n";
        std::cout << "      " << title << "      \n";
        std::cout << "-----------------------------\n";
        std::cout << "What would you like to do?\n";
        std::cout << "1. Shop Produce\n";
        std::cout << "2. Buy Upgrades or Lands(Current number of land: " << farm -> getCurrentLand()<<  ")\n";
        std::cout << "3. Sell/Harvest Animals/Crops\n";
    }

    // Function to get user choice
    int getUserChoice() {
        int choice;
        std::cout << "Enter your choice (1-3): ";
        std::cin >> choice;
        return choice;
    }

    void produce_menu(){
        int choice = 0;
        std::cout << "------------------------------------\n"
                  << "Which produce would you like to buy?\n"
                  << "------------------------------------\n"
                  << "1. Crops\n"
                  << "2. Animals\n";
        std::cin >> choice;
        switch(choice){
            case 1:
                // go into another Crops menu
                std::cout << "Here are the crops.\n";
                std::cout << "1. Wheat\n"
                          << "2.Carrots\n"
                          << "3. Potatoes\n";
                break; 
            case 2:
                std::cout << "Here are the animals\n";
                // go into another Animals menu
         
                break;
        }
        std::cin.get();

       
        

    }

    // Function to execute the chosen action
    void executeAction(int choice){
        switch (choice) {
            case 1:
                std::cout << "You chose to Shop Produce.\n";
                // Add code for shopping produce
                // The method below will try to access the produce's sub classes and 
                // a menu that prints 
                produce_menu();
                // After clicking on the animal icon: sheep ($50), cow($35), 
                // After clicking on the crop icon: carrot ($12), potatoes($10), and whear
                
                
                break;

            case 2:
                std::cout << "You chose to Buy Upgrades or Lands.\n";
                // Add code for buying upgrades or lands
                farm -> buyNewLand();
                break;

            case 3:
                std::cout << "You chose to Sell/Harvest Animals/Crops.\n";
                // Add code for selling/harvesting animals/crops
                break;

            default:
                std::cout << "Invalid choice. Please enter a number between 1 and 3.\n";
                exit(0);
        }
    }

    // Function to start the game loop
    void startGame() {
        while (1) {
            displayMenu();         // Display the menu
            int choice = getUserChoice();  // Get user choice
            executeAction(choice); // Execute the chosen action
        }
    }

    ~textBased(){
        delete farm;
        delete land;
    }

};



#endif