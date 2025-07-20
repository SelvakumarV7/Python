# Union:

a = {10,20,30}
b = {40,50,60}
x = a.union(b)
print(x)

# Intersection:

q = {10,20,30,40}
w = {30,40,50,60}
e = q.intersection(w)
print(e)
print(q.difference(w))  # eliminates the common data in q & w and return the remaining data in q variable.
print(q.symmetric_difference(w))  # eliminates the common word in both variable and return the remaining data in both variable.
