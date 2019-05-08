# This function mainly initializes memo[] and calls getMinSteps(n, memo) 
def getsMinSteps(n): 
  
      memo = [0 for i in range(n+1)] 
  
      # initialize memoized array 
      for i in range(n+1): 
          memo[i] = -1
  
      return getMinSteps(n, memo)

# function to calculate min steps 
def getMinSteps(n, memo): 
  
     if (n == 1):   #base case 
         return 0
     if (memo[n] != -1):    #already solved 
         return memo[n] 
  
    #res will finally contain the optimal answer
     res = 1 + getMinSteps(n-1, memo)
  
     if (n % 2 == 0): 
         res = min(res, 1 + getMinSteps(n//2, memo)) 
     if (n % 3 == 0): 
         res = min(res, 1 + getMinSteps(n//3, memo)) 
  
    # save the result
     memo[n] = res
     return memo[n] 

print (getsMinSteps (10))