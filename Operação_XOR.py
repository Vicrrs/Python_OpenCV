"""Operação XOR bit a bit na imagem:
Operação OR exclusiva bit a bit em elementos da matriz de entrada.


Sintaxe: cv2.bitwise_xor(source1, source2, destination, mask)
Parâmetros:
source1: Matriz de imagem de primeira entrada (canal único, 8 bits ou ponto flutuante)
source2: matriz de imagem de segunda entrada (canal único, 8 bits ou ponto flutuante)
dest: Matriz de saída (semelhante às dimensões e tipo de matriz de imagem de entrada)
máscara: Máscara de operação, máscara de canal único de entrada/saída de 8 bits """

# Programa Python para ilustrar
# operação aritmética de
# XOR bit a bit de duas imagens

# Python program to illustrate
# arithmetic operation of
# bitwise XOR of two images

# organizando importações
import cv2
import numpy as np

# caminho para as imagens de entrada são especificados e
# imagens são carregadas com o comando imread
img1 = cv2.imread('E1.png')
img2 = cv2.imread('E2.png')

# cv2.bitwise_xor é aplicado sobre o
# entradas de imagem com parâmetros aplicados
dest_xor = cv2.bitwise_xor(img1, img2, mask=None)

# a janela mostrando a imagem de saída
# com a operação Bitwise XOR
# nas imagens de entrada
cv2.imshow('Bitwise XOR', dest_xor)

# Desalocar qualquer uso de memória associado
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
