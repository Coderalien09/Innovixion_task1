# This is number guessing game

import random

import logo_art

print("Welcome to ")
print(logo_art.logo)


c_num = random.randint(1, 100)
guess = 0

while guess != c_num:
    user = int(input("Guess a number between 1 to 100 : "))

    if guess < c_num:
        print("The guess number is low.")
    elif guess > c_num:
        print(" The guess number is high.")
    else:
        print("well done!, You won the game!")
