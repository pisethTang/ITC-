#include "Farm.h"
#include <iostream>

Farm::Farm(std::string name, int max_land) : name(name), max_land(max_land), money(1000), current_land(0) {
    // no need to allocate lands array, vector will manage it
}

Farm::Farm(): Farm("", 1){}

// getters
std::string Farm::getName(){
    return name;
}

int Farm::getDayNum(){
    return day_num;
}

int Farm::getTimeOfDay(){
    return time_of_day;
}

int Farm::getMaxLand(){
    return max_land;
}

int Farm::getCurrentLand(){
    return current_land;
}

int Farm::getMoney(){
    return money;
}

bool Farm::getHasGoodSoil(){
    return has_good_soil;
}

bool Farm::getHasGoodFood(){
    return has_good_food;
}

// setters
void Farm::setDayNum(int newDay){
    this -> day_num = newDay;
}

void Farm::setTimeOfDay(int newTime){
    this -> time_of_day = newTime;
}

void Farm::setMoney(int newMoney){
    this -> money = newMoney;
}

void Farm::setCurrentLand(int newLand){
    this -> current_land = newLand;
}

void Farm::setGoodSoil(bool newSoil){
    this -> has_good_soil = newSoil;
}

void Farm::setGoodFood(bool newFood){
    this -> has_good_food = newFood;
}


// methods
void Farm::buyNewLand() {
    if (getMoney() > 250) {
        lands.push_back(Land(true, true));   
        setMoney(getMoney() - 250);
        current_land++;
    } else {
        std::cout << "MONEY = " << getMoney() <<  " <= 250 NOT ENOUGH!------------------------------------\n";
        exit(0);
    }
}




Farm::~Farm(){}


