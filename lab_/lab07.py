#%%
import random
import matplotlib.pyplot as plt


#Part 1
def binarySearch(arrayList, item):
    first = 0
    last = len(arrayList)-1
    found = False
    searchCount = 0

    #scan the array
    while first <= last and not found:
        searchCount += 1
        midpoint = (first + last)//2

        #when the list value matches the item value
        if arrayList[midpoint] == item:
            found = True
        
        else:
            #search elsewhere in the list
            if item < arrayList[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    
    #count the number of searches
    return searchCount

binarySearch([4,3,7,1,8,2], 8)  #True


#Part 2
maximum = 50
unsorted = []
x_axis = []
y_axis = []
randNum = random.randint(5, 100)

for n in range(1, maximum):
    #store number of elements (N)
    x_axis.append(n)

    #create an array consisting of random integers
    for p in range(n):
        unsorted.append(random.randint(5, 100))

    #store number of operations (P)
    counter = binarySearch(unsorted, randNum)
    y_axis.append(counter)
    
    unsorted.clear()

#graph the algorithm
plt.title("Complexity Graph of Binary Search Algorithm")
plt.xlabel("Input Size (N)")
plt.ylabel("Number of Operations (P)")
plt.plot(x_axis, y_axis, 'b')
plt.show()
