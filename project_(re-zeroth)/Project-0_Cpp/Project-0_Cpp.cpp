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
    sf::RenderWindow window(sf::VideoMode(500, 250), "Randomly Chosen Japanese Kana & Kanji Font Symbol Display");
    window.setFramerateLimit(60);

    // Load the meiryo font
    sf::Font font_kana;
    if (!font_kana.loadFromFile("meiryo.ttc"))
    {
        std::cout << "\nError: The font file couldn't be loaded.\n" << std::endl;

        std::cout << "\nWarning: Add the japanese font files to the same folder for avoiding the program exiting suddenly.\n" << std::endl;
        std::cout << "\nWarning: Change the system & software settings to include japanese if necessary for avoiding a blank display.\n" << std::endl;

        system("pause");

        return 1;
    }

    // Load the mincho font
    sf::Font font_kanji;
    if (!font_kanji.loadFromFile("msmincho.ttc"))
    {
        std::cout << "\nError: The font file couldn't be loaded.\n" << std::endl;

        std::cout << "\nWarning: Add the japanese font files to the same folder for avoiding the program exiting suddenly.\n" << std::endl;
        std::cout << "\nWarning: Change the system & software settings to include japanese if necessary for avoiding a blank display.\n" << std::endl;

        system("pause");

        return 1;
    }

    // Set up the kanji text object
    sf::Text textKanji;
    textKanji.setFont(font_kanji);
    textKanji.setCharacterSize(80);
    textKanji.setFillColor(sf::Color::Black);
    textKanji.setStyle(sf::Text::Bold);
    textKanji.setPosition(250, 5);

    // Set the initial kanji 
    sf::String chosenKanji = sf::String::fromUtf32(1, std::rand() % 20901 + 11904);
    textKanji.setString(sf::String(chosenKanji));

    sf::Text textKana("", font_kana, 80);

    textKana.setFillColor(sf::Color::Black);
    textKana.setStyle(sf::Text::Bold);
    textKana.setPosition(50, 5);

    int randomChar = std::rand() % 86; // Generate random number between 0 and 85
    textKana.setString(std::wstring(1, 0x3041 + randomChar)); // Set text to Japanese kana font symbol

    std::cout << "\nautomatically set japanese kana & kanji font symbols\n" << std::endl;

    sf::Text reminderText("(expect next random japanese kana \n & kanji font symbols in one minute)", font_kana, 25);
    reminderText.setFillColor(sf::Color::Black);
    reminderText.setStyle(sf::Text::Bold);
    reminderText.setPosition(5, 110);

    // Create the randomization button
    sf::RectangleShape button(sf::Vector2f(150, 50)); // length & breadth
    button.setPosition(150, 190); // left vs right & down vs up
    button.setFillColor(sf::Color::Green);

    // Create the button text
    sf::Text buttonText("RANDOMIZE", font_kana, 20);
    buttonText.setFillColor(sf::Color::Black);
    buttonText.setStyle(sf::Text::Bold);
    buttonText.setPosition(160, 205); // left vs right & down vs up

    // Set up clocks
    sf::Clock clock_a;
    sf::Clock clock_b;

    sf::Color grey(220, 220, 220);

    // Main loop
    while (window.isOpen())
    {
        // Handle events
        sf::Event event;
        while (window.pollEvent(event))
        {
            clock_b.restart();

            if (event.type == sf::Event::Closed)
            {
                window.close();
            }

            // Handle button clicks
            if (event.type == sf::Event::MouseButtonReleased && event.mouseButton.button == sf::Mouse::Left) 
            {
                sf::Vector2f mousePos = window.mapPixelToCoords(sf::Mouse::getPosition(window));
                if (button.getGlobalBounds().contains(mousePos)) 
                {

                    button.setFillColor(sf::Color::Yellow);
                    buttonText.setFillColor(sf::Color::Red);

                    chosenKanji = sf::String::fromUtf32(1, std::rand() % 20901 + 11904);
                    textKanji.setString(sf::String(chosenKanji));

                    randomChar = std::rand() % 86;
                    textKana.setString(std::wstring(1, 0x3041 + randomChar));
                    clock_a.restart();

                    //std::cout << "\nchanged japanese kana & kanji font symbols on button click\n" << std::endl;
                }
            }
        }

        // Change font symbols once per minute
        if (clock_a.getElapsedTime().asSeconds() >= 60)
        {

            chosenKanji = sf::String::fromUtf32(1, std::rand() % 20901 + 11904);
            textKanji.setString(sf::String(chosenKanji));

            randomChar = std::rand() % 86; // Generate random number between 0 and 85
            textKana.setString(std::wstring(1, 0x3041 + randomChar)); // Set text to Japanese kana font symbol
            clock_a.restart();

            std::cout << "\nautomatically changed japanese kana & kanji font symbols\n" << std::endl;
        }

        // Reset the button color
        if (clock_b.getElapsedTime().asSeconds() >= 0.05 && buttonText.getFillColor() == sf::Color::Red) 
        {
            button.setFillColor(sf::Color::Green);
            buttonText.setFillColor(sf::Color::Blue);
            clock_b.restart();
        }

        // Draw text
        window.clear(grey);
        window.draw(textKana);
        window.draw(reminderText);
        window.draw(textKanji);
        window.draw(button);
        window.draw(buttonText);
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
