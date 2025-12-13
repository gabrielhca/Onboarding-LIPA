""" Aula 05 - Tipos de Dados """

# Numerericos
# int float

idade = 27
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# strings

nome = 'Carlos'
sobrenome = 'Carneiro'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca-Cola'

print(f'O cliente {nome} {sobrenome} comprou 1 {produto}.')

print(nome[0], nome[-1])

print(nome.lower())
print(nome.upper())

print(1, 7, 2, 3, 5, sep='xxxx')

# booleanos
ligado = True
print(ligado, type(ligado))

resultado = 10 < 3
print(resultado, type(resultado))

# Listas
frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])

frutas[0] = 'banana nanica'
frutas.append('abacaxi')
print(frutas)
print(len(frutas))

for frutas in frutas:
    print(frutas.upper())

# Tuplas
codigos = ('SP01', 'RJ02', 'MG03')
print(codigos[0])

# codigo[0] = 'SP99'  # Erro!

# conjuntos (sets)
resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(18)
print(resultado_sorteio)

# dicionarios
funcionario = {
    'codigo': 123,
    'nome': 'Carlos',
    'salario': 4500.00
}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())