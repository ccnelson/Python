import tkinter as tk

root = tk.Tk()

def clear_entry(self): # function is passed event from bind
    print("clearin")
    print(self.widget) # event.widget tells us which btn was clicked
    print(btn._name) # this correlates with btn._name
    
btn = tk.Button(root, text='Clear')
btn.grid()
btn.bind('<Button-1>', clear_entry) # no parentheses for function as it is
                                    # a reference not a call
root.mainloop()
