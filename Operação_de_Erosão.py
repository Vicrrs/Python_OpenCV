# Operação de Erosão
"""
A operação de erosão pode ser comparada com a ideia de corrosão das arestas de interesse resultando em uma imagem
'encolhida' do objeto.

O algoritmo da operação de erosão sobrepoe cada pixel da imagem de entrada com o centro do elemento estruturante. Se
todos os pontos do elemento estruturante coincidirem com os pontos do objeto de interesse, então, esse ponto torna-se
parte do objeto na imagem de saída.
"""

# Importando as Bibliotecas
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Carregando a imagem inicial
img = cv.imread("002_placa.PNG")

# Elemento Estruturante
"""
O elemento estruturante pode ser encarado como uma imagem binária, menor que a imagem original, armazenando geralmene em
uma matriz quadrada

O elemento estruturante é a base para que qualquer operacao morfologica seja executada
"""
element_estr = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
print(element_estr)
"""
Funcao de entrada erode(img, elem_estr, interc):
Entrada:
    1. img= Imagem com a qual podemos trabalhar
    2. elem_estr = Elemento estruturante
    3. Interc = interalçao desejada
Saída:
    1. Matriz referente a imagem sofrida com a erosão
"""
img_process = cv.erode(img, element_estr, iterations=2)

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(211)
plt.imshow(img)

ax2 = fig.add_subplot(212)
plt.imshow(img_process)

plt.show()
