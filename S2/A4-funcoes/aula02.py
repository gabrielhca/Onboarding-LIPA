""" Aula 02 - Argumentos: positional, keyword, default value"""

# declara uma funcao que soma dois numeros


def somar(n1, n2):
    return n1 + n2


def dividir(dividendo, divisor):
    return dividendo / divisor


# argumentos posicionais
print(somar(13.5, 5.5))
print(somar(2.0, 6.5))
print(dividir(10.0, 2.0))

# unpak list e tuplas
# tem que ter a mesma quantidade de elementos
numeros = [7.5, 2.5]
print("somar numeros de uma lista:", somar(numeros[0], numeros[1]))
print("somar numeros de uma lista:", somar(*numeros))

# unpak dicionários
numeros_dict = {
    'n2': 10.0,
    'n1': 5.0
}

print("somar numeros de um dicionario:", somar(**numeros_dict))

# declaracao
# nome: saudacoes
# parametros: nome (obrigatorio), saudacao (opicional)
# retorno: string


def saudacoes(nome, saudacao="Oi"):
    return f"{saudacao}, {nome}!"


print(saudacoes("Ana", "Olá"))
print(saudacoes("Carlos", "Bom dia"))
print(saudacoes("Gabriel"))

print(saudacoes(saudacao="Oi Oi", nome="Mariana"))
print(saudacoes(nome="Pedro"))

# argumentos nomeados (keyword arguments)
print(somar(n2=10.0, n1=7.5))
print(somar(n2=4.0, n1=3.5))
print(dividir(divisor=4.0, dividendo=20.0))
