# Cores
"""
- As caracteristicas de aspectos de um objeto de interesse define informações sobre a sua cor. As informações extraidas pela
cor é uma da características mais importantes.
- Uma das forma de extração de caracteristicas pela cor seria atravės do médiaeodesvio padrão da mesma.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("009_tampa_azul.jpg", 1)
img_gray = cv2.imread("009_tampa_azul.jpg", 0)

cv2.imshow("Imagem em RGB", img)
cv2.imshow("Imagem em tons de cinza", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
- Calculo da média e do desvio padrão das imagem em RGB e tons de cinza.

-A função mean retorna a média de todos os canais RGB começando pelo azul, depois o verde e por último o vermelho.O
quarto parametro é o valor do alpha da imagem, pode-se dizer que seria a transparencia da imagem.

-A função meanStdDev calcula a média e o desvio padrão da imagem de forma independente para cada canal e os retorna
através dos parametros de saida.

-Assim, os valores mean e stdev são valores escalares para imagens coloridas que dividem a imagem em canais e
calculam e a plicam um limite para cada canal de forma independente.

-Para essa programaçãoéusado tambémafunção flatten. Essa função retorma uma cópia da matriz em uma dimensão
(1D).
"""
valorMedio = cv2.mean(img)
valorMedioGray =cv2.meanStdDev(img_gray)

(mean, std) = cv2.meanStdDev(img)
(means, stds) = cv2.meanStdDev(img_gray)

RGB = np.concatenate([(mean, std)]).flatten
Gray = np.concatenate([(mean, std)]).flatten

print("Valores da média e o desvio padrão RGB")
print(valorMedio)
print(RGB)


print("Valores da media e desvio padrão de Tons de Cinza")
print(valorMedioGray)
print(Gray)
