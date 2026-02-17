""" Aula 01 - Introdução ao NumPy """

import numpy as np
from numpy.random import default_rng
from time import process_time
import matplotlib.pyplot as plt

# ndarray
# 1-D array
# 2-D matrix
# 3-D tensor

# np.array()
a = np.array([1, 2, 3, 4, 5, 6])
print(a, type(a))

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b, type(b))

# np.zeros()
zeros_3d = np.zeros(shape=(5, 3, 6))
print(zeros_3d)

zeros_4d = np.zeros(shape=(2, 5, 3, 6))
print(zeros_4d)

# np.ones()
ones_3d = np.ones((5, 3, 6))
print(ones_3d)

# np.empty()
vazio = np.empty((3, 4))
print(vazio)

# np.arange()
arr = np.arange(50, 400, 30)
print(arr)

# posso inverter a ordem dos argumentos ao nomear os parâmetros
arr2 = np.arange(step=30, start=50, stop=200)
print(arr2)

# np.linspace()
# # Gera 20 números linearmente espaçados entre 0 e 100
array_linear = np.linspace(0, 100, num=40, endpoint=False)
print(f'Array linear, com endpoint=False: {array_linear}')

array_linear2 = np.linspace(0, 100, num=40, endpoint=True)
print(f'Array linear, com endpoint=True: {array_linear2}')

array_linear3 = np.linspace(0, 100, num=40, endpoint=False, retstep=True)
print(f'Array linear com retstep=True: {array_linear3}')

array_linear3 = np.linspace(0, 100, num=40, endpoint=False, retstep=False)
print(f'Com retstep=False: {array_linear3}')

# descobrindo o tamanho do array
print('\n')
print(f'Forma do zeros_3d: {zeros_3d.shape}')
print(f'Tamanho do zeros_3d: {zeros_3d.size}')
print(f'Dimensão do zeros_3d: {zeros_3d.ndim}')
print('\n')
print(f'Forma do vazio: {vazio.shape}')
print(f'Tamanho do vazio: {vazio.size}')
print(f'Dimensão do vazio: {vazio.ndim}')
print('\n')

# transformando um vetor (1-D) em matriz (2-D)
vetor = np.array([1, 2, 3, 4, 5, 6])
print('Vetor original:')
print(vetor.shape)
print(vetor.ndim)
print(vetor)
print('\n')
matriz = vetor[np.newaxis, :]
print('Matriz:')
print(matriz.shape)
print(matriz.ndim)
print(matriz)
print('\n')
matriz2 = vetor[:, np.newaxis]
print('Matriz 2:')
print(matriz2.shape)
print(matriz2.ndim)
print(matriz2)
print('\n')
print(f'matriz2[0, 0] = {matriz2[0, 0]}')
print(f'matriz2[1, 0] = {matriz2[1, 0]}')
print(f'matriz2[2, 0] = {matriz2[2, 0]}')

# concatenando arrays
print('\n')
print('Concatenando arrays:')
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
d = np.concatenate((b, a, b))
print(c)
print(d)
print('\n')

# consultando itens de uma array
print('Consultando itens de um array:')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

maior_8 = a[a > 8]
print(f'Números maiores que 8: {maior_8}')

pares = a[a % 2 == 0]
print(f'Números pares: {pares}')

# operações com arrays
print('\n')
print('Operações com arrays:')
a = np.array([1, 2, 3,])
print(f'Array original: {a}')
print(f'Soma do array: {a.sum()}')
print(f'Max do array: {a.max()}')
print(f'Min do array: {a.min()}')
print(f'Média do array: {a.mean()}')

# gerando números aleatórios
print('\n')
print('Gerando números aleatórios:')
rng = default_rng()
aleatorio = rng.integers(10, size=(2, 4))
print(aleatorio)

# diferença entre array e a lista
print('\n')
print('Diferença entre array e lista:')
# array é mais rapido por ter o mesmo tipo sempre
a = np.array([1, 2, 'Gabriel', 4, 5, 7, 8])
print(a, type(a))
b = [1, 2, 'Gabriel', 4, 5, 7, 8]
print(b, type(b))

# comparando o prcessamento
print('\n')
print('Comparando o processamento:')
lista_a = list(rng.integers(1, 100, size=10000))
lista_b = list(rng.integers(1, 100, size=10000))
c = []
t1 = process_time()
# c = lista_a * lista_b

for i in range(len(lista_a)):
    c.append(lista_a[i] * lista_b[i])
t2 = process_time()
print(t2-t1)

a = rng.integers(1, 100, size=10000)
b = rng.integers(1, 100, size=10000)
t1 = process_time()
c = a * b
t2 = process_time()
print(t2-t1)

# plotando um gráfico
print('\n')
print('Plotando um gráfico:')

dados_x = rng.integers(20, size=30)
dados_y = rng.integers(12, size=30)
plt.scatter(x=dados_x, y=dados_y)
plt.show()
