# Order Based Crossover
# Permutation crossover encoding
# for TSP sytle problems.
# C.NELSON 2018
#### THEORY ################
# parents
# 25036147
# 34072516
# choose mask positions:
#  ||  |   [1,2,5] positions
# 25036147 [5,0,1] values
# impose order of values
# in positions 
#   |  ||
# 34572016 = offspring 1
# repeat vice versa
#  ||  |   [1,2,5]
# 34072516 [4,0,5]
# 24036157 = offspring 2
############################
# the above example uses
# a crossover mask of length 3
# this module produes a mask
# longer than 1 and less than
# parent length
############################

import random

def o_mask(length):
    """ give length return obx x-over mask """
    positions = [i for i in range(length)] # possible positions
    mask_length = random.randrange(2, length) # number of positions to mask
    #chosen_pos = [1, 2, 5] # test values
    chosen_pos = {random.choice(positions) for j in range(mask_length + 1)} # its a set
    return chosen_pos

def obx(par1, par2):
    c_pos = list(o_mask(len(par1))) #get mask
    print("Parent 1: ", par1)
    print("Parent 2: ", par2)
    print("Chosen positions: ", c_pos)
    par_A_x = [par1[i] for i in c_pos] # get masked values
    par_B_x = [par2[j] for j in c_pos]
    count1 = 0 # init counters
    count2 = 0
    for k in range(len(par1)): # parse lisrs
        if par2[k] in par_A_x: # if value is masked
            par2[k] = par_A_x[count1] # switch the order
            count1 += 1 # increment counter
        if par1[k] in par_B_x: # do same for other gene
            par1[k] = par_B_x[count2]
            count2 += 1
    return par1, par2

x, y = obx(list("25036147"), list("34072516"))
print(x)
print(y)
