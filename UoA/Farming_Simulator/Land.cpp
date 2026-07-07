#include "Land.h"


Land::Land(bool empty_or_used, bool unlocked){
    this -> empty_or_used = empty_or_used;
    this -> unlocked = unlocked;
}

//constructors
Land::Land(): Land(false, false){
    //<put a produce here?? but need to initialise with nothing so that the produce can change>

}



//getters and setters
bool Land::getEmptyOrUsed(){
    return empty_or_used;
}

void Land::setEmptyOrUsed(bool a){
    empty_or_used = a;
}

bool Land::getUnlocked(){
    return unlocked;
}


void Land::setUnlocked(bool b){
    unlocked = b;
}

Land::~Land(){
    
}

