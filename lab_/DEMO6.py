# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:15:20 2018

@author: larry
"""

#%%
import random
#import matplotlib.pyplot as plt

def inorder(x):
    i = 0
    j = len(x)

    while i+1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True

def bogosort(x):
    counter = 0
    while not inorder(x):
        counter += 1
        random.shuffle(x)
    
    return(x, counter)

MAXITER = 10
MINITER =  1
x_array = []
y_array = []
unsort = []

for x in range(MINITER, MAXITER + 1):
    x_array.append(x)
    for y in range(x):
        unsort.append(random.randint(5, 109))
    (sorted_list, counter) = bogosort(unsort)
    print(sorted_list, counter)

    y_array.append(counter)
    unsort.clear()

print(x_array)
print(y_array)

"""
#graphing the values
plt.title("Complexity Graph of BogoSort")
plt.xlabel("Amount of Elements")
plt.ylabel("Amount of Operations")
plt.plot(x_array, y_array, 'g')
plt.show()
"""