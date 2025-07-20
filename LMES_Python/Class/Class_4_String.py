#indexing concept:

#s = 'Selva' for left to right indexing -- s[0] = S, s[1] = e, s[2] = l and so on.
#s = 'Selva' for right to left indexing -- s[-1] = a, s[-2] = v, s[-3] = l and so on.

#string Slicing:
#Slice = a Small portion which is mentioned in ':' colon.
#s = 'Selva'
#print(s[1:4]) = elv

s = 'selva'
print(s[1:4])
print(s[:3])
print(s[1:])
print(s[-1])
print(s[0:5:2])    #here '2' is step counter

a = 'learning python is easy'
print(a[1:7:2])    #earning - #eri
print(a[5:12:2])   #ing python  - #igpt
print(a[::-1])
print(a[:])