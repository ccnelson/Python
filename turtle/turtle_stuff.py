import turtle

leonardo = turtle.Turtle()

ts = leonardo.getscreen() # return screen object
ts.bgcolor('pink') # change background colour

leonardo.forward(150) # forward 15 pixels
leonardo.right(25)   # right 25 degrees

leonardo.forward(100)

print(leonardo.xcor()) # return xcor
print(leonardo.ycor())

leonardo.color("black", "red") # black outline red fill
leonardo.begin_fill() # start fill
leonardo.circle(30) # draw circle 30 radius
leonardo.end_fill() # stop fill

leonardo.clear() # clear screen

leonardo.dot() # draw a dot

# leonardo.ondrag(leonardo.goto)

print(leonardo.position()) # return position

leonardo.reset() # reset to 0,0
print(leonardo.position())

leonardo.write('Home = ', True, align="center") # write some text

leonardo.pu() # pen up
leonardo.fd(50) # forward
leonardo.pd() # pen down
leonardo.circle(15)

print(leonardo.distance(0, 0)) # turtles distance from 0,0

leonardo.goto(-10, -10) # move to absolute position, retaining heading

print(leonardo.heading()) # return current heading
leonardo.right(10)
print(leonardo.heading())


