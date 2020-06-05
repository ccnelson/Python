import tkinter as tk
from tkinter import ttk
import builder_methods as bm

root = tk.Tk()
style = ttk.Style()


a, b = bm._build_yscroll_text(root, "hello", 10, 0, 0, 30, 30)

#scrollbar = ttk.Scrollbar(root)
#scrollbar.grid(column=1, row=0, sticky=tk.NS) # scroll bar needs to exist
#maintxt = bm._build_text(root, "word", 10, 0, 0, 30, 30, scrollbar) # to create text
#scrollbar.config(command=maintxt.yview) # to which scroll bar conects

# hence why it was put in a single command _build_yscroll_text

root.mainloop()