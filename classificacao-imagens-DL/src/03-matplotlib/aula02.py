""" Aula 02 - Introdução ao Matplotlib """

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)  # Gera 10 pontos entre 0 e 5
y = np.cos(4*t)
y1 = np.sin(4*t)

plt.figure("Cosseno", figsize=(3, 2))  # Cria a figura 1
plt.plot(t, y)
plt.title("Gráfico de Coseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
# plt.grid(True)

plt.figure("Seno", figsize=(3, 2))  # Cria a figura 2
plt.plot(t, y1)
plt.title("Gráfico de Seno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
# plt.grid(True)
plt.show()
