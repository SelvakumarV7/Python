# OOPS: Object Oriented Programming System
# known as implementation of classes and objects.

# Create a Class

class Customer:
    # Class Attributes(Variables)
    bank_name = 'ABCD Bank'

    # Methods(Functions)
    def greet(self):
        print("Welcome to ABCD Bank")

# Create a Object
c1 = Customer()
c1.greet()


class Bank:
    def __init__(self, name, age, initial_amount):
        self.name = name
        self.age = age
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of {amount} is successful. Balance is {self.balance}.')
b1 = Bank('Selva',30,50000)
b2 = Bank('Niru',25,40000)
b1.deposit(5000)
b2.deposit(7000)
print()

# Encapsulation: Protection of data.

class Car:
    __price = 50000         # Encapsulate by '__' before the variable. '__' Makes private and '_' makes protected of variable.

    def display_price(self):
        print(f'{self.__price} is the price of the Car.')

c = Car()
c.display_price()
print()

# Inheritance:"To achieve the concept of code reusability."
# Types:
    # Single level = 1 Parent and 1 Child
    # Multiple level = 2 Parent and 1 Child
    # Multi level  =  1 Grand Parent and 1 Parent and 1 Child
    # Hierarchical  =  1 Parent and multiple child
    # Hybrid  =  combination of two or more type of inheritance.

class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Child(Parent):
    def __init__(self,name,age,school):
        Parent.__init__(self,name,age)
        self.school = school
obj = Child('selva',30,'SVN')
print(obj.name)
print(obj.age)
print(obj.school)
