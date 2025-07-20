a = 'Selva is Great'
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.title())
print(a.capitalize())

# 'in' is a Membership Operator which helps to check substr characters in mainstr.

mainstr = 'Selva Eat Fruits'
substr = input('Enter a word: ')
if substr in mainstr:
    print('Present')
else:
    print('Not Present')