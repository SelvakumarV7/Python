import random

print("Welcome to ROCK/PAPER/SCISSOR Game")
print("Lats Play")



while True:

    print("Enter one option from 1 to 3: \n 1 - Rock \n 2 - Paper \n 3 - Scissor")
    option = int(input("Enter Your Option: "))
    while option > 3 or option < 1:
        option = int(input("Enter a valid input 1 to 3: "))

    if option == 1:
        option_name = "Rock"
    elif option == 2:
        option_name = "Paper"
    else:
        option_name = "Scissor"
    print("User Option is: ",option)

    comp_option = random.randint(1,3)
    if comp_option == 1:
        comp_option_name = "Rock"
    elif comp_option == 2:
        comp_option_name = "Paper"
    else:
        comp_option_name = "Scissor"

    print("computer Option is: ",comp_option)
    print(option, "VS", comp_option)

    if option == comp_option:
        print("Draw")
    elif option == 1 and comp_option == 2:
        print("You Won")
    elif option == 2 and comp_option == 3:
        print("You Won")
    elif option == 3 and comp_option == 1:
        print("You Won")
    else:
        print("Computer Won")