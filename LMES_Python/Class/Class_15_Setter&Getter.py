# Setter and Getter:

class Product:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
p = Product()
p.set_name('Iphone')
print('The product is: ',p.get_name())