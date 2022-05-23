# Good corners

"""
Função: cv.goodFeaturesToTracking(img, n, qual, k)
Entrada:
img = imagem de entrada em tons de cinza
n = número de cantos que deseja-se encontrar
qual = nível de qualidade (valor entre 0 e 1)
k = distância euclidiana mínima entre os cantos detectados

Saída = Pontos de detecção de canto da imagem
"""


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('012_hospital2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, 255, -1)

plt.imshow(img)
plt.show()
