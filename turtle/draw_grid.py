# draw grid with turtle
# C.NELSON 2018
import turtle


def draw_grid(turt, size):
    """ supply turtle and size - produces
        square of width/length = size
        with 0,0 at centre """
    corner_list = [turtle.Vec2D(-size/2, -size/2),
                   turtle.Vec2D(size/2, -size/2),
                   turtle.Vec2D(size/2, size/2),
                   turtle.Vec2D(-size/2, size/2)] # set coords
    # outer grid
    turt.goto(corner_list[0]) # goto start
    turt.pd()
    turt.color("white")
    turt.write(turt.position(), True, align="right")
    for i in range(1, 4):
        turt.goto(corner_list[i])
        turt.write(turt.position(), True, align="right")
        turt.pu() 
        turt.goto(corner_list[i]) # reallign after writing
        turt.pd()
    turt.goto(corner_list[0]) # back to start
    # inner grid
    for j in range(2):
        turt.pd()
        turt.forward(size/4)
        turt.left(90)
        turt.forward(size)
        turt.right(90)
        turt.forward(size/4)
        turt.right(90)
        turt.color("red")
        turt.forward(size)
        turt.left(90)
        turt.color("white")
        turt.forward(size/4)
        turt.left(90)
        turt.forward(size)
        turt.pu()
        if j == 0:
            turt.goto(corner_list[1])

leon = turtle.Turtle()
ts = leon.getscreen()
ts.bgcolor('black')

draw_grid(leon, 400)
