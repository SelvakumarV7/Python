# You are required to create a class to represent a rectangle with attributes like length and width. Write methods to calculate the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self,length,width):
        self.l = length
        self.w = width
    def area(self):
        print("Area: ", self.l * self.w)
    def parameter(self):
        print("Parameter: ", 2* (self.l + self.w))
r = Rectangle(5,3)
r.area()
r.parameter()

