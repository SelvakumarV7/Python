# Dictionaries: dict().
# {key:value}
# Ordered, changeable, allow duplicates, but keys not duplicate here.

d1 = {'Name': 'Selva',
      'Age': 30,
      'Married': True,
      'Car': 'VW'}
print(d1)
print(d1['Name'])
print(d1.keys())
print(d1.values())
print(d1.items())
d1['Car'] = 'BMW'
print(d1)
d1.update({'Age': 29})
print(d1)
d1['car color'] = 'Blue'
print(d1)
d1.update({'Car Regd': 2030})
print(d1)


print()




l1 = [(1,'a'),(2,'b'),(3,'c')]      #if a list convert to dict means it contains keys and values inside a tuple within list.
d2 = dict(l1)
print(d2)
print()


keys = [1, 2, 3]
values = ['a', 'b', 'c']
d3 = dict(zip(keys, values))
print(d3)
print()

count={}
count[(1,2,4)] = 5
count[(4,2,1)] = 7
count[(1,2)] = 6
count[(4,2,1)] = 2
tot= 0
for i in count:
    tot=tot+count[i]        # 0+5 = 5, 0+6 = 6, 0+2 = 2 tot = 13
    print(tot)
print(len(count)+tot)       # 3 + 13 = 16
print()

a={i: i*i for i in range(6)}
print(a)
print()

d5 = {'a': 2, 'c': 4, 'b': 1,'d': 3}
x = dict(sorted(d5.items()))            # sort by Key
print(x)

y = dict(sorted(d5.items(), key=lambda item: item[1]))      # sort by values
print(y)
print()

def f1(d):          # using function
    for key, val in d.items():
        print(key, val)
f1(d5)