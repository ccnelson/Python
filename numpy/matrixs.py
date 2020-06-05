
import numpy as np
import pandas as pd



xa = [[-200, -100, 0, 100, 200],
     [-200, -100, 0, 100, 200],
     [-200, -100, 0, 100, 200],
     [-200, -100, 0, 100, 200],
     [-200, -100, 0, 100, 200]]

ya = [[200, 200, 200, 200, 200],
     [100, 100, 100, 100, 100],
     [-0,   -0,   -0,   -0,   -0],
     [-100, -100, -100, -100, -100],
     [-200, -200, -200, -200, -200]]

x1 = np.array(xa)
y1 = np.array(ya)

x = pd.DataFrame(x1)
y = pd.DataFrame(y1)

#for i in x:
#    print(i)
#print("\t\t---------")
#for j in y:
#    print(j)

print(x)
print(y)

#print(me[0][0][0])

