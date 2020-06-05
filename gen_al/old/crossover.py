import random

gene1 = "11111111" # genes given
gene2 = "00000000"

gene1c = gene1 # copies
gene2c = gene2

rand1 = random.randrange(8) # define range
rand2 = random.randrange(8)
while rand2 < rand1:
    rand2 = random.randrange(8) # make sure of logic

if rand1 != rand2: # if numbers ARE the same
    for i in range(rand1, rand2+1):
        gene1c = gene1c[:i] + gene2[i] + gene1c[i + 1:]
        gene2c = gene2c[:i] + gene1[i] + gene2c[i + 1:]

else: # do this instead
    gene1c = gene1c[:rand1] + gene2[rand1] + gene1c[rand1 + 1:]
    gene2c = gene2c[:rand1] + gene1[rand1] + gene2c[rand1 + 1:]

print(rand1)
print(rand2)
print(gene1)
print(gene2)
print(gene1c)
print(gene2c)

