from art import logo
from random import randint


def play():
    """Starts the game"""
    print(logo)

    print("Welcome to the NUMBER GUESSING GAME!")
    print("I'm thinking a number between 1 and 100.")
    number = randint(1, 100)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        attempts = 10
    elif level == 'hard':
        attempts = 5
    else:
        print('INVALID INPUT')
        return

    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess == number:
            print("You Win!")
            return
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
    print("You Lose!")


play()
