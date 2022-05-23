""" Average para encontrar  a cor média das imagens em Python"""

import cv2
import numpy as np

#  imread() função para ler a imagem e armazená-la em uma matriz.
src_img = cv2.imread('003_RGB.jpg')
# average()função de NumPy para encontrar a média da matriz da imagem
average_color_row = np.average(src_img, axis=0)
average_color = np.average(average_color_row, axis=0)
print(average_color)

# cria uma imagem preta usando a ones() função do NumPy
d_img = np.ones((312, 312, 3), dtype=np.uint8)
d_img[:, :] = average_color

"""O valor do tripleto RGB é salvo na average_colorvariável e também é mostrado junto com a imagem de origem. 
O primeiro argumento na average()função é a imagem de origem."""

cv2.imshow('Source image', src_img)
cv2.imshow('Average Color', d_img)
cv2.waitKey(0)
