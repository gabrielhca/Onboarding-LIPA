""" ex02 - definindo o mes com dicionario"""

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

numero_mes = int(input("Digite o numero do mes do seu aniversario (1-12): "))

if 1 <= numero_mes <= 12:
    mes_aniversario = meses[numero_mes]
    print(f'Seu aniversario é em {mes_aniversario}.')
else:
    print("Numero errado! ('._.)")
