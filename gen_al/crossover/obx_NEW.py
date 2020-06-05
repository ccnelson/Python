

import random


def o_mask(length):
    """ give length return obx x-over mask """
    startpos = random.randrange(0, length-1)
    endpos = random.randrange(startpos, length)
    while startpos == endpos:
        endpos = random.randrange(startpos, length)
    chosen_pos = [i for i in range(startpos, endpos+1)]
    return chosen_pos


def obx(par1, par2):
    c_pos = o_mask(len(par1))  # get mask
    print("Chosen positions: ", c_pos)
    local_par1 = list(par1)  # local copies
    local_par2 = list(par2)
    par_a_masked = [par1[i] for i in c_pos]  # get masked values
    par_b_masked = [par2[j] for j in c_pos]
    count1 = 0  # init counters
    count2 = 0
    for k, m in enumerate(par1):  # parse lists
        if local_par2[k] in par_a_masked:  # if value is in masked list
            local_par2[k] = par_a_masked[count1]  # insert masked
            count1 += 1  # increment counter, iterating thru mask
        if local_par1[k] in par_b_masked:  # do same for other gene
            local_par1[k] = par_b_masked[count2]
            count2 += 1
    return local_par1, local_par2


parent1 = list("25036147")
parent2 = list("34072516")

for i in range(100):
    x, y = obx(list(parent1), list(parent2))
    print("Parent 1: ", parent1)
    print("Child  1: ", x)
    print()
    print("Parent 2: ", parent2)
    print("Child  2: ", y)
