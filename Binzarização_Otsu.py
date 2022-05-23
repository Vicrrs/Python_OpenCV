# Binarização por OTSU
"""
Foi abordado na binarização por limiar e adaptativa um valor no qual cada pixel da imagem é comparado e depois
segmentado de acordo com essa comparação. Mas um grande incoveniente desses métodos é que o usuário precisa passar esse
valor de limiar para ser feito a segmentação da imagem

Uma forma de automatizar esse procedimento é justamente o algoritmo de otsu, no qual define um limiar baseado no histogr
-ama da imagem.

Esse algoritmo pode ser usado junto à função threshold, necessitando apenas que a constante THRESH_OTSU seja tomada ao
tipo definido para binarizaçãp
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('005_cafe.jpg', 0)

# Definindo o método de binarização

metodo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
ret, imgBin = cv2.threshold(img, 0, 255, metodo)

print(f"O melhor limiar é: {ret}")

plt.hist(img.ravel(), 256, [0, 256])
cv2.imshow("Original", img)
plt.show()
cv2.imshow("Otsu", imgBin)

cv2.waitKey(0)
cv2.destroyAllWindows()
