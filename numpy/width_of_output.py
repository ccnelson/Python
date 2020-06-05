
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)   # <- comment out this command to see output restricted

x = np.arange(-200, 201, 10)
y = np.arange(200, -201, -10)

me = np.meshgrid(x, y)

print(me)

