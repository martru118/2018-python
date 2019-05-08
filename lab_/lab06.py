#%%
import random
import matplotlib.pyplot as plt

#Part 1
def insertionSort(nArray): 
    sortCount = 0

    for i in range(1, len(nArray)):
        #initialize pointers
        num = nArray[i] 
        j = i-1

        #when smaller and/or larger values have been found
        while j >= 0 and num < nArray[j]:
            #move the value by j indexes
            sortCount += 1
            nArray[j+1] = nArray[j] 
            j -= 1
        
        #set the values of the array
        nArray[j+1] = num 
    
    #count the number of insertions
    return sortCount

insertionSort([4,3,7,1,8,2])    #[1,2,3,4,7,8]


#Part 2
maximum = 50
x_array = []
y_array = []
unsorted = []

for n in range(1, maximum):
    #store number of elements (N)
    x_array.append(n)

    #create an array consisting of random integers
    for p in range(n):
        unsorted.append(random.randint(1, 100))

    #store number of operations (P)
    counter = insertionSort(unsorted)
    y_array.append(counter)

    unsorted.clear()

#graph the algorithm
plt.title("Complexity Graph of Insertion Sort Algorithm")
plt.xlabel("Input Size (N)")
plt.ylabel("Number of Operations (P)")
plt.plot(x_array, y_array, 'b')
plt.show()
