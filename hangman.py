import random
from itertools import count

guessed_word = False
lives = [1, 2, 3, 4]
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
->""")#1-5, 6-7, 8+ respectivly (letter count)

#print(hard_words) so the lists work.

def call(difficulti):
    if difficulti == 'easy':
        return random.choice(easy_words)
    elif difficulti == 'mid':
        return random.choice(medium_words)
    elif difficulti == 'hard':
        return random.choice(hard_words)


def letterGuessed(letter):
    if word.find(letter) == -1:
        return "Guess Failed."
    else:
        for i in word:
            pass
            index_letter = word.index(letter)
            blanks = ['_' * len(word)]
            bob = word.split()

            # bob = blanks.insert(index_letter, letter)
            blanks.insert(index_letter, letter)
            print(blanks.insert(index_letter, letter))
            print(bob)
            # print(type(blanks))
            # print(index_letter)
            return blanks

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
->""")
print('BTW, We do not have machine learning here, so sometimes you will get a word you dont know.')
print('Happy Guessing!')
print('-')

guesses = input('Input your guess (a letter) ->')
for life in lives:
    remaining = 4 - life
    print(letterGuessed(guesses))

    print(f'{remaining} remaining life.') #if guessed 1 letter correctly
    # print(f'{lives - life} remaining')
    guesses = input('Input your guess..')




