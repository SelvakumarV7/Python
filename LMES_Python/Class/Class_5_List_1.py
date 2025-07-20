# Data enclosed within a square bracket is List
# Values are separated by comma
# Insertion Order: Input order is maintained/preserved.
# Duplicate values: Repeated values/data are allowed in List.
# Heterogeneous Values: Allows multiple data types(string,float,int,boolean)
# Mutable: Data's in list are updatable(insert, delete, replace)/changes in list is possible
# Indexing Concept: Indexing also allowed in list
# Slicing concept: it also allowed(1:2).
# to add a value: append(), Insert().
# to remove: pop(), remove().

a = [1,2,3,4,5,6,7,2,3,4,5,6]
print(a)
print(len(a))   # count the number of data in list

print(a.count(5))  # to count the occurance of specific data in a list.
print(a.index(7))  # to find the index position of a data value but it return the first occurance of value.
a.append(8)   #append: adds the data in a list at last place.
print(a)
a.insert(7,8)  # it adds the data in mentioned indexing position
a.pop()  # it removes the last value in a list.
print(a)
a.remove(1) # it removes the mentioned value in first occurance.
print(a)
a.reverse()  # it revere the data in a list.
print(a)
a.sort()  # ascending order the data in a list.
print(a)
a.sort(reverse=True)  # descending order the data in a list.
print(a)
print(7 in a)
print(1 not in a)

a_1 = [10,20,30]
a_2 = [40,50,60]
print(a_1+a_2)   # + - Concatination Operator which adds the variables.
print(a_1*3)  # it thrice the values in a mentioned variable not multiplies.