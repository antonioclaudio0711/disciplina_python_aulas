from code.Mammal import Mammal


class Dog(Mammal):
    def __init__(self, age, weight, height, length, position):
        super().__init__(age, weight, height, length, position)
        self.breed = None

    def move_x(self):
        pass

    def move_y(self):
        pass

    def move_z(self):
        pass
