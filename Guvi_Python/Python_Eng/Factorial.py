# Factorial

num = int(input("Enter a Number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(factorial)


#method 2:

def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
x = 4
result = fact(x)
print(result)