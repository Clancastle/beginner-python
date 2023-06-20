import random
import time
try:
    number = random.randint(0, 10)
    print(number)

    g = int(input("""number guess
"""))
    if number == g:
        print('win')
        time.sleep(.5)
        number = random.randint(0, 10)
        print(number)

        g = int(input("""number guess
"""))

    elif number != g:
        print('guessed wrong')
except Exception as e:
    number = random.randint(0, 10)

    print(e)
    g = int(input("""number guess
"""))



