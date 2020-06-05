
import turtle as t
import random as r
import math

turk = t.Turtle()
ts = turk.getscreen()
ts.tracer(1,0)
ts.bgcolor('black')
turk.color('white')

nco = -200
pco = 200

a = t.Vec2D(r.randrange(nco, pco),r.randrange(nco, pco))
b = t.Vec2D(r.randrange(nco, pco),r.randrange(nco, pco))
c = t.Vec2D(r.randrange(nco, pco),r.randrange(nco, pco))

start = t.Vec2D(r.randrange(nco, pco),r.randrange(nco, pco))

turk.pu()
turk.setpos(a)
turk.dot()
turk.setpos(b)
turk.dot()
turk.setpos(c)
turk.dot()

turk.setpos(start)
turk.dot()
turk.ht()

while True:
    x = r.randrange(3)
    if x == 0:
        turk.setheading(turk.towards(a))
        y = math.sqrt(((a[0] - turk.pos()[0])**2)+((a[1] - turk.pos()[1])**2))
        y = y / 2
    elif x == 1:
        turk.setheading(turk.towards(b))
        y = math.sqrt(((b[0] - turk.pos()[0])**2)+((b[1] - turk.pos()[1])**2))
        y = y / 2
    elif x == 2:
        turk.setheading(turk.towards(c))
        y = math.sqrt(((c[0] - turk.pos()[0])**2)+((c[1] - turk.pos()[1])**2))
        y = y / 2
    turk.forward(y)
    turk.dot(size=1.5)
    
t.mainloop()
