# mutations (and masks. for permutation)
# new tsp project
# C.NELSON 2019
# v1.1 updated 20/01
# Python 3.6
############################
import random

# main interface #

def mutation(sub, mut_type):
    """ input subject and type of mutation
        0 = random
        1 = displacement inverted
        2 = displacement
        3 = exchange
        4 = insertion
        5 = inversion
        6 = shuffle
        FUNCTION DECIDES IF MUTATIONS OCCURS -
        RETURNS EITHER UNCHANGED SUBJECT OR
        MUTATED VERSION - MIGHT CHANGE THIS...
        NOT VERY EFFICIENT (unless cache func locally?)
        """
    z = random.randrange(200)  # from 0 to 199 inclusive
    if z < 2:  # 1/200 = 0.5% chance to mutate
        if mut_type == 0:
            a = random_mutation(sub)
        elif mut_type == 1:
            a = displacement(sub, inverted=True)
        elif mut_type == 2:
            a = displacement(sub, inverted=False)
        elif mut_type == 3:
            a = exchange(sub)
        elif mut_type == 4:
            a = insertion(sub)
        elif mut_type == 5:
            a = inversion(sub)
        else:
            a = shufflem(sub)
        return a
    return sub


def random_mutation(sub):
    """ random choice of mutation type
    input subject return mutated subject"""
    x = random.randrange(6)
    if x == 0:
        a = displacement(sub, inverted=True)
    elif x == 1:
        a = displacement(sub, inverted=False)
    elif x == 2:
        a = exchange(sub)
    elif x == 3:
        a = insertion(sub)
    elif x == 4:
        a = inversion(sub)
    else:
        a = shufflem(sub)
    return a


# masks #

def masks(length, mtyp):
    """ input length and mask type
        return 2, 3, or 2 values:
        a = start, end (a 'slice' > 1 but < length)
        b = start, end, pos (as above + pos outside 'slice')
        c = 2 unique positions"""
    if mtyp == "a" or mtyp == "b":
        start = random.randrange(length)
        end = random.randrange(start, length)
        while (start == end) or (start == 0 and end == (length - 1)):
            start = random.randrange(length)
            end = random.randrange(start, length)
        if mtyp == "a":
            return start, end
        if mtyp == "b":
            pos = random.randrange(length)
            while (pos >= start) and (pos <= end):
                pos = random.randrange(length)
            return start, end, pos
    elif mtyp == "c":
        pos_a = random.randrange(length)
        pos_b = random.randrange(length)
        while pos_a == pos_b:
            pos_a = random.randrange(length)
            pos_b = random.randrange(length)
        return pos_a, pos_b


# mutation functions #

def displacement(subject, inverted):
    """ input subject and inversion option
    returns displaced / displaced & inverted subject """
    start, end, pos = masks(len(subject), "b")
    int_subj = list(subject)                                 # interim copy
    act_values = [int_subj[i] for i in range(start, end+1)]  # actual vals
    for j, _ in enumerate(act_values):                       # remove values
        int_subj.remove(act_values[j])
    if not inverted:
        for k, _ in enumerate(act_values):
            int_subj.insert(pos, act_values[k])     # insert at new position
            pos += 1
    elif inverted:
        for k in reversed(range(len(act_values))):  # enumerate is not reversible
            int_subj.insert(pos, act_values[k])     # insert at new position
            pos += 1
    return int_subj


def exchange(subject):
    """ input subject return exchange mutated subject"""
    p1, p2 = masks(len(subject), "c")
    subject[p1], subject[p2] = subject[p2], subject[p1]
    return subject


def insertion(subject):
    """ input subject return insertion mutated subject"""
    value, position = masks(len(subject), "c")
    actual_val = subject[value]
    subject.remove(actual_val)
    subject.insert(position, actual_val)
    return subject


def inversion(subject):
    """ input subject return inversion mutated subject"""
    mask_start, mask_end = masks(len(subject), "a")
    selection = []
    for i in range(mask_start, mask_end+1):
        selection.append(subject[i])
    selection = list(reversed(selection))
    count = 0
    for j in range(mask_start, mask_end+1):
        subject[j] = selection[count]
        count += 1
    return subject


def shufflem(subject):
    """ input subject return shuffle mutated subject"""
    mask_start, mask_end = masks(len(subject), "a")
    selection = []
    for i in range(mask_start, mask_end+1):
        selection.append(subject[i])
    random.shuffle(selection)
    count = 0
    for j in range(mask_start, mask_end+1):
        subject[j] = selection[count]
        count += 1
    return subject

