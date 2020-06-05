# Inversion mutation
# Permutation encoding
# for TSP style problems
# C.NELSON 2018
#### THEORY ##############
# subject:
# 61072543
# choose a mask area
#  |-|     [1,2,3] positions
# 61072543 [1,0,7] values
# reverse the values
#  |-|     [1,2,3] pos
# 67012543 [7,0,1] val
# 67012543 = mutated
#########################

import random


def inv_mask(length):
    start = random.randrange(length)
    end = random.randrange(start, length)
    if (start == end) or (start == 0 and end == (length -1)):
        start, end = inv_mask(length)
    return start, end


def inversion(subject):
    mask_start, mask_end = inv_mask(len(subject))
    chromo = []
    for i in range(mask_start, mask_end+1):
        chromo.append(subject[i])
    # the following few lines are the main
    # deviation from shuffle mutation
    chromo_mut = list(reversed(chromo))
    count = 0
    for j in range(mask_start, mask_end+1):
        subject[j] = chromo_mut[count]
        count += 1
    return subject


x = inversion(['0','1','2','3','4','5','6','7'])
print(x)
