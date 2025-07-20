# Classes and Objects:
    # __init__      -->  Constructor: It is a unique function that gets called automatically when an object is created.
    # self          -->  Constructor: Main purpose is to assign values to the data members of that class.
from tkinter.font import names


class Laptop:
    name = ''
    processor = ''
    ram = ''
    price=''

dell = Laptop()
hp = Laptop()

hp.name = "Name: HP Pavilion"
hp.price = {"Price: ":50000}
print(hp.name)
print(hp.price)

class Student:
    def __init__(self,name,register):
        self.name = name
        self.register = register
    def display(self):
        print("Name: ",self.name)
        print("Register No: ",self.register)
s1 = Student("Selva",12345)
s2 = Student("Niru",56789)
s1.display()
s2.display()

class Fruit:
    def __init__(self,color):
        self.color = color
Apple = Fruit("Red")
print(Apple.color)

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def display(self):
        print("Name: ",self.name)
        print("Subject: ",self.subject)
t1 = Teacher("Selva","Maths")
t2 = Teacher("Niru","Science")
t1.display()
t2.display()

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        print("Sum: ",self.a+self.b)
    def sub(self):
        print("Sub: ",self.a-self.b)
    def mul(self):
        print("Mul: ",self.a*self.b)
    def div(self):
        print("Div: ",self.a/self.b)
c = Calculator(5,2)
c.sum()
c.sub()
c.mul()
c.div()