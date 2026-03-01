import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv(
    "./classificacao-imagens-DL/src/03-matplotlib/exercicios/data/classification_results_trial_0001.csv")

df["acerto"] = df["real_class"] == df["predicted_class"]


def categorizar_erros(linha):
    if linha["real_class"] == "benign" and linha["predicted_class"] == "malign":
        return "Falso Positivo (FP)"
    elif linha["real_class"] == "malign" and linha["predicted_class"] == "benign":
        return "Falso Negativo (FN)"
    else:
        return "Acerto"


df["resultado"] = df.apply(categorizar_erros, axis=1)

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 16))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle("Diagnostico da Classificação: Realidade x Predição",
             fontsize=18, color="blue")


# Gráfico de barras: contagem por real_class.
contagem_real = df["real_class"].value_counts()
axes[0, 0].bar(contagem_real.index, contagem_real.values,
               color=["red", "green"])
axes[0, 0].set_title("Distribuição Real")
axes[0, 0].set_ylabel("Contagem")

# Gráfico de barras: contagem por predicted_class.
contagem_pred = df["predicted_class"].value_counts()
axes[0, 1].bar(contagem_pred.index, contagem_pred.values,
               color=["green", "red"])
axes[0, 1].set_title("Distribuição Prevista")
axes[0, 1].set_ylabel("Contagem")

# Histograma de prob_benign.
axes[1, 0].hist(df["prob_benign"], bins=20, color="green", edgecolor="black")
axes[1, 0].set_title("Distribuição de Probabilidade: Benigno")
axes[1, 0].set_xlabel("Probabilidade")

# Histograma de prob_malign.
axes[1, 1].hist(df["prob_malign"], bins=20, color="red", edgecolor="black")
axes[1, 1].set_title("Distribuição de Probabilidade: Maligno")
axes[1, 1].set_xlabel("Probabilidade")

# Scatter plot: X=prob_benign, Y=prob_malign, com cor diferente para acertos erro.
acertos = df[df["acerto"] == True]
erros = df[df["acerto"] == False]

axes[2, 0].scatter(acertos["prob_benign"], acertos["prob_malign"],
                   color="green", label="Acerto", marker="o")
axes[2, 0].scatter(erros["prob_benign"], erros["prob_malign"],
                   color="red", marker="o", label="Erro")
axes[2, 0].set_title("Dispersão de Confiança")
axes[2, 0].set_xlabel("Prob. Benigno")
axes[2, 0].set_ylabel("Prob. Maligno")
axes[2, 0].legend()

# Qual erro é mais comum (FP ou FN)? Crie um gráfico que ajude a visualizar isso.
erros_df = df[df["resultado"] != "Acerto"]
contagem_erros = erros_df["resultado"].value_counts()

if not contagem_erros.empty:
    axes[2, 1].bar(contagem_erros.index, contagem_erros.values,
                   color=["green", "red"])
    axes[2, 1].set_title("FP vs FN")
    axes[2, 1].set_ylabel("Ocorrências")

plt.show()

# E em contexto médico: qual é mais preocupante e por quê?

# O Ultimo grafico. Ele mostra que a quantidade de Falsos Negativos (FN)
# é muito maior do que a quantidade de Falsos Positivos (FP).
# Em um contexto médico, os Falsos Negativos geralmente são mais preocupantes.
# Isso pode levar a atrasos no tratamento e piora da condição do paciente.
