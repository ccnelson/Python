# turtle functions (drawing)
# new tsp project
# C.NELSON 2019
# v1.2 updated 12/03
# Python 3.6
############################

import turtle


def setup_turtle(canv):
    """ prepare turtle return turtle
        and screen object """
    # t = turtle.Turtle()
    t = turtle.RawTurtle(canv)
    t.speed(0)
    ts = t.getscreen()
    ts.bgcolor('black')
    ts.tracer(0, 0)  # fast as
    #ts.title('New tsp project')
    return t, ts  # t = turtle, ts = screen object


def reset_turt(turt):
    turt.reset()


def draw_grid(turt, size):
    """ supply turtle and size - produces
        cartesian coordinate grid with red
        central axis, and coord labels """
    turt.ht()
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
        if i == 3:
            turt.write(turt.position(), True, align="right")
        else:  # reallign text for right side
            turt.pu()
            turt.write(turt.position(), True, align="left")
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


def draw_point(turt, pos, count):
    """ supply turtle, position, and count,
        turtle will goto position, draw a
        dot & write its count adjacently """
    turt.goto(pos)
    turt.color("lawngreen")
    turt.dot(4)
    turt.pu()
    turt.forward(5)
    turt.color("HotPink1")
    turt.write(count, True, align="left")
    turt.hideturtle()


def draw_coord(turt, coords, chromo):
    """ suply turtle, list of vector coords,
        and chromosome string, turtle will
        illustrate path taken - beginning and
        ending with location 0 """
    #turt.reset()
    turt.pu()
    turt.goto(coords[0])  # starts at 0
    turt.color("lawngreen")
    turt.pd()
    for c in chromo:
        i = int(c)
        turt.goto(coords[i])
    turt.goto(coords[0])  # ends at 0
    turt.pu()
