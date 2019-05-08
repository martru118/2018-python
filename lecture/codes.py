# This is a comment


userInput = input('Enter a number: ')
userGuess = int(userInput)

if (userGuess % 2) == 0:
    print('You have entered an even number!')
    if userGuess < 10 and userGuess >= 0:
        print('This is a single-digit even number')

else:
    print('You have entered an odd number.')

    
    
username = input("Username: ")
if username == 'Vicky':
    print('Greetings!')
elif username == 'Peter':
    print('Hello!')
elif username == 'Mary':
    print('You are not allowed to continue!')
else:
    print('Username unrecognized')


    
x = 5
if x < 10:
        print('does this work?')
        print('x is small')
print('x is', x)




maxValue = 10
currentNum = 0
total = 0
while currentNum <= maxValue:
    total = total + currentNum
    currentNum += 1
print('the sum is', total)



x = 0
while x < 10:
    print(x, 'is small')
    x = x + 1




# Our implementation of the find function. Prints the index where 
# the target is found; a failure message, if it isn't found. 
# This version only searches for a single character.

river = 'Mississippi'
target = input('Input a character to find: ')
for index in range(len(river)):         # for each index
    if river[index] == target:          # check if the target is found
        print("Letter found at index: ", index)  # if so, print the index
        break                           # stop searching
else:
    print('Letter',target,'not found in',river)