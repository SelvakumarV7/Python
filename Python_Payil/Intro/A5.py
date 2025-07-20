# For Loop:Sequence

a = input("Enter email to find alphabets in mail: ")
for i in a:
    if i>='a' and i<='z':
        print(i,end='')
print()

# to find numbers in string:
a = input("Enter word with number to separate number:")
for i in a:
    if i>='0' and i<='9':
        print(i,end='')
print()
# to find word count:
b = input("Enter word to calculate: ")
count = 1
for i in b:
    if i == ' ':
        count+=1
else:
    print("Count of words is: ",count)

# to find sentence count:
c = input("Enter sentences to count: ")
count = 0
for i in c:
    if i =='.':
        count+=1
else:
    print("Count of sentence: ",count)

# Factorial:
d = int(input("Enter a number to factorial: "))
fact = 1
for i in range(1,d+1):
    fact = fact * i        # 1 * 1 = 1, 1 * 2=2,2*3=6,6*4=24
else:
    print("Factorial of ",d,'is: ',fact)

# Prime Number:
e = int(input("Enter a number to find Prime or Not: "))
for div in range(2,e):
    if e%div == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# Word range:
f = input("Enter a word to split: ")
for i in range(len(f)):
    print(f[i],end='')
print()

# Word reverse:                         #  01234 = 5(no 5 so -1), end at last value index 0 so -1 means stops at 0 th index,reverse so -1
g = input("Enter word to reverse: ")    #   5-1=4 ,  end, reverse
for i in range(len(g)-1,-1,-1):         # len(g)-1,  -1,    -1
    print(g[i],end='')
print()

# Nested Loop:
for i in range(1,6):
    for j in range(1,6):
        print(i, end=' ')
    print()

# Nested Loop for reverse print:
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end=' ')
    print()

# for digit reduction(pyramid):
for  col in range(6,0,-1):
    for row in range(1,col):
        print(row,end=' ')
    print()

# same number pyramid:
n = 1
for i in range(5,0,-1):
    for j in range(i):
        print(n, end=' ')
    print()
    n+=1
print()

# Word Pyramid:
name = input("Enter the name to pyramid: ")
count = len(name)
for i in range(1,count+1,1):
    for j in range(i):
        print(name[j], end=' ')
    print()
print()

# Pyramid:
name = input("Enter the name to pyramid: ")
total = len(name)
for i in range(total,-1,-1):
    for j in range(i):
        print(' ',end=' ')
    for j in range(total-i):
        print(name[j], end=' ')
    print()