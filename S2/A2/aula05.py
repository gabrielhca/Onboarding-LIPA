""" Aula 05 - break e continue"""

for i in range(10):
    if i == 5:
        break
    print(i)

# encontrar a posiçõ de um numero
# # em uma lista de inteiros. Caso não
# encontr posição é igual a -1

busca = 5
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
posicao = -1
contador = 0

for numero in numeros:
    print("Procurando na posição:", contador, "encontrado o numero:", numero)
    if numero == busca:
        posicao = contador
        break
    contador += 1

print("Posição =", posicao)


# for i in range(len(numeros)):
#     print("Procurando na posição:", i, "encontrado o numero:", numeros[i])
#     if numeros[i] == busca:
#         posicao = i
#         break

# print("Posição =", posicao)

# continue
# não para o loop em si, mas pula a iteração atual
print("-----")
for numero in numeros:
    if numero == 3:
        continue
    print(numero)
