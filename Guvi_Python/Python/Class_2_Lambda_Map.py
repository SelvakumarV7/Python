# Lambda: Small and anonymous function
# supports multiple arguments but one expression.
from idlelib.debugobj import myrepr


def addition(x):
    return x + 10       # single expression(function has single expression)

print(addition(5))

# or

a = lambda y: y + 10        # from y: y + 10 is the arguments
print(a(5))

def power(n):
    return lambda   a: a ** n       # lambda function used for reduce lines of code and for simple functions. lambda a: a ** 2
square = power(2)           # a: a ** 2
print(square(2))            # a: 2 ** 2
cube = power(3)             # a: a ** 3
print(cube(2))              # a: 2 ** 3

# Generators and Decorators: whenever the function can be modified then we use decorators.(like wrapper in chocolate).
# Decorator:

def deco(func):
    print('First line before wrapping')
    func()
    print('Last line after wrapped')

@deco                   # it consider the above function also.
def wrap():
    print('Wrapping happens')

#wrap()

# Generators:   pause  = yield

def fibo():
    yield 1
    yield 2

for i in fibo():
    print(i)
    print(i, 'first')
    print('========')


# Input: default class is string for the user input
a = input('Enter any: ')
print(a)
print(type(a))

# Map: Runs a function on all items in a collection.

collec = [10,20,30,40,50]
collec_2 = []

for i in collec:
    collec_2.append(float(i))
print(collec_2)

# if use Map:

colle = [10,20,30,40,50]
colle_2 = list(map(float, colle))       # inside the list we change the values to float values.
print(colle_2)
double = list(map(lambda x:x*2,colle))
print(double)

# Filter: Save the True values(used to filter out elements from a list)

age = [12,18,25,30,24,10,45,55,20,11]
adults = list(filter(lambda x:x >= 18, age))        # filter only stores the TRUE values(conditions only satisfies).
print(adults)