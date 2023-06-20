import random
from itertools import count


guessed_word = False #i dont think this has much effect but ill keep it.
lives = [1, 2, 3, 4] #lives = 10, while lives != 0

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()

# use groupby -> word list, easy, med hard, with 1-5, 6-7, 8+ respectivly
# or use lambda

easy_words = list(filter(lambda x: len(x) <= 4 and len(x) > 2, words))
medium_words = list(filter(lambda x: len(x) <= 7, words))
hard_words = list(filter(lambda x: len(x) >= 8, words))

difficulty = input("""Choose your difficulty.
(Easy) -- Just say you are a coward.
Medium(Mid) -- That's fine...
(Hard) -- Oh, a daredevil!
->""").lower()#1-5, 6-7, 8+ respectivly (letter count)

#print(hard_words) so the lists work.

def call(difficulti):
    if difficulti == 'easy':
        return random.choice(easy_words).lower()
    elif difficulti == 'mid':
        return random.choice(medium_words).lower()
    elif difficulti == 'hard':
        return random.choice(hard_words).lower()


def letterGuessed(letter):
    if word.find(letter) == -1:
        return "Guess Failed."

    else:
        for i in word:
            if i in letter:
                print(i,end="") #copied, do not know how this works
            else:
                print('_',end=''),

while not guessed_word:
    for i in count(1):
        if difficulty.lower() == 'easy':
            word = call('easy')
            print(word)

            break

        elif difficulty.lower() == 'mid':
            word = call('mid')
            print(word)

            break

        elif difficulty.lower() == 'hard':
            word = call('hard')
            print(word)

            break

        elif difficulty != 'easy' or 'mid' or 'hard':
            print('Sorry, what was that?')
            difficulty = input("""
    (Easy) -- Medium(Mid)-- (Hard)
    ->""").lower()
    print('BTW, We do not have machine learning here, so sometimes you will get a word you dont know.')
    print('Happy Guessing!')
    print('-')

    guesses = input('Input your guess (a letter/ guess the word) ->').lower()
    for life in lives:
        if guesses == word:
            guessed_word = True
            print('You Win!')
            print('Play again?')
            y_n = input('(y) or (n)').lower()

            if y_n == 'y':
                guessed_word = False
                difficulty = input("""
    (Easy) -- Medium(Mid)-- (Hard)
    ->""").lower()
            elif y_n == 'n':
                print('Sorry to see you go.')
            else:
                guessed_word = False
                print("Didn't understand that.")
                difficulty = input("""
    (Easy) -- Medium(Mid)-- (Hard)
    ->""").lower()
                break
            #break #
        remaining = 4 - life
        print(letterGuessed(guesses))

        #print(f'{remaining} remaining life.') #if guessed 1 letter correctly
        # print(f'{lives - life} remaining')




