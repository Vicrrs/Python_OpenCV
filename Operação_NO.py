"""
Operação NÃO bit a bit na imagem:
Inversão de elementos da matriz de entrada.


Sintaxe: cv2.bitwise_not(source, destination, mask)
Parâmetros:
source: Matriz de imagem de entrada (canal único, 8 bits ou ponto flutuante)
dest: Matriz de saída (semelhante às dimensões e tipo de matriz de imagem de entrada)
máscara: Máscara de operação, máscara de canal único de 8 bits de entrada/saída
"""
# Programa Python para ilustrar
# operação aritmética de
# bit a bit NÃO na imagem de entrada

# organizando importações
import cv2
import numpy as np

# caminho para as imagens de entrada são especificados e
# imagens são carregadas com o comando imread
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')

# cv2.bitwise_not é aplicado sobre o
# entrada de imagem com parâmetros aplicados
dest_not1 = cv2.bitwise_not(img1, mask=None)
dest_not2 = cv2.bitwise_not(img2, mask=None)

# as janelas mostrando a imagem de saída
# com a operação Bitwise NOT
# na 1ª e 2ª imagem de entrada
cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)

# Desalocar qualquer uso de memória associado
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
