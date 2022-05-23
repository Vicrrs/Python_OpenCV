# Conexão com a WebCam

import cv2 as cv

# captura do vídeo, 0 = Webcam
cap = cv.VideoCapture(0)

# Largura e altura

larg = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
alt = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Laço para mostrar a imagem e fechar a aba
while True:
    ret, frame = cap.read()
    cv.imshow('FRAME', frame)

    if cv.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()
cv.destroyAllWindows()
