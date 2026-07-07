#include <iostream>
#include <ostream>
#include "textBased.h"
#include "graphicBased.h"

#include "testCrops.h"



int main(){
    // textBased game("Farming Simulator");

    // game.startGame();
    // OOPGame game("Farming Simulator");
    // game.run_graphics();

    // --------------------------------------------------


    // ---------------------Test Crops class-----------------------------
    CropsUnitTest c;
    c.runTests();

    // --------------------------------------------------


    // --------------------------------------------------


    return 0;
}