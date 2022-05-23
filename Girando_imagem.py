"""
Processamento de imagens em Python (escalonamento, rotação, deslocamento e detecção de bordas)

As imagens podem ser giradas em qualquer grau no sentido horário ou não. Só precisamos definir a matriz de rotação
listando o ponto de rotação, o grau de rotação e o fator de escala.
"""

import cv2
import numpy as np

FILE_NAME = 'chowchow.jpg'
try:
    # Lê a imagem do disco.
    img = cv2.imread(FILE_NAME)

    # Forma da imagem em termos de pixels.
    (rows, cols) = img.shape[:2]

    # getRotationMatrix2D cria uma matriz necessária para transformação.
    # Queremos matriz para rotação w.r.t center a 45 graus sem escala.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(img, M, (cols, rows))

    # Grava a imagem de volta no disco.
    cv2.imwrite('result.jpg', res)
except IOError:
    print('Error while reading files !!!')