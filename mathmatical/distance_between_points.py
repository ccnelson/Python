
import math
#  https://ncalculators.com/geometry/length-between-two-points-calculator.htm
#  Euclidean distance

p1 = (23.765, 55.51)
p2 = (-1.9, -207.8)
dist = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(dist)


def find_dist(p1, p2):
    """ euclidean distance calculation expects two tuples: (x,y)(x,y)"""
    dist = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return dist


print("Function example: ", find_dist(p1, p2))

