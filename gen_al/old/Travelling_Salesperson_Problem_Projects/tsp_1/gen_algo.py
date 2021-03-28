# Genetic algorithm
# for TSP style probelems
# C.NELSON 2018
########################

import builder_methods as bm
import crossovers as co
# from dataclasses import dataclass # not in 3.6 you dont
import itertools
import mutators as mu
# import numpy as np
import random
import statistics
import tkinter as tk
from tkinter import ttk
import turtle
import turtle_func as tf
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

## MATPLOTLIB IS USING DEPRECATED COMMANDS!! ##


# @dataclass  # reverted to Python 3.6 to use anaconda
# class Gene:
#     chromo: any
#     pos: int
#     dist: int = 0
#     rank: int = 0
#     score: int = 0
#     sigscal: int = 0
#     fit_prop: int = 0

class Gene:
    def __init__(self, chromo, pos):
        self.chromo = chromo
        self.pos = pos
        self.dist = 0
        self.rank = 0
        self.score = 0
        self.sigscal = 0
        self.fit_prop = 0

    def __repr__(self):
        return 'Gene(Chromo:%r|Pos:%r|Dist:%r|Rank:%r|Score:%r|Sigma:%r|FitProp:%r)' % \
               (self.chromo, self.pos, self.dist, self.rank, self.score, self.sigscal, self.fit_prop)


class DataStore:
    loc_coords = []
    loc_values = []
    g_list = []  # store population of Gene class
    stan_dev = 0
    mean = 0
    par_list = []
    par_list2 = []
    generation = 0
    tabu_list = []
    avg_scores = []
    stan_dev_list = []
    sigma_list = []
    fitprop_list = []
    matplotfig = Figure(figsize=(6, 4), dpi=100)  # initiate matplotlib figure
    plot1 = None  # matplotfig.add_subplot(111)
    plot2 = None  # matplotfig.add_subplot(111)
    matplotfig2 = Figure(figsize=(6, 4), dpi=100)  # initiate matplotlib figure
    plot3 = None  # matplotfig.add_subplot(111)

class Location:
    """ each location initialised with coords
        wihch are then illustrated """
    count = 0

    def __init__(self, switch, coords):
        if switch == 0:
            self.pos = turtle.Vec2D(random.randrange(-200, 201),
                                    random.randrange(-200, 201))
        elif switch == 1:
            self.pos = turtle.Vec2D(coords[0], coords[1])
        tf.draw_point(turk, self.pos, Location.count)
        send_to_console(right_text, "Loc %r pos: %r \n" % (Location.count, self.pos))
        Location.count += 1


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def send_to_console(console: object, content):
    console.insert('end', content)
    console.see('end')  # scroll to end


def clear_consoles():
    right_text.delete(1.0, 'end')
    left_text.delete(1.0, 'end')
    bottom_text.delete(1.0, 'end')
    leftright_text.delete(1.0, 'end')


def local_draw_grid(turt, size):
    if circvar.get() == 0:
        tf.draw_grid(turt, size)  # call external grid draw
        rframe_button_5.destroy()  # disable grid draw button
    elif circvar.get() == 1:
        send_to_console(right_text, "\nNo grid for circular orientation\n")


def circle_of_points_2(turt, n):
    gary.reset()  # remove any grid
    turt.setheading(90)     #
    turt.forward(140)       # position circle
    turt.setheading(180)    # within viewable area
    turt.forward(20)        #
    x = []
    for i in range(n):
        turt.pu()
        x.append(turt.position())
        turt.circle(150, 360/n)  # (radius, extent)
    return x


def gen_loc(n):
    DataStore.loc_coords = []
    Location.count = 0
    turk.reset()
    bob.reset()
    right_text.delete(1.0, 'end')
    send_to_console(right_text, "Possible combinations: %r\n" % "{:,}".format(factorial(n)))
    if circvar.get() == 0:
        DataStore.loc_coords = [Location(0, 0) for i in range(n)]
    elif circvar.get() == 1:
        list_coords = circle_of_points_2(turk, n)
        for i in list_coords:
            DataStore.loc_coords.append(Location(1, i))


def gen_pop(quantity):
    DataStore.g_list = []
    # starts from 1 as 0 will always be first AND last
    DataStore.loc_values = [str(i) for i in range(1, len(DataStore.loc_coords))]
    for j in range(quantity):
        random.shuffle(DataStore.loc_values)
        DataStore.g_list.append(Gene(list(DataStore.loc_values), j)) # other values are default 0s
    send_to_console(right_text, "Generation 0\n")
    send_to_console(leftright_text, "Generation: %r\n" % DataStore.generation)
    send_to_console(leftright_text, "Initial population: \n")
    send_to_console(leftright_text, "*journey starts and ends at zero* \n")
    for k in DataStore.g_list:
        send_to_console(leftright_text, "\n%r:" % (k.pos))
        for x in k.chromo:
            send_to_console(leftright_text, "%r" % x)


def traverse_pop():
    send_to_console(left_text, "Generation: %r\n" % DataStore.generation)
    send_to_console(left_text, "Distances: \n")
    for inhab in DataStore.g_list:
        inhab.dist = tf.trav_coord_ret_val(bob, DataStore.loc_coords, inhab.chromo)
        send_to_console(left_text, "%r : %r \n" % (inhab.pos, inhab.dist))
    

def gen_score():

    x = sorted(DataStore.g_list, key=lambda g: g.dist)
    scores = []
    for index, instance in enumerate(x):
        DataStore.g_list[instance.pos].rank = index
        DataStore.g_list[instance.pos].score = 10000 / DataStore.g_list[instance.pos].dist  # store score while here
        scores.append(DataStore.g_list[instance.pos].score)  # make a list
    DataStore.mean = statistics.mean(scores)
    DataStore.stan_dev = statistics.pvariance(scores) ** 0.5
    send_to_console(right_text, "mean score: %r\nstandard deviation: %r\n" % (DataStore.mean, DataStore.stan_dev))
    sigscal_list = []
    fp_list = []
    for g in DataStore.g_list:
        if DataStore.stan_dev > 0:
            g.sigscal = ((g.score - DataStore.mean) / (2 * DataStore.stan_dev))
        g.fit_prop = g.score / DataStore.mean
        g.dist = round(g.dist, 3)
        g.score = round(g.score, 3)
        g.sigscal = round(g.sigscal, 3)
        sigscal_list.append(g.sigscal)
        fp_list.append(g.fit_prop)
        g.fit_prop = round(g.fit_prop, 3)
    send_to_console(bottom_text, "Scores:\n")
    for a in DataStore.g_list:
        send_to_console(bottom_text, "%r\n" % a)
    DataStore.avg_scores.append(DataStore.mean)
    DataStore.stan_dev_list.append(DataStore.stan_dev)
    DataStore.sigma_list.append(statistics.mean(sigscal_list))
    DataStore.fitprop_list.append(statistics.mean(fp_list))

    if radvar2.get() <= 1:  # check speed isnt 'run till convergence'
        plot_stuff()


def choose_parents():
    send_to_console(bottom_text, "Parents: \n")
    DataStore.par_list = []
    DataStore.par_list2 = []
    #  top 4 ranked become parents
    for i in range(4):
        for g in DataStore.g_list:
            if g.rank == i:
                DataStore.par_list.append(g)
    #  add 2 fitness prop to 2nd parent list, 2 = faster convergence
    if propvar.get() == 1:
        w = []
        for m in DataStore.g_list:
            w.append(m.fit_prop)
        DataStore.par_list2 = list(random.choices(DataStore.g_list, weights=w, k=2))

    for a in DataStore.par_list:
        send_to_console(bottom_text, "chromo:%rrank:%r\n" % (a.chromo, a.rank))
    for b in DataStore.par_list2:
        send_to_console(bottom_text, "chromo:%rrank:%r\n" % (b.chromo, b.rank))

    # use tabu search to refine parent list
    #
    # XOVER seems ok with tabu now... keep testing
    #
    # TODO
    #DataStore.tabu_list = []
    if tabuvar.get() == 1:
        if DataStore.stan_dev > 0.1:
            if DataStore.generation % 2 == 0:
                pars = list(DataStore.par_list)
                for ind, par in enumerate(pars):  # loop through them
                    m = mu.exchange(par.chromo)  # exchange mutation
                    #print("mutation:", m)
                    while m in DataStore.tabu_list:
                        m = mu.exchange(par.chromo)
                        print("Reroll:", m)
                    new_dist = tf.trav_coord_ret_val(bob, DataStore.loc_coords, m)
                    #print("Old gene:", DataStore.par_list[ind])
                    #print("old dist:", par.dist)
                    #print("new dist:", new_dist)
                    if new_dist < par.dist:
                        DataStore.par_list[ind].chromo = m
                        DataStore.par_list[ind].dist = new_dist
                        print("new chromo: ", m)
                        print("stored: ", DataStore.par_list[ind])
                    DataStore.tabu_list.append(m)
                    #print("Tabu list:", DataStore.tabu_list)
                if len(DataStore.tabu_list) > Location.count*4:
                    DataStore.tabu_list = []


def intercourse(par1, par2, ind1, ind2):
    send_to_console(bottom_text, "PARENT 1:%r PARENT 2:%r \n" % (par1, par2))
    a, b = co.cross_over(list(par1), list(par2), radvar1.get())  # lists stop us changing value inline
    a = mu.mutation(a, mutvar.get())
    b = mu.mutation(b, mutvar.get())
    DataStore.g_list.append(Gene(a, ind1))
    DataStore.g_list.append(Gene(b, ind2))
    send_to_console(bottom_text, "CHILD  1:%r CHILD  2:%r\n" % (a, b))


def strongest_survive():
    for i in DataStore.par_list:
        DataStore.g_list.append(Gene(i.chromo, len(DataStore.g_list)))


def breed_population():
    DataStore.g_list = []
    count = 0
    val = [0,1,2,3]
    #  ranked parents
    for h in range(2):  # increases size of pop *2
        for i in itertools.permutations(val, 4):  # 144 offspring, 24(permutations)*6(offspring)
            intercourse(DataStore.par_list[i[0]].chromo, DataStore.par_list[i[1]].chromo, count, count+1)
            intercourse(DataStore.par_list[i[0]].chromo, DataStore.par_list[i[2]].chromo, count+2, count+3)
            intercourse(DataStore.par_list[i[0]].chromo, DataStore.par_list[i[3]].chromo, count+4, count+5)
            count += 6
    #  fit prop parents
    if propvar.get() == 1:
        val = [0, 1]
        for i in itertools.permutations(val, 2):  # 144 offspring, 24(permutations)*6(offspring)
            intercourse(DataStore.par_list2[i[0]].chromo, DataStore.par_list2[i[1]].chromo, count, count+1)
            intercourse(DataStore.par_list2[i[1]].chromo, DataStore.par_list2[i[0]].chromo, count+2, count+3)
            count += 4
    send_to_console(bottom_text, "New population\n")
    DataStore.generation += 1
    if radvar2.get() == 1:
        ts.update()
    send_to_console(right_text, "\n\t ## Generation: %r ##\n" % DataStore.generation)
    send_to_console(bottom_text, "\n\t ## Generation: %r ##\n" % DataStore.generation)
    send_to_console(leftright_text, "Generation: %r\n" % DataStore.generation)
    if strongvar.get() == 1:
        strongest_survive()  # keep fittest
    for z in DataStore.g_list:
        send_to_console(leftright_text, "\n%r:" % (z.pos))
        for x in z.chromo:
            send_to_console(leftright_text, "%r" % x)


def auto_play():
    DataStore.avg_scores = []  # reset scores
    DataStore.stan_dev_list = []
    DataStore.sigma_list = []
    DataStore.fitprop_list = []
    DataStore.matplotfig.clf()  # clear matplotlib figure
    right_canvas.draw()
    DataStore.matplotfig2.clf()
    right_canvas2.draw()
    DataStore.tabu_list = []  # clear tabu list
    rframe_button_6['state'] = 'disabled'
    clear_consoles()
    bob.reset()
    DataStore.generation = 0
    if radvar2.get() == 0:
        ts.tracer(1, 1)  # slow
    elif radvar2.get() == 1:
        ts.tracer(0, 0)  # faster (slowed by ts.update)
    elif radvar2.get() == 2:
        ts.tracer(0, 0)  # fastest
    send_to_console(right_text, "\n...AUTOPLAY...\n")
    gen_loc(int(rframe_spinbox.get()))
    gen_pop(int(rframe_spinbox_2.get()))
    traverse_pop()
    gen_score() # this needs to occur before loop so stan_dev > 0
    while DataStore.stan_dev > 0:
        choose_parents()
        breed_population()
        traverse_pop()
        gen_score()
    total = int(rframe_spinbox_2.get()) + (len(DataStore.g_list) * (DataStore.generation - 1))
    send_to_console(right_text, "\n\t---CONVERGENGE---\n")
    send_to_console(right_text, "\n\tTotal population = %r\n" % total)
    send_to_console(left_text, "\n\t***FINISHED***\n")
    send_to_console(leftright_text, "\n\n\t***FINISHED***\n")
    send_to_console(bottom_text, "\n\t***FINISHED***\n")
    rframe_button_6['state'] = 'normal'
    tf.draw_coord(bob, DataStore.loc_coords, DataStore.g_list[0].chromo)  # draw final solution
    plot_stuff()


def plot_stuff():
    # plot 1 and 2
    DataStore.plot1 = DataStore.matplotfig.add_subplot(111)
    DataStore.plot1.set_xlabel('generation')
    #DataStore.plot2 = DataStore.matplotfig.add_subplot(111)  # cannot plot 2 lines in same graph nowadays
    DataStore.plot1.set_ylabel('avg. score')
    DataStore.plot1.plot(DataStore.avg_scores)
    #DataStore.plot2.plot(DataStore.stan_dev_list)
    # plot 3
    DataStore.plot3 = DataStore.matplotfig2.add_subplot(111)
    DataStore.plot3.plot(DataStore.sigma_list)
    # DataStore.plot3.scatter(DataStore.fitprop_list, DataStore.sigma_list)
    DataStore.plot3.set_title('avg. sigma scaled scores')
    right_canvas.draw()
    right_canvas2.draw()


def do_nothing():
    print("i didnt do anything")


# setup
root = tk.Tk()
root.title("Travelling Salesman Genetic Algorithm")
style = ttk.Style()
style.theme_use('alt')

# tk variables
radvar1 = tk.IntVar()  # tk radio button var
radvar1.set(1)
radvar2 = tk.IntVar()
radvar2.set(1)
circvar = tk.IntVar()
propvar = tk.IntVar()
mutvar = tk.IntVar()
strongvar = tk.IntVar()
tabuvar = tk.IntVar()

# gui
# left side
lframe = bm.build_frame(root, 0, 0)
canv = bm.build_canvas(lframe, 0, 1)
canv.grid(columnspan=4)
left_text, left_text_s  = bm.build_yscroll_text(lframe, "...general info...\n", 10, 0, 2, 10, 32)
leftright_text, leftright_text_s = bm.build_yscroll_text(lframe, "...more general info...\n", 10, 2, 2, 10, 54)
bframe = bm.build_frame(root, 0, 1)
bframe.grid(columnspan=3, sticky=tk.W)
bottom_text, bottom_text_s  = bm.build_yscroll_text(bframe, "...detailed info...\n", 8, 0, 0, 10, 180)
# right side
# settings
rframe = bm.build_frame(root, 1, 0)
plot_frame = bm.build_frame(root, 2, 0)
plot_frame.grid(rowspan=3)
rframe_int_frame = bm.build_frame(rframe, 0, 0)
rframe_data_1 = bm.build_label(rframe_int_frame, 0, 0, "locations", 10)
rframe_spinbox = bm.build_spinbox(rframe_int_frame, 0, 1)
rframe_spinbox.delete(0)  # set defaults
rframe_spinbox.insert('end', 8)
seperator = bm.build_h_separator(rframe_int_frame, 0, 2)
rframe_data_2 = bm.build_label(rframe_int_frame, 0, 3, "init pop", 10)
rframe_spinbox_2 = bm.build_spinbox(rframe_int_frame, 0, 4)
rframe_spinbox_2.delete(0)
rframe_spinbox_2.insert('end', 500)
seperator0 = bm.build_h_separator(rframe_int_frame, 0, 5)
check2 = bm.build_checkbox(rframe_int_frame, "circular", circvar, 0, 6)
seperator1 = bm.build_h_separator(rframe_int_frame, 0, 7)
rframe_int_label = bm.build_label(rframe_int_frame, 0, 8, "UPDATE PER:", 10)
rad5 = bm.build_radio(rframe_int_frame, radvar2, "gene", 0, 0, 9)
rad6 = bm.build_radio(rframe_int_frame, radvar2, "generation", 1, 0, 10)
rad7 = bm.build_radio(rframe_int_frame, radvar2, "convergence", 2, 0, 12)
seperator3 = bm.build_h_separator(rframe_int_frame, 0, 13)
check3 = bm.build_checkbox(rframe_int_frame, "inject proportionate", propvar, 0, 14)
seperator4 = bm.build_h_separator(rframe_int_frame, 0, 15)
check4 = bm.build_checkbox(rframe_int_frame, "strongest survive", strongvar, 0, 16)
seperator5 = bm.build_h_separator(rframe_int_frame, 0, 17)
rframe_x_label = bm.build_label(rframe_int_frame, 0, 18, "X-OVER", 10)
rad1 = bm.build_radio(rframe_int_frame, radvar1, "random", 0, 0, 19)
rad2 = bm.build_radio(rframe_int_frame, radvar1, "position based", 1, 0, 20)
rad3 = bm.build_radio(rframe_int_frame, radvar1, "order based", 2, 0, 21)
rad4 = bm.build_radio(rframe_int_frame, radvar1, "partially mapped", 3, 0, 22)
seperator6 = bm.build_h_separator(rframe_int_frame, 0, 23)
rframe_m_label = bm.build_label(rframe_int_frame, 0, 24, "MUTATION", 10)
rad8 = bm.build_radio(rframe_int_frame, mutvar, "random", 0, 0, 25)
rad9 = bm.build_radio(rframe_int_frame, mutvar, "displaced inversion", 1, 0, 26)
rad10 = bm.build_radio(rframe_int_frame, mutvar, "displacement", 2, 0, 27)
rad12 = bm.build_radio(rframe_int_frame, mutvar, "exchange", 3, 0, 28)
rad13 = bm.build_radio(rframe_int_frame, mutvar, "insertion", 4, 0, 29)
rad14 = bm.build_radio(rframe_int_frame, mutvar, "inversion", 5, 0, 30)
rad15 = bm.build_radio(rframe_int_frame, mutvar, "shuffle", 6, 0, 31)
seperator7 = bm.build_h_separator(rframe_int_frame, 0, 32)
check5 = bm.build_checkbox(rframe_int_frame, "tabu filter", tabuvar, 0, 33)
# text
right_text, right_text_s = bm.build_yscroll_text(rframe_int_frame, " ", 10, 1, 0, 35, 50)
right_text.grid(rowspan=34, columnspan=1)
right_text_s.grid(rowspan=34)
# buttons
rframe_button_6 = bm.build_button(rframe_int_frame, "go", 1, 34, auto_play)
rframe_button_5 = bm.build_button(rframe_int_frame, "draw\ngrid", 0, 34, lambda: local_draw_grid(gary, 400))
#matplotstuff
#canv1
right_canvas = FigureCanvasTkAgg(DataStore.matplotfig, plot_frame)
right_canvas.get_tk_widget().grid(column=0, row=0, sticky=tk.N)
#canv2
right_canvas2 = FigureCanvasTkAgg(DataStore.matplotfig2, plot_frame)
right_canvas2.get_tk_widget().grid(column=0, row=1, sticky=tk.S)

# turtle turk
turk = turtle.RawTurtle(canv)  # draws locations
bob = turtle.RawTurtle(canv)  # draws journeys
gary = turtle.RawTurtle(canv)  # draws grid
turk.speed(0)
bob.speed(0)
gary.speed(0)
turk.pu()
bob.pu()
gary.pu()
turk.hideturtle()  # hideturtle
bob.hideturtle()
gary.hideturtle()
ts = turk.getscreen()  # return screen object
ts.bgcolor('black')  # change background colour

# go
root.mainloop()
