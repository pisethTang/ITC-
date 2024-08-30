#include <SFML/Graphics.hpp>
#include <SFML/Window/Keyboard.hpp>
#include <SFML/Audio.hpp>
#include <iostream>

using namespace sf;

enum GameState {
    MENU,
    CHOICE_1,
    CHOICE_2,
    CHOICE_3
};

class OOPGame {
private:
    RenderWindow* win;
    Font font;
    SoundBuffer clickBuffer;
    Sound clickSound;
    GameState currentState;

public:
    OOPGame(int size, std::string title) {
        win = new RenderWindow(VideoMode(size, size), title);
        font.loadFromFile("Pacifico.ttf"); // Change this to the path of your font file
        clickBuffer.loadFromFile("/home/sething2002/.vscode-server/extensions/ms-vsliveshare.vsliveshare-1.0.5883/audio/Scroll_Wheel_singleClick_2.wav"); // Change this to the path of your sound file
        clickSound.setBuffer(clickBuffer);
        currentState = MENU;
    }

    OOPGame(std::string title) {
        win = new RenderWindow(VideoMode(800, 600), title);
        font.loadFromFile("Pacifico.ttf"); // Change this to the path of your font file
        clickBuffer.loadFromFile("/home/sething2002/.vscode-server/extensions/ms-vsliveshare.vsliveshare-1.0.5883/audio/Scroll_Wheel_singleClick_2.wav"); // Change this to the path of your sound file
        clickSound.setBuffer(clickBuffer);
        currentState = MENU;
    }

    void drawText(const std::string& message, const Vector2f& position, unsigned int size, const Color& color = Color::White) {
        Text text(message, font, size);
        text.setPosition(position);
        text.setFillColor(color);
        win->draw(text);
    }

    void drawButton(const std::string& message, const Vector2f& position, unsigned int size, const Color& fillColor, const Color& outlineColor) {
        RectangleShape button(Vector2f(400, 70));
        button.setPosition(position);
        button.setFillColor(fillColor);
        button.setOutlineThickness(2);
        button.setOutlineColor(outlineColor);
        win->draw(button);

        Text text(message, font, size);
        text.setPosition(position.x + 10, position.y + 5);
        text.setFillColor(outlineColor);
        win->draw(text);
    }

    void run_graphics() {
        while (win->isOpen()) {
            Event e;
            while (win->pollEvent(e)) {
                if (e.type == Event::Closed)
                    win->close();
                else if (e.type == Event::KeyPressed) {
                    if (e.key.code == Keyboard::Num1) {
                        currentState = CHOICE_1;
                        clickSound.play();
                    } else if (e.key.code == Keyboard::Num2) {
                        currentState = CHOICE_2;
                        clickSound.play();
                    } else if (e.key.code == Keyboard::Num3) {
                        currentState = CHOICE_3;
                        clickSound.play();
                    } else if (e.key.code == Keyboard::B && currentState != MENU) {
                        currentState = MENU;
                        clickSound.play();
                    } else if (e.key.code == Keyboard::X) {
                        win->close(); // Exit the game when 'X' is pressed
                    }
                }
                else if (e.type == Event::MouseButtonPressed) {
                    if (currentState != MENU) {
                        // Check if the mouse click is within the bounds of the buttons
                        Vector2i mousePos = Mouse::getPosition(*win);

                        if (currentState == CHOICE_1 && mousePos.x >= 100 && mousePos.x <= 400 && mousePos.y >= 100 && mousePos.y <= 150) {
                            currentState = MENU;
                            clickSound.play();
                        } else if (currentState == CHOICE_2 && mousePos.x >= 100 && mousePos.x <= 400 && mousePos.y >= 200 && mousePos.y <= 250) {
                            currentState = MENU;
                            clickSound.play();
                        } else if (currentState == CHOICE_3 && mousePos.x >= 100 && mousePos.x <= 400 && mousePos.y >= 300 && mousePos.y <= 350) {
                            currentState = MENU;
                            clickSound.play();
                        }
                    }
                }
            }

            win->clear();

            // Draw based on the current state
            switch (currentState) {
                case MENU:
                    // Draw the game title
                    drawButton("Team 40's Farming Simulator", Vector2f(100, 50), 50, Color(255, 255, 255, 200), Color::Black);

                    // Draw the menu options
                    drawButton("1. Buy Produce", Vector2f(100, 150), 30, Color(255, 255, 255, 200), Color::Black);
                    drawButton("2. Buy Upgrades/Lands", Vector2f(100, 250), 30, Color(255, 255, 255, 200), Color::Black);
                    drawButton("3. Sell/harvest crops/animals", Vector2f(100, 350), 30, Color(255, 255, 255, 200), Color::Black);

                    // Draw the exit button
                    drawButton("Press 'X' to exit", Vector2f(20, 500), 20, Color(255, 255, 255, 100), Color::Black);
                    break;

                case CHOICE_1:
                    drawText("You've chosen 1", Vector2f(200, 200), 40, Color::Green);
                    drawButton("Press 'B' to go back", Vector2f(500, 20), 20, Color(255, 255, 255, 100), Color::Black);
                    break;

                case CHOICE_2:
                    drawText("You've chosen 2", Vector2f(200, 200), 40, Color::Blue);
                    drawButton("Press 'B' to go back", Vector2f(500, 20), 20, Color(255, 255, 255, 100), Color::Black);
                    break;

                case CHOICE_3:
                    drawText("You've chosen 3", Vector2f(200, 200), 40, Color::Red);
                    drawButton("Press 'B' to go back", Vector2f(500, 20), 20, Color(255, 255, 255, 100), Color::Black);
                    break;
            }

            win->display();
        }
    }
};
