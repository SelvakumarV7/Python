import random

print("Welcome to Random Password Generator")
random_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&"
no_of_password = int(input("Enter number of Passwords: "))
len_of_password = int(input("Enter the length of passwords: "))
print("Your Passwords are: ")

for i in range(no_of_password):
    password = ""
    for j in range(len_of_password):
        password = password + random.choice(random_char)
    print(password)