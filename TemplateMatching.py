"""
ACorrespondência de modelos,ou mais conhecido como template matching,éum método procurarelocalizaro "local" de
uma imagem de modelo em uma imagem maior.O OpenCV vem comafunção cv2.matchTemplate() para essa finalidade.
Ele simplesmente deslizaaimagem do modelo sobreaimagem de entrada(como na convolução 2D)e compara o modelo e o
patch da imagem de entrada sobaimagem do modelo.Vários métodos de comparação são implementados no OpenCV.O
retorno da funçãoéuma imagem em escala de cinza,em que cada pixel indicaoquantoavizinhança desse pixel corresponde
ao modelo.
Se a imagem de entrada for do tamanho(WxH)e a imagem do modelo for do tamanho(wxh),a imagem de saída terá o
tamanho(W-w+1,H-h+1).Depois de obter o resultado,você pode usar a função cv2.minMaxLoc() para descobrir onde
está o valor máximo/mínimo.Tome-o como o canto superior esquerdo do retângulo e interprete(w,h) como largura e
altura do retângulo. Esse retângulo é sua região de modelo.
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('003_Lenna.png', 0)
img2 = img.copy()
template = cv.imread('013_rosto_template.JPG', 0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img, top_left, bottom_right, 255, 2)
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
