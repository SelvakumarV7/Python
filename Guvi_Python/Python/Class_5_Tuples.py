# Tuples: Round Brackets
# Items are ordered, Immutable(datas are not changeable), allow duplicates
T=tuple("tuple")
print(T)
print()

t1 = ('A','B','C','D','E','F')
print(t1)
a,b,*c = t1         # * - assign the remaining data to the respective variable.

print(a)
print(b)
print(c)
print()

*a, b,c = t1            # for b & c last two values assigned and remaining front values assign for * variable(a).

print(a)
print(b)
print(c)

t2 = (10,20,40,50,60,30)
t3 = sorted(t2)
print(t3)

tup_1 = (5,4)
tup_2 = (1,6)
nested = tup_1 + tup_2
print(str(nested))