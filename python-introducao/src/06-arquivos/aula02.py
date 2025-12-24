""" Aula 02 - Manipulação de Arquivos em Python """

# arquivo = open("python-introducao/src/06-arquivos/aula02.txt", "w")

# lista = ["Sergio", "Juliana", "Ricardo", "Amanda"]

# escreve uma string no arquivo e apaga o conteúdo anterior
# arquivo.write("Caio\nMarcos\nAna\nPatricia\n")

# escreve uma lista de strings no arquivo

# for nome in lista:
#     arquivo.write(f"{nome}\n")

# arquivo.close()

# leitura de arquivos com gerenciador de contexto (with)
# with open("python-introducao/src/06-arquivos/aula02.txt", "r") as arquivo:
# arquivo.write("Julia\n")
# x = arquivo.read()
# print(x)
# print(type(x))
# x = arquivo.readlines()
# print(x)
# print(type(x))

# leitura de arquivos em modo binário com gerenciador de contexto (with)
# with open("python-introducao/src/06-arquivos/aula02.txt", "rb") as arquivo:
# x = arquivo.read()
# print(x)
# print(type(x))
# print(x.decode())  # decodifica os bytes para string
# print(type(x.decode()))
# for i in arquivo:
#     print(i)
#     print(next(arquivo))

# o arquivo é um gerador por isso podemos iterar sobre ele
# não somos dependentes dos seus metodos como o read() ou readlines()
# with open("python-introducao/src/06-arquivos/aula02.txt", "r") as arquivo:
# for i in arquivo:
#   print(i)
#     print(next(arquivo))
#     print(next(arquivo))

# print("fim")
