class Robot:

    #__init__ indicates constructor
    def __init__(self, givenName, givenColor, givenWeight):
        self.name = givenName
        self.color = givenColor
        self.weight = givenWeight

    def introduce_self(self):
        print("My name is", self.name)

"""    
r1 = Robot()
r1.name = "Alex"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Peter"
r2.color = "blue"
r2.weight = 40
"""

r1 = Robot("Alex", "red", 30)
r2 = Robot("Peter", "blue", 40)
r1.introduce_self()
r2.introduce_self()

class Person():
    def __init__(self, n, p, i):
        #self.whatever can only be initialized in __init__ function
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True
    
    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Ali", "talkative", True)
p1.robot_owned = r2
p2.robot_owned = r1

print(p1.robot_owned)