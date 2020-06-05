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



def circle_of_points(turt, n):
    for i in range(n):
        y = turt.position()  # draw_point knocks turt off track
        draw_point(turt, turt.position(), i)
        turt.goto(y)  # put turt back on track
        turt.circle(60, 360/n)  # (radius, extent)
        turt.pu()

def circle_of_points_2(turt, n):
    x = []
    for i in range(n):
        turt.pu()
        #y = turt.position()  # draw_point knocks turt off track
        #draw_point(turt, turt.position(), i)
        #turt.goto(y)  # put turt back on track
        x.append(turt.position())
        turt.circle(60, 360/n)  # (radius, extent)
        #turt.pu()
    return x

        
bob = turtle.Turtle()
bob.speed(9)
z = circle_of_points_2(bob, 8)
print(z)

