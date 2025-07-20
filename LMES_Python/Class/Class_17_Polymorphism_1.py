# Polymorphism: Same thing happened in multiple places.(1 person act as different character like person as husband,father,son and so on.)
# It is the ability to use a single type of entity, such as an object, method, or operator, to represent multiple types in different contexts.
# The ability of a single function or method to work with different types of data.
    # Static Polymorphism or Compile time Polymorphism
    # Dynamic Polymorphism or Run time Polymorphism

# Static/Compile time Poly: - Overloading:
    # Operator Overloading
    # Method Overloading
    # Constructor Overloading

# Operator Overloading: An Operator will do 2 or more operations.
# Operator overloading not in Java but available in Python, C++

a = 10
b = 20
print(a+b)  # here addition will takes place
a = '10'
b = '20'
print(a+b)  # here Concatination will takes place

# Method Overloading: Last method within a class is only supported/allowed remaining methods are not allowed that takes error.
# 1 or more methods in same name but number of arguments different.
# Java and C++ allowed Method overloading but Python not supported it only support last defined method is considered.

class Test:
    def m1(self):
        print('no Arguments/First method')
    def m1(self,a):
        print('1 argument/second method')
    def m1(self,a,b):                       # Last defined method only considered.
        print('2 argument/third method')
t = Test()
#t.m1()
#t.m1()
t.m1(30,50)

# Constructor Overloading: Same as Method Overloading(supports only the last defined constructor function).
# Python Not support Constructor overloading but Java, C++ support constructor overloading.

class CO:
    def __init__(self):
        print('1')
    def __init__(self,a):
        print('2')
    def __init__(self,a,b):
        print('3')
#C = CO()
#C1 = CO(1)
C2 = CO(3,4)        # Lat defined function only considered/Supported.

# Example:

class Bill:
    @staticmethod
    def totalbill(*n):
        total = 0
        for i in n:
            total+=i
        print(total)
b = Bill()
b.totalbill(1,2,3,4,5)
b.totalbill(10,30)