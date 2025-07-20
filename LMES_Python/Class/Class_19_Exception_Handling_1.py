# Exception Handling:

# Abnormal Termination - program terminate in between not complete the code to run.
# Technical messages are given by machine it normally understand by lane members.

# to overcome the above 2 problems by Exception Handling.

# try: block will not terminate the program.

#example:

print('Program Begins')
a= 10
b = 0
try:
    print(a/b)
except ZeroDivisionError:   # This is the Exception Block(copy the error after except) which helps to run the below message without showing error.
    print("Cannot divide a number by '0'. Change the number of b")
print('Program Ends')


# example 2 - TypeError:

print('Program Starts')
try:
    print(10/'ten')
except TypeError:
    print('Please provide Integer Value')
print('program Ends')

# example 3 - ValueError:
# Multiple Error happens means provide multiple exceptions.

print('Program Starts')
try:
    a = int(input('Enter a Number: '))
    b = int(input('Enter a number: '))
    print(a/b)
except ZeroDivisionError:       # except(ZeroDivisionError, ValueError):
    print('provide values other than Zero')
except ValueError:
    print('Provide Int values')
print('program Ends')