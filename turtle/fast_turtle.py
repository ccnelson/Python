import turtle
import random

terry = turtle.Turtle()
ts = terry.getscreen() # screen object
ts.tracer(0, 0) # makes turtle drawing instant
                # default is ts.tracer(1, 10)


for i in range(230):
    x = turtle.Vec2D(random.randrange(-150, 151), random.randrange(-150, 151))
    terry.goto(x)

ts = terry.getscreen() # screen object
ts.tracer(0, 0) # makes turtle drawing instant
                # default is ts.tracer(1, 10)
                # ts.tracer(n, d)
                # (n=refreshes, d=delay)

