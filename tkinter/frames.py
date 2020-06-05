import tkinter as tk

root = tk.Tk()

def do_this1():
    frame1.grid_remove()
    print("rmoving")

def do_this2():
    frame1.grid()
    print("adding")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

tk.Label(frame1, text="this is frame one").pack()
tk.Label(frame2, text="this is frame two").pack()

tk.Button(frame1, text="button 1", command=do_this1).pack()

tk.Button(frame2, text="button 2", command=do_this2).pack()


frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)


root.mainloop

