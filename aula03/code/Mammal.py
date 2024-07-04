from abc import ABC

from code.Animal import Animal


class Mammal(Animal, ABC):
    def __init__(self, age, weight, height, length, position):
        super().__init__(age, weight, height, length, position)
        self.fur = None

    def fur_type(self):
        pass
