# from code.Cat import Cat
#
# new_cat = Cat(age=10, weight=5, height=30, length=50, position=(0, 0))
# print(new_cat.age)

# from code.AnimalFactory import AnimalFactory
#
# new_dog = AnimalFactory.new_animal(animal_type='dog', age=1, weight=10, height=20, length=30)
# new_cat = AnimalFactory.new_animal(animal_type='cat', age=3, weight=10, height=20, length=30)
#
# print(new_dog.position)
# print(new_cat.position)

# class Casa:
#     def __init__(self, num_quartos=None, num_banheiros=None, tem_garagem=None, tem_jardim=None):
#         self.num_quartos = num_quartos
#         self.num_banheiros = num_banheiros
#         self.tem_garagem = tem_garagem
#         self.tem_jardim = tem_jardim
#
#     def __str__(self):
#         caracteristicas = []
#         if self.num_quartos:
#             caracteristicas.append(f'Número de quartos: {self.num_quartos}')
#         if self.num_banheiros:
#             caracteristicas.append(f'Número de banheiros: {self.num_banheiros}')
#         if self.tem_garagem:
#             caracteristicas.append(f'Possui garagem')
#         if self.tem_jardim:
#             caracteristicas.append(f'Possui jardim')
#
#         return ', '.join(caracteristicas)
#
#
# casa = Casa(num_quartos=3, num_banheiros=2, tem_garagem=True, tem_jardim=True)
# print('Características da casa:', casa)
#
# outra_casa = Casa(num_quartos=4, num_banheiros=3)
# print('Características da casa:', outra_casa)

class Casa:
    def __init__(self):
        self.num_quartos = None
        self.num_banheiros = None
        self.tem_garagem = False
        self.tem_jardim = False

    def __str__(self):
        caracteristicas = []
        if self.num_quartos:
            caracteristicas.append(f'Número de quartos: {self.num_quartos}')
        if self.num_banheiros:
            caracteristicas.append(f'Número de banheiros: {self.num_banheiros}')
        if self.tem_garagem:
            caracteristicas.append(f'Possui garagem')
        if self.tem_jardim:
            caracteristicas.append(f'Possui jardim')

        return ', '.join(caracteristicas)


class CasaBuilder:
    def __init__(self):
        self.casa = Casa()

    def set_num_quartos(self, num_quartos):
        self.casa.num_quartos = num_quartos
        return self

    def set_num_banheiros(self, num_banheiros):
        self.casa.num_banheiros = num_banheiros
        return self

    def adicionar_garagem(self):
        self.casa.tem_garagem = True
        return self

    def adicionar_jardim(self):
        self.casa.tem_jardim = True
        return self

    def obter_casa(self):
        return self.casa


builder_casa = CasaBuilder()
casa = builder_casa.set_num_quartos(3). \
    set_num_banheiros(2). \
    adicionar_garagem(). \
    adicionar_jardim(). \
    obter_casa()
print('Características da casa:', casa)

outra_casa = CasaBuilder().set_num_quartos(4).set_num_banheiros(3).adicionar_garagem().obter_casa()
print('Características da casa:', outra_casa)
