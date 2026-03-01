""" Aula 07 - Gráficos de Linhas com Matplotlib """

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 30)
y = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color="purple", lw=1.5, ls="dashdot", marker="o")
plt.xlabel("Eixo Tempo")
plt.ylabel("Eixo Amplitude")
plt.title("Gráficos de Cosseno")
plt.grid(True)
plt.show()