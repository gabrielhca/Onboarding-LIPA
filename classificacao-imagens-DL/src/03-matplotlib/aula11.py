""" Aula 11 - Identificando com linhas paralelas e marcadores """

from matplotlib import pyplot as plt
import numpy as np

plt.style.use("ggplot")

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.text(2.6, 0.35, "P(2.5, 0.4)", fontsize=10, color="red")
axe.text(3, 0.42, "Logaritmo de 2.5", fontsize=10, color="red",
         bbox=dict(facecolor="white", edgecolor="red", boxstyle="round"))
axe.annotate("P(2.5, 0.4)", xy=(2.5, 0.4), xytext=(0.5, 0.5),
             fontsize=10, arrowprops=dict(facecolor="gray"), color="red")
axe.plot(x, y, lw=1.2, color="green")
axe.plot([0, 2.5], [0.4, 0.4], lw=1.2, color="gray", ls="--")
axe.plot([2.5, 2.5], [0, 0.4], lw=1.2, color="gray", ls="--")
axe.plot([2.5], [0.4], marker="o", markersize=8, color="red")
axe.set_xticks(np.arange(0, 5.5, 0.5))
axe.set_title("Gráfico de Logaritmo", fontsize=16, color="blue")
axe.set_xlabel("Eixo X", fontsize=12, color="gray")
axe.set_ylabel("Eixo Y", fontsize=12, color="gray")
plt.show()
