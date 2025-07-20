word = "a1b2c3"
alpha = ''
number = ''
for i in word:
    if i.isalpha():
        alpha = alpha+i
    else:
        number = number + i
else:
    print(alpha+number)