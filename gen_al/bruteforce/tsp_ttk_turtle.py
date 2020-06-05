import tkinter as tk
from tkinter import ttk
import builder_methods as bm
import turtle
import random
import itertools

class Storage():
    def __init__(self):
        self.total_distance = 0
        self.distances = []
        self.best_distance = 0
        self.best_distance_index = 0


class Location():
    """ each location initialised with coords
        wihch are then illustrated """
    def __init__(self):
        c.pu()
        self.coordx = random.randrange(-200, 201)
        self.coordy = random.randrange(-200, 201)
        c.goto(self.coordx, self.coordy)
        self.vec = c.position()
        c.pd()
        c.dot(10)
        c.pu()
        self.dist = 0

def do_tsp(n):
    #prep
    c.clear()
    t.clear()
    t.color("black")
    ## brute force for testing later
    values = range(2, n+1)
    perms = [i for i in itertools.permutations(values, n-1)]
    print(perms)
    ## prepare list of combinations
    ## too big a number will freeze system
    xlist = [Location() for i in range(n)]
    
    c.hideturtle()
    t.color("blue")
    dist = 0
    #visit locations
    for p in perms:
        dist = 0
        t.goto(xlist[0].vec)
        t.pd()
        for l in p:
            print(l)
            dist = dist + abs(xlist[l-1].vec - t.position())
            t.goto(xlist[l-1].vec)
        print(p)
        dist = dist + abs(t.position() - xlist[0].vec)
        #back to start
        t.goto(xlist[0].vec)
        s.distances.append(dist) #save in class
        s.total_distance = dist
        rightframe_data_1.configure(text = "Total: \n" + str(s.total_distance))
        t.pu()
        t.clear()
    #show stats
    for z in xlist:
        print(z.vec)
    print(s.total_distance)
    rightframe_data_1.configure(text = "Total: \n" + str(s.total_distance))
    s.best_distance = min(s.distances)
    s.best_distance_index = s.distances.index(min(s.distances))
    rightframe_text.delete(1.0, 'end')
    rightframe_text.insert('end', s.best_distance)
    rightframe_text.insert('end', '\n')
    rightframe_text.insert('end', s.best_distance_index)
    rightframe_text.insert('end', '\n')
    rightframe_text.insert('end', perms[s.best_distance_index])
    
    
#setup
root = tk.Tk()
root.title("Travelling Salesman Problem")
style = ttk.Style()
style.theme_use('alt')

s = Storage()

#gui
mainframe = bm._build_frame(root, 0, 0)
mainframe_label = bm._build_label(mainframe, 0, 0, "MAP", 20)
maincanv = bm._build_canvas(mainframe, 0, 1)
rightframe = bm._build_frame(root, 1, 0)
rightframe_label = bm._build_label(rightframe, 0, 0, "STATS", 20)
rightframe_data_1 = bm._build_label(rightframe, 0, 1, "...Calculating...", 15)
rightframe_spinbox = bm._build_spinbox(rightframe, 0, 2)
rightframe_button = bm._build_button(rightframe, "do it", 0, 3,
                                     lambda: do_tsp(int(rightframe_spinbox.get())))
rightframe_text = bm._build_text(rightframe, "stuff", 20, 1, 0, 15, 30)
rightframe_text.grid(rowspan=4)
#turtle t
t = turtle.RawTurtle(maincanv)
c = turtle.RawTurtle(maincanv)
c.speed(5)
t.speed(5)
t.pu()
c.pu
c.color('black')

root.mainloop()
