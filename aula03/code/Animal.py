from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age, weight, height, length, position):
        self.age = age
        self.weight = weight
        self.height = height
        self.length = length
        self.position = position

    @abstractmethod
    def move_x(self):
        pass

    @abstractmethod
    def move_y(self):
        pass

    @abstractmethod
    def move_z(self):
        pass
