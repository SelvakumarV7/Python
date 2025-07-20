# Python Collections:
    # List
        # Square braces[]
        # Allows duplicate
        # Heterogeneous Values(Allows Multiple Datatypes)
        # Mutable (Data inside list is updatable(insert,replace,delete)
        # Indexing and slicing concept allowed
        # Modification allowed
        # Functions: insert(),append(),extend(),pop()

list = [1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]
list.insert(6,7)        # insert data in wherever need by index
print(list)
list.append(8)      # insert data in last of the list
print(list)
list.pop()          # removes last data
print(list)
list.pop(0)         # also remove data from selective index
print(list)
list.extend(list2)
print(list)         # Adds the new list into old one.