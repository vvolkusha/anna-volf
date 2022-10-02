import math
class Base:
    def set(self, x, y):
        return self.x, self.y
    def set(self, x, y):
        self.x = x #действительная часть
        self.y = y #мнимая часть
    def __init__(self, x = 0, y = 0):
        self.set(x, y)
    def __sum__(self, num):
        return Base(self.x + num.x, self.y + num.y)
    def __sub__(self, num):
        return Base(self.x - num.x, self.y - num.y)
    def __mul__(self,num):
        return Base(self.x * num.x - num.y * self.y, self.x * num.y + self.y * num.x)
    def __div__(self,num):
        return Base((self.x * num.x + self.y * num.y)/(num.x * num.x + num.y * num.y), (self.y * num.x - self.x * num.y)/(num.x * num.x + num.y * num.y))

sum = Base()
sub = Base()
mult = Base()
div = Base()
self = Base(1,1)
num = Base(1,1)
x,y = sum(self,num)
print(sum(self,num))
print(sub(self, num))
print(mul(self, num))
print(div(self, num))