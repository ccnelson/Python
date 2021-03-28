# gui class
# new tsp project
# C.NELSON 2019
# v1.0 updated 13/03
# Python 3.6
#################################

import turtle_func as tf
import builder_methods as bm
import art as art
import tkinter as tk  # needed for tk vars?
from tkinter import filedialog
import numpy as np
import csv
import genetic as g
#import pandas as pd


class GUI:
    def __init__(self):
        ######################### setup ##################################################################
        self.root = bm.ttk_setup()  # initalise tk
        self.tkvar1 = tk.IntVar()  # tk var (radio selection)
        self.tkvar2 = tk.IntVar()  # tk var (is circular)
        self.file_loc = None
        self.no_of_locs = None
        self.locations = None
        self.no_in_population = None
        ####### initial / options window #################################################################
        # MAKE UI
        # main frame
        self.frame_x1 = bm.build_frame(self.root, 0, 0)
        # sub frames
        self.frame1 = bm.build_frame(self.frame_x1, 0, 0)
        # main frame content
        self.label1 = bm.build_label(self.frame1, 0, 0, "Number of destinations:", 9)
        self.spin1 = bm.build_spinbox(self.frame1, 1, 0)
        self.check = bm.build_checkbox(self.frame1, 1, 1, "Circular", self.tkvar2)
        self.rad1 = bm.build_radio(self.frame1, 0, 1, "Generate random destinations:", 0, self.tkvar1, )
        self.rad1.bind("<Button-1>", self.radio_click)
        self.rad2 = bm.build_radio(self.frame1, 0, 2, "Input destinations:", 1, self.tkvar1, )
        self.rad2.bind("<Button-1>", self.radio_click)
        self.rad3 = bm.build_radio(self.frame1, 0, 3, "Load destination file:", 2, self.tkvar1, )
        self.rad3.bind("<Button-1>", self.radio_click)
        self.but1 = bm.build_button(self.frame1, 1, 2, "GO", self.go_to_main)
        # hidden widj 1 - add coordinates
        self.add_x_label = bm.build_label(self.frame1, 1, 4, "X", 8)
        self.add_y_label = bm.build_label(self.frame1, 2, 4, "Y", 8)
        self.add_x_label.grid_remove()
        self.add_y_label.grid_remove()
        self.addtolist = bm.build_button(self.frame1, 0, 5, "ADD", self.add_loc)
        self.addtolist.grid_remove()
        self.add_x = bm.build_entry(self.frame1, 1, 5)
        self.add_y = bm.build_entry(self.frame1, 2, 5)
        self.add_x.grid_remove()
        self.add_y.grid_remove()
        self.listboxes = bm.build_listbox(self.frame1, 0, 6)
        self.listboxes.grid_remove()
        # hidden widj 2 - choose file
        self.load_but = bm.build_button(self.frame1, 0, 8, "LOAD", self.load_loc)
        self.load_but.grid_remove()
        ###### main window #############################################################################
        # prepare frames
        # top row
        # main frame
        self.frame_x2 = bm.build_frame(self.root, 0, 0)
        # sub frames
        self.lframe = bm.build_label_frame(self.frame_x2, 0, 0, "map")
        self.mframe = bm.build_label_frame(self.frame_x2, 1, 0, "general info")
        self.rframe = bm.build_label_frame(self.frame_x2, 2, 0, "console output")
        # bottom row
        self.lbframe = bm.build_label_frame(self.frame_x2, 0, 1, "settings")
        self.mbframe = bm.build_label_frame(self.frame_x2, 1, 1, "controls")
        self.rbframe = bm.build_label_frame(self.frame_x2, 2, 1, "dataplots")
        # add canvas and turtle top left
        self.map_canv = bm.build_canvas(self.lframe, 0, 0)
        self.turtle, self.turtle_screen = tf.setup_turtle(self.map_canv)
        # message top mid
        self.general_info = bm.build_message(self.mframe, 0, 0, art.general_info)
        self.loc_list = bm.build_listbox(self.mframe, 0, 1)
        # bottom right right
        self.dataplot_canv = bm.build_square_canvas(self.rbframe, 0, 0)
        # lower left
        self.settings_panel_1 = bm.build_label(self.lbframe, 0, 0, " SPEED: ", 10)
        self.settings_panel_spin1 = bm.build_spinbox(self.lbframe, 1, 0)
        self.settings_panel_2 = bm.build_label(self.lbframe, 0, 1, " RANGE: ", 10)
        self.settings_panel_spin2 = bm.build_spinbox(self.lbframe, 1, 1)
        self.settings_panel_3 = bm.build_label(self.lbframe, 0, 2, " MUTATION: ", 10)
        self.settings_panel_spin3 = bm.build_spinbox(self.lbframe, 1, 2)
        self.settings_panel_4 = bm.build_label(self.lbframe, 0, 3, " MUTATION: ", 10)
        self.settings_panel_spin4 = bm.build_spinbox(self.lbframe, 1, 3)
        self.settings_panel_5 = bm.build_label(self.lbframe, 0, 4, " MUTATION: ", 10)
        self.settings_panel_spin5 = bm.build_spinbox(self.lbframe, 1, 4)
        self.settings_panel_6 = bm.build_label(self.lbframe, 0, 5, " MUTATION: ", 10)
        self.settings_panel_spin6 = bm.build_spinbox(self.lbframe, 1, 5)
        # lower mid
        self.control_button_1 = bm.build_button(self.mbframe, 0, 0, "START", self.begin)
        self.control_button_2 = bm.build_button(self.mbframe, 0, 1, "STOP", self.test_func)
        self.control_button_3 = bm.build_button(self.mbframe, 0, 2, "RESET", self.reset)
        self.control_button_4 = bm.build_button(self.mbframe, 1, 0, "SAVE", self.test_func)
        self.control_button_5 = bm.build_button(self.mbframe, 1, 1, "LOAD", self.test_func)
        self.control_button_6 = bm.build_button(self.mbframe, 1, 2, "UPLOAD", self.test_func)
        #self.control_button_7 = bm.build_button(self.mbframe, 2, 0, "NEUTRALISE", self.test_func)
        # upper right
        self.rtext = bm.build_text(self.rframe, 0, 0, 8, "other words", 15, 80)
        # hide main window until user clicks go
        self.frame_x2.grid_remove()

    ### intial window methods #########################################################################
    def radio_click(self, event):
        """ function deals with setup radiobox selection
        when user clicks on option """
        if str(event.widget) == ".!frame.!frame.!radiobutton":  # event comes from caller
            self.label1['state'] = 'enabled'  # enable widgets
            self.spin1['state'] = 'normal'
            self.check['state'] = 'enabled'
            self.listboxes.grid_remove()  # hide invalid options
            self.addtolist.grid_remove()
            self.add_x.grid_remove()
            self.add_x_label.grid_remove()
            self.add_y.grid_remove()
            self.add_y_label.grid_remove()
            self.load_but.grid_remove()
        elif str(event.widget) == ".!frame.!frame.!radiobutton2":
            self.label1['state'] = 'disabled'  # grey out invalid
            self.spin1['state'] = 'disabled'
            self.check['state'] = 'disabled'
            self.tkvar2.set(0)  # zero out chkbox var
            self.listboxes.grid()  # enable
            self.addtolist.grid()
            self.add_x.grid()
            self.add_x_label.grid()
            self.add_y.grid()
            self.add_y_label.grid()
            self.load_but.grid_remove()  # hide
        elif str(event.widget) == ".!frame.!frame.!radiobutton3":
            self.label1['state'] = 'disabled'
            self.spin1['state'] = 'disabled'
            self.check['state'] = 'disabled'
            self.tkvar2.set(0)  # zero out chkbox var
            self.load_but.grid()
            self.listboxes.grid_remove()
            self.addtolist.grid_remove()
            self.add_x.grid_remove()
            self.add_x_label.grid_remove()
            self.add_y.grid_remove()
            self.add_y_label.grid_remove()

    def load_loc(self):
        self.file_loc = filedialog.askopenfilename\
            (initialdir="/", title="Select file", filetypes=
            (("csv files", "*.csv"), ("all files", "*.*")))
        self.go_to_main()

    def go_to_main(self):
        tf.draw_grid(self.turtle, 200)
        self.radio_options()
        self.frame_x2.grid()
        self.frame_x1.grid_remove()

    def add_loc(self):
        self.listboxes.insert(0, [float(self.add_x.get()), float(self.add_y.get())])

    ### main window methods ########################################################
    def radio_options(self):
        if self.tkvar1.get() == 0:  # random locations
            self.no_of_locs = int(self.spin1.get())
            if self.tkvar2.get() == 0:  # not circular
                self.locations = np.round(np.random.uniform(low=-100.00, high=100.01, size=(self.no_of_locs, 2)), 1)
            elif self.tkvar2.get() == 1:  # is circular
                self.locations = self.circle_of_points(self.no_of_locs)
                self.turtle.setposition(0, 0)
        elif self.tkvar1.get() == 1:  # locations from listbox
            self.no_of_locs = int(self.listboxes.size())
            templist = self.listboxes.get(0, tk.END)
            revtemp = []  # listbox output reverse
            for _ in reversed(templist):
                revtemp.append(_)
            self.locations = np.array(revtemp)
        else:  # locations from file
            file = open(self.file_loc, newline='')
            reader = csv.reader(file)
            tmpload = []
            for row in reader:  # for each line
                x = float(row[0])  # make first item a float
                y = float(row[1])  # then second item
                tmpload.append([x, y])  # append to new list
            self.no_of_locs = len(tmpload)  # measure number of entries
            self.locations = np.array(tmpload)  # translate tmp list to np vectors
        self.no_in_population = self.no_of_locs * 8
        for i, l in enumerate(self.locations):
            tf.draw_point(self.turtle, l, i)
            self.loc_list.insert(0, "%s:%s" % (i, l))

    def circle_of_points(self, n):
        self.turtle.setpos(0, 0)
        self.turtle.setheading(90)
        self.turtle.forward(90)  # position circle
        self.turtle.setheading(180)
        x = []
        for i in range(n):
            self.turtle.pu()
            x.append(self.turtle.position())
            self.turtle.circle(90, 360 / n)  # (radius, extent)
        x = np.round(np.array(x), 1)
        return x

    def test_func(self):
        print(self.tkvar1, self.tkvar2)

    def reset(self):
        self.file_loc = None  # reset vars
        self.no_of_locs = None
        self.locations = None
        self.no_in_population = None
        self.frame_x2.grid_remove()  # swap frames
        self.frame_x1.grid()
        tf.reset_turt(self.turtle)  # clear drawings
        self.listboxes.delete(0, tk.END)  # empty listboxes
        self.loc_list.delete(0, tk.END)
        self.rtext.delete(1.0, tk.END)  # clear console
        self.general_info['text'] = ""

    @staticmethod  # this indicates the function doesnt need access to the class
    def send_to_console(console: object, content):
        console.insert('end', content)
        console.see('end')  # scroll to end

    def begin(self):
        print(self.no_of_locs, self.tkvar1, self.tkvar2)
        #tmp = "%i, %i, %i" % (self.no_of_locs, self.tkvar1.get(), self.tkvar2.get())
        self.rtext.delete(1.0, tk.END)
        #self.send_to_console(self.rtext, tmp)
        ####################
        # todo
        ####################
        #pd.set_option('display.max_colwidth', -1)
        ga = g.Ga(self.locations, console_out=self.rtext, turt=self.turtle)
        #self.send_to_console(self.rtext, ga.returnpop())
        self.general_info['text'] = ga.returninfo()
        ga.create_pop()
        ga.start_algo()




