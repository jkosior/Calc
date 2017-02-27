import math


class Calculator(object):
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2, self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2, self.num2 / self.num1
    
    def abs_substract(self):
        return abs(self.substract()[0])
    
    def power(self):
        return pow(self.num1, self.num2), pow(self.num2, self.num1)
    
    def sqroot(self):
        return math.sqrt(self.num1), math.sqrt(self.num2)
    
    def factorials(self):
        return math.factorial(self.num1), math.factorial(self.num2)


# different type of factorial

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

c = Calculator(2,3)
print(c.add())
print(c.substract())
print(c.multiply())
print(c.divide())
print(c.abs_substract())
print(c.power())
print(c.sqroot())
print(c.factorials())

print(factorial(8))