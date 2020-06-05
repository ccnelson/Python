# Exchange mutation
# Permutation encoding
# for TSP style probelems
# C.NELSON 2018
###### THEORY #############
# subject:
# 25036147
# choose 2 positions:
#  |    |  [1,6] pos
# 25036147 [5,4] values
# swap these values
#  |    |  [1,6] pos
# 24036157 [4,5] values
###########################

import random


def e_mask(length):
    pos_1 = random.randrange(length)
    pos_2 = random.randrange(length)
    if (pos_1 == pos_2):
        pos_1, pos_2 = e_mask(length)
    return pos_1, pos_2


def exchange(subject):
    p1, p2 = e_mask(len(subject))
    subject[p1], subject[p2] = subject[p2], subject[p1]
    return subject


x = exchange(list("01234567"))
print(x)

