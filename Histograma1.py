"""O histograma de uma imagem é a distribuição da frequência dos níveis de cinza em relação ao número de
 amostras. Essa distribuição nos fornece informação sobre a qualidade da imagem, principalmente no que diz
 respeito a intensidade luminosa"""

"""Função Hist(img, num1,intervalo)
3 parametros
1. img - imagem que vamos trabalhar
2. num1 - numero de elementos distintos que podem ser representados
3. intervalo - intervalo entre os elementos"""

"""Função Ravel
Img = Matriz de entrada, no caso a imagem. Os elementos em um são lidos na ordem específicada e empacotados com matriz
1D
Saída: retorna uma matriz plana contínua (Matriz 1D com todos os elemntos da matriz de entrada e com o mesmo tipo que
ela)"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def mostra_imagem():
    local_img = "Cinza.jpg"  # caminho da imagem
    img = cv.imread(local_img)
    cv.imshow("Janela", img)  # cria janela
    k = cv.waitKey(0)  # mostra jamela criada e aguarda evento de uma tecla
    if k == ord("s"):  # se s for pressionado salva a imagem
        cv.imwrite('Cinza.jpg', img)
    cv.destroyAllWindows()


def histograma():
    local_img = "Cinza.jpg"  # caminho da imagem
    img = cv.imread(local_img)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


mostra_imagem()
histograma()