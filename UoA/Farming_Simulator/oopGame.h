#ifndef OOPGAME_H
#define OOPGAME_H
#include <iostream>

#include <SFML/Graphics.hpp>
#include <SFML/Window/Keyboard.hpp>
using namespace sf;


class OOPGame{
    private:
        sf::RenderWindow* win;

    public:
        OOPGame(int size, std::string title){
        }

        OOPGame(std::string title){}
        


        void run_graphics(){
            while(win -> isOpen()){
                Event e;
                while(win -> pollEvent(e)){
                    if(e.type == Event::Closed) win -> close();
                }

            win -> clear();      
            win -> display();
            }
        }

        
        ~OOPGame(){}
};










#endif