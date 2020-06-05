# #####################################
# ###  TURTLE VECTOR 2D SPEED TEST ####
# ### empirical evidence that its  ####
# ### better to do it yourself     ####
# #####################################
# # C NELSON 2018 #####################
import turtle
import random
import time
import math

no_of_locs = 100000
distances = []


def find_dist(p1, p2):
    """ euclidean distance calculation expects a tuple (z,y)"""
    dist = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return dist


# ##### round 2 - tuples and manual function calculation ######
y = [(random.randrange(-200, 201), random.randrange(-200, 201)) for i in range(no_of_locs)]
start2 = time.time()
for j, i in enumerate(y):
    if j < len(y)-1:
        distances.append(find_dist(y[j], y[j+1]))
end2 = time.time()
duration2 = end2 - start2
# print(distances)
print("Manual way: ")
print("Duration: ", duration2)

###################
# reset
distances = []
###################

# ##### round 1 - turtle.Vec2D and abs() ######
x = [turtle.Vec2D(random.randrange(-200, 201), random.randrange(-200, 201)) for i in range(no_of_locs)]
start1 = time.time()
for j, i in enumerate(x):
    if j < len(x)-1:  # if not at end of list
        distances.append(abs(x[j] - x[j+1]))  # use abs on vectors
end1 = time.time()
duration1 = end1 - start1
# print(distances)
print("Vector2D: ")
print("Duration: ", duration1)

