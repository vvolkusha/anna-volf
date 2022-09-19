class Base:
    _x = 0
    _y = 0

    def __init__(self, x=0, y=0):
        self.set(x, y)
    def get(self):
        return self._x, self._y
    def set(selfself, x, y):
        self._x = x
        self._y = y
a = Base(4, 7)
b = Base(0, 0)
c = Base()
a.set(4,6)
print(*a.get())