"""Operação AND bit a bit na imagem:
Conjunção bit a bit de elementos da matriz de entrada.


Sintaxe: cv2.bitwise_and(source1, source2, destination, mask)
Parâmetros:
source1: Matriz de imagem de primeira entrada (canal único, 8 bits ou ponto flutuante)
source2: matriz de imagem de segunda entrada (canal único, 8 bits ou ponto flutuante)
dest: Matriz de saída (semelhante às dimensões e tipo de matriz de imagem de entrada)
máscara: Máscara de operação, máscara de canal único de entrada/saída de 8 bits """

# Programa Python para ilustrar
# operação aritmética de
# bit a bit AND de duas imagens

#organizando importações
import cv2
import numpy as np

# caminho para as imagens de entrada são especificados e
# imagens são carregadas com o comando imread
img1 = cv2.imread('E1.png')
img2 = cv2.imread('E2.png')

# cv2.bitwise_and é aplicado sobre o
# entradas de imagem com parâmetros aplicados
dest_and = cv2.bitwise_and(img2, img1, mask=None)

# a janela mostrando a imagem de saída
# com a operação E bit a bit
# nas imagens de entrada
cv2.imshow('Bitwise And', dest_and)

# Desalocar qualquer uso de memória associado
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()