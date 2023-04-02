// Project-0_Cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <SFML/Graphics.hpp>
#include <iostream>
#include <cstdlib>
#include <ctime>

int main()
{
    // Set up random number generator
    std::srand(std::time(nullptr));

    // Set up SFML window
    sf::RenderWindow window(sf::VideoMode(600, 300), "Randomly Chosen Japanese Kana Font Symbol Display");
    window.setFramerateLimit(60);

    // Set up font and text
    sf::Font font;
    if (!font.loadFromFile("meiryo.ttc")) 
    {
        std::cout << "\nError: The font file couldn't be loaded.\n" << std::endl;

        std::cout << "\nWarning: Add the japanese font files to the same folder for avoiding the program exiting suddenly.\n" << std::endl;
        std::cout << "\nWarning: Change the system & software settings to include japanese if necessary for avoiding a blank display.\n" << std::endl;

        system("pause");

        return 1;
    }
    sf::Text mainText("", font, 80);

    int randomChar = std::rand() % 86; // Generate random number between 0 and 85
    mainText.setString(std::wstring(1, 0x3041 + randomChar)); // Set text to Japanese kana font symbol
    std::cout << "\nset japanese kana font symbol\n" << std::endl;

    mainText.setFillColor(sf::Color::Black);
    mainText.setPosition(5, 0);

    sf::Text reminderText("(expect next random japanese kana \n font symbol in one minute)", font, 25);
    reminderText.setFillColor(sf::Color::Black);
    reminderText.setPosition(5, 100);

    // Set up clock
    sf::Clock clock;

    // Main loop
    while (window.isOpen())
    {
        // Handle events
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }
        }

        // Change font symbol once per minute
        if (clock.getElapsedTime().asSeconds() >= 60)
        {
            int randomChar = std::rand() % 86; // Generate random number between 0 and 85
            mainText.setString(std::wstring(1, 0x3041 + randomChar)); // Set text to Japanese kana font symbol
            std::cout << "\nchanged japanese kana font symbol\n" << std::endl;
            clock.restart();
        }

        // Draw text
        window.clear(sf::Color::White);
        window.draw(mainText);
        window.draw(reminderText);
        window.display();
    }

    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
