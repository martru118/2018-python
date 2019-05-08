import numpy as np
import time

size = 1000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [x+y for(x,y) in zip(l1,l2)]
end = time.time()
print((end-start)*1000)

start1 = time.time()
result1 = a1 + a2
end1 = time.time()
print((end1-start1)*1000)
print()

c = np.array([[1, 2, 3], (2, 3, 4)])
print(c.ndim)
print(c.itemsize)
print(c.dtype)
print(c.size)
print(c.shape)

d = c.reshape(3, 2)
print(d)

a = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(a[0,2])