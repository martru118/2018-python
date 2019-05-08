## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species


## class name Dog is-a animal
class Dog(Animal):
    def __init__(self, name, barks_often, wags_tail):
        Animal.__init__(self, name, "Dog")
        self.barks_often = barks_often
        self.wags_tail = wags_tail

    def barksOften(self):
        return self.barks_often

    def wagsTail(self):
        return self.wags_tail



"""
## class Cat is-a animal
class Cat(Animal):

    def __init__(self, name, drinks_milk):
        Animal.__init__(self, name, "Cat")
        self.drinks_milk = drinks_milk


    def drinksMilk(self):
        return self.drinks_milk
"""

## rover is-a Dog
rover = Dog("Rover", True, True)

## satan is-a Cat
#satan = Cat("Satan", True)

print("%s is a %s" % (rover.getName(), rover.getSpecies()))

print("%s barks often: %s" % (rover.getName(), rover.barksOften()))

print("%s wags his tail: %s" % (rover.getName(), rover.wagsTail()))

"""
print("%s is a %s" % (satan.getName(), satan.getSpecies()))

print("%s drinks milk: %s" % (satan.getName(), satan.drinksMilk()))
"""