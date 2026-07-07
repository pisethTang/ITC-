#ifndef LAND_H
#define LAND_H




class Land{
    protected:
    bool empty_or_used;
    bool unlocked;

    public:
    //constructors
    Land(bool empty_or_used, bool unlocked);
    Land();     //initialises without produce, and empty

    //functions
    bool getEmptyOrUsed();
    void setEmptyOrUsed(bool a);
    bool getUnlocked();
    void setUnlocked(bool b);
    //<put the above in the diagram>

    //void plantProduce(int produceIteration, Farm farm);    //Also takes away money and only does the following:
                                                //this function finds the first available element in
                                                //the Land vector and assigns that pointer to a produce
                                                //of iteration produceIteration

    void harvestProduce(); //this function removes the produce and adds money

    //destructor
    ~Land();

};

#endif