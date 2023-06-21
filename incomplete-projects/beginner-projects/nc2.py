import random
import string

#this below gives a number to computer to choose randomly between, and you have to guess.
# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, too low.')
#         elif guess > random_number:
#             print('Try again, too high.')
#
#     print(f' Congrats, you guessed the number {random_number}')


#this plays w computer, you choose a number and the computer narrows it down.
# def com_guests(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low
#         guess = random.randint(low, high)
#         feedback = input(f'Is {guess} too high (H) or too low (L), or correct (C)??').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f'Guessed number. ')
#
# com_guests(1000)


#sad shit. so you call the function, and the computer picks a random choice, and you will see if you will beat it or not.
# def play():
#     user = input("'r' for rock, 'p' for paper, 's' for scissors")
#     computer = random.choice(['r', 'p', 's'])
#
#     if user == computer:
#         return 'It\'s a tie'
#     if is_win(user, computer):
#         return 'Player, you won!'
#     if is_win(user, computer):
#         return 'Computer won, try again.'
#
#
# def is_win(player, opponent):
#     if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
#         return True
#
# print(play())


#hangman with different code than ive written. and it seems better
# word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
# word_file = "/usr/share/dict/words"
# words = open(word_file).read().splitlines()
#
#
# def get_valid_word(words):
#     word = random.choice(words)
#     while 'z' in word or '-' in word:
#         word = random.choice(words)
#     return word.upper()
#
# def hangman():
#
#     word = get_valid_word(words)
#     alphabet = set(string.ascii_uppercase)
#     word_letters = set(word)
#     used_letters = set()
#     lives = 6
#     while len(word_letters) > 0 and lives > 0:
#         print('You have', lives, 'lives and have used these:', ' '.join(used_letters))
#
#         word_list = [letter if letter in used_letters else '_' for letter in word]
#         print('Current word: ', ' '.join(word_list))
#         user_letter = input('Guess a letter: ').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#             else:
#                 lives = lives - 1
#                 print('Not in word.')
#
#         elif user_letter in used_letters:
#             print('You\'ve used that before')
#         else:
#             lives = lives - 1
#             print('Invalid Input')
#     if lives == 0:
#         print('Sorry, you\'ve lost')
#         print(word)
#
# hangman()


