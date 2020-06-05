import tkinter as tk

root = tk.Tk()

w = tk.Canvas(root)

coord= 10, 50, 240, 210
arc = w.create_arc(coord, start=0, extent=150, fill="blue")

filename = tk.PhotoImage(file = "sunshine.gif")
image = w.create_image(50, 50, anchor=tk.W, image=filename) 


w.pack()

#root.mainloop()
