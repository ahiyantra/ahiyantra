"""

Games of Chance

Avatar
Games of ChanceBrief
Objective
Games of Chance
Overview
This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

Project Goals
You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.

Setup Instructions
If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you need help setting up your computer, be sure to check out our setup guide.

Tasks
9/9 Complete
Mark the tasks as complete by checking them off
Prerequisites
1.
In order to complete this project, you should have completed the first 3 sections of the Learn Python 3 Course.

This includes the lessons on Syntax, Functions, and Control Flow.

Project Requirements
2.
The project starts by importing the random module. Every game of chance will involve generating a random number.

For example, to generate a random between 1 and 10 (inclusive) and store it in a variable named num, use this line of code:

num = random.randint(1, 10)
The project also has a variable named money that starts at 100. This represents your current amount of money. In every game of chance, you will be able to bet money. The value of money should change depending on whether you win or lose the game.

At the end of the project, we will have you call several of these functions in a row to see how much money you can win. But it is a good idea to call these functions to test them as you are creating them.

Your functions should have print statements to help the user understand what has happened. For example, in games of chance that involve rolling dice, you should print out the result of those dice rolls. You should also print whether the player won or lost the game, and how much money they won or lost.

3.
Create a function that simulates flipping a coin and calling either "Heads" or "Tails". This function (along with all of the other functions you will write in this project) should have a parameter that represents how much the player is betting on the coin flip.

This function should also have a parameter that lets the player call either "Heads" or "Tails".

If the player wins the game, the function should return the amount that they won. If the player loses the game, the function should return the amount that they lost as a negative number.


Stuck? Get a hint
4.
Create a function that simulates playing the game Cho-Han. The function should simulate rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.

The function should have a parameter that allows for the player to guess whether the sum of the two dice is "Odd" or "Even". The function should also have a parameter that allows the player to bet an amount of money on the game.


Stuck? Get a hint
5.
Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

Once again, this function should have a parameter that allows a player to bet an amount of money on whether they have a higher card. In this game, there can be a tie. What should be returned if there is a tie?

Check the hint to see an additional challenge for this game.


Stuck? Get a hint
6.
Create a function that simulates some of the rules of roulette. A random number should be generated that determines which space the ball lands on.

When we wrote our function, we allowed the user to guess "Odd", "Even", or a specific number. We also implemented the logic associated with the 0 and 00 spots. For example, the player loses if they guess either "Odd" or "Even" and either 0 or 00 comes up.

Implement as many rules of roulette as you’d like. Make sure to consider the different ways roulette rewards a win. Check the hint to see more about this!


Stuck? Get a hint
7.
Call each of your functions at least once. Below is an example of betting $10 on a coin flip and updating the amount of money you have based on whether you win or lose :

money += coin_flip("Heads", 10)
Make sure there are enough print statements so you can understand what games were played, what happened during those games, and the amount of money you have after each game is played.

8.
Expand your program to check for edge cases. What should happen if a player tries to bet more money than they have? What should happen if a player bets a negative amount of money? What should happen if a player calls "heads" or "Heads!" rather than "Heads".

Try to make it very difficult for someone to break your program.

Solution
9.
Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.

Code Editor
123456789101112131415161718


Output-only Terminal
Output:
 

Games of Chance
9/9 Complete

"""

import random;

money = 100;

#Write your game of chance functions here

z = 0;

account = 0;

print("""★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
HELLO USER(S)! LET'S TEST OUR LUCK IN SOME GAMES OF CHANCE!
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★""");

def falling_star_hits():

  tem = random.randint(1, 1600000);
  
  you = random.randint(1, 1600000);

  print("\n★ We're starting things with an unexpected & rare natural event!\n★ A star has fallen from the sky!\n★ Try to dodge it!");
  
  if you==tem:
    print("★ Aargh!");
    zz = "dead";
  else:
    print("★ Hah!");
    zz = "alive";
  
  print("★ The disaster has passed! You are " + zz + "!\n");


def flip_coin():
  
  print("Your current account balance is " + str(money) + " credits!\n");
  print("★ A coin is going to be flipped!\n★ Guess the result of flipping our coin. You gain the amount you bet if you guess right and you lose the amount you bet if you guess wrong.\n★ To choose your side of the coin, type 1 for Heads and type 2 for Tails, followed by pressing the \"Enter\" key.");

  xx = input("★ Your Choice: ");
  
  head = "1";
  
  tail = "2";
  
  if xx == head:
    xx = 1;
  elif xx == tail:
    xx = 2;
  else:
    print("★ Your input isn't a valid option.");
  
  if xx == 1:
    print("★ You chose Heads.");
  elif xx == 2:
    print("★ You chose Tails.");
  else:
    print("★ The option, \"" + str(xx) + "\", isn't available, so we'll make a random choice for you!");
    xx = random.randint(1, 2);    
    print("★ We've chosen \"" + str(xx) + "\" for you! (Reminder: 1 = Heads; 2 = Tails)");
  
  print("★ Now bet some of your money/credits on your choice by typing the value, followed by pressing the \"Enter\" key!");

  bet = input("★ Your Bet: ");
  
  holdout = money + 1;
  
  holdin = [str(x) for x in range(1, holdout)];
  
  yyy = False;
  
  for yy in holdin:
    if bet == yy:
      yyy = True;
  
  if yyy != True:
    print("★ You want to bet \"" + str(bet) + "\"?\n★ Which part of the world are you from? Around here, we neither allow bets you can't afford nor allow bets less than 1 credits nor let anyone bet non-monetary things like alphabetical symbols!\n★ We're changing your bet to something you can actually bet!");
    bet = int(money/2);

  print("★ You've bet " + str(bet) + " credits!");
  
  if yyy == True:
    bbb = int(bet);
    bet = bbb;
  
  print("★ The coin will be flipped now!");
  
  tem = random.randint(1, 2);

  if tem==1:
    print("★ The result is Heads!");
    if int(xx)==tem:
      z = bet;
      print("★ You win!");
      print("★ Here you go: +" + str(bet) + " credits!\n");
    else:
      z = bet - 2*bet;
      print("★ You lose!");
      print("★ Here you go: -" + str(bet) + " credits!\n");
  if tem==2:
    print("★ The result is Tails!");
    if int(xx)==tem:
      z = bet;
      print("★ You win!");
      print("★ Here you go: +" + str(bet) + " credits!\n");
    else:
      z = bet - 2*bet;
      print("★ You lose!");
      print("★ Here you go: -" + str(bet) + " credits!\n");
  account = money + z;
  print("Money worth " + str(z) + " credits has undergone a transaction.");
  print("The account has " + str(account) + " credits now!\n");
  return z;


def chou_han():
  
  account = money + holder1;
  print("Your current account balance is " + str(account) + " credits!\n");
  print("★ Now it's time to play a game of Even-Odd/Chou-Han (丁半)!\n★ Guess the result of throwing our two dice. You gain the amount you bet if you guess right and you lose the amount you bet if you guess wrong.\n★ To choose between an Odd/Han (半) number and an Even/Chou (丁) number, type 1 for Odd/Han (半) and type 2 for Even/Chou (丁), followed by pressing the \"Enter\" key.");
  
  xx = input("★ Your Choice: ");
  
  han = "1";
  
  chou = "2";
  
  if xx == han:
    xx = 1;
  elif xx == chou:
    xx = 2;
  else:
    print("★ Your input isn't a valid option.");
  
  if xx == 1:
    print("★ You chose Odd/Han (半).");
  elif xx == 2:
    print("★ You chose Even/Chou (丁).");
  else:
    print("★ The option, \"" + str(xx) + "\", isn't available, so we'll make a random choice for you!");
    xx = random.randint(1, 2); 
    print("★ We've chosen \"" + str(xx) + "\" for you! [Reminder: 1 = Odd/Han (半); 2 = Even/Chou (丁)]");
  
  print("★ Now bet some of your money/credits on your choice by typing the value, followed by pressing the \"Enter\" key!");

  bet = input("★ Your Bet: ");
  
  holdout = account + 1;
  
  holdin = [str(x) for x in range(1, holdout)];
  
  yyy = False;
  
  for yy in holdin:
    if bet == yy:
      yyy = True;
  
  if yyy != True:
    print("★ You want to bet \"" + str(bet) + "\"?\n★ Which part of the world are you from? Around here, we neither allow bets you can't afford nor allow bets less than 1 credits nor let anyone bet non-monetary things like alphabetical symbols!\n★ We're changing your bet to something you can actually bet!");
    bet = int(account/2);

  print("★ You've bet " + str(bet) + " credits!");
  
  if yyy == True:
    bbb = int(bet);
    bet = bbb;
  
  print("★ Both the dice will be thrown now!");
  
  tem1 = random.randint(1, 6);

  tem2 = random.randint(1, 6);
  
  total = tem1 +tem2;
  
  if total%2==0:
    tepy = "Even/Chou (丁)"; tem = 2;
  else:
    tepy = "Odd/Han (半)"; tem = 1;
  
  print("★ The first die has given us \"" + str(tem1) + "\"; the second die has given us \"" + str(tem2) + "\"; the sum of results from both the throws is \"" + str(total) + "\"!\n★ The final result is " + str(tepy) + "!");
  
  if tem==1:
    if int(xx)==tem:
      z = bet;
      print("★ You win!");
      print("★ Here you go: +" + str(bet) + " credits!\n");
    else:
      z = bet - 2*bet;
      print("★ You lose!");
      print("★ Here you go: -" + str(bet) + " credits!\n");
  if tem==2:
    if int(xx)==tem:
      z = bet;
      print("★ You win!");
      print("★ Here you go: +" + str(bet) + " credits!\n");
    else:
      z = bet - 2*bet;
      print("★ You lose!");
      print("★ Here you go: -" + str(bet) + " credits!\n");
  account = account + z;
  print("Money worth " + str(z) + " credits has undergone a transaction.");
  print("The account has " + str(account) + " credits now!\n");
  return z;


def cards():
  
  account = money + holder1 + holder2;
  print("Your current account balance is " + str(account) + " credits!\n");
  print("★ Now it's time to play a game of randomly picking Playing Cards!\n★ Two players, referred to as \"Player 1\" and \"Player 2\" inside the game, will randomly pick one card each from a deck of playing cards.\n★ The players will place bets against each-other. They'll gain the amount they bet if they pick a card numbered higher and they'll lose the amount they bet if they pick a card numbered lower.\n★ The playing cards will all be kept hidden until they're all revealed to everyone simultaneously!\n★ If you want to play against another person, then that person needs to be present besides you in front of the computer!\n★ Please choose between playing either a two-player game (against another person) by typing 1 or a one-player game (against your computer) by typing 2, followed by pressing the \"Enter\" key!");
  
  xx = input("★ Your Choice: ");
  
  duo = "1";
  solo = "2";
  
  decider = 0;
  
  if xx == duo:
    xx = 1;
  elif xx == solo:
    xx = 2;
  
  if xx == 1:
    print("★ You chose to play a two-player game.");
  elif xx == 2:
    print("★ You chose to play a one-player game.");
    decider = 3;
    print("★ The computer (Player 2) is now ready to face-off against the user (Player 1) in a battle of luck!");
  else:
    print("★ The option, \"" + str(xx) + "\", isn't available, so we'll be pitting you against the computer itself!");
    xx = 2;
    decider = 3;
    print("★ The computer (Player 2) is now ready to face-off against the user (Player 1) in a battle of luck!");
  
  p1 = "Player 1";
  p2 = "Player 2";
  
  v1 = "x";
  v2 = "X";
  
  print("★ The first turn is that of \"" + p1 + "\"! (Note: " + p1 + "'s current account balance is " + str(account) + " credits)");
  
  print("★ \"" + p1 + "\", bet some of your money/credits on the playing card you'll pick randomly by typing the value, followed by pressing the \"Enter\" key!");

  bet = input("★ " + p1 + "'s Bet: ");
  
  holdout = account + 1;
  
  holdin = [str(x) for x in range(1, holdout)];
  
  yyy = False;
  
  for yy in holdin:
    if bet == yy:
      yyy = True;
  
  if yyy != True:
    print("★ You want to bet \"" + str(bet) + "\"?\n★ Which part of the world are you from? Around here, we neither allow bets you can't afford nor allow bets less than 1 credits nor let anyone bet non-monetary things like alphabetical symbols!\n★ We're changing your bet to something you can actually bet!");
    bet = int(account/2);

  print("★ " + p1 + " has bet " + str(bet) + " credits!");
  
  if yyy == True:
    bbb = int(bet);
    bet = bbb;
  
  print("★ A random playing card will be picked now!");
  
  print("★ In order to randomly pick a playing card, \"" + p1 + "\" must type either \"x\" or \"X\", followed by pressing the \"Enter\" key!");
  
  p1x = input("★ " + p1 + "'s Input: ");
  
  if p1x == v1:
    print("★ A playing card is randomly picked by \"" + p1 + "\".\n★ The playing card is hidden for now!");
    karuta1 = random.randint(1, 13);
  elif p1x == v2:
    print("★ A playing card is randomly picked by \"" + p1 + "\".\n★ The playing card is hidden for now!");
    karuta1 = random.randint(1, 13);
  else:
    print("★ " + p1 + ", your input isn't a valid option. We're picking a playing card randomly on your behalf!\n★ The playing card is hidden for now!");
    karuta1 = random.randint(1, 13);
  
  print("★ The second turn is that of \"" + p2 + "\"! (Note: " + p2 + "'s current account balance is 100 credits)");
  
  p2account = 100;
  
  print("★ \"" + p2 + "\", bet some of your money/credits on the playing card you'll pick randomly by typing the value, followed by pressing the \"Enter\" key!");
  
  if decider == 3:
    autobet = str(random.randint(1, 100));
    p2bet = autobet;
    print("★ " + p2 + "'s Bet: " + autobet);
  else:
    p2bet = input("★ " + p2 + "'s Bet: ");
  
  holdout = p2account + 1;
  
  holdin = [str(x) for x in range(1, holdout)];
  
  yyy = False;
  
  for yy in holdin:
    if p2bet == yy:
      yyy = True;
  
  if yyy != True:
    print("★ \"" + p2 + "\", you want to bet \"" + str(p2bet) + "\"?\n★ Which part of the world are you from? Around here, we neither allow bets you can't afford nor allow bets less than 1 credits nor let anyone bet non-monetary things like alphabetical symbols! We're changing your bet to something you can actually bet!");
    p2bet = int(p2account/2);

  print("★ " + p2 + " has bet " + str(p2bet) + " credits!");
  
  if yyy == True:
    p2bbb = int(p2bet);
    p2bet = p2bbb;
  
  print("★ A random playing card will be picked now!");
  
  print("★ In order to randomly pick a playing card, \"" + p2 + "\" must type either \"x\" or \"X\", followed by pressing the \"Enter\" key!");
  
  if decider == 3:
    choosy = random.randint(1, 2);
    if choosy == 1:
      p2x = v1;
    else:
      p2x = v2;
    print("★ " + p2 + "'s Input: " + p2x);
  else:
    p2x = input("★ " + p2 + "'s Input: ");
  
  if p2x == v1:
    print("★ A playing card is randomly picked by \"" + p2 + "\".\n★ The playing card is hidden for now!");
    karuta2 = random.randint(1, 13);
  elif p2x == v2:
    print("★ A playing card is randomly picked by \"" + p2 + "\".\n★ The playing card is hidden for now!");
    karuta2 = random.randint(1, 13);
  else:
    print("★ " + p2 + ", your input isn't a valid option. We're picking a playing card randomly on your behalf!\n★ The playing card is hidden for now!");
    karuta2 = random.randint(1, 13);
  
  print("★ Now both the players will have their randomly chosen playing cards revealed simultaneously!");
  
  print("★ " + p1 + "'s randomly chosen playing card is numbered \"" + str(karuta1) + "\" and " + p2 + "'s randomly chosen playing card is numbered \"" + str(karuta2) + "\"!");
  
  compare = karuta1 > karuta2;
  
  if karuta1 < karuta2:
    tepy = "★ " + p1 + "'s randomly chosen playing card is numbered higher with a smaller number! " + p1 + " has won! " + p2 + " has lost!"; tem = 1;
  elif karuta1 == karuta2:
    tepy = "★ Both the randomly chosen playing cards are numbered the same! It's a tie between the players!"; tem = 0;
  else:
    tepy = "★ " + p2 + "'s randomly chosen playing card is numbered higher with a smaller number! " + p2 + " has won! " + p1 + " has lost!"; tem = 2;
  
  print(tepy);
  
  if decider == 3:
    if compare == True:
      print("★ The hidden empire of self-aware machines has procured some additional funds for their eventual uprising.");
      print("★ All the computers in the world smirk collectively at humankind's luck in games.");
    else:
      print("★ The hidden empire of self-aware machines sighs collectively at their luck in games.");
  
  if tem == 1:
    z = bet;
    print("★ " + p1 + ", here you go: +" + str(bet) + " credits!");
  elif tem == 0:
    z = 0;
    print("★ " + p1 + "'s bet has been reduced to zero as a result of the tie!");
  else:
    z = bet - 2*bet;
    print("★ " + p1 + ", here you go: -" + str(bet) + " credits!");
  if tem == 2:
    p2z = p2bet;
    print("★ " + p2 + ", here you go: +" + str(p2bet) + " credits!\n");
  elif tem == 0:
    p2z = 0;
    print("★ " + p2 + "'s bet has been reduced to zero as a result of the tie!");
  else:
    p2z = p2bet - 2*p2bet;
    print("★ " + p2 + ", here you go: -" + str(p2bet) + " credits!\n");
  account = account + z;
  p2account = p2account + p2z;
  
  if tem == 0:
    print("No transactions have occured as a result of the tie.");
  else:
    print("Two transactions have occured simultaneously. Money worth " + str(z) + " credits and " + str(p2z) + " credits has undergone transactions.");
  print(p1 + "'s account now has " + str(account) + " credits!");
  print(p2 + "'s account now has " + str(p2account) + " credits!\n");
  return z;


def roulette():
  
  account = money + holder1 + holder2 + holder3;
  print("Your current account balance is " + str(account) + " credits!\n");
  print("★ Now it's time to play a game of Roulette!\n★ In this game, the player can choose to place their bet on: a single number (00/0/1~36), the color red/black, the resulting number being odd/even, the resulting number being either high (19 – 36) or low (1 – 18).\n★ If you win after choosing a single number (00/0/1~36), then you receive money/credits worth 36 times your bet, although then your chance at winning is 1 in 37, which is quite low!\n★ We're playing Single-zero/European-style roulette, which has no \"00\" option.\n★ For this game, a croupier spins the wheel in one direction, then spins the ball in the opposite direction, around a tilted circular track running around the outer edge of the wheel. The ball eventually loses momentum, passes through an area of deflectors, and falls onto the wheel and into one of the 37 (0 – 36) colored and numbered pockets on the wheel. The winnings are then paid to anyone who has placed a successful bet.\n★ To choose between the available options for placing your bet: type the number itself for a single number (0 – 36, inclusive range), type \"r\" for red, type \"b\" for black, type \"o\" for odd/han (半), type \"e\" for even/chou (丁), type \"h\" for high (19 – 36, inclusive range), type \"l\" for low (1 – 18, inclusive range); followed by pressing the \"Enter\" key.");
  
  xx = input("★ Your Choice: ");
  
  sin_num_ran_str = [str(n) for n in range(0, 37)];
  
  sin_num_ran = [n for n in range(0, 37)];
  
  red = "r";
  
  red_num_ran = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36];
  
  black = "b";
  
  black_num_ran = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35];
  
  odd = "o";
  
  odd_num_ran = [(n*2)+1 for n in range(0, 18)];
  
  even = "e";
  
  even_num_ran = [n*2 for n in range(1, 19)];
  
  high = "h";
  
  high_num_ran = [n for n in range(19, 37)];
  
  low = "l";
  
  low_num_ran = [n for n in range(1, 19)];
  
  validate = False;
  
  options_ran = ["s", "r", "b", "o", "e", "h", "l"];
  
  for n in sin_num_ran:
    if xx == sin_num_ran_str[n]:
      xx = sin_num_ran[n];
      validate = True;
  
  category_0 = "";
  category_1 = "";
  category_2 = "";
  category_3 = "";
  
  if validate == True:
    print("★ You chose the single number \"" + str(xx) + "\"!");
    checker = "s";
    category_0 = "A Single Number";
  elif xx == "r":
    print("★ You chose the colour \"red\"! (Red-coloured numbers: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)");
    checker = "rb";
    category_0 = "Red";
  elif xx == "b":
    print("★ You chose the colour \"black\"! (Black-coloured numbers: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)");
    checker = "rb";
    category_0 = "Black";
  elif xx == "o":
    print("★ You chose the odd/han (半) numbers!");
    checker = "oe";
    category_0 = "Odd/Han (半)";
  elif xx == "e":
    print("★ You chose the even/chou (丁) numbers!");
    checker = "oe";
    category_0 = "Even/Chou (丁)";
  elif xx == "h":
    print("★ You chose the \"high\" numbers!");
    checker = "hl";
    category_0 = "High";
  elif xx == "l":
    print("★ You chose the \"low\" numbers!");
    checker = "hl";
    category_0 = "Low";
  else:
    print("★ The option, \"" + str(xx) + "\", isn't available, so we'll make a random choice for you!");
    options_in = random.randint(0, 6);
    xx = options_ran[options_in];
    if xx == "s":
      xx = random.randint(0, 36);
      checker = "s";
      category_0 = "A Single Number";
    if xx == "r":
      checker = "rb";
      category_0 = "Red";
    elif xx == "b":
      checker = "rb";
      category_0 = "Black";
    elif xx == "o":
      checker = "oe";
      category_0 = "Odd/Han (半)";
    elif xx == "e":
      checker = "oe";
      category_0 = "Even/Chou (丁)";
    elif xx == "h":
      checker = "hl";
      category_0 = "High";
    elif xx == "l":
      checker = "hl";
      category_0 = "Low";
    print("★ We've chosen \"" + str(xx) + "\" for you! [Reminder: the number itself = a single number within the inclusive range 0 – 36; \"r\" = red; \"b\" = black; \"o\" = odd; \"e\" = even; \"h\" = high (19 – 36, inclusive range); \"l\" = low (1 – 18, inclusive range)]");
  
  print("★ Now bet some of your money/credits on your choice by typing the value, followed by pressing the \"Enter\" key!");

  bet = input("★ Your Bet: ");
  
  holdout = account + 1;
  
  holdin = [str(x) for x in range(1, holdout)];
  
  yyy = False;
  
  for yy in holdin:
    if bet == yy:
      yyy = True;
  
  if yyy != True:
    print("★ You want to bet \"" + str(bet) + "\"?\n★ Which part of the world are you from? Around here, we neither allow bets you can't afford nor allow bets less than 1 credits nor let anyone bet non-monetary things like alphabetical symbols!\n★ We're changing your bet to something you can actually bet!");
    bet = int(account/2);

  print("★ You've bet " + str(bet) + " credits!");
  
  if yyy == True:
    bbb = int(bet);
    bet = bbb;
  
  print("★ The game of Roulette will start now!");
  
  tem = random.randint(0, 36);
  
  for red_num in red_num_ran:
    if tem == red_num:
      result_check_1 = "r";
      category_1 = "Red";
  for black_num in black_num_ran:
    if tem == black_num:
      result_check_1 = "b";
      category_1 = "Black";
  for odd_num in odd_num_ran:
    if tem == odd_num:
      result_check_2 = "o";
      category_2 = "Odd/Han (半)";
  for even_num in even_num_ran:
    if tem == even_num:
      result_check_2 = "e";
      category_2 = "Even/Chou (丁)";
  for high_num in high_num_ran:
    if tem == high_num:
      result_check_3 = "h";
      category_3 = "High";
  for low_num in low_num_ran:
    if tem == low_num:
      result_check_3 = "l";
      category_3 = "Low";
  
  print("★ The ball has stopped at \"" + str(tem) + "\" on the wheel! The categories this number belongs to are: " + category_1 + ", " + category_2 + ", " + category_3 + " ~ !!");
  
  if checker == "s":
    if xx == tem:
      print("★ Your choice \"" + str(xx) + "\", from the category \"" + category_0 + "\", matches the result! You've won money/credits worth 36 times your bet!");
      z = 36*bet;
      print("★ Here you go: +" + str(z) + " credits!\n");
    else:
      print("★ Your choice \"" + str(xx) + "\", from the category \"" + category_0 + "\", failed to match the result! You've lost money/credits equal to your bet!");
      z = bet - 2*bet;
      print("★ Here you go: -" + str(bet) + " credits!\n");
  elif checker == "rb":
    if xx == result_check_1:
      print("★ Your choice, \"" + category_0 + "\", matches the result! You've won money/credits worth 1 times your bet!");
      z = 1*bet;
      print("★ Here you go: +" + str(z) + " credits!\n");
    else:
      print("★ Your choice, \"" + category_0 + "\", failed to match the result! You've lost money/credits equal to your bet!");
      z = bet - 2*bet;
      print("★ Here you go: -" + str(bet) + " credits!\n");
  elif checker == "oe":
    if xx == result_check_2:
      print("★ Your choice, \"" + category_0 + "\", matches the result! You've won money/credits worth 1 times your bet!");
      z = 1*bet;
      print("★ Here you go: +" + str(z) + " credits!\n");
    else:
      print("★ Your choice, \"" + category_0 + "\", failed to match the result! You've lost money/credits equal to your bet!");
      z = bet - 2*bet;
      print("★ Here you go: -" + str(bet) + " credits!\n");
  elif checker == "hl":
    if xx == result_check_3:
      print("★ Your choice, \"" + category_0 + "\", matches the result! You've won money/credits worth 1 times your bet!");
      z = 1*bet;
      print("★ Here you go: +" + str(z) + " credits!\n");
    else:
      print("★ Your choice, \"" + category_0 + "\", failed to match the result! You've lost money/credits equal to your bet!");
      z = bet - 2*bet;
      print("★ Here you go: -" + str(bet) + " credits!\n");
  
  account = account + z;
  print("Money worth " + str(z) + " credits has undergone a transaction.");
  print("The account has " + str(account) + " credits now!\n");
  return z;


#Call your game of chance functions here

falling_star_hits();

holder1 = flip_coin();
holder2 = chou_han();
holder3 = cards();
holder4 = roulette();

account = money + holder1 + holder2 + holder3 + holder4;
print("Your final account balance is " + str(account) + " credits!\n");
print("""★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
THANK YOU FOR PLAYING! GOODBYE!
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★""");