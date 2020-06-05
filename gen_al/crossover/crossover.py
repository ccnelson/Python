# single point crossover.
# retains up to xpos of parA, inserts
# remaining entries in order from parB

import random

parent_A = [1,2,3,4,5,6,7]
parent_B = [7,6,5,4,3,2,1]
xpos = random.randrange(1, len(parent_A))
offspring = []

for i in range(0, xpos):
    offspring.append(parent_A[i])

for j, k in enumerate(parent_B):
    if k not in offspring:
        offspring.append(k)

print(xpos)
print(offspring)

