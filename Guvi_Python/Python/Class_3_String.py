# Strings:
# Strings are immutable(Original string not changed)


a = 'Hello'
b = 'World'

print(a, b, sep ='\n')
print()

# String Methods:

c = 'SelvaKumar'
d = c.startswith('Selva')       # check whether the string starting words are True or False
print(d)
print()

e = c.endswith('Kumar')
print(e)
print()

f = 'Selva studying Python'
g = f.split()       # gives list of words in the input into a list
print(g)
print()

print(f.split(' ',1))
print()

print(f.rsplit(' ',1))
print()

print(f.find('l'))
print(f.index('a'))     # to find the index of string
print()

h = ['A','B','C','D','E']
print(' '.join(h))
print('--'.join(h))
print()

# Format method: Takes an argument and places it where there are placeholder {}.
# Method 1:

age  = 31
school = 'ABCD'
text = 'I am {} years old. I study in {}'
print(text.format(age, school))
print()

# Method 2:

text2 = 'I am {} years old. I study in {}'.format(age, school)
print(text2)
print()

# Method 3:

text3 = f'I am {age} years old. I study in {school}'
print(text3)
