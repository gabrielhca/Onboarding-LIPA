""" Aula 06 - Subplots com Matplotlib """

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**2
y2 = x**3
y3 = x**4
y4 = x**5


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
plt.suptitle("Gráficos de Potências")
plt.subplots_adjust(wspace=0.5, hspace=0.5)

axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Quadrado")
axes[0, 0].set_xlabel("Eixo X")
axes[0, 0].set_ylabel("Eixo Y")
axes[0, 0].grid(True)

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("Cubo")
axes[0, 1].set_xlabel("Eixo X")
axes[0, 1].set_ylabel("Eixo Y")
axes[0, 1].grid(True)

axes[1, 0].plot(x, y3)
axes[1, 0].set_title("Quarta Potência")
axes[1, 0].set_xlabel("Eixo X")
axes[1, 0].set_ylabel("Eixo Y")
axes[1, 0].grid(True)

axes[1, 1].plot(x, y4)
axes[1, 1].set_title("Quinta Potência")
axes[1, 1].set_xlabel("Eixo X")
axes[1, 1].set_ylabel("Eixo Y")
axes[1, 1].grid(True)

plt.show()
