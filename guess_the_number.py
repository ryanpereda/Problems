# Create a simple number guessing game where the computer generates a
# random number and the user has to guess it.

import random

while True:
    number = random.randint(1, 10)
    try:
        inp = int(input("Pick a number between 1 and 10: "))
        print (inp, number)
        print(inp == number)
        if inp == number:
            print('you win')
        else:
            print(f'wrong, it was {number}')
    except ValueError:
        print('error')