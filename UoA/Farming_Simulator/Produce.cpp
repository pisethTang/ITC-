#include "Produce.h"
#include <string>

using namespace std;

//constructors
Produce::Produce(){
    name = "";
    cost_per_day = 0;
    selling_price = 0;
    buying_price = 0;
}

Produce::Produce(string newName, int newCost, int newSellPrice, int newBuyPrice){
    name = newName;
    cost_per_day = newCost;
    selling_price = newSellPrice;
    buying_price = newBuyPrice;
}

//functions
string Produce::getName(){
    return name;
}

int Produce::getCostPerDay(){
    return cost_per_day;
}

int Produce::getSellingPrice(){
    return selling_price;
}

int Produce::getBuyingPrice(){
    return buying_price;
}

void Produce::setSellingPrice(int newSellPrice){
    selling_price = selling_price + newSellPrice;
}

Produce::~Produce(){

}