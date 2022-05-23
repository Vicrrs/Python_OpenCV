import cv2
import imutils
import numpy as np
import pytesseract

verbose = True

image = cv2.imread("014_placa-mercosul.png")

image = imutils.resize(image, width=500)

if verbose == True:
    cv2.imshow("Imagem Original", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if verbose == True:
    cv2.imshow("Imagem em tons de cinza", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

gray = cv2.bilateralFilter(gray, 11, 17, 17)

if verbose == True:
    cv2.imshow("Imagem Filtrada", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

edged = cv2.Canny(gray, 170, 200)

if verbose == True:
    cv2.imshow("Imagem Bordas", edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1 = image.copy()
cv2.drawContours(img1, cnts, -1, (0, 255, 0), 0)

if verbose == True:
    cv2.imshow("Imagem Contornos", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumPlacaCnt = None

img2 = image.copy()
cv2.drawContours(img2, cnts, -1, (0, 255, 0), 3)

if verbose == True:
    cv2.imshow("Imagem TOP 30", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

count = 0
idx = 1

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        NumPlacaCnt = approx

        x, y, w, h = cv2.boundingRect(c)
        new_img = gray[y:y + h, x:x + w]
        cv2.imwrite('Placa' + str(idx) + '.png', new_img)

cv2.drawContours(image, [NumPlacaCnt], -1, (0, 255, 0), 3)

if verbose == True:
    cv2.imshow("Imagem final com placa detectada", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Cropped_img_loc = 'Placa' + str(idx) + '.png'

if verbose == True:
    cv2.imshow("Imagem cropped placa", cv2.imshow(Cropped_img_loc))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

text = pytesseract.image_to_string(Cropped_img_loc, config='-1 eng --oem 3 --psm 1')
print("Número da placa: ", text)
