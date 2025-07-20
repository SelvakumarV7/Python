# Parent Class or Super Class or Base Class.
# Child Class or Sub Class or Derived Class.
# Types of inheritance:
    # Single Level Inheritance   -  1 Parent and 1 Child
    # Multi Level Inheritance    -  Grand parent, Parent, and child
    # Multiple Inheritance       -  2 Parents and 1 child
    # Hierarchical Inheritance   -  1 Parent and multiple Childs's
    # Hybrid Inheritance         -  Combination of any 2 type of inheritances
    # Cyclic Inheritance

# Single Level Inheritance:

class Parent:
    def m1(self):
        print('parent class')
class Student(Parent):
    def m2(self):
        print('child class')
s = Student()
s.m2()
s.m1()
print()

# Multi Level Inheritance:

class Grand_parent:
    def m1(self):
        print('grand Parent')
class Parent(Grand_parent):
    def m2(self):
        print("Parent Class")
class Child(Parent):
    def m3(self):
        print('Child Class')
c = Child()
c.m3()
c.m2()
c.m1()
print()

# Multiple Inheritance:

class Parent1:
    def m1(self):
        print('Parent 1')
class Parent2:
    def m2(self):
        print('Parent 2')
class Child(Parent1, Parent2):
    def m3(self):
        print('Child Class')

c = Child()
c.m1()
c.m2()
c.m3()
print()

# Hierarchical Inheritance:

class Parent:
    def m1(self):
        print('Parent Hierarchical')
class Child1(Parent):
    def m2(self):
        print('Child Class 1')
class Child2(Parent):
    def m3(self):
        print('Child Class 2')
class Child3(Parent):
    def m4(self):
        print('Child Class 3')
c = Child1()
c.m2()
c.m1()
c2 = Child2()
c2.m1()
c2.m3()
c3 = Child3()
c3.m1()
c3.m4()
print()
