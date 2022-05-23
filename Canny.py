"""
Detector de Bordas - Canny

Função: Canny(img, int_detc1, int_detc2)
Entrada:
img = imagem com a qual queremos trabalhar em tons de cinza
int_detc1 = intensidade de detecção 1
int_detc2 = intensidade de detecção 2

Saída = Matriz referente a imagem com o realce por Canny

o algoritmo Canny visa satisfazer três critérios principais:

1. Baixa taxa de erro: significa uma boa detecção de apenas arestas existentes.
2. Boa localização: A distância entre os pixels de borda detectados e os pixels de borda reais devem ser minimizados.
3. Resposta mínima: Apenas uma resposta do detector por borda.

A supressão não máxima é aplicada. Isso remove pixels que não são considerados parte de uma aresta. Assim, apenas
linhas finas (bordas candidatas) permanecerão.

Histerese : O passo final. Canny usa dois limites (superior e inferior):

Se um gradiente de pixel for maior que o limite superior , o pixel será aceito como uma borda

Se um valor de gradiente de pixel estiver abaixo do limite inferior , ele será rejeitado.

Se o gradiente de pixel estiver entre os dois limites, ele será aceito somente se estiver conectado a um pixel que esteja
acima do limite superior .

Canny recomendou uma proporção superior : inferior entre 2:1 e 3:1.

Para mais detalhes, você sempre pode consultar seu livro de Visão Computacional favorito.
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('007_predio.jpg')

canny = cv.Canny(img, 75, 50)

fig = plt.figure(figsize=(20, 50))

ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)
plt.title("Imagem original")

ax2 = fig.add_subplot(122)
plt.imshow(canny, cmap=plt.cm.gray)
plt.title("Operador Canny")
plt.show()
