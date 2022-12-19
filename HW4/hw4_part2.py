import math
class ComplexNumber:

    def __init__(self, Re, Im):
        if not isinstance(Re, float):
            raise ValueError
        if not isinstance(Im, float):
            raise ValueError
        self._Re = Re
        self._Im = Im
        self._r, self._phi = self.get_exponential_form()

    def error(self, msg):
        print(msg)
        exit(-1)

    def get_Re(self):
        return self._Re

    def get_Im(self):
        return self._Im

    def get_r(self):
        return self._r

    def get_phi(self):
        return self._phi

    def set_Re(self, Re):
        if not isinstance(Re, float):
            raise ValueError
        self._Re = Re
        self._r, self._phi = self.get_exponential_form()


    def set_Im(self, Im):
        if not isinstance(Im, float):
            raise ValueError
        self._Im = Im
        self._r, self._phi = self.get_exponential_form()


    def set_r(self, r):
        if not isinstance(r, float):
            raise ValueError
        self._r = r
        self._Re, self._Im = self.get_algebraic_form()


    def set_phi(self, phi):
        if not isinstance(phi, float):
            raise ValueError
        self._phi = phi
        self._Re, self._Im = self.get_algebraic_form()


    def get_exponential_form(self):
        r = math.sqrt(self._Re**2 + self._Im**2)
        if r == 0:
            raise ValueError
        x = self._Re
        y = self._Im

        if x > 0 and y == 0:
            phi = 0
        elif x > 0 and y > 0:
            phi = math.atan(abs(y/x))
        elif x == 0 and y > 0:
            phi = math.pi / 2
        elif x < 0 and y > 0:
            phi = math.pi - math.atan(abs(y/x))
        elif x < 0 and y == 0:
            phi = math.pi
        elif x < 0 and y < 0:
            phi = -math.pi + math.atan(abs(y/x))
        elif x == 0 and y < 0:
            phi = - math.pi / 2
        elif x > 0 and y < 0:
            phi = -math.atan(abs(y/x))

        return r, phi


    def get_algebraic_form(self):
        Re = self._r * math.cos(self._phi)
        Im = self._r * math.sin(self._phi)
        return Re, Im

    def sum(self, z):
        return ComplexNumber(self.get_Re() + z.get_Re(), self.get_Im() + z.get_Im())


    def substract(self, z):
        return ComplexNumber(self.get_Re() - z.get_Re(), self.get_Im() - z.get_Im())

    def product(self, z):
        return ComplexNumber(self.get_Re() * z.get_Re() - self.get_Im() * z.get_Im(),
                             self.get_Re() * z.get_Im() + self.get_Im() * z.get_Re())

    def divide(self, z):
        if z.get_Re() == 0 and z.get_Im() == 0:
            error("division by zero is impossible")
        a = self.get_Re()
        b = self.get_Im()
        c = z.get_Re()
        d = z.get_Im()
        return ComplexNumber((a*c+b*d)/(c**2+d**2), (b*c-a*d)/(c**2+d**2))

    def __add__(self, z):
        return self.sum(z)

    def __sub__(self, z):
        return self.substract(z)

    def __truediv__(self, z):
        return self.divide(z)

    def __mul__(self, z):
        return self.product(z)

    def __eq__(self, z):
        return self.get_Re() == z.get_Re() and self.get_Im() == z.get_Im()

    def __str__(self):
        return str(self.get_Re()) + " + i * " + str(self.get_Im())

    def __abs__(self):
        return (self.get_Re()**2 + self.get_Im()**2)**0.5

    def __getitem__(self, i):
        if i == 0:
            return self.get_Re()
        if i == 1:
            return self.get_Im()
        return None

z = ComplexNumber(3, 4)
print(z)
print(abs(z))
print(z[0], z[1])