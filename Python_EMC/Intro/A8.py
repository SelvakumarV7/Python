# Polymorphism: Having many forms | Same function Name being used for types.

class Animal:
    def sound(self):
        print("Animal Makes sound.")

class Dog(Animal):
    def sound(self):
        print("Dog Barks.")

class Bird(Animal):
    def sound(self):
        print("Birds Sing.")

d = Dog()
d.sound()
b = Bird()
b.sound()