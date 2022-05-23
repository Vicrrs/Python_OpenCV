"""O redimensionamento de imagem refere-se ao dimensionamento de imagens. O dimensionamento é útil em muitos aplicativos
de processamento de imagem e aprendizado de máquina. Ajuda na redução do número de pixels de uma imagem e isso tem
várias vantagens, por exemplo, pode reduzir o tempo de treinamento de uma rede neural quanto mais é o número de pixels
em uma imagem mais é o número de nós de entrada que por sua vez aumenta o complexidade do modelo.
Também ajuda no zoom nas imagens. Muitas vezes precisamos redimensionar a imagem, ou seja, reduzi-la ou dimensioná-la
para atender aos requisitos de tamanho. O OpenCV nos fornece vários métodos de interpolação para redimensionar
uma imagem.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Escolha do Método de Interpolação para Redimensionamento -

cv2.INTER_AREA: Isso é usado quando precisamos reduzir uma imagem.
cv2.INTER_CUBIC: Isso é lento, mas mais eficiente.
cv2.INTER_LINEAR: Isso é usado principalmente quando o zoom é necessário.
Esta é a técnica de interpolação padrão no OpenCV.
Segue abaixo o código para redimensionamento.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("python.png", 1)
# Loading the image

half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1060, 675))
# a função cv2.resize() é que a tupla
# passada para determinar o tamanho da nova imagem

stretch_near = cv2.resize(image, (780, 540),
                          interpolation=cv2.INTER_NEAREST)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()
