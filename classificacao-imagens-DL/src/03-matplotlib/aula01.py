""" Aula 01 - Introdução ao Matplotlib """

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)  # Gera 10 pontos entre 0 e 5
y = np.cos(4*t)

plt.plot(t, y)
plt.title("Gráfico de Coseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
# plt.grid(True)
plt.show()
