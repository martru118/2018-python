#------------------------------------------Queston 1------------------------------------------
class Pet():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return(str(self.name) + ' -- ' + self.sound)

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Woof!")

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Meow!")

class Bird(Pet):
    def __init__(self, name):
        super().__init__(name, "Cheep!")


print(Bird("Pete").speak())
print(Bird("Yappy").speak())
print(Cat("Boots").speak())
print(Cat("Mr. Fluffington").speak())
print(Cat("Sylvester").speak())
print(Dog("Spot").speak())
print(Dog("Odie").speak())
print(Dog("Charles").speak())


#------------------------------------------Queston 2------------------------------------------
def getWords(sentence):
    #return sentence.split()

    words = []
    blank = ''

    for i in range(len(sentence)):
        if sentence[i] == ' ':
            words.append(blank)
            blank = ''
        else:
            blank += sentence[i]

    if len(blank) > 0:
        words.append(blank)

    return words

print(getWords("The quick brown fox jumped over the lazy dogs"))
print(getWords("He's the hero Gotham deserves, but not the one it needs right now"))


#------------------------------------------Queston 3------------------------------------------
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
        self.shapeName = 'Triangle'

class Square(Shape):
    def __init__(self):
        self.numberOfSides = 4
        self.sumOfAngles = 360
        self.shapeName = 'Square'

class Pentagon(Shape):
    def __init__(self):
        self.numberOfSides = 5
        self.sumOfAngles = 540
        self.shapeName = 'Pentagon'

print(Triangle())
print(Square())
print(Pentagon())


#------------------------------------------Queston 4------------------------------------------
def getReverseWords(sentence):
    words = []
    blank = ''

    for i in range(len(sentence) - 1, -1, -1):
        if sentence[i] == ' ':
            words.append(blank)
            blank = ''
        else:
            blank = sentence[i] + blank
    if len(blank) > 0:
        words.append(blank)

    return words

print(getReverseWords('The quick brown fox jumped over the lazy dogs'))
print(getReverseWords("He's the hero Gotham deserves, but not the one it needs right now"))


#------------------------------------------Queston 5------------------------------------------
def isVowel(char):
    if char == 'a':
        return True
    elif char == 'e':
        return True
    elif char == 'i':
        return True
    elif char == 'o':
        return True
    elif char == 'u':
        return True
    else:
        return False

def getLongestVowelSequence(string):
    if len(string) == 0:
        return ''

    vowelSequence = ''
    for i in range(len(string)):
        if isVowel(string[i]):
            vowelSequence += string[i]
        else:
            perhapsLongest = getLongestVowelSequence(string[i+1:])

            if len(vowelSequence) > len(perhapsLongest):
                return vowelSequence
            else:
                return perhapsLongest
    
    return vowelSequence

print(isVowel('e'))
print(isVowel('y'))
print(getLongestVowelSequence("Hooiaioia is a cool word in Hawaiian"))
print(getLongestVowelSequence("Queuing is not quite as impressive"))


#------------------------------------------Queston 6------------------------------------------
def insertionSort4(toSort):
    #print original array
    print("Original array:", toSort)

    #do insertion sort 4 times
    for i in range(1, 5):
        current = toSort[i]

        while i > 0 and toSort[i-1] > current:
            toSort[i] = toSort[i-1]
            i -= 1

        toSort[i] = current

    #output the resulting array
    return "Resulting array (after 4 iterations): " + str(toSort)

print(insertionSort4([14, 24, 6, 40, 13, 21, 12, 18]))


#------------------------------------------Queston 7------------------------------------------
def isSubset(list1, list2):
    #set s1 is a subset of another set s2 
    #if all elements that are in s1 are also in s2

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True
            else:
                return False

print(isSubset([4,18,1,12,6], [4,2,18,6,9,12,23,5,1]))
print(isSubset([12,8,19,4,7], [3,12,8,19,7]))


#------------------------------------------Queston 8------------------------------------------
def findMinAndMax(values):
    if len(values) > 0:
        maximum = values[0]
        minimum = values[0]
        
        for val in values:
            if val > maximum:
                maximum = val
            elif val < minimum:
                minimum = val
        
        return minimum, maximum
    
    else:
        return 'ERROR: No elements in list'

print('findMinAndMax([4,1,21,-7,9,13]):', findMinAndMax([4,1,21,-7,9,13]))
print('findMinAndMax([-2,4,7,3,5,11,2,9]):', findMinAndMax([-2,4,7,3,5,11,2,9]))
print('findMinAndMax([7,10,4,30,-17,52]):', findMinAndMax([7,10,4,30,-17,52]))


#------------------------------------------Queston 9------------------------------------------
def zipMultiply(list1, list2):
    product = []
    for shift8 in range(len(list1)):
        product.append(list1[shift8] * list2[shift8])

    return product

print(zipMultiply([1,2,3], [4,5,6]))
print(zipMultiply([4,3,7], [2,0,7]))
print(zipMultiply([2,4,6,8,10], [1,3,5,7,9]))


#------------------------------------------Queston 10------------------------------------------
def computeTotal(items, discounts):
    subtotal = 0
    if (len(items) == len(discounts)):
        for i in range(len(items)):
            disc = items[i] - (items[i] * (discounts[i]/100))
            clearanceDisc = disc - disc * (25/100)
            subtotal += clearanceDisc

        if (subtotal < 50):
            subtotal -= 5
        elif(subtotal >= 50) and (subtotal <= 150):
            subtotal -= 15
        elif(subtotal > 150):
            subtotal -= 30
        
        return subtotal
    
    return "Invalid input."

print(computeTotal([50.99, 70.99], [25, 50]))
print(computeTotal([15.99, 43.75, 68.25], [10, 35, 20]))
print(computeTotal([40.25, 24.99], [10]))
