
class Infmo:
    def __init__(self, name):
        self.name = name

listo = []
done = False

while done == False:
    x = input("Name: ")
    listo.append(Infmo(x))
    for i in range(0, len(listo)):
        print(listo[i].name)
    if x == "X":
        done = True
    else:
        x = ""

