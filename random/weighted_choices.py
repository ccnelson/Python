# random weighted choice
# C.NELSON 2018

import random

xlist = [1,2,3,4,5,6,7,8,9,10]

w = [10,1,1,1,1,1,1,1,1,1] # weights corresponding to xlist
                            # dont need to add up to
                            # anything inparticular

print(random.choices(xlist, weights=w))

print(random.choices(xlist, weights=w, k=3)) # k=3 gives 3 selections
                                                # with replacement
