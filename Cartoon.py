import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Imagem original

img = cv.imread("005_fone.jpg")

plt.figure(figsize=(10, 8))
plt.imshow(img)
plt.show()

# desfoque da imagem usando a funcao edgePreservingFilter

ePI = cv.edgePreservingFilter(img, flags=2, sigma_s=50, sigma_r=0.4)

plt.figure(figsize=(10, 8))
plt.imshow(ePI)
plt.show()

# Filtro Stylization

cartoon = cv.stylization(img, sigma_s=150, sigma_r=0.5)

plt.figure(figsize=(10, 8))
plt.imshow(cartoon)
plt.show()
