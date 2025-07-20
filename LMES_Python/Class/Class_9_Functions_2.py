# Arguments:
# Positional Arguments:

def display(name,age):
    print('Name: ', name)
    print('Age: ', age)
display('Selva',30)   # name and age are the mention the position.

# Named Arguments:

def display(name,age):
    print('Name: ', name)
    print('Age: ', age)
display(age = 25, name = 'Niru')  # age and name is changed the position and defines the name(variable).

# Default Arguments:

def display(name,salary = 20):   # salary has default value provided.
    print('Name: ', name)
    print('Salary: ', salary)
display('Selva')
display("Niru", 50)

# Variable Arguments:

def addition(*n):  # multiple numbers are available inside the '*'.
    sum = 0
    for i in n:
        sum+=i
    print('The sum is: ',sum)
addition(0)
addition(10,20)
addition(30,40,50)
addition(60,70,80,90)