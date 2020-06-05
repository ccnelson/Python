import tkinter as tk

def my_command():
    print("command")

def my_command2():
    print("commanded")

root = tk.Tk() # all our code goes here
root.geometry('800x600')

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0) # all file menu-items will be added here next
edit_menu = tk.Menu(menu_bar, tearoff=0)
view_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label="New", accelerator='Ctrl+N', compound='left', underline=0, command=my_command)
file_menu.add_command(label="Old", accelerator='Ctrl+O', compound='left', underline=0, command=my_command2)

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_separator()
menu_bar.add_cascade(label='View', menu=view_menu)

root.config(menu=menu_bar) 

root.mainloop()
