# builder methods (ttk)
# new tsp project
# C.NELSON 2019
# v1.2 updated 01/03
# Python 3.6
#################################

import tkinter as tk
from tkinter import ttk


def ttk_setup():
    """ set up tk/ttk - return root (main parent) object """
    root = tk.Tk()
    root.title("Ternimal")
    root.wm_iconbitmap("favicon.ico")
    style = ttk.Style()
    style.theme_use('winnative')  # alt, classic, winnative, default, vista, xpnative, clam
    return root


def build_entry(par, col, row):
    x = tk.Entry(par)
    x['width'] = 5
    x.grid(column=col, row=row, padx=10, pady=2, ipadx=10, ipady=2)
    return x


def build_frame(par, col, row):
    """ input parent, column, row - return frame """
    x = ttk.Frame(par)
    x.grid(column=col, row=row)
    return x


def build_label_frame(par, col, row, lbl):
    """ input parent, column, row, label -
        return labelled frame """
    x = ttk.LabelFrame(par, text=lbl)
    x.grid(column=col, row=row)
    return x


def build_label(par, col, row, lbl, size):
    """ input parent, column, row, label -
            return label """
    x = ttk.Label(par, text=lbl, font=("Ariel", size))
    x.grid(column=col, row=row, padx=10, pady=2, ipadx=10, ipady=2)
    return x


def build_button(par, col, row, lbl, exe):
    """ input parent, column, row, label, function
     return button """
    x = ttk.Button(par, text=lbl, command=exe)
    x.grid(column=col, row=row, padx=1, pady=2, ipadx=1, ipady=2)
    return x


# tk object
def build_text(par, col, row, size, content, h, w):
    """ input parent, column, row, textsize, content,
    widjet height / width, return textbox """
    x = tk.Text(par, font=("Courier", size), bg='black', fg='lawngreen',
                height=h, width=w, insertbackground='white', highlightthickness=0)
    x.insert('end', content)
    x.grid(column=col, row=row)
    return x


def build_yscroll_text(par, col, row, size, content, h, w):
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
    """ input parent, column, row -
            return horizontal seperator """
    x = ttk.Separator(par, orient='horizontal')
    x.grid(column=col, row=row, columnspan=2, sticky='ew')
    return x


# tk object
def build_spinbox(par, col, row):
    """ input parent, column, row -
            return spinbox """
    x = tk.Spinbox(par, from_=12, to=100, width=10)
    x.grid(column=col, row=row, padx=10, pady=2, ipadx=10, ipady=2 )
    return x


# tk object
def build_canvas(par, col, row):
    """ input parent, column, row, return canvas"""
    x = tk.Canvas(par, width=400, height=250)
    x.grid(column=col, row=row)
    return x


# tk object
def build_square_canvas(par, col, row):
    """ input parent, column, row, return canvas"""
    x = tk.Canvas(par, width=200, height=200)
    x.grid(column=col, row=row)
    return x


def build_radio(par, col, row, text, val, var):
    """ var is tk.IntVar() accessed through x.get()
    val is value of option """
    x = ttk.Radiobutton(par, text=text, variable=var, value=val)
    x.grid(column=col, row=row, padx=10, pady=2, ipadx=10, ipady=2)
    return x


def build_checkbox(par, col, row, text, var):
    x = ttk.Checkbutton(par, text=text, variable=var)
    x.grid(column=col, row=row, padx=10, pady=2, ipadx=10, ipady=2)
    return x


def build_listbox(par, col, row):
    """ input parent, column, row -
            return listbox """
    x = tk.Listbox(par, cursor='hand2', selectmode=tk.SINGLE, height=13, width=20)
    x.grid(column=col, row=row, rowspan=4, columnspan=2)
    return x


def build_message(par, col, row, contents):
    """ to alter text use
    message_widjet['text'] = 'some text'"""
    x = tk.Message(par, text=contents, width=245)
    x.grid(column=col, row=row)
    return x

