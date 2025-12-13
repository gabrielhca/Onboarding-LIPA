""" ex04 - identificador codigo do usuario e mostra os erros"""

# o codigo identificador contem 7 caracteres
# começa com BR
# seguido de um numero inteiro entre 0001 e 9999
# por fim, terminacom o caractere X

erro = []
chave = False

TAMANHO_CODIGO = 7
INICIO_CODIGO = 'BR'
FIM_CODIGO = 'X'

while chave == False:
    codigo = input('Digite o codigo de usuario: ')
    numero_codigo = codigo[2:6]
    if len(codigo) != TAMANHO_CODIGO:
        erro.append("O identificador não tem 7 caracteres")
    if codigo[0:2] != INICIO_CODIGO:
        erro.append("O identificador não começa com BR")
    if codigo[-1:] != FIM_CODIGO:
        erro.append("O identificador não termina com X")
    if not (numero_codigo.isdigit() and 1 <= int(numero_codigo) <= 9999):
        erro.append("O numero do identificador não está entre 0001 e 9999")
    if len(erro) == 0:
        chave = True
        break
    else:
        print("Acesso negado. :(")
        for x in erro:
            print('- ' + x)
        erro = []

print("Codigo valido! Acesso permitido. :)")
