" HISTOGRAMA DE IMAGENS COLORIDAS "

# Importando as bibliotecas

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


# Leitura da imagem e segmentação dos canais da imagem (RGB)


def mostra_imagem():
    local_img = "001_fruits.jpg"  # caminho da imagem
    img = cv.imread(local_img)
    cv.imshow("Janela", img)  # cria janela
    k = cv.waitKey(0)  # mostra jamela criada e aguarda evento de uma tecla
    if k == ord("s"):  # se s for pressionado salva a imagem
        cv.imwrite('003_RGB.jpg.jpg', img)
    cv.destroyAllWindows()


def histograma():
    local_img = "001_fruits.jpg"  # caminho da imagem
    img = cv.imread(local_img)
    azul, verde, vermelho = cv.split(img)
    fig = plt.figure(figsize=(20, 5))
    # uma linha, 3 colunas, referente a primeira imagem
    ax1 = fig.add_subplot(131)
    ax1.hist(azul.ravel(), 256, [0, 256])
    plt.title("Histograma com canal azul")
    ########################################
    ax2 = fig.add_subplot(132)
    ax2.hist(verde.ravel(), 256, [0, 256])
    plt.title("Histograma com canal verde")
    ########################################
    ax3 = fig.add_subplot(133)
    ax3.hist(vermelho.ravel(), 256, [0, 256])
    plt.title("Histograma com canal vermelho")
    plt.show()


histograma()
mostra_imagem()