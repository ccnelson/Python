import tkinter as tk
from tkinter import ttk


cont = """\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x                                                x
x                                                x
x           t                                    x
x        t T                xxxxxxxxxxxxxx       x
x       t   t               x     D      x       x
x         t t               O            O       x
x        T                  x  h         x       x
x                           xxxxxxx xxoxxx       x
x                                                x
x                                                x
x                                                x
x                                                x
x                                                x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

## helper functions ###

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

def _build_alert_button(par, lbl, col, row, exe):
    x = ttk.Button(par, text=lbl, command=exe, style='danger.TButton')
    x.grid(column=col, row=row, padx=5, pady=5, ipadx=5, ipady=5)
    return x

def _build_text(par, content, size, col, row, h, w):
    x = tk.Text(par, font=("Courier", size), bg='black', fg='lawngreen',
                height=h, width=w, insertbackground='white', highlightthickness=0)
    x.insert('end', content)
    x.grid(column=col, row=row)
    return x

def _build_h_separator(par, col, row):
    x = ttk.Separator(par, orient='horizontal')
    x.grid(column=col, row=row, columnspan=3, sticky='ew')
    return x

def _build_spinbox(par, col, row):
    x = tk.Spinbox(par, from_=0, to=100, width=10)
    x.grid(column=col, row=row)

def _print_this():
    print("this...")

## initial config ###
root = tk.Tk()
root.configure(bg='black')
style = ttk.Style()

### STYLE OPTIONS ##
style.configure('.', font='Arial 14', foreground='lawngreen', background='black',
                padding=15)
#style.theme_use('clam')
style.theme_use('alt')
#style.theme_use('winnative')
#style.theme_use('default')
#style.theme_use('classic')
#style.theme_use('vista')#default
#style.theme_use('xpnative')

style.configure('danger.TButton', font='Times', foreground='red', padding=1)
#above is extension (danger) to default style (TButton)

## build GUI ##

## mainframe ##
mainframe = _build_frame(root, 0, 0)
main_label = _build_label(mainframe, 0, 0, "Forest", 30)
main_label.grid(columnspan = 3)

## separator ##
sep = _build_h_separator(mainframe, 0, 1)

## map frame##
map_frame = _build_label_frame(mainframe, 0, 2, "MAP")
map_frame_label = _build_label(map_frame, 0, 0, "wasd", 15)
map_frame_label.grid(columnspan=2)
map_frame_text = _build_text(map_frame, cont, 10, 0, 1, 15, 50)
map_frame.grid(rowspan=2)

## 2nd frame ##
stats_frame = _build_label_frame(mainframe, 1, 2, "STATS")
stats_frame_label = _build_label(stats_frame, 0, 0, "Health:     10", 10)
stats_frame_label_2 = _build_label(stats_frame, 0, 1, "Will:        8", 10)
stats_frame_label_3 = _build_label(stats_frame, 0, 2, "Strength:    7", 10)
stats_frame_label_4 = _build_label(stats_frame, 0, 3, "Motivation:  8", 10)
stats_frame_label_5 = _build_label(stats_frame, 0, 4, "Honour:      6", 10)
stats_frame_label_6 = _build_label(stats_frame, 0, 5, "Coin:        0", 10)


#3rd frame
third_frame = _build_label_frame(mainframe, 1, 3, "MISSIONS")
third_frame_label = _build_label(third_frame, 0, 0, "Visit Bob     ", 10)
third_frame_label_2 = _build_label(third_frame, 0, 1, "Shine shoe    ", 10)
third_frame_label_3 = _build_label(third_frame, 0, 2, "Eat grape     ", 10)
third_frame_label_4 = _build_label(third_frame, 0, 3, "              ", 10)
third_frame_label_5 = _build_label(third_frame, 0, 4, "              ", 10)



## prog starts here ##

root.mainloop()

########################################################################################



