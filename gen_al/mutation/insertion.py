# Insertion mutation
# Permutation encoding
# for TSP style problems
# C.NELSON 2018
#### THEORY #########
# subject:
# 25036147
# choose a number
#    v
# 25036147 [3] value
# choose a position
#  |       [1] position
# 25036147
# insert value and shift
# remaining values accordingly 
# 23506147 = mutated
########################

import random


def i_mask(length):
    val = random.randrange(length)
    pos = random.randrange(length)
    if val == pos:
       val, pos = i_mask(length)
    return val, pos


def insertion(subject):
    value, position = i_mask(len(subject))
    actual_val = subject[value]
    int_subj = list(subject) # interim copy
    int_subj.remove(actual_val)
    int_subj.insert(position, actual_val)
    return int_subj


x = insertion(list("1234567"))
print(x)
