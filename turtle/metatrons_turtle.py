
import turtle

turk = turtle.Turtle()
turk.speed(0)
turk.ht()
circum = 75

locs = []


######## start pos ###############

locs.append(turtle.Vec2D(turk.xcor(), turk.ycor())) # save start
turk.dot()
turk.pu()
turk.setheading(270) # face south
turk.forward(circum) # middle 
turk.setheading(0) # rotate back
turk.pd()
turk.circle(circum) # central circle


#### cycle 1 - UNIQUE ###############


turk.pu()
turk.setheading(90)
turk.forward(circum * 2)
turk.setheading(0)
turk.pd()
turk.circle(circum) # first circle
turk.setheading(90)
turk.pu()
turk.forward(circum)
locs.append(turtle.Vec2D(turk.xcor(), turk.ycor())) # first loc
turk.dot()
turk.pu()
turk.forward(circum)
turk.setheading(0)
turk.pd()
turk.circle(circum) # second circle
turk.setheading(90)
turk.pu()
turk.forward(circum)
locs.append(turtle.Vec2D(turk.xcor(), turk.ycor())) # second loc
turk.dot()

turk.setposition(locs[0])


#### LOOP #################

for i in range(5):
    turk.right(60)
    turk.forward(circum)
    turk.right(90)
    turk.pd()
    turk.circle(circum)
    turk.pu()
    turk.left(90)
    turk.forward(circum)
    locs.append(turtle.Vec2D(turk.xcor(), turk.ycor()))
    turk.dot()
    turk.forward(circum)
    turk.right(90)
    turk.pd()
    turk.circle(circum)
    turk.pu()
    turk.left(90)
    turk.forward(circum)
    locs.append(turtle.Vec2D(turk.xcor(), turk.ycor()))
    turk.dot()
    turk.setposition(locs[0])

turk.color("blue")
turk.pd()

for j in locs:
    turk.goto(j)
    for k in locs:
        turk.goto(k)
        turk.goto(j)

turtle.mainloop()


