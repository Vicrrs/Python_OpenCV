# Segmentação por Binarização

"""
A segmentação por biarização também é conhecida como aplicação de limiar de intensidade. A separação do objeto de
interesse por meio desse método ocorre pela definição do valor de um limiar.

Quando uma imagem é submetida a esse procedimento, os pixels representados por valores maiores que o limiar são estabel
ecidos como o objeto de interesse, sendo redefinidos para cor preta ou branca. Do contrário, os pixels representados por
valores menores que o limiar são estabelecidos como o segundo plano, sendo reefinidos para a cor oposta à do objeto de
interesse.

A segmentação por binarização resulta em uma imagem binária, na qual geralmente o objeto de interesse é representado
pela cor branca e o segundo plano pela cor preta

Limiar - Pixels representados por valores maiores que o limiar são estabelecidos como objetos de interesse (brancos ou
pretos)
Função: threshold(img, limiar, val_int, método)
Entrada: img - imagem com a qual queremos trabalhar em tons de cinza
limiar - valor estiplado pelo usuário
val_int - valor de interesse dos pixels com valores maiores que o limiar

método: THRESH_BINARY - Objeto de interesse com a cor preta
        TRESH_BINARY_INV - Objeto de interesse em cor branca

Saída: Matriz referente a binarização

"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('005_cafe.jpg')

metodo = cv.THRESH_BINARY_INV
metodo1 = cv.THRESH_BINARY
ret, imBin = cv.threshold(img, 200, 255, metodo)

fig = plt.figure(figsize=(15, 15))

ax1 = fig.add_subplot(221)
plt.imshow(img)
plt.title("Imagem original")

ax2 = fig.add_subplot(222)
plt.imshow(imBin)
plt.title("Imagem Segmentada")

plt.show()
