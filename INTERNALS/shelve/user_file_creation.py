import shelve
import os

class Datastore:
    def __init__(self):
        self.title = "x2"
        
x = Datastore()
z = os.listdir()
a = []
print("")
for i in range(0, len(z)):
    if z[i].endswith(".dat", -4):
        a.append(z[i])
a = list(enumerate(a, start=1))
for i in range(0, len(a)):
    print(a[i])
y = input("\n\tChoose database: ")

db = shelve.open(y, flag='c')

db["1"] = {"one": 1, "two": 2, "three": 3}
db["2"] = 2
db["3"] = x

print(db["3"])
input()
print(db["3"].title)



