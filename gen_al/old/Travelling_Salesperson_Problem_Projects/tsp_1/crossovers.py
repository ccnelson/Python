

import random


def cross_over(par1, par2, val):  # val determinse xover type
    if val == 0:
        a, b = random_cross_over(par1, par2)
    elif val == 1:
        a, b = pbx(par1, par2)
    elif val == 2:
        a, b = obx(par1, par2)
    elif val == 3:
        a, b = pmx(par1, par2)
    return a, b


def random_cross_over(par1, par2):
    x = random.randrange(3)
    if x == 0:
        a, b = pbx(par1, par2)
    elif x == 1:
        a, b = obx(par1, par2)
    elif x == 2:
        a, b = pmx(par1, par2)
    return a, b


def mask(length):
    positions = [i for i in range(length)]
    mask_length = random.randrange(2, length)
    chosen_pos = {random.choice(positions) for j in range(mask_length + 1)}
    return chosen_pos


def o_mask(length):
    startpos = random.randrange(0, length-1)
    endpos = random.randrange(startpos, length)
    while startpos == endpos:
        endpos = random.randrange(startpos, length)
    chosen_pos = [i for i in range(startpos, endpos+1)]
    return chosen_pos


def x_mask(length):
    start = random.randrange(length)
    end = random.randrange(start, length)
    if (start == 0 and end == length -1) or (start == end):
        start, end = x_mask(length) # recursion
    return start, end


def pbx(par1, par2):
    # print("pbx")
    c_pos = mask(len(par1))
    int_par1 = list(par1) # interim copies
    int_par2 = list(par2)
    for i, k in enumerate(par1):
        if i not in c_pos:
            int_par1[i] = ' '
            int_par2[i] = ' '
    for ii, m in enumerate(par2):
        if m not in int_par1:
            for iii, n in enumerate(int_par1):
                if n == ' ':
                    int_par1[iii] = m
                    break
        if par1[ii] not in int_par2:
            for iiii, p in enumerate(int_par2):
                if p == ' ':
                    int_par2[iiii] = par1[ii]
                    break
    return int_par1, int_par2


def obx(par1, par2):
    c_pos = o_mask(len(par1))  # get mask
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


def pmx(par1, par2):
    # print("pmx")
    pos_start, pos_end = x_mask(len(par1))
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





