""" Aula 03 - Multiplos gráficos com Matplotlib """

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)
y = np.cos(t)
y1 = np.sin(t)

# tudo que coloco entre plt.figure() e plt.show() é referente a um gráfico específico
plt.figure("Grafico", figsize=(6, 4))
plt.plot(t, y, label="Cosseno")
plt.plot(t, y1, label="Seno")
plt.title("Gráfico de Cosseno e Seno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
