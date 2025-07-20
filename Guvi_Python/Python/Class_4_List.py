# Datatypes:
# List: Square Brackets
# Ordered, Changeable, Allow duplicates
l1 = list(range(11))
print(l1)
l2 = list(range(0,11,2))
print(l2)
l=[1,2,3,4,5,6,7,8]
print(l[::-2])
l3 = ['Cherries', 'Banana', 'Apple', 'Orange', 'apple']
l3.sort()
print(l3)
l3.sort(key=str.lower)      # to sort the lower case word as alphabetical order
print(l3)

l=[1,2,3,4,2,1,3,5,9,1]
c=0
for i in l:
    if(i==1):
        c+=1
print(c)

t = l.copy()
print(t)

l=[1,2]
t=l.copy()
l[1]=5
print(t)

Mat1 = [[11, 12, 13],
[14, 15, 16],
[17, 18, 19]]
Mat2 = [[21, 22, 23],
[24, 25, 26],
[27, 28, 29]]
sum12 = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
for i in range (len (Mat1)):
    for j in range (len (Mat1 [0])):
        sum12 [i][j] = Mat1 [i][j] + Mat2 [i][j]
for i in sum12:
    print (i)

l = [["a","b","c"],["d","e","f"],["g","h","i"]]
print(l[1:][1])

# List Comprehension:  to reduce number of lines of code.

names = ['Selva', 'Niru', 'Hevanthika']
names_with_a = [i for i in names if 'a' in i]
print(names_with_a)

# nested list comprehension:

matrix = [[y for y in range(4)] for x in range(4)]
print(matrix)

print(ord('i'))