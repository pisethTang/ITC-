#ifndef PRODUCE_H
#define PRODUCE_H

#include <string>
using namespace std;

class Produce{
    protected:
    string name;        //<do we even need a name?>
    int cost_per_day;   //the cost of upkeep per day
    int selling_price;  //the price that a Produce sells for
    int buying_price;   //the price to buy and plant a Produce

    public:
    //constructors
    Produce();
    //<do we need any constructors in between here?>
    Produce(string newName, int newCost, int newSellPrice, int newBuyPrice);

    //functions
    virtual string getName();
    virtual int getCostPerDay();
    virtual int getSellingPrice();
    virtual int getBuyingPrice();
    void setSellingPrice(int newSellPrice);

    //destructor    
    virtual ~Produce();

};


#endif