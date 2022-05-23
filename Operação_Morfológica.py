# Operações Morfológicas - TOP HAT e BLACK HAT

"""
1. Gradiente Morfológico: A operação  chamada gradiente morfológico é a diferença entre a operação
de dilatação e erosão de uma imagem. O resultado é uma imagem que representa a borda do objeto de 
interesse. 

2. TOP HAT: A operação TOPHAT consiste na subtração da versão morfologicamente aberta de uma imagem 
com a versão original. Esse tipo de operação é aplicada a fim de realçar objetos brilhantes em fundos
escuros. Além dessa utilidade, ela também é aplicada com intuito de corrigir a variação de luminosi-
dade em imagens, possibilitando que objetos representados em regiões mais escuras sejam realçadas.

3. BLACK HAT - Essa operação consiste a subtração da imagem original por sua versão morfologicamente 
fechada.
"""

"""
FUNÇÃO: morphologyEx(img, oper, elem_estr)
Entrada:
img= Imagem com a qual queremos trabalhar
oper = Operação que será realizda
elem_estr = Elemento estruturante

Saída = Imagem nova 
"""

import cv2 as cv
import matplotlib.pyplot as plt



class Teste():
    def __init__(self, path=None):
        self.img1 = None
        if path is not None:
            self.img1 = cv.imread(path)

    def Imagens(self):
        fig = plt.figure(figsize=(15, 15))

        ax1 = fig.add_subplot(221)
        plt.imshow(self.img1)
        plt.title("Imagem original")

        plt.show()

    # Aplicando o elemento estruturante
    def Elemento_estruturante(self):
        self.elem_estr1 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
        print(self.elem_estr1)

    def Funcao_morfologica(self):
        imgProc1 = cv.morphologyEx(self.img1, cv.MORPH_GRADIENT, self.elem_estr1)
        imgProc2 = cv.morphologyEx(self.img1, cv.MORPH_TOPHAT, self.elem_estr1)
        imgProc3 = cv.morphologyEx(self.img1, cv.MORPH_BLACKHAT, self.elem_estr1)

        fig = plt.figure(figsize=(15, 15))

        ax1 = fig.add_subplot(131)
        plt.imshow(imgProc1)
        plt.title("Gradiente Morfológico")

        ax2 = fig.add_subplot(132)
        plt.imshow(imgProc2)
        plt.title("TOPHAT")

        ax3 = fig.add_subplot(133)
        plt.imshow(imgProc3)
        plt.title("BLACKHAT")

        plt.show()


teste = Teste("002_placa.PNG")
teste.Imagens()
teste.Elemento_estruturante()
teste.Funcao_morfologica()
