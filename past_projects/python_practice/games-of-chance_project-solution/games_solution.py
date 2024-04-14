import random

total = 100

def coin_flip(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        return 0
        print("------------------")

    #Starts the game and flips the coin
    print("------------------")
    print("Let's flip a coin! You guessed " + guess)
    result = random.randint(1,2)

    # Prints the result of the coin flip. A 1 is heads, a 2 is tails
    if result == 1:
        print("Heads!")
    elif result == 2:
        print("Tails")

    # Determines if you won or lost and returns either bet or -bet
    if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet

def higher_card(bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0

    # Draws two cards between 1 and 10 and prints the result
    print("------------------")
    print("Let's play a game of cards!")
    mine = random.randint(1, 10)
    theirs = random.randint(1, 10)
    print("Your card was " + str(mine))
    print("Their card was " + str(theirs))

    #Determines who won and returns either bet, -bet or 0 (in the case of a tie.)
    if mine > theirs:
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    elif mine < theirs:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet
    else:
        print("It was a tie!")
        print("------------------")
        return 0

def cho_han(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0

    print("------------------")
    print("Let's play Cho-Han!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("The sum of the two dice is " + str(total))

    if guess == "Even" and total % 2 == 0:
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    elif guess == "Odd" and total % 2 == 1:
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet

def roulette(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0

    #A standard roulette wheel has the numbers 0 through 36 as well as 00. We'll use 37 to represent 00.
    print("------------------")
    print("Let's play roulette!")
    result = random.randint(0, 37)
    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on " + str(result))

    #Checks to see if we guessed Even and the result was even. If the result was 0, the player shouldn't win
    if guess == "Even" and result % 2 == 0 and result != 0:
        print(str(result) + " is an even number.")
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet

    #Checks to see if we guessed Odd and the result was odd. If the result was 37, the player shouldn't win, since that's what we are using to represent 00.
    elif guess == "Odd" and result % 2 == 1 and result != 37:
        print(str(result) + " is an odd number.")
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet

    # If you guessed a number and the result was that number, you should win 35 times the amount they bet
    elif guess == result:
        print("You guessed " + str(guess) + " and the result was " + str(result))
        print("You won " + str(bet * 35)+" dollars!")
        print("------------------")
        return bet * 35

    # If none of the above are true, you lost.
    else:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet

total += coin_flip("Heads", 10)
total += higher_card(5)
total += cho_han("Even", 2)
total += roulette("Even", 10)
total += roulette(3, 1)
total += roulette("Odd", total)
print("Your total amount of money is " + str(total))
