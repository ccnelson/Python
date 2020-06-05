
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)   # <- comment out this command to see output restricted

x = np.arange(-200, 201, 100)
y = np.arange(200, -201, -100)

m = np.meshgrid(x, y)

print(m)
