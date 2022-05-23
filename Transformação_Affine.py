"""
Na transformação Affine, todas as linhas paralelas na imagem original ainda serão paralelas na imagem de saída.
Para encontrar a matriz de transformação, precisamos de três pontos da imagem de entrada e suas localizações
correspondentes na imagem de saída. Então cv2.getAffineTransform criará uma matriz 2×3 que será passada
para cv2.warpAffine.

-> cv2.getAffineTransform método:

Sintaxe: cv2.getPerspectiveTransform(src, dst)

Parâmetros:
src: Coordenadas dos vértices do quadrilátero na imagem de origem.
dst: Coordenadas dos vértices do quadrilátero correspondentes na imagem de destino

-> método cv2.warpAffine:

Sintaxe: cv2.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)

Parâmetros:

src: imagem de entrada.

dst: imagem de saída que tem o tamanho dsize e o mesmo tipo que src.

M: matriz de transformação.

dsize: tamanho da imagem de saída.

flags: combinação de métodos de interpolação (veja resize() ) e o flag opcional

WARP_INVERSE_MAP que significa que M é a transformação inversa (dst->src).

borderMode: método de extrapolação de pixels; quando borderMode=BORDER_TRANSPARENT, significa que os pixels na imagem
de destino correspondentes aos “outliers” na imagem de origem não são modificados pela função.

borderValue: valor utilizado no caso de borda constante; por padrão, é 0.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('003_RGB.jpgdf')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')

plt.show()

# Displaying the image
while (1):

    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()