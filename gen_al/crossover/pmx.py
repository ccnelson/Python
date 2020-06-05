# Partially Mapped Crossover.
# Permutation crossover encoding
# for TSP style problems.
# C.NELSON 2018
##### THEORY ####################
# (parents 25036147 & 34072516)
# choose places to split parents
# 250|361|47
# 340|725|16
# proceed to swap and
# replace duplicates
# step 1:
# 250|761|43
# 740|325|16
# step 2:
# 650|721|43
# 740|365|12
# step 3: (final step
# 610|725|43
# 740|361|52
################################
# in the above example crossover mask
# is 3 long. this module produces
# a mask longer than 1 and less than
# the total length
# i.e from 2 to length-1 maximum

import random

def x_mask(length):
    """ give length return pmx x-over mask """
    start = random.randrange(length)
    end = random.randrange(start, length)
    if (start == 0 and end == length -1) or (start == end):
        start, end = x_mask(length) # recursion
    return start, end

def pmx(par1, par2):
    """ supply 2 str list parents -
    return 2 str list decendants """
    pos_start, pos_end = x_mask(len(par1))
    #print("start: ", pos_start)
    #print("end: ", pos_end)
    for i in range(pos_start, pos_end + 1):
        int1 = list(par1) # interim copies
        int2 = list(par2)
        par1[i], par2[i] = par2[i], par1[i] # switch values
        if par1[i] != par2[i]: # if numbers not equal
            x = int1.index(par1[i]) # locate duplicates
            y = int2.index(par2[i])
            par1[x] = par2[i]  # replace with counterparts
            par2[y] = par1[i]
    return par1, par2

for i in range(1):
    x, y = pmx(list("25036147"), list("34072516"))
    print(x)
    print(y)
    print("----")

