# Grabcut
"""
cv.grabCut(imagem, máscara, retângulo, backgroundModel, foregroundModel, iterationCount[modo])
Parâmetros:
imagem: imagem de entrada de 3 canais de 8 bits
máscara: máscara de canal único de entrada/saída de 8 bits. A máscara é inicializada pela função quando o modo é defini-
do como GC_INIT_WITH_RECT. Seus elementos podem ter um dos seguintes valores:
1. GC_BGD define pixels de fundos óbvios
2. GC_FGD define um pixel óbvio de primeiro plano (objeto)
3. GC_PR_BGD define um possível pixel de fundo
4. GC_PR_FGD define um possível pixel de primeiro plano

- retângulo: é a região de interesse que contém um objeto segmentado. Os pixels da ROI são marcados como plano de fundo. O
parâmetro é usado apenas quando mode == GC_INIT_WITH_RECT.

- backgroundModel: array temporário para o modelo de fundo

- foregroundModel: array temporário para o modelo do primeiro plano

- iterationCount: Número de iterações que o algoritmo deve fazer antes de retomar o resultado. Observe que o resultado
pode ser refinado com outras chamadas com mode == GC_INIT_WITH_MASK ou  mode == GC_EVAL

modo: define o modo de operação. Pode ser um dos seguintes

1. GC_INIT_WITH_RECT: A função inicializa o estado e a máscaara usando o retângulo fornecido. Depois disso, ele executa
iterações interCount de algoritmo.
2. GC_INIT_WITH_MASK: A função inicializa o estado usando a máscara fornecida. Observe que GC_INIT_WITH_RECT e GC_INIT_
WITH_MASK podem ser combinados. Então, todos os pixels fora da ROI são inicializados automaticamente com GC_BGD.
3. GC_EVAL: O valor significa que o algoritmo deve apenas retomar
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('003_Lenna.png')
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 450, 290)
cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]
plt.imshow(img), plt.colorbar(), plt.show()
