
import numpy as np
import random

print("One dimension")
print(np.array([1, 2, 3]))
print("Casting up")
print(np.array([1, 2, 3.0]))
print("Two dimensions")
print(np.array([[1, 2], [3, 4]]))


w = np.arange(5)
v = np.arange(1, 6)
  # tuples inside a list
y = np.random.randint(-200, 201, (3,2))
z = np.random.uniform(low=-200.0, high=201.0, size=(10, 2))

a = np.append(w, v, axis=0)

print("Easy range list")
print(w)
print("Extended range list")
print(v)
print("Two tuples in list")
print(x)
print("First entry in list")
print(x[0])
print("First element of first entry")
print(x[0][0])
print("Random integers between range, and 3,2 shape")
print(y)
print("Random floats between range, and 10, 2 shape")
print(z)
print("Appended arrays")
print(a)




