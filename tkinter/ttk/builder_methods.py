import tkinter as tk
from tkinter import ttk



def _build_frame(par, col, row):
    x = ttk.Frame(par)
    x.grid(column=col, row=row)
    return x


def _build_label_frame(par, col, row, lbl):
    x = ttk.LabelFrame(par, text=lbl)
    x.grid(column=col, row=row)
    return x


def _build_label(par, col, row, lbl, size):
    x = ttk.Label(par, text=lbl, font=("Courier", size))
    x.grid(column=col, row=row)
    return x


def _build_button(par, lbl, col, row, exe):
    x = ttk.Button(par, text=lbl, command=exe)
    x.grid(column=col, row=row, padx=5, pady=5, ipadx=5, ipady=5)
    return x


# text is a tk object NOT ttk
def _build_text(par, content, size, col, row, h, w):
    x = tk.Text(par, font=("Courier", size), bg='black', fg='lawngreen',
                height=h, width=w, insertbackground='white', highlightthickness=0)
    x.insert('end', content)
    x.grid(column=col, row=row)
    return x


def _build_yscroll_text(par, content, size, col, row, h, w):
    y = ttk.Scrollbar(par)
    x = tk.Text(par, font=("Courier", size), bg='black', fg='lawngreen',
                height=h, width=w, insertbackground='white', highlightthickness=0,
                yscrollcommand=y.set)
    x.grid(column=col, row=row)
    y.grid(column=col+1, row=row, sticky=tk.NS)
    x.insert('end', content)
    y.config(command=x.yview)

    return x, y



#def _build_yscroll(par, com, column, row):
#    x = ttk.Scrollbar(par, )



def _build_h_separator(par, col, row):
    x = ttk.Separator(par, orient='horizontal')
    x.grid(column=col, row=row, columnspan=3, sticky='ew')
    return x


# also tk object
def _build_spinbox(par, col, row):
    x = tk.Spinbox(par, from_=0, to=100, width=10)
    x.grid(column=col, row=row)
    return x


def _print_this():
    print("this...")
