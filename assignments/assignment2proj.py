"""
----------------------------------Question 1---------------------------------
"""

class StudentEntry:
    
    labs = 0
    assignments = 0
    midterm = 0
    final = 0
    
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    def average(self):
        self.midterm = self.midterm*30/100
        self.final = self.final*40/100
        self.AVG = self.labs + self.assignments + self.midterm + self.final
        
        return self.AVG
    
    def letterGrade(self):
        
        self.average()
        
        if self.AVG > 80:
            return "A"
        elif self.AVG > 69 and self.AVG < 80:
            return "B"
        elif self.AVG > 59 and self.AVG < 70:
            return "C"
        elif self.AVG > 49 and self.AVG < 60:
            return "D"
        else:
            return "F"
        

print("This is question 1:")

bsmith = StudentEntry("Bob Smith", "1000001")
bsmith.labs = 9.0
bsmith.assignments = 17.0
bsmith.midterm = 57.5
bsmith.final = 60.0

print("Bob Smith: ", bsmith.letterGrade())


sjones = StudentEntry("Sally Jones", "1000002")
sjones.labs = 9.5
sjones.assignments = 19.5
sjones.midterm = 81.0
sjones.final = 74.5

print ("Sally Jones: ", sjones.letterGrade())
print()


"""
----------------------------------Question 2---------------------------------
"""

class Product:
    
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        
    def getShippingCost(self):
        self.shippingCost = self.weight * 10
        
    def getTax(self):
        self.tax = self.price * 0.13
    
    def getTotalCost(self):
        
        self.getShippingCost()
        self.getTax()

        self.totalCost = self.price + self.tax + self.shippingCost
        return self.totalCost
        
print("This is question 2:")    

razor = Product("Electric Razor", 49.99, 0.25)
homeGym = Product("Home Gym", 879.99, 115.0)

print("Total cost of", razor.name, ":", razor.getTotalCost())
print("Total cost of", homeGym.name, ":", homeGym.getTotalCost())

print()

"""
----------------------------------Question 3---------------------------------
"""


def subset(x1, x2):

    check = True
    for i in range(len(x1)):
        checkminor = False
        for j in range(len(x2)):
            if x1[i] == x2[j]:
                checkminor = True
        
        if checkminor == False:
            check = False
    
    print(check)
    
print("This is question 3:")
subset([1,9,13,15,23], [1,3,5,7,9,11,13,15,17,19,21,23,25])
subset([3,8,13,21,25], [1,3,5,7,9,11,13,15,17,19,21,23,25])
print()
    


"""
----------------------------------Question 4---------------------------------
"""

def sublistInRange (list, min, max):
    app = []

    for i in range(len(list)):
        if list[i] >= min and list [i] <=max:
            app.append(list[i])
    
    print(app)
    
print("This is question 4:")
sublistInRange([1,2,3,4,5], 2, 4)
sublistInRange([5,8,3,21,7,4,14], 4, 14)
print()

"""
----------------------------------Question 5---------------------------------
"""

def palindromeRec(str):
    
    if len(str) <= 1:
        return True
    
    if str[0] == str[len(str) - 1]:
        return palindromeRec(str[1:len(str) - 1])
    
    else:
        return False
    
    """
    strList = []
    for x in str:
        strList.append(x)
    
    first = 0
    last = len(str)-1
    mirror = (len(str)//2)-1
    check = False
    
    for x in range(mirror):
        if strList[first+x] == strList[last-x]:
            check = True
        else:
            check = False
            break
    
    return check
    """
    
print("This is question 5:")
print("is level a palindrone?",palindromeRec("level"))
print("is lever a palindrone?",palindromeRec("lever"))
print()

"""
----------------------------------Question 6---------------------------------
"""

def jumpMaximum(list):
    
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] <= list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    print(list)

print("This is question 6:")
jumpMaximum([1,2,3,4])
jumpMaximum([5,8,3,21,7,4,14])
print()

"""
----------------------------------Question 7---------------------------------
"""

def isReordering(list1, list2):

    check = True
    for i in range(len(list1)):
        checkminor = False
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                checkminor = True
        
        if checkminor == False:
            check = False
    
    print(check)
    
print("This is question 7:")
isReordering([4,1,3,2],[1,2,3,4])
isReordering([5,8,3,21],[5,21,8])
    
    