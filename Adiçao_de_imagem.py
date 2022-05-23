"""Podemos adicionar duas imagens usando a função cv2.add() . Isso adiciona diretamente pixels de imagem
nas duas imagens.

Sintaxe: cv2.add(img1, img2)

Mas adicionar os pixels não é uma situação ideal. Então, usamos cv2.addweighted(). Lembre-se, ambas as imagens
 devem ter o mesmo tamanho e profundidade.


Sintaxe : cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
Parâmetros :
img1 : Matriz da primeira imagem de entrada (canal único, 8 bits ou ponto flutuante)
wt1 : Peso dos primeiros elementos da imagem de entrada a serem aplicados a imagem final
img2 : Matriz da segunda imagem de entrada (canal único, 8 bits ou ponto flutuante)
wt2 : Peso dos elementos da segunda imagem de entrada a serem aplicados à imagem final
gammaValue : Medição da luz

"""

# Programa Python para ilustrar
# operação aritmética de
# adição de duas imagens

# organizando importações

import cv2

# caminho para as imagens de entrada são especificados e
# imagens são carregadas com o comando imread
imagem1 = cv2.imread('wallpapersden.jpg')
imagem2 = cv2.imread('thumb-1920-973877.jpg')

# cv2.addWeighted é aplicado sobre as
# entradas de imagem com parâmetros aplicados
soma = cv2.addWeighted(imagem1, 0.5, imagem2, 0.4, 0)

# a janela mostrando a imagem de saída
# com a soma ponderada
cv2.imshow("Imagem ponderada", soma)

# Desalocar qualquer uso de memória associado
if cv2.waitKey(0) & 0xff == 27:
     cv2.destroyAllWindows()