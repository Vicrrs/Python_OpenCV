"""
Detecção de borda em uma imagem: -
O processo de detecção de imagem envolve a detecção de bordas nítidas na imagem. Essa detecção de borda é essencial
no contexto de reconhecimento de imagem ou localização/detecção de objetos . Existem vários algoritmos para detecção
de bordas devido a sua ampla aplicabilidade. Usaremos um algoritmo conhecido como Canny Edge Detection .
"""

import cv2
import numpy as np

FILE_NAME = 'bola.jpg'
try:
	# Lê a imagem do disco.
	img = cv2.imread(FILE_NAME)

	# Detecção de borda inteligente.
	edges = cv2.Canny(img, 100, 200)

	# Grava a imagem de volta no disco.
	cv2.imwrite('result.jpg', edges)
except IOError:
	print ('Error while reading files !!!')