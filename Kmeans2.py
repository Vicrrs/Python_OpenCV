import numpy as np
import cv2 as cv

img = cv.imread("004_home.jpg")
Z = img.reshape((-1, 3))

# converter para np.float32
Z = np.float32(Z)

# define critérios, número de clusters(K) e aplica kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

# Agora convertendo de volta para uint8 e faça a imagem original
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape(img.shape)

cv.imshow('res2', res2)
cv.waitKey(0)
cv.destroyAllWindows()