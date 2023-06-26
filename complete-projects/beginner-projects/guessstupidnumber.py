import random
import time
# game is, we guess a number, and if the number is too high or low, it tells us
# game ends when number is guessed

def GenRandomNumber(setting):
    number = 0
    if setting == 'easy':
        number = random.randint(1, 1000)
        print(number)
    elif setting == 'hard':
        number = random.randint(1, 100000)
        print(number)
    return number


def UserCallGame():
    response = input("Would you like to play an easy or hard game (e/h)(1000/100000) \n")
    if response == 'e':
        return 'easy'
    elif response == 'h':
        return 'hard'
    else:
        try:
           raise 'InvalidInputError'
        except Exception as e:
            print('Try Again.')
            UserCallGame()
            return e


game = GenRandomNumber(UserCallGame())
"""^^^^^Interesting cause this actually saves this times call of the function, so the random number will get saved
but if we call Game(GenRandomNumber(UserCallGame())), this will give a new number"""

def Guess(HiddenNumber):
    guesses = input('Guess a number..')
    if guesses.isdigit():
        guess = int(guesses)
        if HiddenNumber == guess:
            print('Congrats you won')#, would you like to play again? (y/n) \n')
            # y_n = input('> ') ## this code doesnt work, it doesnt save the new number as the hidden number
            # if y_n == 'y':
            #     Guess(GenRandomNumber(UserCallGame()))
            # elif y_n == 'n':
            #     print('Sorry to see you go.')
            # else:
            #     print('Understandable, have a great day.')

        elif guess < HiddenNumber:
            print(f"Hidden Number is higher than: {guess}")
            Guess(game)
        else: #higher
            print(f"Hidden Number is lower than: {guess}")
            Guess(game)

    else:
        try:
            raise 'InvalidInputError'
        except Exception:
            print('Please don\'t fool around.')
            Guess(game)
            # print(e)

"""Wow I am actually amazed. I wrote this myself, no help.
I did not know I could call functions in functions in functions or idk like this.
It does get confusing after a while."""
Guess(game) #or put this function in a while game:, and game is bool, if they want to play