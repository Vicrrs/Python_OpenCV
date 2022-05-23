"""
Detector de Bordas - Laplaciano -Arestas

Operador Laplaciano se trata de um operados sensível a ruídos por isso é comum usar Filtros passa baixas na imagem
antes de utilizalos

1. segunda derivada pode ser usada para detectar arestas . Como as imagens são "*2D*", precisaríamos obter a derivada
em ambas as dimensões. Aqui, o operador Laplaciano é útil.

2.  operador Laplaciano é implementado no OpenCV pela função Laplacian() . De fato, como o Laplaciano utiliza o gradiente
das imagens, ele chama internamente o operador Sobel para realizar sua computação.

3. O que este programa faz?
- Carrega uma imagem
- Remova o ruído aplicando um desfoque gaussiano e, em seguida, converta a imagem original em escala de cinza
- Aplica um operador Laplaciano à imagem em tons de cinza e armazena a imagem de saída
- Exibir o resultado em uma janela

Função Laplacian(img, var_arm)

Entrada:
Img = Imagem com a qual queremos trabalhar
var_am = Valor que representa o pixel

Saída = Matriz referente a imagem com o realce do filtro laplaciano
"""

import cv2 as cv
from matplotlib import pyplot as plt

# Carregando a imagem
img = cv.imread("007_predio.jpg")

# Aplicando o operadoLaplacian()
Lap = cv.Laplacian(img, cv.CV_8U)

# Gerando os Gráficos
fig = plt.figure(figsize=(20,50))

ax1 = fig.add_subplot(121)
plt.imshow(img)
plt.title("Imagem original")

ax2 = fig.add_subplot(122)
plt.imshow(Lap)
plt.title("Operador Laplaciano")
plt.show()