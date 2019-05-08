#------------------------------------------------------Question 1------------------------------------------------------
def isSublist(list1, list2):

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True
            else:
                return False

print(isSublist([4,18,1,12,6], [4,2,18,6,9,12,23,5,1]))
print(isSublist([12,8,19,4,7], [3,12,8,19,7]))


#------------------------------------------------------Question 2------------------------------------------------------
def computeTotal(price, percentOff):
    subtotal = 0

    if len(price) == len(percentOff):
        for i in range(len(price)):
            discount = price[i] - (price[i]*(percentOff[i]/100))
            clearanceDiscount = discount - discount * (25/100)
            subtotal += clearanceDiscount
        
        if subtotal < 50:
            subtotal -= 5
        elif subtotal >= 50 and subtotal <= 150:
            subtotal -= 15
        elif subtotal > 150:
            subtotal -= 30

        return subtotal

    return "Invalid input."

print(computeTotal([50.99, 70.99], [25, 50]))
print(computeTotal([15.99, 43.75, 68.25], [10, 35, 20]))
print(computeTotal([40.25, 24.99], [10]))


#------------------------------------------------------Question 3------------------------------------------------------
def wordFrequency(toCheck):

    asList = toCheck.split()
    frequencyCount = 0
    countDict = {}

    for a in range(len(asList)):
        for b in range(len(asList)):
            if asList[a] == asList[b]:
                frequencyCount += 1
        
        countDict[asList[a]] = frequencyCount
        frequencyCount = 0
    
    return countDict

string_1 = "Apple Mango Orange Mango Guava Guava Mango"
string_2 = "Train Bus Bus Train Taxi Aeroplane Taxi Bus"
print(wordFrequency(string_1))
print(wordFrequency(string_2))
