# String Datatype:

a = "Today is Tuesday"
for i in a:
    print(i, end=' ')
print()

l = len(a)
print(l)
for i in range(l):
    print(a[i], end=' ')
print()

for i in a[::]:
    print(i,end=' ')
print()

# reverse Print:

for i in a[::-1]:
    print(i, end=' ')
print()

for i in range(l-1,-1,-1):
    print(a[i], end=' ')
print()

k = l-1
while k>=0:
    print(a[k],end=' ')
    k-=1

print()
# Check word in sentence:
sen = input("Enter sentence to find word in it: ")
word = input("Enter the word to find in sen: ")
if word in sen:
    print("Word is present")
else:
    print("Word is not present")

# string methods:
b = input("Enter words with space front & back: ")
b = b.strip()           # remove space at start and end
print(b)

# find:
c = "Python Django Flask"
print(c.find("Django"))         # if available show the start index value of text
print(c.find("Flask",10,15))    # if not available the respective text then it shows false
print(c.rfind("Django"))        # reverse find

# using find function:
a = input("Enter word to find character: ")
word = input("Enter a character to find: ")
l = len(a)
index = 0
count = 0
while True:
    index = a.find(word,index,l)
    if index == -1:
        print("Word not found")
        break
    else:
        print("Given character presented at: ", index)
    index+=1
    count+=1
print("Count of character is: ",count)
print()