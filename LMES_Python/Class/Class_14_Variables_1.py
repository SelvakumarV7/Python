# Types of Variables:
    # Instance variable or Object level variable
    # Static variable or Class level variable
    # Local variable or Method level variable


# 'self' - use this keyword then it is known as instance variable. it refers the respective object.

# Instance Variable: we use this method at object to object changes only i.e., the customers end.

class Student:     #Class
    def __init__(self,name,age):    # constructor: default name - __init__
        self.name = name            # instance variable
        self.age = age

    def display(self):              # instance method - to access the instance variable.
        print('Name: ', self.name)
        print('Age: ', self.age)

s1 = Student('Selva', 30)
s2 = Student('Niru', 25)
s1.display()
s2.display()

# Static Variable: - we use this method at common object names like bank name and so on.

class Customers:
    bankname = 'SNH Bank'

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    @classmethod
    def details(cls):
        print('Bank name is: ', cls.bankname)
    def display(self):
        print('Name: ', self.name)
        print('Balance: ', self.balance)

c1 = Customers('Selva', 10000)
c2 = Customers('Niru', 20000)
c1.display()
c2.display()

print('Bank name: ', Customers.bankname)
print('Bank Name: ', c1.bankname)
c2.bankname = "SHN Bank"  # Bank name/static variable can be permanently change by using the class name only. Here, Object nae not change the static variable(bankname).
Customers.bankname = "SNH Bank"
print('Bank name: ', c2.bankname)

# Local Variable: we use this method by temporarily calculating the variables.

class Calculator:
    @staticmethod       # we use this by acessing the output for local variable.
    def addition():
        a = 10     # local variable: which is used only inside this method that's y it is local variable.
        b = 20
        print('Sum of a & b is: ',a+b)

c = Calculator()
c.addition()