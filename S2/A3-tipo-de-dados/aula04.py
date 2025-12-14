""" Aula 04 - Tipos de Dados - dicionario """

# dicionario (dict)
# coleção de key-value (chave-valor)
# key ela é unica
# mutavel

# criando um dicionario
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

print(carro, type(carro))

# acessando valores pelo key
print(carro["marca"])
print(carro.get("modelo"))

# pegar todas as chaves, valores, pares
print(carro.keys())
print(carro.values())
print(carro.items())

# verificar se uma chave existe
print("marca" in carro)
print("cor" in carro)

# adicionar chave/valor
carro["cor"] = "azul"
print("cor" in carro)
print(carro, type(carro))


# remover a chave/valor
marca = carro.pop("marca")
print(marca)
print(carro)

# loop
print('-----')
for key in carro:
    print(key, carro[key], type(key))

print('-----')

for value in carro.values():
    print(value)

print('-----')

for key in carro.keys():
    print(key)

print('-----')

for key, value in carro.items():
    print(key, value)

# lista de dicionarios

aluno1 = {
    "nome": "Ana",
    "email": "ana@example.com",
    'notas': [9.0, 8.5, 7.5]
}

aluno2 = {
    "nome": "Bia",
    "email": "bia@example.com",
    'notas': [6.0, 7.0, 8.0]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)
