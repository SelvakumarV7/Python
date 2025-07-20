# Tuples:
# Data can be enclosed with parenthesis.
# Immutable in Nature  --  No other values can be inserted, replaced, removed in the tuple list./ Changes in list is not possible.
# Tuples data are not changeable anytime.
# Insertion order is maintained/preserved.
# Duplicate values are allowed.
# Heterogeneous values are allowed(float, int, num, boolean).
# Indexing concept is allowed.
# Slicing concept is allowed.
# by default bracket missing means it considers as tuple.

a = 1,2,3,4,5,6
print(a)
print(type(a))
a1 = sorted(a)
print(a1)
a2 = sorted(a, reverse=True)  # descending order
print(a2)

t = (1,2,3,4,5,6,7)
print(t)
print(type(t))
print(len(t))
print(t[1])
print(t[1:5])
print(t.count(3))
print(t.index(7))
print(max(t))
print(5 in t)

t_1 = (10,20,30)
t_2 = (40,50,60)
print(t_1+t_2)
print(t_1*3)

# if we sort a tuple then it converted into list.

t1 = sorted(t)
print(t1)
print(type(t1))

Friend = ('Selva', 'Arul', 'Suren', 'Mani', 'Arun')
print(Friend)
f = sorted(Friend)
print(f)

