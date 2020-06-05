import tkinter as tk

root = tk.Tk()

class Frame_contents():
    def __init__(self, p): 
        self.menu_bar = tk.Menu(p)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='new')
        self.file_menu.add_command(label='old')
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        self.text_display = tk.Text(p, height=10, width=30)
        self.button1 = tk.Button(p, text='button1')
        self.button2 = tk.Button(p, text='button2')
        self.button3 = tk.Button(p, text='button3')
        self.button4 = tk.Button(p, text='button4')
        self.exit_button = tk.Button(p, text='exit', command=root.destroy)
        
    def packem(self):
        self.text_display.grid(column=0, row=0, columnspan=3, ipadx=3, ipady=3, padx=10, pady=10)
        self.button1.grid(column=0, row=1, ipadx=3, ipady=3, padx=10, pady=10)
        self.button2.grid(column=1, row=1, ipadx=3, ipady=3, padx=10, pady=10)
        self.button3.grid(column=0, row=2, ipadx=3, ipady=3, padx=10, pady=10)
        self.button4.grid(column=1, row=2, ipadx=3, ipady=3, padx=10, pady=10)
        self.exit_button.grid(column=2, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        
class Frames():
    def __init__(self, p):
        self.frame1 = tk.Frame(p, bg='khaki')
        self.frame2 = tk.Frame(p)

    def packem(self):
        self.frame1.grid(column=0, row=0)
        self.frame2.grid(column=1, row=0)

frames_1 = Frames(root)
frames_1.packem()

set1 = Frame_contents(frames_1.frame1)
set2 = Frame_contents(frames_1.frame2)

set1.packem()
set2.packem()
set2.exit_button.grid_remove()

root.config(menu=set1.menu_bar)
root.mainloop()
