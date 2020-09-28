import numpy as np
import random

# z = np.arange(9).reshape(3, 3)
# print(z)

# z = np.ones((10, 10))
# z[1:-1, 1:-1] = 0
# print(z)


# z = np.zeros((5, 5))

# k = 0
# for i in z:
#     i[k] = k + 1
#     k += 1
# print(z)

# Z = np.random.random(10)
# # Z.sort()
# print(Z)
# a = sorted(Z)
# print(a)
# Z.sort()
# print(Z)

# some_list = []
# for i in range(10):
#     r = random.randrange(10, 50, 10)
#     some_list.append(r)
# print(some_list)

z = np.random.randint(5, 10, 5)
print(z)
# print(max(z))

# A = np.random.randint(0,5,(8,3))
# B = np.random.randint(0,5,(2,2))
# print(A)
# print(B)

a = np.array([1, 3, 0], float)
b = np.array([0, 3, 2], float)
print(a == b)
c = np.concatenate((a, b))
print(c)
d = c[c > 2]
print(d)

# result_points = np.empty([0, 2], dtype=int)  # создать 2-х мерный пустой массив, нужен, если необходимо аппенднуть
