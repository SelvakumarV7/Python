# Examples:

class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def area(self):
        l = 10
        w = 5
        print(l*w)
r = Rectangle()
r.area()

class Person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name: ",self.name)

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
    def display(self):
        super().display()
        print("Grade: ",self.grade)

s = Student("Selva","A+")
s.display()

class Vehicle:
    def start(self):
        print("Vehicle Started.")
class Car(Vehicle):
    def start(self):
        print("Car Started")
c = Car()
c.start()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
        def __init__(self,name,salary,department):
            super().__init__(name,salary)
            self.department = department
        def display(self):
            print("Name: ",self.name)
            print("Salary: ",self.salary)
            print("Department: ",self.department)
m = Manager("Selva",70000,"IT")
m.display()