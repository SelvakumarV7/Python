# Dynamic/run time Polymorphism - Overriding - We have to access other classes through inheritance.
# It presents inside the different class(inherit).
# Types of overriding is same as Overloading but access via inheritance.

# Method Overriding:

class Parent:
    def display(self):
        print('From Parent Class/method')
class Child(Parent):
    def display(self):
        super().display()
        print('From Child Class/Method')
c = Child()
c.display()
print()

# Example:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
        print('Employee Name: ',self.name)
        print('Employee Age: ',self.age)
        print('Employee Number: ',self.eno)
        print('Employee Salary: ',self.esal)
e1 = Employee('Selva',30,123,60000)
print()
e2 = Employee('Niru',25,456,80000)