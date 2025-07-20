# Cows and Bulls

import random

print("Welcome to Digit Guessing Game")
print("It is two digit Guessing Game")
print("Chances = 7")

secret_number = str(random.randint(10,99))
chances = 7

while chances<=7:
    guess_number = input("Enter your Guessing number: ")
    if guess_number == secret_number:
        print("You are Win!")
        print("Congrats!")
        break
    else:
        cows = 0
        bulls = 0

    if secret_number[0] == guess_number[0]:
        bulls += 1
    if secret_number[1] == guess_number[1]:
        bulls += 1
    if secret_number[0] == guess_number[1]:
        cows += 1
    if secret_number[1] == guess_number[0]:
        cows += 1
    print('cows: ', cows)
    print('Bulls: ', bulls)
    chances -= 1
    if chances<1:
        print("Sorry! Your chances are Over")
        print("Game Over")