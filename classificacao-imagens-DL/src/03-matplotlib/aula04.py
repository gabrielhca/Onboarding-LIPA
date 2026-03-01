""" Aula 04 - subplots com Matplotlib """

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
c = np.cos(x)
s = np.sin(x)

plt.figure("Grafico consenoidais", figsize=(8, 6))
plt.subplots_adjust(
    #left=0.1,
    #bottom=0.1,
    #right=0.9,
    #top=0.9,
    wspace=0.5,
    hspace=0.5
)

# (n_linhas, n_colunas, posicao)
ax1 = plt.subplot(2, 2, 1)  
plt.plot(x, c)
ax1.set_title("Cosseno")
ax1.set_xlabel("Tempo (s)")
ax1.set_ylabel("Amplitude")

ax2 = plt.subplot(2, 2, 2)
plt.plot(x, s)
ax2.set_title("Seno")
ax2.set_xlabel("Tempo (s)")
ax2.set_ylabel("Amplitude")

ax3 = plt.subplot(2, 2, 3)  
plt.plot(x, c)
ax3.set_title("Cosseno")
ax3.set_xlabel("Tempo (s)")
ax3.set_ylabel("Amplitude")

ax4 = plt.subplot(2, 2, 4)
plt.plot(x, s)
ax4.set_title("Seno")
ax4.set_xlabel("Tempo (s)")
ax4.set_ylabel("Amplitude")

plt.show()
