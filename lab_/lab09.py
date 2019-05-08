import math

class Shape():
    def __init__(self, width, height, numSides):
        self.width = width
        self.height = height
        self.numSides = numSides
    
    def getArea(self):
        if self.numSides == 4:
            area = (self.width + self.height)*2
        elif self.numSides == 0:
            area = math.pi * self.width**2

    def getPerimeter(self):
        return self.getPerimeter()

class Rectangle(Shape):
    def __init__(self):
        self.width = 5
        self.height = 10
        self.numSides = 4

class Circle(Shape):
    def __init__(self):
        self.width = 5
        self.height = self.width
        self.numSides = 0