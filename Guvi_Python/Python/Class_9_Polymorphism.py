# Polymorphism: Method resolution order.(C3 algorithm) -->DFS(Depth First Search) & LTR(Left TO Right)  and BFS(Base First Search).
# Overloading: if the funtion names are same but the arguments are different so it provides all output.
# Overriding: if multiple function are having a same name and parameter then its overriding the latest one.
# Duck Typing: Behaviour of an Object.

def add_number(a, b):
    return a + b
print(add_number(10, 20))
print(add_number('Selva ', 'Niru'))
print()

# Errors and Exception:
# If we break the Rules in python that gives Errors.(Syntax Error).
# If we break the logic in python which is Exception(Logical errors). We will handle these errors.
# From the whole program first it checks the syntax error then only it shows the logical errors.

#eg. for syntax error:
# print('selva)   # if missing quotes ends with syntax error

# eg. for logical error:
# print(x)        # we missed the value of x makes exception error which is logical error.

# To handle Errors by following:
# try...except....else...finally

print('Errors & Exceptions:')
try:
    print('Selva')
except:
    print('If error Occurs')
else:
    print('If no error Occurs')
finally:
    print('Anything Happens above but mandatory try block.')
print()

print('Exception Handling:')
class Invalidnumber(Exception):
    pass

x = int(input('Enter a number within range of 0 to 10: '))
if 0 <= x <= 10:
    print('Given number is Valid.')
else:
    raise Invalidnumber('Given value is not in range between 0 to 10.')
