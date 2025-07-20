# Methods:
    # Instance Method - to access instance variable
    # Class Method - to access static variable
    # Static Method - to access local variable

# Instance Method:

class  Student:

    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def display(self):
        print('Name: ', self.name)
        print('Mark: ', self.mark)
    def grade(self):
        if self.mark >=80 and self.mark == 100:
            print('A Grade')
        elif self.mark >= 60 and self.mark < 80:
            print('B Grade')
        elif self.mark >= 40 and self.mark < 60:
            print('C Grade')
        else:
            print('Fail')
n = int(input('Enter the number of Students: '))
for i in range(n):
    name = input('Enter the Student Name: ')
    mark = int(input('Enter the Student Mark: '))
    s = Student(name,mark)
    s.display()
    s.grade()
    print()


# Class Method:

class Animal:
    legs = 4
    def method1(self):
        print(self.legs)
    @classmethod            # Decorator
    def details(cls,name):
        print('{0} has {1} legs'.format(name,cls.legs))
a = Animal()
a.details('Cow')
a.details(('Dog'))
a.details(('Horse'))
a.method1()


# Static Method:

class Calculator:
    @staticmethod
    def addition():
        a = 10
        b = 20
        print('Sum is: ',a+b)
c = Calculator()
c.addition()