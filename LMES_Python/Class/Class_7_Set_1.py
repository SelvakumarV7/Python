# SET:
# Data should be enclosed with Curly/Braces Brackets.
# Insertion Order is not Maintained/not Preserved.
# Duplicate/Repeated Values are not Allowed.
# Heterogeneous Values are allowed(diff. data types allowed, float, string, boolean, int).
# Mutable in Nature(data can be added, replace, remove and so on).
# to add a value: add(), update().
# to remove a value: pop(), discard() - it not showing an error if data not available in set., remove().


s = {1,2,3,4,5,4,3,2,1}
print(s)

# How to remove a duplicate values in  a list:

List = [1,2,3,4,5,6,5,1,2,3,4]
print(List)
Set = set(List)
print(Set)
print(type(Set))
List = list(Set)
print(List)
print(type(List))

#as same of tuples:

t = (1,2,3,4,5,4,3,2,1)
print(t)
s = set(t)
print(s)
print(type(s))
t1 = tuple(s)
print(t1)
print(type(t1))
