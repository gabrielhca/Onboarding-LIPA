""" Aula 01 - debugging"""


def somar(n1, n2, n3):
    """Função que soma três números."""
    soma = n1 + n2 + n3
    return soma


def calcular_media(n1, n2, n3):
    """Função que calcula a média de três números"""
    total = somar(n1, n2, n3)
    soma_media = total / 3
    return soma_media


NOTA1 = 10.0
NOTA2 = 3.0
NOTA3 = 5.5

# breakpoint()  # Ponto de interrupção para depuração
media = calcular_media(NOTA1, NOTA2, NOTA3)
print(media)
