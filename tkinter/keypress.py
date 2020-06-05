import tkinter

def onKeyPress(event):
    text.insert('end', '\n', event.char)
    text2.insert('end', '\n', event.char)

root = tkinter.Tk()
root.geometry('600x400')
text = tkinter.Text(root, background='black', foreground='white', font=('Ariel', 12))
text.pack()
text2 = tkinter.Text(root, background='black', foreground='white', font=('Ariel', 12))
text2.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()

