import cv2
import os

path = os.getcwd()

# Verificando seapasta com Haarcascades existe
if os.path.isdir('Haarcascades') == False:
    print('Apasta Haarcascades não se encontra.')
else:
    print('Apasta Haarcascades existe.')
# Lendooxml
cascade = cv2.CascadeClassifier(path + '')


def faceBlur(gray, frame):
    faces = cascade.detectMultiscale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        roi_frame = frame[y:y + h, x:x + w]
        blur = cv2.GaussianBlur(roi_frame, (101, 101), 0)
        frame[y:y + h, x:x + w] = blur
    return frame


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = faceBlur(gray, frame)
    cv2.imshow('Video', blur)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destryAllWindows
