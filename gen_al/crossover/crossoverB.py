
import random

parA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parB = [4, 3, 2, 1, 7, 5, 6, 10, 8, 9]
offspringA = []
xpos = random.randrange(1, len(parA)-1)
print(xpos)

for i in range(0, xpos):
    offspringA.insert(len(offspringA), parA[i])

for j, k in enumerate(parB):
    if k not in offspringA:
        offspringA.insert(len(offspringA), k)

print(offspringA)