# Operação de Dilatação
"""
Dilatação -> O objeto ficará maior do que era inicialmente
-Sobrepor cada pixel da image, de entrada com o centro do elemento estruturante

FUNÇÃO: Dilate(img, elem_estr, interc)
Entrada:
img = Imagem com a qual queremos trabalhar
elem_estr = Elemento estruturante
interc = interações desejadas

Saída = Matriz referente  imagem sofrida com a dilatação
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("002_placa.PNG")

element_estr = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
print(element_estr)

img_process = cv.dilate(img, element_estr, iterations=2)

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(211)
plt.imshow(img)

ax2 = fig.add_subplot(212)
plt.imshow(img_process)

plt.show()