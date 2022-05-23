import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:

    # Captação/Leitura dos frames
    ret, frame = cap.read()
    # conversão
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # Detectar Azul claro
    lim_inf = np.array([100, 100, 100])
    # Detectar azul escuro
    lim_sup = np.array([140, 255, 255])
    # Verificar se o frame esta dentro do limite
    color_mask = cv.inRange(hsv, lim_inf, lim_sup)

    # bbox para representar a cor seguimentada
    (couts, hir) = cv.findContours(color_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for cout in couts:
        area = cv.contourArea(cout)

        if area > 800:
            x, y, w, h = cv.boundingRect(cout)
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # filtro
    cv.imshow("Mascara", color_mask)
    # bbox no vídeo original
    cv.imshow("ObjectDetctionTrack", frame)

    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()
cap.read()
