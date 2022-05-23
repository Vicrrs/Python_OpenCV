#Subtração de background
#Captação de movimento
"""
• Separar o fundo do primeiro plano em fluxos de vídeo.
• Todos os métodos de subtração de fundo são moderados em precisão,bem como tempo computacional.

Funções:
• createBackground SubtractorMOG2(history,var Threshold,detectShadows)
• createBackground SubtractorKNN(history,dist2Threshold,detectShadows)

onde:
1. history= é o número de frame usados para construiromodelo estatístico do plano de fundo. Quanto 
menor forovalor,mais rápidas as alterações no plano de fundo serão consideradas pelo modeloe, portanto,
serão consideradas como plano de fundo.E vice versa.

2. dist2Threshold = Limiar na distância quadrada entreopixeleaamostra para decidir se um pixel está 
próximo dessa amostra.Este parâmetro não afeta a atualização em segundo plano.

3. varThreshold = Limiar na distância quadrada de Mahalanobis entreopixeleomodelo para decidir se um 
pixel está bem descrito pelo modelo de fundo. Este parâmetro não afetaaatualização em segundo plano.

4. detectShadows Se setado como True,as sombras serão apresentadas na imagem.

"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

mog = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=10, detectShadows=True)
knn = cv2.createBackgroundSubtractorKNN(history=100, dist2Threshold=40, detectShadows=True)

while (True):
    ret, frame = cap.read()

    fgmask1 = mog.apply(frame)
    fgmask2 = knn.apply(frame)

    cv2.imshow('MOG2', fgmask1)
    cv2.imshow('KNN', fgmask2)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows
