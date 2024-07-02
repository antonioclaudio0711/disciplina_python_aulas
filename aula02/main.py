# 1 - Definir classe Dog e instanciar o seu objeto no main
# class Dog:
#     def __init__(self):
#         pass
#
#
# rex = Dog()
# print(rex)

# 2 - Inserir atributos com valor fixo
# class Dog:
#     def __init__(self):
#         self.age = 5
#
#
# rex = Dog()
# print(f'A idade de Rex é: {rex.age} anos')
#
# caramelo = Dog()
# print(f'A idade de Caramelo é: {caramelo.age} anos')

# 3 - Inserir atributos com passagem de parâmetros no construtor da classe
class Dog:
    def __init__(self, age):
        self.age = age


rex = Dog(age=10)
print(f'A idade de Rex é: {rex.age} anos')

caramelo = Dog(age=5)
print(f'A idade de Caramelo é: {caramelo.age} anos')
