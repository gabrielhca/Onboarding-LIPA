""" Exercicio 02 - Análise de Métricas de Treinamento """

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv(
    "./classificacao-imagens-DL/src/03-matplotlib/exercicios/data/metrics.csv")

lista_epocas = range(1, len(df) + 1)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# Grafico Acurácia
axes[0].plot(lista_epocas, df["train_acc"], label="train", color="blue")
axes[0].plot(lista_epocas, df["val_acc"], label="valid", color="orange")
axes[0].set_title("model accuracy")
axes[0].set_ylabel("accuracy")
axes[0].set_xlabel("epoch")
axes[0].legend(loc="upper left")

# Gráfico Perda
axes[1].plot(lista_epocas, df["train_loss"], label="train", color="blue")
axes[1].plot(lista_epocas, df["val_loss"], label="valid", color="orange")
axes[1].set_title("model loss")
axes[1].set_ylabel("loss")
axes[1].set_xlabel("epoch")
axes[1].legend(loc="upper right")

plt.show()
