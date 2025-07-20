# Dictionary:
    # Curly braces{}
    # Key and value pair
    # Mutable
    # Duplicate values are overwrite
    # Functions: get(), keys(), values(), update(), clear(), del(),


a = {'Name': "Selva",'Age':30,'City': "Salem"}
print(a.keys())
print(a.values())
print(a["Age"])
a['Age'] = 29
print(a['Age'])
a["Cuteness"] = "Sweet"
print(a['Cuteness'])
a.update({'Age':30})
print(a['Age'])
print(a)