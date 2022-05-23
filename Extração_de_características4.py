#Detecção de cantos

"""
Função cv.cornerHarris(img, blockSize, ksize, k)

Entrada:
img = imagem de entrada em tons de cinza
blockSize = Tamanho dos pixels vizinhos considerados como cantos para detecção
ksize = Parâmetro de abertura do derivado de Sobel usado
k = Parâmetro livre do detector Harris

Saída = Pontos de detecção de canto da imagem
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("012_hospital2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.01)
element_estr = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.dilate(dst, element_estr)

img[dst > 0.05*dst.max()] = [0, 0, 255]
fig = plt.figure(figsize=(10, 8))
plt.imshow(img)
plt.show()
