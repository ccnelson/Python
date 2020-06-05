import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="I am a label widget")
button = tk.Button(root, text="I am a button")
label.pack()
button.pack()
var = ["USA", "UP", "India", "Others"]

tk.Label(root, text="Enter your Password:").pack()
tk.Button(root, text="Search").pack()
tk.Checkbutton(root, text="Remember Me").pack()
tk.Entry(root, width=30).pack()
tk.Radiobutton(root, text="Male", variable=1, value=1).pack()
tk.Radiobutton(root, text="Female", variable=1, value=0).pack()
tk.OptionMenu(root, "Select Country", "USA", "UK", "India", "Others").pack(expand=1)
root.mainloop()
