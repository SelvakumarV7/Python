import random

print("Welcome to Number Guessing Game")
print("Let's Start to Play")
secret_number = str(random.randrange(100))
chances = 7
guess_counter = 0
while guess_counter < chances:
    guess_counter += 1
    guess_number = input("Enter your Guess Number: ")
    if guess_number == secret_number:
        print("Guessing number is correct: ",guess_number)
        print("You Won!")
        break
    elif guess_counter > chances and guess_number != secret_number:
        print("Sorry! Your chances are Over")
        print("You Lost!")
        quit()
    elif guess_number > secret_number:
        print("Your guessing number is higher than secret number")
    elif guess_number < secret_number:
        print("Your guessing number is lower than secret number")
