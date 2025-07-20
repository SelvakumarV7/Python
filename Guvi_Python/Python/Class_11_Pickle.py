# Pickle: to serialization(python object convert to memory) and deserialization process.
# to work with pickle with two modes.
    # Load: to load a data from a file
    # Dump: to dumb a particular file.

import pickle

# Serialization: dump()
result = {'a': 1, 'b': 2, 'c': 3}
with open('pickle.bin', 'wb') as f:
    pickle.dump(result, f)
    f.close()

# De-serialization: Load()
with open('pickle.bin','rb') as e:
    text = pickle.load(e)
print(text)
print()

# Seek() and Tell():

with open('trial.txt', 'r') as d:
    d.seek(5)                    # seek() - it starts to move content from index value where we provided
    print(d.tell())              # tell() - prints the start index and end index value of selected file.
    print(d.read())
    print(d.tell())

# Exercise:
f= None
for i in range(5):
   with open("data.txt","w") as f:
      if i>2:
          break
print(f.closed)

# directory control:
import os

os.remove('trail.txt')