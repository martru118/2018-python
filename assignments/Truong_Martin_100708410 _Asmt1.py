"""
Martin Truong
100708410

This assignment covers: Conditionals, Loops, Lists, Functions, and Classes
"""

#Part 1
def intersect(s1, s2):
    equals = [] #store intersecting values

    #scan both lists
    for x in range(len(s1)):
        for y in range(len(s2)):
            #find equivalent value from both lists
            if s1[x] == s2[y]:
                equals.append(s1[x])
    
    print(equals)

intersect([1,3,5,7,9,11,13,15,17,19,21,23,25], [1,4,9,16,25])


#Part 2
def gregoryLeibniz(numIterations):
    sigma = []  #stores all the values from the equation

    for n in range(0, numIterations):
        approx_pi = (4*(-1)**n)/(2*n + 1)  #calculate the approximate value of pi
        sigma.append(approx_pi)

    sigmaSum = sum(sigma)   #calculate the sum of each element in the list
    print(round(sigmaSum, 6))   #round the calculation

gregoryLeibniz(10000000)


#Part 3
def asterisk_triangle(n):
    for i in range(0, n):
        #first row must be drawn seperately
        if i == 0:
            print((n-i)*' ' + i*'*' + '*')

        #draw the second row to the second-last row
        elif i >= 1 and i < n-1:
            print((n-i)*' ' + "*" + ((i-1)*' ') + '*')

        #last row must be drawn seperately
        else:
            print((n-i)*' ' + i*'*' + '*')

asterisk_triangle(7)
asterisk_triangle(13)
