import numpy as np


class Complex_Number:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, num):
        if type(num) == Complex_Number:
            return Complex_Number(self.x + num.x, self.x + num.y)
        elif type(num) == int or type(num) == float or type(num) == np.float64:
            return Complex_Number(self.x + num, self.y)

    def __sub__(self, num):
        if type(num) == Complex_Number:
            return Complex_Number(self.x - num.x, self.y - num.y)
        elif type(num) == int or type(num) == float or type(num) == np.float64:
            return Complex_Number(self.x - num, self.y)

    def __mul__(self, num):
        if type(num) == Complex_Number:
            return Complex_Number(self.x * num.x - num.y * self.y, self.x * num.y + self.y * num.x)
        elif type(num) == int or type(num) == float or type(num) == np.float64:
            return Complex_Number(self.x * num, self.y * num)

    def __truediv__(self, num):
        if type(num) == Complex_Number:
            return Complex_Number((self.x * num.x + self.y * num.y) / (num.x * num.x + num.y * num.y),
                              (self.y * num.x - self.x * num.y) / (num.x * num.x + num.y * num.y))
        elif type(num) == int or type(num) == float or type(num) == np.float64:
            return Complex_Number(self.x / num, self.y / num)

    def __str__(self):
        return str('{:.2f}'.format(self.x)) + ' + ' + str('{:.2f}'.format(self.y)) + 'i'

    def set_real(self, x):
        self.x = x

    def set_image(self, y):
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def get_real(self):
        return self.x

    def get_image(self):
        return self.y

    def get_conjugate(self):
        return Complex_Number(self.x, -1 * self.y)

    def get_module(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)

    def get_angle(self):
        if self.x > 0 and self.y > 0:
            self.phi = np.arctan(self.y / self.x)
        elif self.x < 0 and self.y > 0:
            self.phi = np.pi - np.arctan(self.y / -self.x)
        elif self.x < 0 and self.y < 0:
            self.phi = np.pi + np.arctan(self.y / self.x)
        elif self.x > 0 and self.y < 0:
            self.phi = 2 * np.pi - np.arctan(-self.y / self.x)
        elif self.x == 0 and self.y != 0:
            self.phi = np.pi / 2
        elif self.x >= 0 and self.y == 0:
            self.phi = 0
        else:  # self.x < 0 and self.y == 0
            self.phi = np.pi
        return self.phi

    def exponential_form(self):
        return str('{:.2f}'.format(self.get_module())) + 'e^(' + str('{:.2f}'.format(self.get_angle())) + ')'

    def complex_form(self):
        self.mod, self.phi = self.x, self.y
        self.x = np.cos(self.phi) * self.mod
        self.y = np.sin(self.phi) * self.mod
        return self.x, self.y


if __name__ == "__main__":
    b = Complex_Number(1, 4)
    c = Complex_Number(2)
    b.set_real(3)
    c.set(3, -1)
    print("c angle is", c.get_angle(), "c in exponential form", c.exponential_form())
    a = (b / c + c - b) * 3 * b / 2.2 + 3
    print(a)
    a = a * 2.4
    print(a)
    a *= a.get_conjugate()
    a /= a.get_module()
    print(a)