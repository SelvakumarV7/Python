# Inheritance Examples:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
class Student(Person):
    def __init__(self,name,age,roll_no,mark):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.mark = mark
    def display(self):
        super().display()
        print('Roll No: ',self.roll_no)
        print("Mark: ",self.mark)
s1 = Student('Selva',30, 13546, 99)
s2 = Student('Niru', 25, 12345, 100)
s1.display()
print()
s2.display()

