# Filtro média
"""O filtro média é um filtro linear, classificado como passa-baixas. Esse tipo
de filtro substitui cada pixel da imagem pelo valor médio da vizinhança"""

# Importando as bibliotecas
import cv2 as cv
from matplotlib import pyplot as plt

# Lendo a imagem
img = cv.imread('einstein.png')

# usando a Função blur, sempre passar valores ímpares
imgM = cv.blur(img, (5, 5))

# Vizualizando a imagem sem filtro
fig = plt.figure(figsize=(20, 50))
ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem com ruido")

# Vizualizando a imagem com filtro
ax2 = fig.add_subplot(122)
plt.imshow(imgM)
plt.title("Imagem com filtro")
plt.show()
