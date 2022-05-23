"""Assim como a adição, podemos subtrair os valores de pixel em duas imagens e mesclá-los com a ajuda de cv2.subtract().
 As imagens devem ter o mesmo tamanho e profundidade.

Sintaxe: cv2.subtract(src1, src2)"""
# Programa Python para ilustrar
# operação aritmética de
# subtração de pixels de duas imagens

# organizando importações
import cv2

# caminho para as imagens de entrada são especificados e
# imagens são carregadas com o comando imread
imagem1 = cv2.imread('thumb-1920-973877.jpg')
imagem2 = cv2.imread('wallpapersden.jpg')

# cv2.subtract é aplicado sobre o
# entradas de imagem com parâmetros aplicados
sub = cv2.subtract(imagem1, imagem2)

# a janela mostrando a imagem de saída
# com a imagem subtraída
cv2.imshow('Imagem Subtraída', sub)

# Desalocar qualquer uso de memória associado
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
