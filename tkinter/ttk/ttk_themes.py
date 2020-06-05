import tkinter as tk
from tkinter import ttk

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

#### THEMES ########################
# determined via
# s = ttk.Style()
# s.theme_names() # for a list
# s.these_use() # for current theme

def clamtheme():
    style.theme_use('clam')

def winnativetheme():
    style.theme_use('winnative')

def defaulttheme():
    style.theme_use('default')

def classictheme():
    style.theme_use('classic')

def vistatheme():
    style.theme_use('vista')

def xpnativetheme():
    style.theme_use('xpnative')

def alttheme():
    style.theme_use('alt')

#####################################

## initial config ###
root = tk.Tk()
style = ttk.Style()

### STYLE OPTIONS ##
## configure default
#root.configure(bg='black')
#style.configure('.', font='Arial 14', foreground='lawngreen', background='black',
#                padding=15)
## list of themes ##
#style.theme_use('clam')
#style.theme_use('alt')
#style.theme_use('winnative')
#style.theme_use('default')
#style.theme_use('classic')
#style.theme_use('vista')#default
#style.theme_use('xpnative')
## extension (danger) to default style (TButton) ##
style.configure('danger.TButton', font='Times 12', foreground='red', padding=1)
## changing themes removes effect?

## build GUI ##

## mainframe ##
mainframe = _build_frame(root, 0, 0)
mainframe.grid(columnspan=7)
main_label = _build_label(mainframe, 0, 0, "mainframe text", 88)
main_label.grid(columnspan = 3)

# theme buttons
main_button_1 = _build_button(root, "clam", 0, 1, clamtheme)
main_button_2 = _build_button(root, "winnative", 1, 1, winnativetheme)
main_button_3 = _build_button(root, "default", 2, 1, defaulttheme)
main_button_4 = _build_button(root, "classic", 3, 1, classictheme)
main_button_5 = _build_button(root, "vista", 4, 1, vistatheme)
main_button_6 = _build_button(root, "xpnative", 5, 1, xpnativetheme)
main_button_7 = _build_button(root, "alt", 6, 1, alttheme)

## separator ##
sep = _build_h_separator(mainframe, 0, 1)

## map frame##
map_frame = _build_label_frame(mainframe, 0, 2, "MAP")
map_frame_label = _build_label(map_frame, 0, 0, "wasd", 15)
map_frame_label.grid(columnspan=2)
map_frame_text = _build_text(map_frame, "words", 10, 0, 1, 15, 50)
map_frame.grid(rowspan=2)

## 2nd frame ##
second_frame = _build_label_frame(mainframe, 1, 2, "2nd frame")
second_frame_label = _build_label(second_frame, 0, 0, "2nd frame label", 30)
second_frame_label.grid(columnspan=2)
second_frame_button = _build_button(second_frame, "2nd frame button", 0, 1,
                                    _print_this)
second_frame_spinbox = _build_spinbox(second_frame, 1, 1)
second_frame_spinbox_2 = _build_spinbox(second_frame, 1, 2)

#3rd frame
third_frame = _build_label_frame(mainframe, 1, 3, "3rd frame")
third_frame_label = _build_label(third_frame, 0, 0, "3rd frame label", 30)
third_frame_label.grid(columnspan=2)
third_frame_button = _build_alert_button(third_frame, "3rd frame button", 0, 1,
                                   _print_this)
third_frame_spinbox = _build_spinbox(third_frame, 1, 1)
third_frame_spinbox_2 = _build_spinbox(third_frame, 1, 2)

## prog starts here ##

root.mainloop()

########################################################################################



