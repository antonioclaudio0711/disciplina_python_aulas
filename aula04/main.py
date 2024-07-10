# 1. Criação de eventos para teclas pressionadas no teclado
# import keyboard
#
#
# def on_key_event(event):
#     if event.event_type == keyboard.KEY_DOWN:
#         print(f'Tecla pressionada: {event.name}')
#         if event.name == 'a':
#             print('A em especial')
#
#
# keyboard.on_press(on_key_event)
#
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print('Programa interrompido pelo usuário!')


# 2. Criação de eventos utilizando aspectos temporais
# import sched
# import time
#
#
# def exibir_mensagem(mensagem):
#     print(mensagem)
#
#
# def agendar_evento(scheduler, intervalo, mensagem):
#     scheduler.enter(intervalo, 1, agendar_evento, (scheduler, intervalo, mensagem))
#     exibir_mensagem(mensagem=mensagem)
#
#
# new_scheduler = sched.scheduler(time.time, time.sleep)
# agendar_evento(scheduler=new_scheduler, intervalo=1, mensagem='Esta é a mensagem agendada a cada 1 segundo!')
#
# print('Esperando para exibir as mensagens agendadas!')
#
# new_scheduler.run()


# 3. Criando e utilizando decorators
# def meu_decorator(funcao):
#     def wrapper():
#         print('A função será executada agora!')
#         funcao()
#         print('A função foi executada!')
#
#     return wrapper
#
#
# @meu_decorator
# def minha_funcao():
#     print('Esta é a função original!')
#
#
# minha_funcao()
#
#
# import time
#
#
# def medir_tempo(funcao):
#     def wrapper(*args, **kwargs):
#         inicio = time.time()
#         resultado = funcao(*args, **kwargs)
#         fim = time.time()
#
#         print(f'A função {funcao.__name__} demorou {fim - inicio:.6f} segundos para ser executada!')
#
#         return resultado
#
#     return wrapper
#
#
# @medir_tempo
# def exemplo_funcao(tempo_espera):
#     time.sleep(tempo_espera)
#     print('A função foi executada!')
#
#
# exemplo_funcao(tempo_espera=2)
#
#
# class Carro:
#     def __init__(self, classe_decorada):
#         self.classe_decorada = classe_decorada
#
#     def __call__(self, *args, **kwargs):
#         instancia_classe = self.classe_decorada(*args, **kwargs)
#         instancia_classe.num_rodas = 4
#         return instancia_classe
#
#
# @Carro
# class Automovel:
#     def __init__(self, modelo):
#         self.modelo = modelo
#
#
# new_auto: Automovel = Automovel(modelo='Gol')
# print(new_auto.num_rodas)
# print(new_auto.modelo)


# 4. Compreensão de listas
# import time
#
#
# def medir_tempo(funcao):
#     def wrapper(*args, **kwargs):
#         inicio = time.time()
#         resultado = funcao(*args, **kwargs)
#         fim = time.time()
#         duracao = fim - inicio
#
#         print(f'A função levou {duracao:.6f} segundos para ser executada!')
#         return resultado
#
#     return wrapper
#
#
# @medir_tempo
# def retorna_lista_sem_comprehension(max_value):
#     lista_pares = []
#     for num in range(max_value):
#         if num % 2 == 0:
#             lista_pares.append(num)
#         else:
#             lista_pares.append('Ímpar')
#
#     return lista_pares
#
#
# @medir_tempo
# def retorna_lista_com_comprehension(max_value):
#     lista_pares = [num for num in range(max_value) if num % 2 == 0]
#
#     return lista_pares
#
#
# @medir_tempo
# def retorna_lista_pares_e_impares_com_comprehension(max_value):
#     lista_pares_impares = [num if num % 2 == 0 else 'Ímpar' for num in range(max_value)]
#     return lista_pares_impares
#
#
# retorna_lista_sem_comprehension(max_value=1000000)
# retorna_lista_com_comprehension(max_value=1000000)
# retorna_lista_pares_e_impares_com_comprehension(max_value=1000000)


# 5. Padrão de design comportamental mediador (MEDIATOR)
# class TorreDeControle:
#     def __init__(self):
#         self.avioes = []
#
#     def adicionar_aviao(self, aviao):
#         self.avioes.append(aviao)
#         aviao.registrar_torre(self)
#
#     def enviar_mensagem(self, aviao, mensagem):
#         print(f'Torre de controle para {aviao.nome}: {mensagem}')
#         for outro_aviao in self.avioes:
#             if outro_aviao != aviao:
#                 outro_aviao.receber_mensagem(aviao, mensagem)
#
#
# class Aviao:
#     def __init__(self, nome):
#         self.nome = nome
#         self.torre = None
#
#     def registrar_torre(self, torre):
#         self.torre = torre
#
#     def enviar_mensagem(self, mensagem):
#         self.torre.enviar_mensagem(self, mensagem)
#
#     def receber_mensagem(self, aviao, mensagem):
#         print(f'{self.nome} recebeu uma mensagem de {aviao.nome}: {mensagem}')
#
#
# torre_de_controle = TorreDeControle()
#
# aviao1 = Aviao(nome='Avião 01')
# aviao2 = Aviao(nome='Avião 02')
# aviao3 = Aviao(nome='Avião 03')
#
# torre_de_controle.adicionar_aviao(aviao=aviao1)
# torre_de_controle.adicionar_aviao(aviao=aviao2)
# torre_de_controle.adicionar_aviao(aviao=aviao3)
#
# aviao1.enviar_mensagem(mensagem='Vamos decolar!')
# aviao2.enviar_mensagem(mensagem='Confirmado! Prontos para decolar!')
# aviao3.enviar_mensagem(mensagem='Aguardando autorização para decolar!')


# 6. Padrão de design criacional Observador
class Mensageiro:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, remetente, mensagem):
        for observador in self.observadores:
            observador.receber_notificacao(remetente, mensagem)


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def receber_notificacao(self, remetente, mensagem):
        print(f'[{self.nome}] Nova mensagem de {remetente}: {mensagem}')


class Grupo:
    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def receber_notificacao(self, remetente, mensagem):
        print(f'Grupo {self.nome}: Nova mensagem de {remetente}: {mensagem}')


mensageiro = Mensageiro()

usuario1 = Usuario(nome='Usuário 01')
usuario2 = Usuario(nome='Usuário 02')
usuario3 = Usuario(nome='Usuário 03')

grupo1 = Grupo(nome='Família')
grupo2 = Grupo(nome='Trabalho')

mensageiro.adicionar_observador(usuario1)
mensageiro.adicionar_observador(usuario2)
mensageiro.adicionar_observador(usuario3)

grupo1.adicionar_membro(usuario1)
grupo1.adicionar_membro(usuario2)

grupo2.adicionar_membro(usuario2)
grupo2.adicionar_membro(usuario3)

mensageiro.notificar_observadores('Admin', 'Bem-vindos ao nosso aplicativo de mensagens!')
grupo1.receber_notificacao('Admin', 'Nova reunião marcada para amanhã!')
usuario3.receber_notificacao('Alice', 'Oi, tudo bem?')

