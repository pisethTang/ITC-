#include "Animals.h"

//constructors
Animals::Animals(): Animals("", 0,0,0,0){
    // name = "";
    // cost_per_day = 0;
    // selling_price = 0;
    // buying_price = 0;
    // value_per_day = 0;
}

Animals::Animals(std::string newName, int newCost, int newSellPrice, int newBuyPrice, int newValue){
    name = newName;
    cost_per_day = newCost;
    selling_price = newSellPrice;
    buying_price = newBuyPrice;
    value_per_day = newValue;
}

//functions
// int Animals::getValuePerDay(){
//     return value_per_day;
// }    //<this is a virtual function?>

// std::string Animals::getName(){
//     return "name";  //<can't remove this>
// }

void Animals::setValuePerDay(int newValue){
    value_per_day = value_per_day + newValue;
}