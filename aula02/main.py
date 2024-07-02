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
# class Dog:
#     def __init__(self, age):
#         self.age = age
#
#
# rex = Dog(age=10)
# print(f'A idade de Rex é: {rex.age} anos')
#
# caramelo = Dog(age=5)
# print(f'A idade de Caramelo é: {caramelo.age} anos')


# 4 - Atributos da classe
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age):
#         self.age = age
#
#
# rex = Dog(age=10)
# print(f'A idade de Rex é: {rex.age} anos, e ele pertence à família {rex.family}')
#
# caramelo = Dog(age=5)
# print(f'A idade de Caramelo é: {caramelo.age} anos, e ele pertence à família {caramelo.family}')
#
# print(f'Todos os cachorros pertencem à família {Dog.family}')


# 5 - Definindo o tipo de um atributo:
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age: int):
#         self.age: int = age
#
#
# rex = Dog(age=10)
# print(f'A idade de Rex é: {rex.age} anos, e ele pertence à família {rex.family}')
#
# caramelo = Dog(age=5)
# print(f'A idade de Caramelo é: {caramelo.age} anos, e ele pertence à família {caramelo.family}')
#
# print(f'Todos os cachorros pertencem à família {Dog.family}')


# 6 - Atributos especiais __class__ e __name__
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age: int):
#         self.age: int = age
#
#
# rex = Dog(age=10)
# print(f'A idade de Rex é: {rex.age} anos, e ele pertence à família {rex.family}')
#
# caramelo = Dog(age=5)
# print(f'A idade de Caramelo é: {caramelo.age} anos, e ele pertence à família {caramelo.family}')
#
# print(f'Rex é um objeto da classe {rex.__class__.__name__}')
# print(f'Caramelo é um objeto da classe {caramelo.__class__.__name__}')


# 7 - Atributos protegidos
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age: int, weight):
#         self._age: int = age
#         self.__weight = weight # ERRO AO TENTAR ACESSAR UTILIZANDO __
#
#
# rex = Dog(age=10, weight=45)
# print(f'A idade de Rex é: {rex._age} anos, seu peso é de {rex.__weight} KG e ele pertence à família {rex.family}')
#
# caramelo = Dog(age=5, weight=30)
# print(f'A idade de Caramelo é: {caramelo._age} anos, seu peso é de {caramelo._weight} KG e ele pertence à família {caramelo.family}')
#
# print(f'Rex é um objeto da classe {rex.__class__.__name__}')
# print(f'Caramelo é um objeto da classe {caramelo.__class__.__name__}')


# 8 - Utilizando métodos para retornar atributos protegidos
# class Dog:
#     family = 'Canidae'
#
#     def __init__(self, age):
#         self._age = age
#         self.__weight = 0
#
#     def get_age(self) -> int:
#         return self._age
#
#     def get_weight(self) -> int:
#         return self.__weight
#
#     def set_weight(self, weight: int):
#         self.__weight = weight
#
#
# rex = Dog(age=10)
# rex.set_weight(weight=45)
# print(f'A idade de Rex é: {rex.get_age()} anos, seu peso é de {rex.get_weight()} KG e ele pertence à família {rex.family}')
#
# caramelo = Dog(age=5)
# caramelo.set_weight(weight=30)
# print(f'A idade de Caramelo é: {caramelo.get_age()} anos, seu peso é de {caramelo.get_weight()} KG e ele pertence à família {caramelo.family}')
#
# print(f'Todos os cachorros pertencem à família {Dog.family}')


# 9 - Herança
# class Animal:
#     def __init__(self, age: int, height: int, weight: int, position: tuple):
#         self.age = age
#         self.height = height
#         self.weight = weight
#         self.position: tuple = position  # position [position_x, position_y, position_z]
#
#     def move_x(self):
#         self.position[0] += 1
#
#     def move_y(self):
#         self.position[1] += 1
#
#     def move_z(self):
#         self.position[2] += 1
#
#
# class Dog(Animal):
#     def __init__(self, age: int, height: int, weight: int, position: tuple):
#         super().__init__(age, height, weight, position)
#         # Animal.__init__(self, age, height, weight, position)
#
#     def move_z(self):
#         self.position[2] += 2
#
#
# caramelo = Dog(age=10, height=40, weight=30, position=(0, 0, 0))
# print(caramelo.age)


# Exercício prático
# class Funcionario:
#     def __init__(self, in_id: int, in_nome: str, in_cargo: str, in_salario: int):
#         self.id = in_id
#         self.nome = in_nome
#         self.cargo = in_cargo
#         self.salario = in_salario
#
#     def mostra_reg(self):
#         print()
#         print(f'Registro # {self.id}')
#         print(f'O nome do funcionário é {self.nome}')
#         print(f'O funcionário {self.nome} é {self.cargo}')
#         print(f'O salário do {self.cargo} {self.nome} é de R$ {self.salario}')
#         print()
#
#
# registro = ['zero']
# REG_ID = 0
#
# while True:
#     opcao = input('\r\nSelecione uma ação: ' +
#                   '\r\n1 - Adicionar funcionário' +
#                   '\r\n2 - Mostrar os registros existentes' +
#                   '\r\n3 - Sair' +
#                   '\r\n>>> ')
#
#     if opcao == '1':
#         REG_ID += 1
#
#         while True:
#             nomeReg = input('Insira o nome do funcionário: >> ')
#             cargoReg = input('Insira o cargo do funcionário: >> ')
#
#             while True:
#                 try:
#                     salarioReg = int(input('Insira o salário do funcionário: >> '))
#                     break
#                 except:
#                     print('Insira apenas números inteiros!')
#                     continue
#
#             regFunc = Funcionario(in_id=REG_ID, in_nome=nomeReg, in_cargo=cargoReg, in_salario=salarioReg)
#             registro.append(regFunc)
#             print(f'registro {registro}')
#             registro[REG_ID].mostra_reg()
#
#             break
#
#     elif opcao == '2':
#         for i in range(1, len(registro)):
#             registro[i].mostra_reg()
#
#     elif opcao == '3':
#         print('Encerrando sistema')
#         break
#
#     else:
#         print('Opção inválida, tente novamente!')

class Animal:
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position  # position [position_x, position_y, position_z]

    def move_x(self):
        self.position[0] += 1


class Dog(Animal):
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        super().__init__(age, height, weight, position)

    def move_x(self):
        self.position[2] += 2


class Cat(Dog):
    def __init__(self, age: int, height: int, weight: int, position: tuple, fur_type='liso'):
        super().__init__(age, height, weight, position)

    def move_x(self):
        self.position[3] += 4


melo = Cat(age=10, weight=30, position=(0, 0, 0), height=10)
print(melo.age)
