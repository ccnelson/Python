
def create_class(pet_class_name):
    if pet_class_name is 'pony':
        class Pony(object):
            def __init__(self):
                self.name = "Ponyname"
                self.hp = 100
            def magic_power(self):
                print("neigh")
        return Pony()
        
    elif pet_class_name is 'snake':
        class Snake(object):
            def __init__(self):
                self.name = "Snakename"
                self.hp = 100
            def magic_power(self):
                print("hsss")
        return Snake()

Mypet1 = create_class('pony')
Mypet2 = create_class('snake')
print(Mypet1.name)
print(Mypet1.hp)
Mypet1.magic_power()


##### or #####

class Car(object):
 
    def factory(type):
        if type == "Racecar": 
            return Racecar()
        if type == "Van": 
            return Van()
        assert 0, "Bad car creation: " + type
 
    factory = staticmethod(factory)
 
class Racecar(Car):
    def drive(self): print("Racecar driving.")
 
class Van(Car):
    def drive(self): print("Van driving.")
 
obj = Car.factory("Racecar")
obj2 = Car.factory("Van")
obj.drive()
obj2.drive()
    
