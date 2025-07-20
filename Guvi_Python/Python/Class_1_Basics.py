# Python   ->  Compiler  ->    ByteCodde    ->      Virtual Machine(Interpretar),Also gets data from Library if needs.    ->      Output
# to terminal check = python -m dis .\filename.py

print('hello')


# datatypes:
#
# int
# float
# complex
# string
# boolean
# None: Absence of Value

print(None)
print(type(None))


# Sequences:
    # Strings
    # Lists
    # Tuples
    # Sets
    # Dictionary

a = -10.7
print(bool(a))

a,b,c = 1,2,3
print(a,b,c, sep = '\n')    # Seperator

# Operators:
    # Arithmetic
    # Assignment
    # Comparison
    # Logical
    # Identity
    # Membership
    # Bitwise

# Arithmetic:
x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)        # Modulus -  Returns reminder
print(x ** y)       # Power Of
print(x // y)       # Floor Division - returns int value without decimal


# Assignment Operator:(=,+=,-=./=,*=,%=,**=,&=,!=,>>=,<<=,)
# Comparison Operator:(==,<=,>=,!=,<,>)
# Logical Operator:(AND,OR,NOT)
# Identity and Membership Operator:(is, is not,in,not in)
# Bitwise Operator:(&,|,^,~,<<,>>) - (AND,OR,XOR,NOT,Zero fill left shift,Zero fill right shift).

x = 5       # binary: 101
y = 3       # binary: 011

result = x & y
print(result)

result = x | y      # 101 | 011  -  2^0 th position  - 1 | 1 = 1  and 2^1 th position - 0 | 1 = 1 and 2^2 th position  -  1 | 0  =  1
print(result)                            # 1                            2                               4               =  7

# Control Flow Statement: program flow controlled by order of execution by the programmer.
    # Sequence   =  Flow
    # Selection  =  Decision
    # Iteration  =  certain number of times repeat the program by condition.

# Selection:
# One way Selection:
order = 450
delivery = 50
minimum_order = 500

if order > minimum_order:
    delivery = 0

total = order + delivery
print(total)

# Two Way Selection: Marks -  Pass or Fail using If and else statement
# Multiway Selection: numbers - chances multiple - positive or negative or neutral number(0)(Grade in marks)  -  if/elif/else

# Iterations:
# While Loops: Execute a set of statement as long as the conditions remains True.
i = 0
while i<=3:
    print(i)
    if i == 4:
        break       # instead use continue to skip this specific condition
    i+= 1           # to False the while loop condition to stop the program execution.
# to Stop: break
# to Skip: continue

# Sequences: For loop used here.
l1 = [10,20,30,40,50]
for each_number in l1:      # character wise give output line by line
     print(each_number)

# Nested Loop: 'inner loop' is  executed one time for each item in the 'outer loop'.
colours = ['red', 'white', 'green']         # Outer Loop
transport = ['car', 'bike', 'cycle']        # Inner Loop

for each_color in colours:
    for each_vehicle in transport:
        print(each_color, each_vehicle)

# Assert Keyword: Test if a condition is True or False. if condition is False then it will be raise an assertion error.
# x = 'hello'
# assert x == 'hello'
# assert x == 'bye', 'x is not bye its hello'


# Functions: a block of code only execute when it is called.
# each object is based on a class is known as methods. (class 'str', class 'float')

#defining a function:

def greeting():
    print('hello World')

#calling a function:
# Functions are first class objects: if a function assigned to a variable.

greeting()

def multiply(x, y):
    return x * y
def apply(funct, x, y):
    return funct(x, y)

output = apply(multiply, 5, 2)
print(output)

# arbitrary Arguments: *n in parameter/argument to define the number of data in list, tuple and so on.
# a Function called inside the same function known as recursion.