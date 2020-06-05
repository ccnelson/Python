
class root():
    def __init__(self, key):
        self.key = key

class Animal(root):
    def __init__(self, key, hair):
        root.__init__(self, key)
        #super().__init__(key)
        self.hair = hair
    pass

class Vegetable(root):
    pass

class Mineral(root):
    pass

class Dog(Animal):
    def __init__(self, key, hair, breed):
        Animal.__init__(self, key, hair)
        #super().__init__(hair)
        self.breed = breed

x = root(0)
y = root(1)

print(x.key)
print(y.key)





z = Animal(2, "black")
a = Vegetable(3)
b = Mineral(4)

#c = Dog(4, "browny", "woofo")

print(z.key)
print(a.key)
print(b.key)

c = Dog("4", "Green", "Woofo")

print(vars(c))
print(help(c))
print(type(c).mro())


