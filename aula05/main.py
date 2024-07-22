# 1. Compreendendo a utilização do SQLite
# import sqlite3
#
# # Conectando ao banco de dados (cria um novo banco de dados se não existir)
# conn = sqlite3.connect('animal.db')
#
# # Criando um cursor para executar comandos SQL
# cursor = conn.cursor()
#
# # Criando uma tabela
# cursor.execute('''CREATE TABLE IF NOT EXISTS dog (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT,
#                     age INTEGER,
#                     weight REAL,
#                     height REAL,
#                     breed TEXT
#                 )''')
#
# # Exemplos de dados para inserir na tabela
# pets_data = [
#     ('Luke', 9, 45, 0.80, 'Pastor Alemao'),
#     ('Buddy', 2, 7.2, 0.3, 'Golden Retriever'),
#     ('Whiskers', 1, 1.2, 0.15, 'Siamese'),
#     ('Max', 4, 5.0, 0.4, 'Labrador'),
# ]
#
# # Inserindo os dados presentes no array pets_data na tabela dog
# for pet in pets_data:
#     cursor.execute("INSERT INTO dog "
#                    "(name, age, weight, height, breed) "
#                    "VALUES (?, ?, ?, ?, ?)",
#                    pet)
#
# # Commit das alterações
# conn.commit()
#
# # Fechando a conexão com o banco de dados
# conn.close()
#
# print('Registros inseridos com sucesso!')
#
#
# # Conectando ao banco de dados
# conn = sqlite3.connect('animal.db')
#
# # Criando um cursor para executar comandos SQL
# cursor = conn.cursor()
#
# # Selecionando todos os registros da tabela
# cursor.execute("SELECT * FROM dog")
# rows = cursor.fetchall()
#
# # Mostrando os registros
# for dog in rows:
#     print(f'Informações do cachorro ---> ID: {dog[0]}; Nome: {dog[1]}; Idade: {dog[2]}; Peso: {dog[3]}; '
#           f'Altura: {dog[4]}; Raça: {dog[5]}')


# 2. Compreendendo o uso de JSON (JavaScript Object Notation)
# import json
#
#
# # Dados a serem salvos em um arquivo JSON
# data = {
#     "name": "Luke",
#     "age": 9,
#     "weight": 45,
#     "height": 0.8,
#     "breed": "Pastor Alemão",
# }
#
# # Caminho para o arquivo JSON
# file_path = "data.json"
#
# # Salvar dados em formato JSON no arquivo
# with open(file_path, 'w') as json_file:
#     json.dump(data, json_file, indent=4)
#
# print("Dados salvos em JSON!")
#
# # Carregar dados de um arquivo JSON
# with open(file_path, 'r') as json_file:
#     loaded_data = json.load(json_file)
#
# print('Dados carregados do JSON:')
# print(loaded_data)
#
#
# class Dog:
#     def __init__(self, name, age, weight, height, breed):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
#         self.breed = breed
#
#
# # Criando um objeto da classe Dog
# dog = Dog(name="Luke", age=9, weight=45, height=0.8, breed="Pastor Alemão")
#
# # Caminho para o arquivo JSON
# file_path = "dog.json"
#
# # Convertendo o objeto para um dicionário/map
# dog_dict = {
#     "name": dog.name,
#     "age": dog.age,
#     "weight": dog.weight,
#     "height": dog.height,
#     "breed": dog.breed,
# }
#
# # Salvar dados em formato JSON no arquivo
# with open(file_path, 'w') as json_file:
#     json.dump(dog_dict, json_file, indent=4)
#
# print("Objeto da classe Dog salvo em formato JSON.")
# print("Dados salvos em JSON!")
#
# # Carregar dados de um arquivo JSON
# with open(file_path, 'r') as json_file:
#     loaded_data = json.load(json_file)
#
# print("Dados carregados do JSON:")
# print(loaded_data)
#
# # Convertendo o dicionário/map em um objeto da classe Dog
# new_dog = Dog(name=loaded_data["name"],
#               age=loaded_data["age"],
#               weight=loaded_data["weight"],
#               height=loaded_data["height"],
#               breed=loaded_data["breed"])
#
# print(f'Informações do cachorro ---> Nome: {new_dog.name}; '
#       f'Idade: {new_dog.age}; '
#       f'Peso: {new_dog.weight}; '
#       f'Altura: {new_dog.height}; '
#       f'Raça: {new_dog.breed};')


# 3. Padrão de Design Estrutural: Proxy
# import sqlite3
#
#
# class Dog:
#     def __init__(self, name, age, weight, height, breed):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
#         self.breed = breed
#
#
# # Proxy para interagir com o banco de dados SQLite3
# class DBProxy:
#     def __init__(self, database_path='animal.db'):
#         self.database_path = database_path
#
#     def insert_dog(self, new_dog: Dog):
#         conn = sqlite3.connect(self.database_path)
#         cursor = conn.cursor()
#
#         cursor.execute('''CREATE TABLE IF NOT EXISTS dogs(
#                             id INTEGER PRIMARY KEY AUTOINCREMENT,
#                             name TEXT,
#                             age INTEGER,
#                             weight REAL,
#                             height REAL,
#                             breed TEXT
#                         )''')
#
#         cursor.execute("INSERT INTO dogs "
#                        "(name, age, weight, height, breed) "
#                        "VALUES (?, ?, ?, ?, ?)",
#                        (new_dog.name, new_dog.age, new_dog.height, new_dog.weight, new_dog.breed))
#
#         conn.commit()
#         conn.close()
#         print('Dog inserido com sucesso!')
#
#     def get_all_dogs(self):
#         conn = sqlite3.connect(self.database_path)
#         cursor = conn.cursor()
#
#         cursor.execute("SELECT * FROM dogs")
#         rows = cursor.fetchall()
#
#         dogs = []
#
#         for row in rows:
#             dogs.append(Dog(name=row[1], age=row[2], weight=row[3], height=row[4], breed=row[5]))
#
#         return dogs
#
#     def get_dogs_from_name(self, dog_name):
#         conn = sqlite3.connect(self.database_path)
#         cursor = conn.cursor()
#
#         cursor.execute(f"SELECT * FROM dogs WHERE name = '{dog_name}'")
#         rows = cursor.fetchall()
#
#         dogs = []
#
#         for row in rows:
#             dogs.append(Dog(name=row[1], age=row[2], weight=row[3], height=row[4], breed=row[5]))
#
#         return dogs
#
#     def delete_all_dogs(self):
#         conn = sqlite3.connect(self.database_path)
#         cursor = conn.cursor()
#
#         cursor.execute("DELETE FROM dogs")
#
#         conn.commit()
#         conn.close()
#         print("Todos os registros da tabela dogs foram excluídos com sucesso!")
#
#     def delete_dogs_from_name(self, dog_name):
#         conn = sqlite3.connect(self.database_path)
#         cursor = conn.cursor()
#
#         cursor.execute(f"DELETE FROM dogs WHERE name = '{dog_name}'")
#
#         conn.commit()
#         conn.close()
#         print(f"Registro da tabela dogs com o nome {dog_name} foi excluído com sucesso!")
#
#
# example_dog = Dog(name="Luke", age=9, weight=45, height=0.8, breed="Pastor Alemão")
# example_dog_02 = Dog(name="Lunna", age=9, weight=20, height=0.8, breed="Spitz Alemão")
# example_dog_03 = Dog(name="Dory", age=2, weight=30, height=0.8, breed="Shitzu")
#
# dogDb = DBProxy()
#
# # dogDb.insert_dog(new_dog=example_dog)
# # dogDb.insert_dog(new_dog=example_dog_02)
# # dogDb.insert_dog(new_dog=example_dog_03)
#
# # all_dogs_list = dogDb.get_all_dogs()
# # if not len(all_dogs_list):
# #     print('Nenhum cachorro cadastrado no sistema!')
# # else:
# #     for dog in all_dogs_list:
# #         print(f'Informações do cachorro ---> Nome: {dog.name}; '
# #               f'Idade: {dog.age}; '
# #               f'Peso: {dog.weight}; '
# #               f'Altura: {dog.height}; '
# #               f'Raça: {dog.breed};')
#
# # selected_dogs_list = dogDb.get_dogs_from_name(dog_name='Mel')
# # if not len(selected_dogs_list):
# #     print('Cachorro não encontrado no sistema!')
# # else:
# #     for dog in selected_dogs_list:
# #         print(f'Informações do cachorro ---> Nome: {dog.name}; '
# #               f'Idade: {dog.age}; '
# #               f'Peso: {dog.weight}; '
# #               f'Altura: {dog.height}; '
# #               f'Raça: {dog.breed};')
#
# # dogDb.delete_all_dogs()
# # dogDb.delete_dogs_from_name(dog_name='Luke')


# 4. Padrão de Design Estrutural: Adapter
import sqlite3
import json


class JsonSqliteAdapter:
    def __init__(self, db_name):
        self.db_name = db_name

        self.conn = sqlite3.connect(self.db_name)

    def connect(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS data "
                          "(id INTEGER PRIMARY KEY AUTOINCREMENT, json_data TEXT)")

    def save_data(self, data):
        json_data = json.dumps(data)
        self.conn.execute("INSERT INTO data (json_data) "
                          "VALUES (?)",
                          (json_data,))

        self.conn.commit()

    def load_data(self):
        cursor = self.conn.execute("SELECT json_data FROM data")
        json_data_list = [row[0] for row in cursor.fetchall()]
        data_list = [json.loads(json_data) for json_data in json_data_list]

        return data_list

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    adapter = JsonSqliteAdapter(db_name='data.db')
    adapter.connect()

    data_to_save = [{"name": "Antônio Claudio", "age": 21}, {"name": "Ana Clara", "age": 18}]
    adapter.save_data(data=data_to_save)

    loaded_data = adapter.load_data()
    for item in loaded_data:
        print(item)

    adapter.close()
