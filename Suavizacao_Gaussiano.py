# Filtro Gaussiano
"""O filtro Gaussiano é um filtro linear, passa-baixas. Apresenta bons resultados
no tratamento de imagens com ruido gaussiano"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("006_formas.png")
imgGauss = cv.GaussianBlur(img, (5, 5), 0)

"""Entrada:
img = Imagem com a qual queremos trabalhar
mascara = Dimensao da mascara que sera aplicada
suavização = Grau de suavização"""

# Vizualizando a imagem sem filtro
fig = plt.figure(figsize=(20, 50))
ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem com ruido")

# Vizualizando a imagem com filtro
ax2 = fig.add_subplot(122)
plt.imshow(imgGauss)
plt.title("Imagem com filtro")
plt.show()
