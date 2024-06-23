import time

import numpy as numpy

# O que é um Numpy?
#   - É uma biblioteca que oferece estruturas de dados não nativas do Python com suporte;

# Por que Numpy?
#   - Oferece desempenho e ferramentas superiores à biblioteca padrão;

# O Numpy trabalha com a ideia de vetores (arrays), conhecidos como ndarrays;
# Com a diferença que ndarrays só trabalham com dados do mesmo tipo, lembrando muito as listas do Python;
# Outra vantagem considerável é que, por trabalhar com um só tipo de dado, o ndarray tem um desempenho muito melhor se comparado com listas no Python;

# 1 - Exemplo de criação:
# ndarray1 = numpy.zeros(100000)
# print(f'Conteúdo da lista: {ndarray1}; Tamanho da lista: {len(ndarray1)}')
#
# ndarray2 = numpy.ones(100000)
# print(f'Conteúdo da lista: {ndarray2}; Tamanho da lista: {len(ndarray2)}')
#
# ndarray3 = numpy.linspace(10, 100, 1000)
# print(f'Conteúdo da lista: {ndarray3}; Tamanho da lista: {len(ndarray3)}')


# 2 - Comparação de desempenho
# startTime1 = time.time()
# lista = [0] * 1000000000
# endTime1 = time.time()
# elapsedTime1 = endTime1 - startTime1
# print(f'A criação da lista de 1 bilhão de elementos levou: {elapsedTime1}')

# startTime2 = time.time()
# ndarray = numpy.zeros(1000000000)
# endTime2 = time.time()
# elapsedTime2 = endTime2 - startTime2
# print(f'A criação de um ndarray de 1 bilhão de elementos levou: {elapsedTime2}')


# 3 - Podemos fazer ainda melhor se definirmos o tipo de dado, como por exemplo: dado tipo int8 (para valores de 0 - 255)
# startTime3 = time.time()
# ndarrayUnit8 = numpy.zeros(1000000000, dtype='uint8')
# endTime3 = time.time()
# elapsedTime3 = endTime3 - startTime3
# print(f'A criação de um ndarray de 1 bilhão de elementos em int de 8 não sinalizados levou: {elapsedTime3}')


# 4 - Podemos criar vetores, matrizes e tensores
# rng = numpy.random.default_rng()
# vetor = rng.random(4)
# print(f'Array de 1 dimensão (VETOR) randômico: \n{vetor}\n')
#
# matriz = rng.random([4, 4])
# print(f'Array de 2 dimensões (MATRIZ) randômico: \n{matriz}\n')
#
# tensor = rng.random([4, 4, 4])
# print(f'Array de 3 dimensões (TENSOR) randômico: \n{tensor}\n')


# 5 - Podemos realizar a ordenação de vetores
# rng = numpy.random.default_rng()
# matriz = rng.random([4, 4])
# matrizColuna = numpy.sort(matriz, axis=0)
# matrizLinha = numpy.sort(matriz, axis=1)
# matrizColunaLinha = numpy.sort(matrizLinha, axis=0)
# print(f'Ordenação dentro da coluna: \n{matrizColuna}\n')
# print(f'Ordenação dentro da linha: \n{matrizLinha}\n')
# print(f'Ordenação dentro da coluna e da linha: \n{matrizColunaLinha}\n')


# 6 - Agora vamos preparar alguns ndarrays para serem representados por gráficos
# vetorA = numpy.linspace(10, 1000, 100)
# vetorB = numpy.linspace(10, 3000, 100)
# vetorC = numpy.linspace(10, 8000, 100)
#
# print(vetorA)
# print(vetorB)
# print(vetorC)
#
# numpy.savetxt('vetor_a.txt', vetorA, fmt='%f', delimiter=';')
# numpy.savetxt('vetor_b.txt', vetorB, fmt='%f', delimiter=';')
# numpy.savetxt('vetor_c.txt', vetorC, fmt='%f', delimiter=';')


# 7 - Agora podemos utilizar uma das várias bibliotecas para plotar gráficos. A biblioteca escolhida foi: plotly
import plotly.express

arrayA = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
arrayB = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
arrayC = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')
print(arrayA)

arrayABC = numpy.vstack([arrayA, arrayB, arrayC])
print(arrayABC)

arrayABC = arrayABC.transpose()
print(arrayABC)

figure = plotly.express.line(arrayABC)
figure.show()