# turtle helper functions
# C.NELSON 2018
import turtle


def draw_grid(turt, size):
    turt.ht()
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


def draw_point(turt, pos, count):
    """ supply turtle, position, and count,
        turtle will goto position, draw a
        dot & write its count adjacently """
    turt.goto(pos)
    turt.color("lawngreen")
    turt.dot(8)
    turt.pu()
    turt.forward(5)
    turt.color("HotPink1")
    turt.write(count, True, align="left")
    turt.hideturtle()


def trav_coord_ret_val(turt, coords, chromo):
    """ suply turtle, list of vector coords,
    and a chromosome string, turtle will
    follow chromosome and return distance"""
    turt.reset()  # ! comment these '!' lines out to hide paths taken (faster)
    dist = 0
    turt.goto(coords[0].pos)        # starts at 0
    turt.color("lawngreen")  # !
    turt.pd()                # !
    for c in chromo:
        i = int(c)
        dist += abs(turt.position() - coords[i].pos)
        turt.goto(coords[i].pos)
    dist += abs(turt.position() - coords[0].pos)
    turt.goto(coords[0].pos)        # ends at 0
    turt.pu()                # !
    return dist

def draw_coord(turt, coords, chromo):
    """ suply turtle, list of vector coords,
        and a chromosome string, turtle will
        follow chromosome and return distance"""
    turt.reset()
    turt.goto(coords[0].pos)  # starts at 0
    turt.color("lawngreen")
    turt.pd()
    for c in chromo:
        i = int(c)
        turt.goto(coords[i].pos)
    turt.goto(coords[0].pos)  # ends at 0
    turt.pu()