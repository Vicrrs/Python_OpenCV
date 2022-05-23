"""
Detector de bordas - sobel - bordas

Sobel realça  arestas verticais e horizontais, se trata de um operados sensível a ruídos
por isso é comum usar Filtros passa baixas na imagem antes de utilizalos

*Filtro espacial nao linear usado para realçar bordas verticais e horizontais

Função: sobel(img, var_arm, h,v, mascara)
Entrada -> Img = imagem com a qual queremos trabalhar
var_arm = valor que representa o pixel
h = realce horizotal
v = realce vertical
mascara = dimensao da mascara que sera aplicada

Saída = matriz referente a imagem com o realce do filtro Sobel

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- Uma boa maneira de expressar as mudanças de um pixel é usando derivadas
- Uma alta mudança no gradiente indica uma grande mudança na imagem
- Podemos deduzir que um método para detectar bordas em uma imagem pode ser realizada localizando locais
de pixel onde o gradiente é maior que seus vizinhos
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

O operador de Sobel realiza uma operação para realçar contornos em imagens. Esse tipo de filtro é nao linear
e realça linhas verticais e horizontais maus escuras que o fundo, sem realçar pontos isolados.

Além dessas características, o detector de sobel possibilita realçar as arestas independente da direção: a
filtragem pode ser realizada tanto na vertical quanto na horizontal.

As regiões destacadas por esse procedimento resultam em bordas mais 'grossas' comparadas com as outras técnicas

1.  Operador de Sobel é um operador de diferenciação discreta. Ele calcula uma aproximação do gradiente de uma
função de intensidade da imagem.

2. O Operador de Sobel combina suavização e diferenciação gaussianas.

* O que este programa faz?
3. Aplica o Operador Sobel e gera como saída uma imagem com as bordas detectadas brilhantes em um fundo mais escuro.
4. O código do tutorial é mostrado nas linhas abaixo.

@breve exemplo de código usando as funções Sobel e/ou Scharr OpenCV para fazer um detector de borda simples
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("007_predio.jpg")

sobely = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=7)
sobelx = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=7)

fig = plt.figure(figsize=(20, 50))

ax1 = fig.add_subplot(131)
plt.title("Imagem original")
plt.imshow(img)

ax2 = fig.add_subplot(132)
plt.title("Eixo-y")
plt.imshow(sobely)

ax3 = fig.add_subplot(133)
plt.title("Eixo-x")
plt.imshow(sobelx)

plt.show()
