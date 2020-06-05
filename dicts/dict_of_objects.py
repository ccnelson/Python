
import numpy as np
import random


class Point():
    count = 0

    def __init__(self):
        self.loc = (random.randrange(-200, 200), random.randrange(-200, 200))
        self.index = Point.count
        Point.count += 1


n = np.arange(10)  # numpy array 1-9
d = {}    # empty dictionary

for i in n:
    d[i] = Point()  # fill dictionary with objects

for j in d:
    print("#:", j)  # print index
    print(d[j].loc)  # print values
    print("index:", d[j].index)

# print(d[0].loc)

