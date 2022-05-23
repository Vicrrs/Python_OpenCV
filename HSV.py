"""
Espaço de cor HSV
  •Um dos modelos principais e mais utilizados para representação de cor.
  •Permite um grande grau de separação entre a cor e a iluminação.
  •São os canais para representar a matiz (hue),asaturação (saturation)eovalor (value).
  •O componente Value é desagregado de cor, enquanto o Hue e o Saturation estão intimamente relacionados
  à percepção humana de cores.

"""
# Conversão das cores de RGB para HSV
import numpy as np
import cv2

# Passar padrão RGB
azul = np.uint8([[[255, 0, 0]]])
hsv_azul = cv2.cvtColor(azul, cv2.COLOR_BGR2HSV)

verde = np.uint8([[[0, 255, 0]]])
hsv_verde = cv2.cvtColor(verde, cv2.COLOR_BGR2HSV)

vermelho = np.uint8([[[0, 0, 255]]])
hsv_vermelho = cv2.cvtColor(vermelho, cv2.COLOR_BGR2HSV)

print(f"A cor azul no espaço HSV possuiovalor {hsv_azul}")
print(f"A cor verde no espaço HSV possuiovalor {hsv_verde}")
print(f"A cor vermelho no espaço HSV possuiovalor {hsv_vermelho}")

"""
Limites superioreseinferiores
  •limite inferior: [H-20, 100,100]
  •limite superior: [H+20, 255, 255]
  •ferramenta de edição de imagem comooGIMP ou qualquer conversor online
"""

