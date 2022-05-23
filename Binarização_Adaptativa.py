"""
Calcula diferentes valores de limiar para cada região da imagem.
Obter o melhor resltado considerando o contraste

Esse método é usado quando a imagem não possui iluminação adequada para o procedimento de binarização. A binarização ada-
ptativa calcula diferentes valores de limiar para cada região da imagem, logo, cada região é tratada a fim de obter o me-
lhor resultado considerando o seu contraste
FUNÇÃO: adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize,C)
Entrada:
src = Matriz referente a image
maxValue = Valor de intensidade máxima do pixel
adaptiveMethod = ADAPTATIVE_THRESH_MEAN_C
                ADAPTATIVE_THRESH_GAUSSIAN_C
thresholdType = THRESH_BINARY - Objeto de interesse com a cor preta
            TRESH_BINARY_INV - Objeto de interesse em cor branca

blockSize = Tamanho da máscara
C = Constante de subtração da média ou da média ponderada

Saída = MAtriz referente a imagem binarizada adaptada
"""

import cv2 as cv
import numpy as np

# Filtros de suavização
img = cv.imread('006_olho.PNG', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("Imagem Original", img)
cv.imshow("Binaria", th1)
cv.imshow("Media", th2)
cv.imshow("Gaussiana", th3)

cv.waitKey(0)
cv.destroyAllWindows()
