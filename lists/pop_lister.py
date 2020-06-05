import random
move_options = ["00", "01", "10", "00"]

lister = [random.choice(move_options) for i in range(16)]

print(lister)

for i in range(16):
    new1 = lister.pop(0)
    print(new1)
