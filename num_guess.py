from random import random
import math

active_play = True

print('')
print('Number Guessing Game')
print('designed by Jeffrey Jenison')
print('Ver. 1.0  2020-03-18')
print('')

while active_play == True:

    game_win = False

    # Generate guess between 1 and 20
    guess_value = int(math.ceil(random() * 20))

    # Run game until win condition
    while game_win == False:

        while True:
            raw_guess = input("Guess a number between 1 and 20: ")
            try:
                user_guess = int(raw_guess)
                break
            except ValueError:
                print ("This is not a valid guess. Please enter a valid number")

        # Check if guess is correct
        if user_guess == guess_value:
            print('You guessed correct')
            game_win = True

        elif user_guess > guess_value:
            print('You guessed too high')

        elif user_guess < guess_value:
            print('You guessed too low')

        else:
            print('That\'s not a valid guess')


    # Ask if they wan tto play again
    play = input('Play Again? (y/n) : ')
    
    if play == 'y':
        active_play = True

    else:
        active_play = False

print('')
print('Thanks for playing!')
print('')