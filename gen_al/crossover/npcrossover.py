import numpy as np
import random

parent_A = np.array([1,2,3,4,5,6,7])
parent_B = np.array([4,3,2,1,7,5,6])
xpos = random.randrange(1, len(parent_A))
offspring = np.empty(0, int)  # prevents np defaulting to floats

for i in range(0, xpos):
    offspring = np.append(offspring, parent_A[i])

for j, k in enumerate(parent_B):
    if k not in offspring:
        offspring = np.append(offspring, k)

print(xpos)
print(offspring)


