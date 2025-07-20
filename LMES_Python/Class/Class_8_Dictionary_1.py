# Dictionary has keys and values.
# Keys doesn't have repeated values. Values are followed by Keys(key - 1st, Value - 2nd).
# Data in dictionary is enclosed with curly bracket/braces.

# Bulls and Cows Game:

import random

print('Welcome to Cows and Bulls Game')
print('It is two digit guessing game')
print('Chances = 7')

secret_number = str(random.randint(10,99))
chances = 7

while chances<=7:
    guess_number = input('Enter your Guessing Number: ')
    if secret_number == guess_number:
        print('Congrats!!!!')
        print('Your Guessing number is Correct!')
        print('You Won')
        break
    else:
        cows = 0
        bulls = 0

    if secret_number[0] == guess_number[0]:
        bulls+=1
    if secret_number[1] == guess_number[1]:
        bulls+=1
    if secret_number[0] == guess_number[1]:
        cows+=1
    if secret_number[1] == guess_number[0]:
        cows+=1
    print('Bulls: ',bulls)
    print('Cows: ', cows)
    chances-=1
    if chances<1:
        print('Sorry! Your attempt is over')
        print('Game Over')
        print('Your Secret number is: ', secret_number)
        break