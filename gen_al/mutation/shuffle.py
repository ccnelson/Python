# Scramble mutation
# Permutation encoding
# for TSP style problems.
# C.NELSON 2018
###### THEORY ############
# subject:
# 25036147
# choose mask position:
#   |--|   [2,5] positions
# 25036147 [0,3,6,1] values
# scramble selection in place
#   |--|
# 25613047 [6,1,3,0]
#########################

import random


def s_mask(length):
    start = random.randrange(length)
    end = random.randrange(start, length)
    if (start == end) or (start == 0 and end == (length -1)):
        start, end = s_mask(length)
    return start, end


def shufflem(subject):
    mask_start, mask_end = s_mask(len(subject))
    chromo = []
    for i in range(mask_start, mask_end+1):
        chromo.append(subject[i])
    chromo_mut = list(chromo)
    while chromo_mut == chromo:
        random.shuffle(chromo_mut)
    count = 0
    for j in range(mask_start, mask_end+1):
        subject[j] = chromo_mut[count]
        count += 1
    return subject


x = shufflem(['0','1','2','3','4','5','6','7'])
print(x)

