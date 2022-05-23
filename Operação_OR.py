"""Operação OR bit a bit na imagem:
Disjunção bit a bit dos elementos da matriz de entrada.


Sintaxe: cv2.bitwise_or(source1, source2, destination, mask)
Parâmetros:
source1: Matriz de imagem de primeira entrada (canal único, 8 bits ou ponto flutuante)
source2: matriz de imagem de segunda entrada (canal único, 8 bits ou ponto flutuante)
dest: Matriz de saída (semelhante às dimensões e tipo de matriz de imagem de entrada)
máscara: Máscara de operação, máscara de canal único de entrada/saída de 8 bits """

# Programa Python para ilustrar
# operação aritmética de
# OR bit a bit de duas imagens

# organizando importações
import cv2
import numpy as np

# caminho para as imagens de entrada são especificados e
# imagens são carregadas com o comando imread
img1 = cv2.imread('E1.png')
img2 = cv2.imread('E2.png')

# cv2.bitwise_or é aplicado sobre o
# entradas de imagem com parâmetros aplicados
dest_or = cv2.bitwise_or(img2, img1, mask=None)

# a janela mostrando a imagem de saída
# com a operação OR bit a bit
# nas imagens de entrada
cv2.imshow('Bitwise OR', dest_or)

# Desalocar qualquer uso de memória associado
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
