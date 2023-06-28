import random
import time
# rock paper scissors game computer


def play():
    feedback = random.choice(["r", "p", "s"])
    # print(feedback)  # it is better to do .upper() then give user lower since it has a lower margin error
    user = input('You are playing rock, paper, scissors. \nrock (r); paper(p); scissors(s)\n').lower()
    # r, p, s
    # r > s; s > p; p > r
    if user == feedback:  # tie
        time.sleep(2)
        print(f'A tie occurred. {user} = {feedback}')

    elif (user == 'r' and feedback == 's') or (user == 's' and feedback == 'p') or (user == 'p' and feedback == 'r'):
        time.sleep(.3)
        print(f'Player wins. {user} > {feedback}')
        time.sleep(1)
    elif (feedback == 'r' and user == 's') or (feedback == 's' and user == 'p') or (feedback == 'p' and user == 'r'):
        time.sleep(.3)
        print(f'Computer was \'{feedback}\'. New game coming up..')
        time.sleep(1)
    else:
        print('Sorry, this doesn\'t match the database. ')
        play()


def playagain():
    e = input('(y/n) Play again?\n').lower()
    if e == 'n':
        return 'n'
    elif e == 'y':
        pass
    else:
        print('Sorry try again?')
        playagain()
        time.sleep(1)


while True:
    time.sleep(.2)
    play()
    if playagain() == 'n':
        time.sleep(2)
        break

