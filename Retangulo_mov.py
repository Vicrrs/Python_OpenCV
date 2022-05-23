import cv2 as cv

cap = cv.VideoCapture(0)


# Callback do retangulo
def Draw_rect(event, x, y, flags, params):
    global pt1, pt2, topLeftClicked, bottomRightClicked
    if event == cv.EVENT_LBUTTONDOWN:
        if topLeftClicked == True and bottomRightClicked == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeftClicked = False
            bottomRightClicked = False
        if topLeftClicked == False:
            pt1 = (x, y)
            topLeftClicked = True
        elif bottomRightClicked == False:
            pt2 = (x, y)
            bottomRightClicked = True


## Variaveis

pt1 = (0, 0)
pt2 = (0, 0)
topLeftClicked = False
bottomRightClicked = False

cv.namedWindow('Teste')
cv.setMouseCallback('Teste', Draw_rect)

while True:
    ret, frame = cap.read()
    # Desenhar o retangulo de acordo com a VG
    if topLeftClicked:
        cv.circle(frame, center=pt1, radius=5, color=(0, 0, 255))
    if topLeftClicked and bottomRightClicked:
        cv.rectangle(frame, pt1, pt2, color=(0, 0, 255), thickness=1)

    cv.imshow('Teste', frame)

    if cv.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()
cv.destroyAllWindows()
