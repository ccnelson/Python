import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.configure(bg='black')
style = ttk.Style()
style.configure('.', font='Arial 14', foreground='lawngreen', background='black')
style.configure('danger.TButton', font='Times 12', foreground='red', padding=1)

x = ttk.Label(root, text="some text")
y = ttk.Button(root, text="this", style='danger.TButton')

x.pack()
y.pack()

root.mainloop()
