# to print numbers only from object:

email = input("Enter email: ")
length = len(email)
i = 0
count = 0
while i<length:
    if email[i]>='0' and email[i]<='9':
        print(email[i])
        count+=1
    i+=1
print("Integer count in email is: ",count)

name = input("Enter your name: ")
length = len(name)
i = 0
count = 0
while i<length:
    if name[i] in ['a','e','i','o','u']:
        print(name[i])
        count+=1
    i+=1
print("Count of vowels in name is: ",count)

# choice:

choice = ''
total = 0
while not choice == "no":
    mark = int(input("Enter Mark: "))
    total = total + mark
    choice = input("Type no to stop calculate")
else:
    print("Total mark is: ",total)

# find divisor:
div = 1
no = 120
while div<=no:
    if no%div == 0:
        print(div)
    div+=1

# Common Divisor:

n1 = 100
n2 = 150
div=2
if n1<n2:
    small = n1          # another method to find small value: small= n1 if n1<n2 else n2
elif n2<n1:
    small = n2
while div<=small:
    if n1%div == 0 and n2%div ==0:
        print(div)          # instead last = div is the Greatest common divisor.
    div+=1

# LCM(Least common Multiples):
n1 = 3
n2 = 7
big = n1 if n1>n2 else n2
while True:
    if big%n1==0 and big%n2==0:
        print("LCM is: ",big)
        break
    big+=1

# Prime or not:

a = int(input("Enter a number: "))
div = 2
while div<a:
    if a%div == 0:
        print("Not Prime")
        break
    div+=1
else:
    print("Prime")

# Fibonacci Series:

f = 0       # if it is -1 then print statement before while no need
s = 1
count = 1
print(f)
print(s)
while count<=5:
    t = f+s
    print(t)
    f = s
    s = t
    count+=1

# Fibonacci value find and stop:
f = -1
s = 1
# count = 1
while True:
    t = f + s
    print(t)
    if t == 34:
        break
    f=s
    s=t
    # count+=1

# to print reverse:
bread = int(input("Enter number to reverse: "))     # 1234
while bread>0:
    print(bread%10,end='')     #123.4  --  4 is the answer
    bread = bread//10   # 123

bread = int(input("Enter number to reverse and count: "))
count = 0
while bread>0:
    print(bread%10)
    bread = bread//10
    count+=1
else:
    print("Count is: ",count)

# Addition of digits:
bread = int(input("enter number for digit Sum: "))
count = 0
total = 0
while bread>0:
    total = total + bread%10
    bread = bread//10
    count+=1
else:
    print("Count of digits separate: ",count)
    print("Sum of the Given Digit is: ",total)

# To reverse without space and sum:
bread = int(input("Enter number to Reverse without space and sum: "))
total = 0
while bread>0:
    total = (total*10) + bread%10        # answer 4
    bread=bread//10
else:
    print("Reversed numbers are: ",total)

# Palindrome b/w numbers:
bread = int(input("Enter number for palindrome: "))
rev = 0
pal = bread
while bread>0:
    rev = (rev*10) + bread%10
    bread = bread//10
else:
    print("Reverse number is: ",rev)
    if rev == pal:
        print("Palindrome number")
    else:
        print("Not Palindrome number")