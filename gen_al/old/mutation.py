gene = "00000000"

#mut_rate = 0.7

rand_list = ["0","1"]

import random

print("Random number:", end="")

for i in range(8):
    z = random.randrange(10)
    m = random.choice(rand_list)
    if z == 9:
        gene = gene[:i] + m + gene[i + 1:]
    print(z, end="")

print("\nMutated gene:", gene)

