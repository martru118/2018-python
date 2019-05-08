"""
Martin Truong
100708410

This assignment covers: Conditionals, Loops, Lists, Functions, and Classes
"""


#------------------------------------------Queston 1------------------------------------------
class StudentEntry:

    labs = 0
    assignments = 0
    midterm = 0
    final = 0

    #create constructor
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid
    
    def average(self):
        #calculate total average with weights included
        totalAvg = self.labs + self.assignments + (self.midterm*0.3) + (self.final*0.4)
        return totalAvg
    
    #return a letter grade depending on the condition
    def letterGrade(self):
        if self.average() >= 80 and self.average() <= 100:
            return "A"
        elif self.average() >= 70 and self.average() <= 79:
            return "B"
        elif self.average() >= 60 and self.average() <= 69:
            return "C"
        elif self.average() >= 50 and self.average() <= 59:
            return "D"
        else:
            return "F"
    
bsmith = StudentEntry("Bob Smith", "1000001")
bsmith.labs = 9.0
bsmith.assignments = 17.0
bsmith.midterm = 57.5
bsmith.final = 60.0
print("Bob Smith:", bsmith.letterGrade())   #C

sjones = StudentEntry("Sally Jones", "1000002")
sjones.labs = 9.5
sjones.assignments = 19.5
sjones.midterm = 81.0
sjones.final = 74.5
print ("Sally Jones:", sjones.letterGrade())    #A


#------------------------------------------Queston 2------------------------------------------
class Product:

    #create constructor
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight 
    
    #calculate shipping cost
    def getShippingCost(self):
        shippingCost = self.weight * 10
        return shippingCost

    #calculate taxes
    def getTax(self):
        tax = self.price * 0.13
        return tax
    
    #calculate total cost
    def getTotalCost(self):
        totalCost = self.price + self.getTax() + self.getShippingCost()
        return totalCost

razor = Product("Men's Razor", 49.99, 0.25)
homeGym = Product("Home Gym", 879.99, 115.0)

print("Total cost of", razor.name, ":", razor.getTotalCost())   #58.9887
print("Total cost of", homeGym.name, ":", homeGym.getTotalCost())   #2144.3887


#------------------------------------------Queston 3------------------------------------------
def subset(s1, s2):
    #set s1 is a subset of another set s2 
    #if all elements that are in s1 are also in s2

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                return True
            else:
                return False

print(subset([1,9,13,15,23], [1,3,5,7,9,11,13,15,17,19,21,23,25]))  #True
print(subset([3,8,13,21,25], [1,3,5,7,9,11,13,15,17,19,21,23,25]))  #False


#------------------------------------------Queston 4------------------------------------------
def sublistInRange(arrayList, mini, maxi):
    #store values greater than mini and less than maxi
    sublist = []

    for i in range(len(arrayList)):
        #find the values in between the mini and maxi values
        if arrayList[i] >= mini and arrayList[i] <= maxi:
            sublist.append(arrayList[i])
        
    #show the sublist
    return sublist

print(sublistInRange([1,2,3,4,5], 2, 4))    #[2, 3, 4]
print(sublistInRange([5,8,3,21,7,4,14], 4, 14)) #[5, 8, 7, 4, 14]


#------------------------------------------Queston 5------------------------------------------
def palindromeRec(word):
    lowerword = word.lower()    #use the lowercase word
    
    #check the length of the word
    if len(lowerword) < 2:
        return True

    #check if the word matches its reverse
    elif lowerword == lowerword[::-1]:
        return palindromeRec(lowerword[1:-1])
    
    #the letters do not match
    else:
        return False

print("Is level a palindrome?", palindromeRec("level")) #True
print("Is lever a palindrome?", palindromeRec("lever")) #False


#------------------------------------------Queston 6------------------------------------------
def jumpMaximum(intArray):
    #store the first value of the array
    notMaximum = intArray[0]

    #retreive the maximum value
    for a in range(len(intArray)):
        if intArray[a] > intArray[0]:
            intArray[0] = intArray[a]
    
    #swap the maximum value with the first value
    for b in range(1, len(intArray)):
        if intArray[b] == intArray[0]:
            intArray[b] = notMaximum

    return intArray

print(jumpMaximum([1, 2, 3, 4]))    #[4, 2, 3, 1]
print(jumpMaximum([5, 8, 3, 21, 7, 4, 14]))   #[21, 8, 3, 5, 7, 4, 14]


#------------------------------------------Queston 7------------------------------------------
def isReordering(reordered, mainList):
    #check if both arrays are the same when sorted    
    if sorted(reordered) == sorted(mainList):
        return True
    else:
        return False

print(isReordering([4,1,3,2],[1,2,3,4]))    #True
print(isReordering([5,8,3,21],[5,21,8]))    #False
