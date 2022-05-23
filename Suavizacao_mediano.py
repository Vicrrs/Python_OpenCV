"""O filtro mediana é do tipo não linear e apresenta bons resultados no tratamento de ruído do
tipo sal e pimenta

É um tipo de técnica de tratamento de imagem capaz de suavizar preservando bordas e contornos da imagem
"""

import cv2 as cv
from cv2 import medianBlur
from matplotlib import pyplot as plt

img = cv.imread("head.png")
imgMedian = medianBlur(img, 5)

"""FUNÇÃO  medianBlur(img, intensidade)
Entrada: 
img = Imagem com a qual queremos trabalhar
suavização = Grau de suavização"""

# Vizualizando a imagem sem filtro
fig = plt.figure(figsize=(20, 50))
ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem com ruido")

# Vizualizando a imagem com filtro
ax2 = fig.add_subplot(122)
plt.imshow(imgMedian)
plt.title("Imagem com filtro")
plt.show()
