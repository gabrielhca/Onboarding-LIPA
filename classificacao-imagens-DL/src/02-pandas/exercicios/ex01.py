""" Exercicio 01 - Análise de Resultados de Classificação """

import pandas as pd

# Carregando o dataset
df = pd.read_csv(
    "./classificacao-imagens-DL/src/02-pandas/exercicios/data/classification_results_trial_0001.csv")

# 1 - Quantas imagens são “benign” e “malign” em real_class?
# value_counts() retorna a contagem de cada valor único na coluna "real_class"
distribuicao_real = df["real_class"].value_counts()
print("1. Distribuição de classes reais:\n", distribuicao_real)

# 2 -Identifique em quais imagens o modelo errou a predição.
# filtra as onde a classe real é diferente da classe prevista
erros = df[df["real_class"] != df['predicted_class']]
print("\n2. Imagens com predições erradas:\n", erros)

# 3 - Verifique se o modelo estava confiante mesmo quando errou.
prob_max = erros[['prob_benign', 'prob_malign']].max(axis=1)
erros_confiante = erros[prob_max > 0.7]
print("\n3. Confiança do modelo nas predições erradas:")
print(erros_confiante[['image_path', 'real_class',
      'predicted_class', 'prob_benign', 'prob_malign']])

# 4 - Cálculo da Matriz de Confusão (TP, TN, FP, FN)
TP = len(df[(df["real_class"] == "malign") &
         (df["predicted_class"] == "malign")])
TN = len(df[(df["real_class"] == "benign") &
         (df["predicted_class"] == "benign")])
FP = len(df[(df["real_class"] == "benign") &
         (df["predicted_class"] == "malign")])
FN = len(df[(df["real_class"] == "malign") &
         (df["predicted_class"] == "benign")])

print("\n4. Matriz de Confusão:")
print(f"TP: {TP}, TN: {TN}, FP: {FP}, FN: {FN}")

# 5 - Cálculo de métricas de avaliação
# Acuracia = (TP + TN) / total
# Precisao = TP / (TP + FP)
# Recall = TP / (TP + FN)
# Especificidade = TN / (TN + FP)
print("\n5. Métricas de avaliação:")
print(f"Acuracia: {(TP + TN) / (TP + TN + FP + FN):.2f}")
print(f"Precisao: {TP / (TP + FP) if TP + FP > 0 else 0:.2f}")
print(f"Recall: {TP / (TP + FN) if TP + FN > 0 else 0:.2f}")
print(f"Especificidade: {TN / (TN + FP) if TN + FP > 0 else 0:.2f}")

# 6 - Encontre as 5 imagens benign com menor prob_benign.
menor_prob_benign = df[df["real_class"] == "benign"].sort_values(
    by="prob_benign", ascending=True).head(5)
print("\n6. 5 imagens benign com menor prob_benign:")
print(menor_prob_benign)
# O que isso pode indicar?
# Analisando os falso positivos, é possível notar que os piores 
# erros tendem a se manter perto da faixa de 50% de confiança. 
# Isso indica que ele fica mais confuso ao escolher o diagnostico

# 7 - Encontre as 5 imagens malign com maior prob_benign. 
maior_prob_malign = df[df["real_class"] == "malign"].sort_values(
    by="prob_benign", ascending=False).head(5)
print("\n7. 5 imagens malign com maior prob_benign:")
print(maior_prob_malign)
#  O que isso pode indicar?
# Analisando os falsos negativos, o algoritmo classifica imagens 
# maligna como benignas com mais de 80% de confiança, isso indica 
# que ele tende a classificar a maior partes dos tecidos como 
# saudáveis. O que é um péssimo sinal.
