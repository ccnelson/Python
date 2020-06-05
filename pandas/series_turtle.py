
import turtle
import pandas as pd


# turtle function to test
def draw_point(turt, pos, count):
    turt.goto(pos)
    turt.color("lawngreen")
    turt.dot(8)
    turt.pu()
    turt.forward(5)
    turt.color("HotPink1")
    turt.write(count, True, align="left")


# create series
s = pd.Series([turtle.Vec2D(33.7, 44), turtle.Vec2D(14.2, 10.7), turtle.Vec2D(-10.1, -77.8)])
print('\n\tSeries:\n', s)
# create dataframe
df = pd.DataFrame(s, columns=['x/y'])
print("\n\tDataframe: \n", df)
print("\n\tIndividual record:\n{}".format(df.iloc[1,0]))
print("\n\tIndividual element 1:\n{}".format(df.iloc[1,0][0]))
print("\n\tIndividual element 2:\n{}".format(df.iloc[1,0][1]))
# dataframe basic arithmatic
z = df.iloc[1,0][0] - df.iloc[1,0][1]
print("\nSubraction between individual elements 1&2: ", z)
z = abs(df.iloc[0,0] - df.iloc[1,0])
print("\nDistance between points 0 and 1: ", z)

bob = turtle.Turtle()
bob.speed(9)
bob.pu()
draw_point(bob, df.iloc[1,0], 1)

# parsed
print("Parsed:")
for i, j in enumerate(s):
    draw_point(bob, j, i)
    print(j)

turtle.mainloop()

