import time

def fibonacci(n):
    solutions = [0,1]

    if n < 2:
        return solutions[n]

    for i in range(2, n+1):
        solutions.append(solutions[i-1] + solutions[i-2])
    
    return solutions[n]

start = time.time()
print(fibonacci(10000))
end = time.time()

print("\n", end-start)