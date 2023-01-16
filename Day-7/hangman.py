# Project 7 - Hangman Game

import random
from hangman_art import stages, logo
from hangman_words import word_list
import os


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform os.name is 'nt'
        _ = os.system('cls')


chosen_word = random.choice(word_list)

print(logo)

display = []
word_length = len(chosen_word)
life = 6
for i in range(word_length):
    display += "_"
print(" ".join(display))

end_of_game = False

while end_of_game is not True:
    guess = input("Guess a letter: ").lower()

    screen_clear()

    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life -= 1
        if life == 0:
            end_of_game = True
            print("You lose.")
    print(" ".join(display))
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[life])
