"""
Traduzindo uma Imagem:-
Traduzir uma imagem significa deslocá-la dentro de um determinado quadro de referência.
"""

import cv2
import numpy as np

FILE_NAME = 'volleyball.jpg'
# Criar matriz de tradução.
# Se o deslocamento for (x, y) então a matriz seria
# M = [1 0 x]
# 	  [0 1 y]
# Let's shift by (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])

try:

    # Lê a imagem do disco.
    img = cv2.imread('img1.jpg')
    (rows, cols) = img.shape[:2]

    # warpAffine faz o deslocamento apropriado dado o
    # matriz de tradução.
    res = cv2.warpAffine(img, M, (cols, rows))

    # Grava a imagem de volta no disco.
    cv2.imwrite('result.jpg', res)

except IOError:
    print('Error while reading files !!!')
