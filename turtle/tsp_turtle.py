# TSP combinations grow exponentially 
# 4 destinations means no. of combinatons is
# factorial of 4 (4!) 
# 4 x 3 x 2 x 1 = 24 combinations
# 5! = 120
# 6! = 720
# 25! = more stars than there are in
#       the visible universe
# avg UPS driver has 100+ stops per day

import turtle
#import math
import random

class Location():
    """ each location initialised with coords
        wihch are then illustrated """
    def __init__(self):
        self.coordx = random.randrange(-200, 201)
        self.coordy = random.randrange(-200, 201)
        dave.goto(self.coordx, self.coordy)
        self.vec = dave.position()
        dave.pd()
        dave.dot(10)
        dave.pu()

turtle.setup(500, 500)
dave = turtle.Turtle()
ts = dave.getscreen()
ts.screensize(canvwidth=500, canvheight=500)
dave.speed(8)

## draw border
dave.pu()
dave.goto(-200, -200)
dave.left(90)
dave.color("red")
dave.pd()
for i in range(4):
    dave.forward(400)
    dave.right(90)

dave.pu()
dave.color("black")

loc1 = Location()
loc2 = Location()
loc3 = Location()
loc4 = Location()
loc5 = Location()

dave.goto(0,0)
dave.color("blue")

dave.goto(loc1.vec)
dave.pd()
dave.goto(loc2.vec)
dist = abs(loc1.vec - loc2.vec)
dave.goto(loc3.vec)
dist = dist + abs(loc2.vec - loc3.vec)
dave.goto(loc4.vec)
dist = dist + abs(loc3.vec - loc4.vec)
dave.goto(loc5.vec)
dist = dist + abs(loc4.vec - loc5.vec)
dave.goto(loc1.vec)
dist = dist + abs(loc5.vec - loc1.vec)

print(loc1.vec)
print(loc2.vec)
print(loc3.vec)
print(loc4.vec)
print(loc5.vec)
print(dist)

