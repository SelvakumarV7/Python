# Armstrong Number:(sum of the cubes of three numbers as result of same number) eg. 371 = 3**3 + 1**3 + 7**3 = 371
n = int(input("Enter to find a armstrong number: "))
total = 0
arms = n
while n>0:
    dig = n%10      # 371 means 1
    cube = dig**3      # 1*1*1
    total = total + cube    # 0+1=1
    n = n//10           # 37
else:
    if total == arms:
        print("Number is Armstrong")
    else:
        print("Not a Armstrong")

#Decimal to Binary value find:

n1 = int(input("Enter a decimal value to find Binary Value: "))
binary = ''
while n1>0:
    rem = n1%2
    binary = str(rem) + binary
    n1 = n1//2
else:
    print(binary)

# Binary to Decimal conversion:
# import math
# binary = int(input("Enter Binary value to convert Decimal: "))
# total = 0
# count = 0
# while binary>0:
#     last = binary%10        #123.4

# Nested loop:
row = 1
while row<=5:
    for i in range(5):
        print(row,end=' ')
    print()
    row+=1