import numpy as np
class Base:
    def get(self, x, y):
        return self.x, self.y
    def get(self, x, y):
        self.x = x #действительная часть
        self.y = y #мнимая часть
    def __init__(self, x, y = 0):
        self.x = x
        self.y = y
        self.get(x, y)
    def __sum__(self, num):
        return Base(self.x + num.x, self.y + num.y)
    def __sub__(self, num):
        return Base(self.x - num.x, self.y - num.y)
    def __mul__(self,num):
        return Base(self.x * num.x - num.y * self.y, self.x * num.y + self.y * num.x)
    def __div__(self,num):
        return Base((self.x * num.x + self.y * num.y)/(num.x * num.x + num.y * num.y), (self.y * num.x - self.x * num.y)/(num.x * num.x + num.y * num.y))

    def get_phi(self):
        if self.x > 0 and self.y > 0:
            self.phi = np.arctan(self.y / self.x)

        elif self.x < 0 and self.y > 0:
            self.phi = np.pi - np.arctan(self.y / abs(self.x))

        elif self.x < 0 and self.y < 0:
            self.phi = np.pi + np.arctan(abs(self.y) / abs(self.x))

        elif self.x > 0 and self.y < 0:
            self.phi = 2 * np.pi - np.arctan(abs(self.y) / self.x)

        elif self.x == 0 and self.y > 0:
            self.phi = np.pi / 2

        elif self.x == 0 and self.y < 0:
            self.phi = - np.pi / 2

        elif self.x == 0 and self.y == 0:
            self.phi = 0

        elif self.x > 0 and self.y == 0:
            self.phi = 0

        elif self.x < 0 and self.y == 0:
            self.phi = np.pi

        return self.phi
sum = Base()
sub = Base()
mul = Base()
div = Base()
self = Base(1,1)
num = Base(1,1)
a = Base()
b = Base()
print(sum(self,num))
print(sub(self, num))
print(mul(self, num))
print(div(self, num))