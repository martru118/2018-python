#------------Question 1------------
"""
import math

x = 50
y = 30
values = []
nums = []

for x in input().split(','):
    nums.append(x)

for d in nums:
    values.append(str(int(round(math.sqrt(2*x*float(d)/y)))))

print(values)
"""


#------------Question 2------------
"""
strings = []

for x in input().split(','):
    strings.append(x)

strings.sort()
print(strings)
"""


#------------Question 3------------
"""
def reverse_str(text):
    stack = []

    for char in text:
        stack.append(char)

    rts = ''

    while len(stack) != 0:
        rts += stack.pop()
    
    return rts

print(reverse_str("SAMPLE TEXT"))
"""


#------------Question 5------------
"""
intlist = [4,2,15,6,9,12,23,5,1]

for e in intlist:
    if e%3 == 0:
        print(e, "is divisible by 3")
    else:
        print(e, "is not divisible by 3")
"""


#------------Question 6------------
"""
println = []

while True:
    Nput = input()

    if Nput:
        println.append(Nput.upper())
    else:
        break

for sentence in println:
    print(sentence)
"""


#------------Question 7------------
"""
a = input()
words = []

for word in a.split():
    words.append(word)

print(sorted(list(set(words))))
"""


#------------Question 8------------
"""
thousands = []

for o in range(1000, 3001):
    n = str(o)

    if int(n[0])%2 == 0:
        if int(n[1])%2 == 0:
            if int(n[2])%2 == 0:
                if int(n[3]) %2 == 0:
                    thousands.append(n)

print(thousands)
"""


#------------Question 9------------
"""
sentence = input()
wordData = {"DIGITS": 0, "LETTERS": 0}

for a in sentence:
    if a.isdigit():
        wordData["DIGITS"] += 1
    elif a.isalpha():
        wordData["LETTERS"] += 1
    else:
        pass

print(wordData)
"""


#------------Question 10------------
"""
casestr = input()
casing = {"UPPERCASE": 0, "LOWERCASE": 0}

for a in casestr:
    if a.isupper():
        casing["UPPERCASE"] += 1
    elif a.islower():
        casing["LOWERCASE"] += 1
    else:
        pass

print(casing)
"""


#------------Question 11------------
netAmount = 0

while True:
    s = input()

    if not s:
        break
    
    