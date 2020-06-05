# Position Based Crossover
# Permutation crossover encoding
# for TSP sytle problems.
# C.NELSON 2018
##### THEORY ################
# parents
# 25036147
# 34072516
# choose mask locations
#  ||  |   [1,2,5] positions
# 25036147 [5,0,1] values
# remove all but masked
# *50**1**
# parse other parent filling 
# empty spaces with missing numbers
# 35047126 = offspring 1
# repeat vice versa
#  ||  |   [1,2,5] positions
# 34072516 [4,0,5] values
# remove unmasked
# *40**5**
# insert parent 1
# 24036517
##############################
# the above example uses a 
# crossover mask length 3.
# this module uses a mask length
# longer than 1, less than length
# of parents
#############################

import random

def p_mask(length):
    """ supply length return pbx x-over mask """
    positions = [i for i in range(length)]
    mask_length = random.randrange(2, length)
    chosen_pos = {random.choice(positions) for j in range(mask_length + 1)}
    return chosen_pos

def pbx(par1, par2):
    """ """
    c_pos = p_mask(len(par1))
    int_par1 = list(par1) # interim copies
    int_par2 = list(par2)
    print("Parent 1: ", par1)
    print("Parent 2: ", par2)
    print("Chosen positions: ", c_pos)
    for k in range(len(par1)):
        if k not in c_pos:
            int_par1[k] = ' '
            int_par2[k] = ' '
    for m in range(len(par2)):
        if par2[m] not in int_par1:
            for n in range(len(int_par1)):
                if int_par1[n] == ' ':
                    int_par1[n] = par2[m]
                    break
        if par1[m] not in int_par2:
            for p in range(len(int_par2)):
                if int_par2[p] == ' ':
                    int_par2[p] = par1[m]
                    break
    return int_par1, int_par2
        
x, y = pbx(list("01234567"), list("76543210"))
print("Offspring 1: ", x, "\nOffspring 2: ", y)
