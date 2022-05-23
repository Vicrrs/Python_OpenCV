#Dimensionais

"""
FUNÇÃO -> detectMultiscale(scalefactor, minNeighbors)

Entrada:
scalefactor = Parâmetro que especifica qunato o tamanho da imagem  é reduzido  em cada escala de imagem.
minNeighbors = Parâmetro que específica quantos vizinhos cada retângulo candidato deve ter para retê-lo.

Saída = retângulo com coordenadas(x, y, w, h) ao redor da face detectada
"""
import cv2

face_cascade = cv2.CascadeClassifier('001_Classificador_Faces')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w), (y+w), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('Face Detectada', img)

    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
