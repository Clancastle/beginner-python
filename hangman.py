import random
from itertools import count
word_given = False
guessed_word = False
lives = 9
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
(Medium) -- That's fine...
(Hard) -- Oh, a daredevil! 
""")#1-5, 6-7, 8+ respectivly (letter count)

#print(hard_words) so the lists work.

def call(difficulti):
    if difficulti == 'easy':
        return random.choice(easy_words)
    elif difficulti == 'medium':
        return random.choice(medium_words)
    elif difficulti == 'hard':
        return random.choice(hard_words)

for i in count(1):
    if difficulty.lower() == 'easy':
        word = call('easy')
        word_given = True
        print(word)
        break

    elif difficulty.lower() == 'medium':
        word = call('medium')
        word_given = True
        print(word)
        break


    elif difficulty.lower() == 'hard':
        word = call('hard')
        word_given = True
        print(word)
        break

    elif difficulty != 'easy' or 'medium' or 'hard':
        print('Sorry, what was that?')

        difficulty = input("""
(Easy) -- (Medium) -- (Hard)""")



    #let the user call difficulty again.

# while not guessed_word:
# guesses = input('Input your first guess')
# print('BTW, We do not have machine learning here, so sometimes you will get a word you dont know.')

