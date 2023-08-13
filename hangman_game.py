# Create a simple text-based Hangman game where a player 
# has to guess a word letter by letter.
import random

def hangman_game():
    game_active = True
    words = ['word', 'twenty', 'final fantasy xiv online', 'apple']
    incorrect_guesses = []
    correct_guesses = []
    word = words[random.randint(0,len(words) - 1)]
    while game_active:
        print_hangman(incorrect_guesses)
        print_guesses(incorrect_guesses)
        print_word(word, correct_guesses)
        guess = input("\nGuess the letter: ")
        if guess and len(guess) == 1 and guess not in correct_guesses and guess not in incorrect_guesses:
            if guess in word:
                correct_guesses.append(guess)
                if check_if_win(word, correct_guesses):
                    print('You win!')
                    if try_again():
                        incorrect_guesses = []
                        correct_guesses = []
                        word = words[random.randint(0,len(words) - 1)]
                    else:
                        game_active = False
            else:
                incorrect_guesses.append(guess)
                if len(incorrect_guesses) == 7:
                    print('You lose.')
                    if try_again():
                        incorrect_guesses = []
                        correct_guesses = []
                        word = words[random.randint(0,len(words) - 1)]
                    else:
                        game_active = False

#    _____
#   o    |
#  /|\   |
#   |    |
#  / \  _|_

def hangman0():
    print('   _____')
    print('       |')
    print('       |')
    print('       |')
    print('      _|_')

def hangman1():
    print('   _____')
    print('  o    |')
    print('       |')
    print('       |')
    print('      _|_')

def hangman2():
    print('   _____')
    print('  o    |')
    print('  |    |')
    print('       |')
    print('      _|_')

def hangman3():
    print('   _____')
    print('  o    |')
    print(' /|    |')
    print('       |')
    print('      _|_')

def hangman4():
    print('   _____')
    print('  o    |')
    print(' /|\   |')
    print('       |')
    print('      _|_')

def hangman5():
    print('   _____')
    print('  o    |')
    print(' /|\   |')
    print('  |    |')
    print('      _|_')

def hangman6():
    print('   _____')
    print('  o    |')
    print(' /|\   |')
    print('  |    |')
    print(' /    _|_')

def hangman7():
    print('   _____')
    print('  o    |')
    print(' /|\   |')
    print('  |    |')
    print(' / \  _|_')

def print_hangman(list):
    if len(list) == 0:
        hangman0()
    elif len(list) == 1:
        hangman1()
    elif len(list) == 2:
        hangman2()
    elif len(list) == 3:
        hangman3()
    elif len(list) == 4:
        hangman4()
    elif len(list) == 5:
        hangman5()
    elif len(list) == 6:
        hangman6()
    elif len(list) == 7:
        hangman7()

def print_word(word, correct_guesses):
    for letter in word:
        if letter in correct_guesses:
            print(f' {letter} ', end='')
        elif letter == ' ':
            print('   ', end='')
        else:
            print(' _ ', end='')

def try_again():
    while True:
        answer = input("Try again? (y/n): ")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print("Invalid input.")

def check_if_win(word, correct_guesses):
    new_word = []
    for letter in word:
        if letter != ' ':
            new_word.append(letter)
    for letter in new_word:
        if letter not in correct_guesses:
            return False
    return True

def print_guesses(incorrect_guesses):
    print('Incorrect guesses: ', end='')
    if incorrect_guesses:
        for letter in incorrect_guesses:
            print(letter, end=' ')
    print('')
hangman_game()