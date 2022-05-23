import cv2 as cv

cap = cv.VideoCapture(0)

larg = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
alt = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Parte Superior
x = larg // 2
y = alt // 2

# Alt e Larg do retangulo
l = larg // 4
a = alt // 4

# Soma x+l e y+a

while True:
    ret, frame = cap.read()
    # cv.imshow('FRAME', frame)
    cv.rectangle(frame, (x, y), (x + l, y + a), color=(0, 0, 255), thickness=4)
    cv.imshow('FRAME', frame)
    if cv.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()
cv.destroyAllWindows()