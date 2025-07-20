# File Handling:
# open(filename, mode)
# mode:
    # r(default)  -  Read
    # a: append
    # w: Write
    # x: Create

#f = open('trial.txt', 'x')      # to create a new file
#f.close()

with open('trial.txt', 'w') as w:       # 'with' function always close this fn automatically.
    w.write('This is test of with function.')

with open('trial.txt', 'a') as a:       # append statment
    a.write('\nAppend statement is added.')

with open('trial.txt') as r:        # read statement
    text = r.read()

print(text)
print()


