"""
A desfocagem da imagem refere-se a tornar a imagem menos clara ou distinta. Isso é feito com a ajuda de vários kernels
de filtro passa-baixa.

Vantagens do desfoque:

Ele ajuda na remoção de ruído. Como o ruído é considerado como sinal passa-alta, pela aplicação do kernel do filtro
passa-baixa, restringimos o ruído.
Ajuda a suavizar a imagem.
As bordas de baixa intensidade são removidas.
Ajuda a esconder os detalhes quando necessário. Por exemplo, em muitos casos a polícia deliberadamente quer esconder o
rosto da vítima, em tais casos é necessário desfocar.
Tipos importantes de desfoque:

Desfoque gaussiano: O desfoque gaussiano é o resultado do desfoque de uma imagem por uma função gaussiana. É um efeito
amplamente utilizado em software gráfico, normalmente para reduzir o ruído da imagem e reduzir os detalhes. Ele também
é usado como um estágio de pré-processamento antes de aplicar nossos modelos de aprendizado de máquina ou aprendizado
profundo.
Por exemplo, de um kernel gaussiano (3×3)

        [1 2 1]
1/6     [2 4 2]
        [1 2 1]

Desfoque Mediano: O Filtro Mediano é uma técnica de filtragem digital não linear, frequentemente usada para remover
ruído de uma imagem ou sinal. A filtragem de mediana é muito utilizada no processamento digital de imagens porque, sob
certas condições, preserva as bordas enquanto remove o ruído. É um dos melhores algoritmos para remover o ruído de sal
e pimenta.
Desfoque bilateral: Um filtro bilateral é um filtro de suavização não linear, com preservação de bordas e redução de
ruído para imagens. Ele substitui a intensidade de cada pixel por uma média ponderada dos valores de intensidade dos
pixels próximos. Este peso pode ser baseado em uma distribuição gaussiana. Assim, as arestas vivas são preservadas ao
descartar as fracas.
"""

# importing libraries
import cv2
import numpy as np

image = cv2.imread('001_fruits.jpg')

# cv2.imshow('Original Image', image)
# cv2.waitKey(0)

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 100)
# cv2.imshow('Gaussian Blurring', Gaussian)
# cv2.waitKey(0)
cv2.imwrite("001_Gaussian.jpg", Gaussian)

# Median Blur
median = cv2.medianBlur(image, 101, 21)
# cv2.imshow('Median Blurring', median)
# cv2.waitKey(0)
cv2.imwrite("001_median.jpg", median)

# Bilateral Blur
bilateral = cv2.bilateralFilter(image, 9, 100, 750)
# cv2.imshow('Bilateral Blurring', bilateral)
# cv2.waitKey(0)
cv2.imwrite("001_bilateral.jpg", bilateral)

# cv2.destroyAllWindows()