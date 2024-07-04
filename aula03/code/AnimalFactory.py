from code.Cat import Cat
from code.Dog import Dog


class AnimalFactory:
    @staticmethod
    def new_animal(animal_type, age, weight, height, length):
        match animal_type:
            case 'dog':
                return Dog(age=age, weight=weight, height=height, length=length, position=(0, 0))
            case 'cat':
                return Cat(age=age, weight=weight, height=height, length=length, position=(20, 20))
