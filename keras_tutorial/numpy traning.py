import numpy as np


a = np.random.randint(50, size = (10, 10))

print(a)

max_el = np.where(a == a.max())
max = np.amax(a, axis = None)

print(max_el, max)


c = np.zeros((10, 10))


d = c

# print(d)
