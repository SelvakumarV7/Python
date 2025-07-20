# Example:

#Abstract Method: Definition in Parent class will also provide by Child class mandatory.
# It has a decorator "@abstractmethod"
# It does not have body only has pass.
# Default import name as 'from abc import *'
# abc - Abstract Base Class

from abc import *   #Abstract Base Class
class Fruit(ABC):   #abstract
    @abstractmethod
    def taste(self):
        pass
class Orange(Fruit):
    def taste(self):
        print('Orange is Tangy!')
class Mango(Fruit):
    def taste(self):
        print('Mango is Sweeet!')
o = Orange()
m = Mango()
o.taste()
m.taste()

# Example:

from abc import *
class Test(ABC):
    @abstractmethod             # Object has not created for abstract Method.
    def m1(self):               # If we didn't create a abstract method then object has created and it not showing any error.
        pass                        # But if we create abstract method inside a abstarct class then object has not been created and shows error


