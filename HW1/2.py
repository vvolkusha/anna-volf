class Car:
    _car_list = []

    def __init__(self, name):
        self._name = name
        self._car_count += 1

        def get_number_of_cars(self):
            return self._car_count
a = Car("Lada")
b = Car("Cas")
c = Car("Tesla")
print(c.get_number_of_car())

