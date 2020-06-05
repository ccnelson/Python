
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import tkinter as tk
from tkinter import ttk

# init tk
root = tk.Tk()
root.title("This is running in tkinter")
style = ttk.Style()
style.theme_use('alt')

# create fig to embed
matplotfig = Figure(figsize=(5,5), dpi=100)  # initiate matplotlib figure

# create canvas to hold figure
right_canvas = FigureCanvasTkAgg(matplotfig, root)
right_canvas.get_tk_widget().grid()

# create plots
plot1 = matplotfig.add_subplot(111)
plot1.set_xlabel('x data')
plot2 = matplotfig.add_subplot(111)
plot1.set_ylabel('y data')
# plot data
plot1.plot([1, 1, 2, 2, 1, 1])
plot2.plot([2, 2, 2, 3, 2, 2])
# draw plots
right_canvas.draw()

root.mainloop()