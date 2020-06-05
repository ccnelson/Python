import tkinter as tk

def my_callback():
    print("called right back")

root = tk.Tk()

tk.Button(root, text="click here", command=my_callback).pack()

## the above my_callback is without parentheses, that is because
## we are passing a reference rather than actually calling it.
## if you added parentheses it would be called as soon as the program runs

root.mainloop()
