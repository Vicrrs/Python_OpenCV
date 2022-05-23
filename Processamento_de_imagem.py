"""
(escalonamento, rotação, deslocamento e detecção de bordas)

Dimensionando uma imagem :-

A operação de dimensionamento aumenta/reduz o tamanho de uma imagem.
"""
import cv2
import numpy as np

FILE_NAME = 'chowchow.jpg'
try:
    # Lê a imagem do disco.
    img = cv2.imread(FILE_NAME)

    # Obtém o número de pixels horizontalmente e verticalmente.
    (height, width) = img.shape[:2]

    # Especifique o tamanho da imagem junto com os métodos de interploação.
    # cv2.INTER_AREA é usado para encolher, enquanto cv2.INTER_CUBIC
    # é usado para zoom.
    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    # Grava a imagem de volta no disco.
    cv2.imwrite('result.jpg', res)

except IOError:
    print('Error while reading files !!!')
