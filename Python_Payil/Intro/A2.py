no = 10
name = 'Selva'
no2 = 123.456
print(type(no))
print(id(no))
print(len(name))
print(round(no2))
print(round(no2,2))
print(round(no2,3))

# binary Form(Int):
n = 0b1001      # gives binary values after 0b
print(n)
n1= 0B0101
print(n1)

# Octal Form: which provides octal value limit from 0-7.
n2 = 0o566      # use o or O after zero first value.
print(n2)

# Hexadecimal Form: gives hexa value from 0-9,A,B,C,D,E,F
n3 = 0X896      # use x or X for hexa value finding
print(n3)

n4 = bin(20)
print(n4)
n5 = oct(20)
print(n5)
n6 = hex(20)
print(n6)
n7 = 7.7e3      #e3 - 10^3
print(n7)

print(True+True)        # 1 + 1
print(True+False)       # 1 + 0
print(False+False)      # 0 + 0
print(int(True))        # Casting

# immutability:
n1 = 10
print(id(n1))
n2 = 10
print(id(n2))
n2 = 20
print(id(n2))
print(n1 == n2)     # it compares the value of the variables(equality operator)
print(n1 is n2)     # it compares the id of the variables(identify operator)

# Byte:
value = [10,20,30,40,50]
print(value)
value = bytes(value)
print(value)
print(type(value))
print(value[0])
print(value[-2])
total = 0
for i in value:
    print(i)
    total = total + i
print(total)
# Lexicographical Order: Dictionary order
a = 'selva'     # alphabetical order wise it is small
b = 'sweet'     # alphabetical order wise it is large
print(a>b)
print(a<b)

# escape character:(\)
print("Hi Hello")
print("Hi \t Hello")        # tab space
print("Hi \n Hello")        # new line
print('I\'m Fine')           # escape character which helps to avoid the between quote.

# Ternary Operator(Conditional Operator):
n1,n2 = 10,20
n3 = 30 if n1<n2 else 40        # ternary Operator
print(n3)

# membership Opr:

c = 'Today is Wednesday'
print('Today' in c)
print('h' in c)

# Operator Chaining:
print(100<200<300)
print(100<500<400)

# Bitwise Operator:

print(4&5)      # & makes multiplication of their binary values, binary value of 4 = 0100, 5 = 0101 0100*0101=0100 == 4
print(4|5)      # | makes addition of their binary values
print(4^5)      # ^ XOR, that is if both binary value same means its 0, different means 1
print(~10)      # ~ Bitwise Compliment Operator - which makes - symbol infront and adds with 1.
print(10<<2)    # 8 bit binary values moves twice to left and multiply with it 2^.... to find value
print(40>>2)    #  8 bit binary values moves twice to right and multiply with 2^.... to find value

# Function:
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
def biggest(n1,n2):     # n1,n2 are arguments
    if n1>n2:
        print(n1,"is Greater than ",n2)
    else:
        print(n2," is Greater than ",n1)
biggest(n1,n2)      # Function calling Statement

# print(help('modules'))      # to show built in modules.

# eval function:

expression = input("Enter expression: ")
print("first: ",expression)
expression = eval(expression)
print("Second: ",expression)

# Output statements:

n1,n2,n3,n4 = 10,20,30,40
print(n1,n2,n3,n4,sep="/")  # used to sep the each variable
print(n1,n2,n3,n4,end="/")  # used to place the respective character at end
print("Selvakumar",end=" ")
print("Niru")

# formatting strings:

a = 10
print("Value of a is %i" %a)
print("Value of a is %d" %a)

name = 'Selva'
city = 'Salem'

print("Your name is {0} and you are from {1}".format(name,city))
print("Your name is {a} and you are form {b}".format(a=name,b=city))

# Iteration:

mind = 7
while True:
    guess = int(input("Enter any number between 1 to 10: "))
    if guess == mind:
        print("Guess is Correct")
        break
    elif guess>mind:
        print("Guess is large")
    else:
        print("Guess is small")

count = 1
while count<=10:
    print(count, end=' ')
    count+=1

count = 5
while count>=1:
    print(count, end=' ')
    count-=1

count = 50
while count>=1:
    if count%5 == 0:
        print()
    print(count,end = ' ')
    count-=1

count = 1
while count<=31:
    if count%3 == 0:
        print(count)
    count+=1