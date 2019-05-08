#Fibonacci sequence using dynamic programming/memoization
def fibonacci(n):

    #Taking first two fibonacci numbers as 0 and 1
    fibArray = [0, 1]

    while len(fibArray) < n + 1:
        fibArray.append(0)
    
    if n <= 1:
        return n
    else:
        if fibArray[n - 1] == 0:
            fibArray[n - 1] = fibonacci(n - 1)

        if fibArray[n - 2] == 0:
            fibArray[n - 2] = fibonacci(n - 2)
        
        fibArray[n] = fibArray[n - 2] + fibArray[n - 1]
    
    return fibArray[n]

print(fibonacci(6))