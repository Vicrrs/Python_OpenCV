# Programa Python para explicar o método cv2.imread()
# importando cv2

import cv2

# path -> caminho

path = r'getter.jpeg'

# Usando o método cv2.imread()
# Usando 0 para ler a imagem no modo de tons de cinza
img = cv2.imread(path, 0)

# Exibindo a imagem
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
