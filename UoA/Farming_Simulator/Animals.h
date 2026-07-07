#ifndef ANIMALS_H
#define ANIMALS_H

#include "Produce.h"

class Animals : public Produce{
    protected:
    int value_per_day;  //the value that the player recieves each day for having an Animal in a Land

    public:
    //constructors
    Animals();
    Animals(std::string newName, int newCost, int newSellPrice, int newBuyPrice, int newValue);

    //functions
    // std::string getName() override; //<do NOT remove this>
    virtual int getValuePerDay(bool goodSoil, int dayNum);
    void setValuePerDay(int newValue);  //<function used when food upgrade is given?>

    //destructor

};

#endif