class Employee:

    raise_amount = 1.04

    #create constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #access raise_amount by using class name itself or by using self

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)   #same as using super()
        self.prog_lang = prog_lang

#creating objects
emp_1 = Employee("Peter", "Green", 50000)  #calling the default constructor
emp_2 = Employee("Alice", "Wonder", 60000)

"""
print(emp_1.__dict__)
print(emp_1.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#Class variables: variables that are shared among all instances of a class
#Instance variables: contains data that is unique to each instance
"""

emp_1 = Developer("Peter", "Green", 50000, "Python")
emp_2 = Developer("Alice", "Wonder", 60000, "Java")

print(emp_1.email)
print(emp_1.prog_lang)