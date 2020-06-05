import tkinter as tk
from tkinter import ttk

## helper functions ###
def _build_label_frame(par, col, row, lbl):
    x = ttk.LabelFrame(par, text=lbl)
    x.grid(column=col, row=row)
    return x

def _build_label(par, col, row, lbl, size):
    x = ttk.Label(par, text=lbl, font=("Courier", size))
    x.grid(column=col, row=row)
    return x

def _build_button(par, lbl, col, row, exe):
    x = ttk.Button(par, text=lbl, command=exe, style='danger.TButton')
    x.grid(column=col, row=row, padx=5, pady=5, ipadx=5, ipady=5)
    return x

def _build_text(par, content, size, col, row, h, w):
    x = tk.Text(par, font=("Courier", size), bg='black', fg='lawngreen', height=h, width=w, insertbackground='white', highlightthickness=0)
    x.insert('end', content)
    x.grid(column=col, row=row)
    return x

def _build_h_separator(par, col, row):
    x = ttk.Separator(par, orient='horizontal')
    x.grid(column=col, row=row, columnspan=3, sticky='ew')

def _print_this():
    print("this...")

## initial config ###
root = tk.Tk()
root.configure(bg='black')
style = ttk.Style()
style.configure('.', font='Arial 14', foreground='lawngreen', background='black', padding=15)
style.configure('danger.TButton', font='Times 12', foreground='red', padding=1) #extension (danger) to default style (TButton)

## build GUI ##

## mainframe ##
mainframe = _build_label_frame(root, 0, 0, "main frame")
main_label = _build_label(mainframe, 0, 0, "mainframe text", 88)
main_label.grid(columnspan = 3)
## 2nd frame ##
second_frame = _build_label_frame(mainframe, 0, 2, "2nd frame")
second_frame_label = _build_label(second_frame, 0, 0, "2nd frame label", 30)
second_frame_button = _build_button(second_frame, "2nd frame button", 0, 1, _print_this)
## 3rd frame ##
third_frame = _build_label_frame(mainframe, 1, 2, "3rd frame")
third_frame_label = _build_label(third_frame, 0, 0, "3rd frame label", 30)
third_frame_button = _build_button(third_frame, "3rd frame button", 0, 1, _print_this)
## separator ##
sep = _build_h_separator(mainframe, 0, 1)
## 4th frame ##
fourth_frame = _build_label_frame(mainframe, 0, 3, "4th frame")
fourth_frame_label = _build_label(fourth_frame, 0, 0, "4th frame label", 30) 
fourth_frame_button = _build_button(fourth_frame, "4th frame button", 0, 1, _print_this)

## prog starts here ##

root.mainloop()

########################################################################################



