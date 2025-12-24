""" Aula 01 - Manipulação de Arquivos em Python """

# open("caminho", "modo")

# Modos de abertura de arquivos
# r - leitura
# a - Append / incrementar
# w - escrita (sobrescreve o arquivo)
# x - cria o arquivo
# r+ - leitura e escrita

# abre o arquivo em modo de leitura
# arquivo = open("python-introducao/src/06-arquivos/test.txt", "r")

# print(arquivo.readable())  # verifica se o arquivo pode ser lido
# print(arquivo.read())      # lê todo o conteúdo do arquivo
# print(arquivo.readline())   # lê o arquivo linha por linha
# print(arquivo.readline())
# print(arquivo.readline())

# lê o arquivo linha por linha e retorna uma lista
# lista = arquivo.readlines()
# print(lista)
# print(lista[3])

# escreve o conteúdo do arquivo
# arquivo = open("python-introducao/src/06-arquivos/test.txt", "a")
# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# apaga o conteúdo do arquivo e escreve novos dados
# arquivo = open("python-introducao/src/06-arquivos/test2.txt", "w")
# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# cria um novo arquivo e escreve dados nele
# arquivo = open("python-introducao/src/06-arquivos/test3.txt", "x")
# arquivo.write("Python\n")


# arquivo.close()

# exclusão de arquivos

import os

# remove o arquivo
# if os.path.exists("python-introducao/src/06-arquivos/test2.txt"):
#     os.remove("python-introducao/src/06-arquivos/test2.txt")
# else:
#     print("O arquivo não existe")

# remove um diretório vazio
os.rmdir("python-introducao/src/06-arquivos/novapasta")
