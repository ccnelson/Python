import numpy as np

a_xy = np.array((1.2, 3.6))
b_xy = np.array((-10.0, 10.1))

dist = np.linalg.norm(a_xy - b_xy)

print(dist)
