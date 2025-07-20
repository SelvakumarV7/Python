# Sets: curly brackets{}.
# unordered, unchangeable, and not allowed duplicates.

s1 = {'A','B','Orange',10,20,520}
s2 = {'Orange',10,20,'Sweet'}
print(s1)

s1.discard('selva')     # it not shows any error while the data not in sets.
print(s1)

s1.remove(520)
print(s1)
print()

#s1.clear()          # remove all data inside the sets.
#print(s1)

s3 = s1.union(s2)       # shows data except the common repeated values.
print(s3)

s4 = s1.intersection(s2)    # shows only the common values
print(s4)

s5 = s1.symmetric_difference(s2)    # exclude the common values and shows remaining data
print(s5)