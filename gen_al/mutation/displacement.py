# Displacement mutation
# Permutation encoding
# for TSP style problems
# C.NELSON 2018
##### THEORY ############
# subject:
# 25036147
# choose a mask size:
#     |-|  [4,5,6] positions
# 61072543 [2,5,4] values
# choose a position destination:
#  |       [1] pos dest
# 61072543
# move the mask chunk to new
# position desintation & 
# displace remaining nos
#  |-|
# 62541073 = mutated
#########################

import random


def d_mask(length):
    start = random.randrange(length)
    end = random.randrange(start, length)
    mask_length = end - start
    pos = random.randrange(length - mask_length)
    if (start == end) or (start == 0 and end == (length -1)) or (pos == start):
        start, end, pos = d_mask(length)
    return start, end, pos


def displacement(subject):
    start, end, pos = d_mask(len(subject))
    int_subj = list(subject) # interim copy
    act_values = [int_subj[i] for i in range(start, end+1)] # actual vals
    for j in range(len(act_values)): # remove values
        int_subj.remove(act_values[j])
    for k in range(len(act_values)): # insert at new position
        int_subj.insert(pos, act_values[k])
        pos += 1
    return int_subj


for i in range(1000):
    x = displacement("1234567")
    print(x)



