""" Aula 03 - Diferentes estilos de gráficos com Matplotlib """""" Aula 08 - Customiizando as escalas dos eixos com Matplotlib """

import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.style as slay # Importa o módulo de estilos do Matplotlib

plt.style.use("ggplot")


x = np.linspace(0, 2*np.pi, 500)
y = np.cos(3*x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y)
axe.set_title("Gráfico de Cosseno", fontsize=16, color="blue")
axe.set_xlabel("Eixo Tempo", fontsize=12, color="red")
axe.set_ylabel("Eixo Amplitude", fontsize=12, color="red")

plt.xticks(np.arange(0, 2*np.pi+0.1, np.pi/2),
           ["0", "π/2", "π", "3π/2", "2π"], color="green")
plt.yticks(np.arange(-1, 1.1, 0.5), color="green")

axe.grid(True)
plt.show()
