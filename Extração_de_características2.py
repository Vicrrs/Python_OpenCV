#Dimensionais 
"""
Refere-se ao tamanho do objeto: Área, Perímetro

*Função findContours(img, modo, método)
Entrada: img = Imagem com a qual queremos trabalhar
modo = pontos extraídos da imagem serão armazenados (cv2.RETE_TREE)
método = pontos da imagem
binária(cv2.CHAIN_APPROX_NONE, cv2.CHAIN_APPROX_SIMPLE)
saída = dados da umagem que queremos calcular a área

*Função contourArea(Saida_findContours)
Entrada: Saida_findContours = Objetos segmentaada obtido pela funçõa
Saída Área do objeto estudado

*Função arcLength(Saida_findContours, contornos)
Entrada:Saida_findContours = Objeto segmentado obtido pela função find Contours

contornos=contorno que será obtido(TRUE=contorno fechado, FALSE=contorno fechado)
Saída=Área do objeto estudado.
"""
import cv2 as cv
import numpy as np

im = cv.imread("010_triangle.JPG")
tipo = cv.THRESH_BINARY_INV
_, imgBin = cv.threshold(im, 0, 255, tipo)
modo = cv.RETR_TREE
metodo = cv.CHAIN_APPROX_SIMPLE

contorno, hierarquia = cv.findContours(imgBin, modo, metodo)

if len(contorno) > 0:
    obj = contorno[0]
    area = cv.contourArea(obj)
    print(area)

    perimetro = cv.arcLength(obj, True)
    print(perimetro)
else:
    print("Sem contorno encontrado")
