""" Aula 03 - Tipos de Dados - Set """

# set(conjunto)
# não ordenados
# mutaveis
# não indexaveis
# não aceitam elementos duplicados

# criando um set
numeros = {1, 12, 5, 7}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)

print(12 in numeros)
print(50 in numeros)

# adicionar itens no set
numeros.add(20)
print(numeros)

# adicionar um elemento de um set em outro set
print('-----')
numeros2 = {100, 200, 300}
print(numeros2)
numeros.update(numeros2)
print(numeros2)
print(numeros, type(numeros))
