# Mutators for permuation
# 6 kinds
# problems
# C.NELSON 2018
############################

import random


def mutation(sub, val):  # val determines mut type
    z = random.randrange(401)
    if z < 3:  # 0.7% chance to mutate
        if val == 0:
            a = random_mutation(sub)
        elif val == 1:
            a = displaced_inversion(sub)
        elif val == 2:
            a = displacement(sub)
        elif val == 3:
            a = exchange(sub)
        elif val == 4:
            a = insertion(sub)
        elif val == 5:
            a = inversion(sub)
        elif val == 6:
            a = shufflem(sub)
        return a
    return sub


def random_mutation(sub):
    x = random.randrange(6)
    if x == 0:
        a = displaced_inversion(sub)
    elif x == 1:
        a = displacement(sub)
    elif x == 2:
        a = exchange(sub)
    elif x == 3:
        a = insertion(sub)
    elif x == 4:
        a = inversion(sub)
    elif x == 5:
        a = shufflem(sub)
    return a


def d_mask(length):
    start = random.randrange(length)
    end = random.randrange(start, length)
    mask_length = end - start
    pos = random.randrange(length - mask_length)
    if (start == end) or (start == 0 and end == (length -1)) or (pos == start):
        start, end, pos = d_mask(length)
    return start, end, pos


def e_mask(length):
    pos_1 = random.randrange(length)
    pos_2 = random.randrange(length)
    if pos_1 == pos_2:
        pos_1, pos_2 = e_mask(length)
    return pos_1, pos_2


def i_mask(length):
    val = random.randrange(length)
    pos = random.randrange(length)
    if val == pos:
       val, pos = i_mask(length)
    return val, pos


def ix_mask(length):
    start = random.randrange(length)
    end = random.randrange(start, length)
    if (start == end) or (start == 0 and end == (length -1)):
        start, end = ix_mask(length)
    return start, end

## THESE TWO NEED FIXING

def displaced_inversion(subject):
    start, end, pos = d_mask(len(subject))
    int_subj = list(subject)  # interim copy
    act_values = [int_subj[i] for i in range(start, end+1)] # actual vals
    for j in range(len(act_values)):  # remove values
        int_subj.remove(act_values[j])
    #  !!! identical to displacement apart from 'reversed' below !!
    for k in reversed(range(len(act_values))):  # insert at new position
        int_subj.insert(pos, act_values[k])
        pos += 1
    return int_subj


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


def exchange(subject):
    p1, p2 = e_mask(len(subject))
    subject[p1], subject[p2] = subject[p2], subject[p1]
    return subject


def insertion(subject):
    value, position = i_mask(len(subject))
    actual_val = subject[value]
    int_subj = list(subject) # interim copy
    int_subj.remove(actual_val)
    int_subj.insert(position, actual_val)
    return int_subj


def inversion(subject):
    mask_start, mask_end = ix_mask(len(subject))
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


def shufflem(subject):
    mask_start, mask_end = ix_mask(len(subject))
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

