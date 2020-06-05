
import turtle

archy = turtle.Turtle()  # initiate turtle

ts = archy.getscreen()   # get its screen
image = "donatelo.gif"   # make image variable
ts.addshape(image)       # add shape to screen
archy.shape(image)       # use shape for turtle
archy.speed(1)
archy.goto(-300, -300)
archy.goto(177, 265)

turtle.done()

