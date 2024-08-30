#include "Crops.h"


//constructors
Crops::Crops(): Crops("", 0,0,0){}

Crops::Crops(std::string newName, int newCost, int newSellPrice, int newBuyPrice){
    name = newName;
    cost_per_day = newCost;
    selling_price = newSellPrice;
    buying_price = newBuyPrice;
    growth_stage = 0;
}

//functions
int Crops::getGrowthStage(){
    return growth_stage;
}

void Crops::setGrowthStage(int newGrowthStage){
    if ((getGrowthStage() + newGrowthStage) <= 10){      //growth_stage cannot be greater than 10 (chosen arbitrarily)
        growth_stage = getGrowthStage() + newGrowthStage;
    }
}

