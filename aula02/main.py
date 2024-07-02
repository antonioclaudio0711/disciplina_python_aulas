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


# Exercício prático 01
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


# Exercício prático 02
# class Peca:
#     def __init__(self, id: int, nome: str, fab: str, preco: int):
#         self.id: int = id
#         self.nome: str = nome
#         self.fab: str = fab
#         self.preco: int = preco
#
#     def mostra_registro(self):
#         print()
#         print(f'Registro # {self.id}')
#         print(f'Peça: {self.nome}')
#         print(f'Fabricante: {self.fab}')
#         print(f'Preço: {self.preco}')
#
#     def get_registro(self):
#         return {
#             'ID': self.id,
#             'nome': self.nome,
#             'fab': self.fab,
#             'preco': self.preco
#         }
#
#
# registro = ['zero']
# REG_ID = 0
#
# while True:
#     opcao = input('\r\nSelecione uma ação: ' +
#                   '\r\n1 - Adicionar peça' +
#                   '\r\n2 - Mostrar todas as peças' +
#                   '\r\n3 - Mostrar peça por nome' +
#                   '\r\n4 - Sair' +
#                   '\r\n>>> ')
#
#     if opcao == '1':
#         REG_ID += 1
#         while True:
#             nomeReg = input('Inserir o nome da peça: >> ')
#             fabReg = input('Inserir o fabricante da peça: >> ')
#
#             while True:
#                 try:
#                     precoReg = int(input('Inserir o preço da peça: >> '))
#                     break
#                 except:
#                     print('Insira apenas números!')
#                     continue
#
#             regPeca = Peca(id=REG_ID, nome=nomeReg, fab=fabReg, preco=precoReg)
#             registro.append(regPeca)
#             registro[REG_ID].mostra_registro()
#             break
#
#     elif opcao == '2':
#         for i in range(1, len(registro)):
#             registro[i].mostra_registro()
#
#     elif opcao == '3':
#         encontrada = False
#         nomePecaBuscada = input('Digite o nome da peça que deseja visualizar: >> ')
#         for i in range(1, len(registro)):
#             reg = registro[i].get_registro()
#             if reg['nome'].lower() == nomePecaBuscada.lower():
#                 encontrada = True
#                 print('\nRegistro da peça:')
#                 registro[i].mostra_registro()
#
#         if not encontrada:
#             print(f"\nA peça '{nomePecaBuscada}' não foi encontrada!")
#
#     elif opcao == '4':
#         print('Saindo do sistema!')
#         break
#
#     else:
#         print('Opção inválida, tente novamente!')


# Exercício prático 03
# class Aluno:
#     def __init__(self, nome: str, idade: int, curso: str):
#         self.nome = nome
#         self.idade = idade
#         self.curso = curso
#
#     def mostrar_info(self):
#         print()
#         print(f'Nome do aluno: {self.nome}')
#         print(f'Idade do aluno: {self.idade}')
#         print(f'Curso em que o aluno está matriculado: {self.curso}')
#
#     def set_data(self, nome, idade, curso):
#         self.nome = nome
#         self.idade = idade
#         self.curso = curso
#
#     def get_data(self):
#         return [self.nome, self.idade, self.curso]
#
#
# def cadastrar_aluno(alt=""):
#     if alt == "":
#         nome = input("Digite o nome do aluno: >> ")
#         while True:
#             try:
#                 idade = int(input('Digite a idade do aluno: >> '))
#                 break
#             except:
#                 print('Insira somente números!')
#                 continue
#
#         curso = input('Digite o curso em que o aluno está matriculado: >> ')
#         return Aluno(nome=nome, idade=idade, curso=curso)
#
#     else:
#         print(f'Alterando as informações do aluno {alt}')
#         while True:
#             try:
#                 idade = int(input('Digite a idade do aluno: >> '))
#                 break
#             except:
#                 print('Insira somente números!')
#                 continue
#
#         curso = input('Digite o curso em que o aluno está matriculado: >> ')
#         return [alt, idade, curso]
#
#
# alunos = []
#
# while True:
#     opcao = input('\r\nSelecione uma ação: ' +
#                   '\r\n1 - Cadastrar aluno' +
#                   '\r\n2 - Mostrar registros de alunos' +
#                   '\r\n3 - Alterar um registro de aluno' +
#                   '\r\n4 - Sair' +
#                   '\r\n>>> ')
#
#     if opcao == '1':
#         aluno = cadastrar_aluno()
#         alunos.append(aluno)
#         print('Aluno cadastrado com sucesso!')
#
#     elif opcao == '2':
#         print('\nRegistros de alunos:')
#         for aluno in alunos:
#             aluno.mostrar_info()
#
#     elif opcao == '3':
#         encontrada = False
#         altReg = input('Qual o aluno que deseja alterar as informações? >> ')
#
#         for aluno in alunos:
#             reg = aluno.get_data()
#
#             if reg[0].lower() == altReg.lower():
#                 encontrada = True
#                 print(f'\nAlterar informações do aluno {altReg}')
#                 infoAluno = cadastrar_aluno(alt=altReg)
#                 aluno.set_data(infoAluno[0], infoAluno[1], infoAluno[2])
#
#                 print('\nInformações alteradas com sucesso!')
#
#                 aluno.mostrar_info()
#                 break
#
#         if not encontrada:
#             print(f'\nAluno {altReg} não encontrado!')
#
#     elif opcao == '4':
#         print('Saindo do sistema!')
#         break
#
#     else:
#         print('Opção inválida, tente novamente!')


# Exercício prático 04
# class ContaBancaria:
#     def __init__(self, titular, saldo=0.0):
#         self.saldo = saldo
#         self.titular = titular
#
#     def depositar(self, valor):
#         self.saldo += valor
#         print(f'Depósito de R$ {valor} realizado. O novo saldo da conta é de: {self.saldo: .2f}')
#
#     def sacar(self, valor):
#         if self.saldo < valor:
#             print(
#                 f'A conta do titular {self.titular} possui R$ {self.saldo: .2f}. Desta forma, não será possível realizar o saque de R$ {valor}')
#         else:
#             self.saldo -= valor
#             print(f'Saque de R$ {valor} realizado. O novo saldo da conta é de: {self.saldo: .2f}')
#
#
# conta = ContaBancaria(titular='Antônio Claudio')
# conta.depositar(valor=1000.0)
# conta.sacar(valor=500.0)
# conta.sacar(valor=700.0)


# Exercício prático 05
class Bolo:
    def __init__(self, agua, farinha, fermento, acucar):
        self.agua: float = agua
        self.farinha: float = farinha
        self.fermento: float = fermento
        self.acucar: float = acucar

    def show_bolo(self):
        return self.agua, self.farinha, self.fermento, self.acucar


class BoloChocolate(Bolo):
    def __init__(self, agua, farinha, fermento, acucar, chocolate):
        super().__init__(agua, farinha, fermento, acucar)
        self.chocolate: float = chocolate

    def show_bolo_chocolate(self):
        return self.agua, self.farinha, self.fermento, self.acucar, self.chocolate


class BoloBaunilha(Bolo):
    def __init__(self, agua, farinha, fermento, acucar, baunilha):
        Bolo.__init__(self, agua, fermento, farinha, acucar)
        self.baunilha: float = baunilha

    def show_bolo_baunilha(self):
        return self.agua, self.fermento, self.farinha, self.acucar, self.baunilha


bolo_chocolate = BoloChocolate(agua=1, farinha=0.5, fermento=0.1, acucar=0.3, chocolate=0.5)
bolo_baunilha = BoloBaunilha(agua=0.8, farinha=0.7, fermento=0.2, acucar=0.6, baunilha=0.9)
print(bolo_chocolate.show_bolo_chocolate())
print(bolo_chocolate.show_bolo())

print(bolo_baunilha.show_bolo_baunilha())
print(bolo_baunilha.show_bolo())
