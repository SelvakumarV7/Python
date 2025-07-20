# Nested list = Matrix in Maths
a = [10,20,[30,40]]  # List inside another list is nested list. [30,40] is the nested list.
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[2][0])
print(a[2][1])

b = [[10,20,30],[40,50,60],[70,80,90]]
print(b)
print(len(b))
for i in b:
    print(i)

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j],end=' ')   #to print in matrix format
    print()