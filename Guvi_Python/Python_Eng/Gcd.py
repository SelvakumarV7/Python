# Greatest Common divisor

a = 12
b = 18
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)