"""As operações morfológicas são um conjunto de operações que processam imagens com base em formas. Eles aplicam um
elemento estruturante a uma imagem de entrada e geram uma imagem de saída.
As operações morfológicas mais básicas são duas: Erosão e Dilatação.


Corrói os limites do objeto em primeiro plano
Usado para diminuir os recursos de uma imagem.

Trabalho de erosão:

1. Um kernel (uma matriz de tamanho ímpar (3,5,7) é convoluído com a imagem.
2. Um pixel na imagem original (1 ou 0) será considerado 1 somente se todos os pixels sob o kernel forem 1, caso
contrário, ele é erodido (feito a zero).
3. Assim, todos os pixels próximos ao limite serão descartados dependendo do tamanho do kernel.
4. Assim, a espessura ou tamanho do objeto em primeiro plano diminui ou simplesmente a região branca diminui na imagem.
Noções básicas de dilatação:

Aumenta a área do objeto
Usado para acentuar recursos

Trabalho de dilatação:

1. Um kernel (uma matriz de tamanho ímpar (3,5,7) é convoluído com a imagem
2. Um elemento de pixel na imagem original é '1' se pelo menos um pixel sob o kernel for '1'.
3. Aumenta a região branca na imagem ou o tamanho do objeto em primeiro plano aumenta
"""

# Programa Python para demonstrar erosão e
# dilatação de imagens.
import cv2
import numpy as np

# Lendo a imagem de entrada
img = cv2.imread('naruto.jpg', 0)

# Tomando uma matriz de tamanho 5 como kernel
kernel = np.ones((5, 5), np.uint8)

# O primeiro parâmetro é a imagem original,
# kernel é a matriz com a qual a imagem é
# convoluído e o terceiro parâmetro é o número
# de iterações, que determinará o quanto
# você deseja erodir/dilatar uma determinada imagem.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)

"""Usos de erosão e dilatação: 

Erosão: 

É útil para remover pequenos ruídos brancos.
Usado para separar dois objetos conectados, etc.

Dilatação:

Em casos como a remoção de ruído, a erosão é seguida de dilatação. Porque a erosão remove ruídos brancos, mas também e
ncolhe nosso objeto. Então nós dilatamos. Desde que o ruído se foi, eles não voltarão, mas nossa área de objeto aumenta.
Também é útil para unir partes quebradas de um objeto."""
