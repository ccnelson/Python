# ttk builder methods
# customised 4 turtle gen algo
# C.NELSON 2018
# Python 3.7
#################################
import tkinter as tk
from tkinter import ttk


def build_frame(par, col, row):
    x = ttk.Frame(par)
    x.grid(column=col, row=row)
    return x


def build_label_frame(par, col, row, lbl):
    x = ttk.LabelFrame(par, text=lbl)
    x.grid(column=col, row=row)
    return x


def build_label(par, col, row, lbl, size):
    x = ttk.Label(par, text=lbl, font=("Courier", size))
    x.grid(column=col, row=row)
    return x


def build_button(par, lbl, col, row, exe):
    x = ttk.Button(par, text=lbl, command=exe)
    x.grid(column=col, row=row, padx=1, pady=1, ipadx=1, ipady=1)
    return x


# text is a tk object NOT ttk
def build_text(par, content, size, col, row, h, w):
    x = tk.Text(par, font=("Courier", size), bg='black', fg='lawngreen',
                height=h, width=w, insertbackground='white', highlightthickness=0)
    x.insert('end', content)
    x.grid(column=col, row=row)
    return x


def build_yscroll_text(par, content, size, col, row, h, w):
    y = ttk.Scrollbar(par)
    x = tk.Text(par, font=("Courier", size), bg='black', fg='lawngreen',
                height=h, width=w, insertbackground='white', highlightthickness=0,
                yscrollcommand=y.set)
    x.grid(column=col, row=row)
    y.grid(column=col+1, row=row, sticky=tk.NS)
    x.insert('end', content)
    y.config(command=x.yview)
    return x, y


def build_h_separator(par, col, row):
    x = ttk.Separator(par, orient='horizontal')
    x.grid(column=col, row=row, columnspan=1, sticky='ew')
    return x


# also tk object
def build_spinbox(par, col, row):
    x = tk.Spinbox(par, from_=1, to=1000, width=10)
    x.grid(column=col, row=row)
    return x


def build_canvas(par, col, row):
    x = tk.Canvas(par, width=600, height=500)
    x.grid(column=col, row=row)
    return x


def build_radio(par, var, text, val, col, row):
    """ var is tk.IntVar() accessed through x.get()
    val is value of option """
    x = ttk.Radiobutton(par, text=text, variable=var, value=val)
    x.grid(column=col, row=row)
    return x


def build_checkbox(par, text, var, col, row):
    x = ttk.Checkbutton(par, text=text, variable=var)
    x.grid(column=col, row=row)
    return
