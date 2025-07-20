# Inheritance: making relationship between two classes. "To achieve the concept of code reusability."
    # making parent and child class to make a connection between two classes.

class First:        # Parent class: it will always above the child class, it arrives first.
    def method_1(self):
        print('First Class')
class Second(First):   # we use the class First here, so it is Child Class.
    def method_2(self):
        print('Second Class')
f = First()
f.method_1()
# f.method_2()    #Parent class not access the child class it access only the parent class.

s = Second()
s.method_1()        # Child class wil access both parent class as well as child class
s.method_2()

# Example 2:

class Parent:
    def property(self):
        self.properties = 'Home, Car, Jewels'
    def source(self):
        self.source = 'Salried'
    def display(self):
        print("Parent Properties: ", self.properties)
        print("Parent Source: ", self.source)
class Child(Parent):
    def property(self):
        self.properties = 'Home, Car, Shares'
    def source(self):
        self.source = 'Trading'
    def display(self):
        #super().display()      # Call the display fn in Parent class.
        print("child Properties: ", self.properties)
        print('Child Source: ', self.source)

p = Parent()
p.property()
p.source()
p.display()
c = Child()
c.property()
c.source()
c.display()