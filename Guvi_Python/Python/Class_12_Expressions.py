# Regular expression: (RegEx)

import re

text = 'Hello World! I am a Python Programming'
pattern = 'o'

a  = re.findall(pattern, text)
print(a)
print()

b = re.search(pattern, text)
print(b)
print(b.span())
print(b.group())
print(b.string)
print()

c = re.split(pattern, text, 2)
print(c)
print()

d = re.sub(pattern, '**', text, 2 )
print(d)
print()

# Exercise:
sentence='we are humans'
matched=re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())
print()

# *: Any number of times including zero
# +: Any number of times excluding zero
# ?: Exactly 0 or 1 time
# {n}: n number of times

# special sequences in expressions:
# \A,\b,\d,\D,\s,\S