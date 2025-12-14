""" Aula 02 -  Tipos de Dados - Tuplas"""

# tuplas
# ordenadas
# imutáveis
# indexaveis

nomes = ('Ana', 'Bia', 'Carlos')
print(nomes, type(nomes))

# acessar elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# tentar modificar elementos (não é possível)
# nomes[0] = 'Alice'

# iteração
for nome in nomes:
    print(nomes)

for i in range(len(nomes)):
    print(nomes[i])

nomes2 = 'Marta', 'Guilherme', 'Nicole'
print(nomes2, type(nomes2))

# unpack
# nome1 = nomes2[0]
# nome2 = nomes2[1]
# nome3 = nomes2[2]
# nome1, nome2, nome3 = nomes2 # coloca cada valor da tupla em uma variável
# print(nome1, nome2, nome3)
nome1, nome2 = nomes2[0:2]
print(nome1, nome2)

# juntar tuplas
todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))
