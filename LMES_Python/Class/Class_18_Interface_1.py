# A program is completely pure abstract class then it is Abstract class or Interface.
# in Abstract class main class of abstract no need to execute it tends to error.

# Example:
from abc import *
class Animal(ABC):
    @abstractmethod
    def foodhabit(self):
        pass
class Carnivorous(Animal):
    def foodhabit(self):
        print('Lion eats only flesh, so its carnivorous')
class Herbivorous(Animal):
    def foodhabit(self):
        print('Cow eats only plant, so its herbivorous')
class Omnivorous(Animal):
    def foodhabit(self):
        print('Beers eats only flesh and plants, so its omnivorous')
C = Carnivorous()
H = Herbivorous()
O = Omnivorous()
C.foodhabit()
H.foodhabit()
O.foodhabit()