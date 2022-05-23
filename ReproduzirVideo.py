import time

import cv2 as cv
import time as tm

cap = cv.VideoCapture("teste.mp4")

# isOpened = Retorna verdadeiro se a captura de vídeo já foi inicializada
if cap.isOpened() == False:
    print("Erro!")

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        time.sleep(1/20)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('p'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()
