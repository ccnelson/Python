# Displaced inversion
# Permutation encoding
# for TSP style problems
# C.NELSON 2018
##### THEORY ###########
# subject:
# 61072543
# choose a mask area
#     |--| [4,5,6,7] positions
# 61072543 [2,5,4,3] values
# choose a destination position
#  |       [1] position
# 61072543 
# insert inverted values at
# destination position &
# displace remaining
#  |--|
# 63452107 = mutated
########################

import random


def d_mask(length):
    start = random.randrange(length)
    end = random.randrange(start, length)
    mask_length = end - start
    pos = random.randrange(length - mask_length)
    if (start == end) or (start == 0 and end == (length -1)) or (pos == start):
        start, end, pos = d_mask(length)
    return start, end, pos


def displaced_inversion(subject):
    start, end, pos = d_mask(len(subject))
    print("Start: %r End: %r pos: %r" % (start, end, pos))
    int_subj = list(subject) # interim copy
    act_values = [int_subj[i] for i in range(start, end+1)] # actual vals
    print("act values: %r" % act_values)
    for j in range(len(act_values)): # remove values
        #if j in int_subj:
        int_subj.remove(act_values[j])

    #  !!! identical to displacement apart from 'reversed' below !!
    for k in reversed(range(len(act_values))): # insert at new position
        int_subj.insert(pos, act_values[k])
        pos += 1
    return int_subj

for i in range(1000):
    x = displaced_inversion(list("1234567"))
    print(x)
