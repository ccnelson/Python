import tkinter as tk

def my_command():
    x = entry.get()
    print(x)

root = tk.Tk() # all our code goes here
entry = tk.Entry(root, width=30)
button = tk.Button(root, text="go", command=my_command)

entry.pack()
button.pack()

root.mainloop()
