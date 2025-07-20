# What are the problems facing when function not available:
# Debugging process is difficult.
# Code readability and understandability is difficult.
# Code reusability is difficult.
# Modularity(Split the different operation to separate members to reduce time)

# 'def' is a keyword.

def printname():   # printname() is a function call.
    print('Selva')
printname()   # Function call here only called so it return the output here only.

# Type 1:
# Function Without Argument and without return type:

def addition():
    a = 10
    b = 20
    print('The Sum is: ', a+b)
addition()

# IPO - Input Process Output.

# Type 2:
# Function With Argument and without return type:

def addition(a,b):  # (a,b) is the argument
    print('The Sum is: ',a+b)

addition(20,50)

# Type 3:
# Function without Argument and with return type:

def addition():
    a = 20
    b = 40
    return a+b
result = addition()
print('The Sum is: ', result)

# Type 4:
# Function with Argument and with return type:

def addition(a,b):
    return a+b
result = addition(50,60)
print('The Sum is: ' , result)

