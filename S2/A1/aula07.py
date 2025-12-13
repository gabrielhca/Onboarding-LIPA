""" I/O Input and Output """

# saida padrao - sys stdout
print('Hello, World!', 'Maria', 1, True, sep=' ; ', end=' !!!\n')
# print('Hello, World!', 'Maria', 1, True, sep=' ; ', end='')

# saida em arquivo
arquivo = open('nomes.txt', 'w', encoding='utf-8')
print('joao@email.com',
      'maria@email.com',
      'pedro@email.com',
      file=arquivo,
      sep=';'
      )

# entrada padrao - sys stdin
# input
# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# print(type(nome), type(idade))

# if idade >= 18:
#     print(f'{nome} voce é maior de idade.')
# else:
#     print(f'{nome} voce é menor de idade.')

# file
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
print(notas)
notas = [float(nota) for nota in notas]
print(notas)

media = (float(notas[0]) + float(notas[1]) + float(notas[2])) / len(notas)
print(media)
