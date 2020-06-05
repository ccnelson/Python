# random.sample(population, k)
# Return list of k unique elements chosen from
# the population sequence
# Returns a new list containing elements from 
# population while leaving the original
# population unchanged.
# !! Occassionaly returns unchanged list
# 1/500 ish chance !!

import random

x = ['1', '2', '3', '4', '5']

for i in range(10):
    y = random.sample(x, 3)
    print(y)
    if y == x:
        print("oops")


