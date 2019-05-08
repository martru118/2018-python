#-------------------Question 1-------------------
def isPalindrome(word):
    return (word == word[::-1])

string = "aibohphobia"
result = isPalindrome(string)
print(result)   #True

string = "not a palindrome"
result = isPalindrome(string)
print(result)   #False


#-------------------Question 2-------------------
def secondSmallest(nums):
    compare = []

    for i in nums:
        if i != max(nums) and i != min(nums):
            if len(nums) > 3:
                compare.append(i)
            else:
                return i

    for a in range(len(compare)):
        for b in range(len(compare)):
            if compare[a] < compare[b]:
                return compare[a]

lst = [5, 10, 1, 8]
second = secondSmallest(lst)
print(second)   #5


#-------------------Question 3-------------------
def getVowels(sentence):
    vowels = ""

    for aeiou in sentence:
        if aeiou == "a":
            vowels += aeiou
        elif aeiou == "e":
            vowels += aeiou
        elif aeiou == "i":
            vowels += aeiou
        elif aeiou == "o":
            vowels += aeiou
        elif aeiou == "u":
            vowels += aeiou
    
    return vowels

print(getVowels("this is a sentence"))  #iiaeee
print(getVowels("computer science"))    #oueiee
print(getVowels("i like pizza"))        #iieia


#-------------------Question 4-------------------
numbers = []

for n in range(2000, 3200+1):
    if n % 7 == 0 and n % 5 != 0:
        numbers.append(n)

print(numbers)


#-------------------Question 5-------------------
class Shape:
    def __init__(self, shapeName):
        self.shapeName = shapeName
        self.numberOfSides = 0
        self.sumOfAngles = 0

    def getNumberOfSides(self):
        return self.numberOfSides

    def getSumOfAngles(self):
        return self.sumOfAngles

    def __str__(self):
        return self.shapeName + ' (# of sides: ' + str(self.numberOfSides) + ', sum of angles: ' + str(self.sumOfAngles) + ')'

class Triangle(Shape):
    def __init__(self):
        self.numberOfSides = 3
        self.sumOfAngles = 180
        self.shapeName = "Triangle"

class Square(Shape):
    def __init__(self):
        self.numberOfSides = 4
        self.sumOfAngles = 360
        self.shapeName = "Square"

class Pentagon(Shape):
    def __init__(self):
        self.numberOfSides = 5
        self.sumOfAngles = 540
        self.shapeName = "Pentagon"

triangle = Triangle()
square = Square()
pentagon = Pentagon()

shapes = [triangle, square, pentagon]
for shape in shapes:
    print(shape)
