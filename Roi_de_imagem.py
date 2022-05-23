# ROI de uma imagem
"""
Um conceito importante em processamento de imagens é a Região de interesse. Estende-se como Região de intere-
sse (ROI - "Region of interest" ou AOI - "Area of Interest") a região obtida de maneira automática ou a part-
ir da interação de um usuário onde o processamento estará totalmente concentrado.

Objetivos:
1. Obter um ROI de uma imagem a partir da área selecionada pelo mouse
"""
import cv2 as cv
import numpy as np

# Imagem teste
image = cv.imread("003_Lenna.png")
image_to_show = np.copy(image)

# Estados iniciais do mouse
cropping = False
x_init, y_init, top_left_pt, bottom_right_pt = 0, 0, 0, 0


def roi(event, x, y, flags, param):
    global image_to_show, x_init, y_init, top_left_pt, bottom_right_pt, cropping

    if event == cv.EVENT_LBUTTONDOWN:
        cropping = True
        x_init, y_init = x, y
        image_to_show = np.copy(image)
        print(f"Ponto inicial em X {x_init}")
        print(f"Ponto inicial em Y {y_init}")

    elif event == cv.EVENT_MOUSEMOVE:
        if cropping == True:
            image_to_show = np.copy(image)
            cv.rectangle(image_to_show, (x_init, y_init), (x, y), (0, 255, 0), 1)

    elif event == cv.EVENT_LBUTTONUP:
        cropping = False
        top_left_pt, bottom_right_pt = x, y
        print(f"Ponto superior {top_left_pt}")
        print(f"Ponto inferior {bottom_right_pt}")

cv.namedWindow('Image')
cv.setMouseCallback('Image', roi)

while True:
    cv.imshow('Image', image_to_show)
    k = cv.waitKey(1)

    if k == ord('c'):
        if y_init > bottom_right_pt:
            y_init, bottom_right_pt = bottom_right_pt, y_init
        if x_init > top_left_pt:
            x_init, top_left_pt = top_left_pt, x_init

        if bottom_right_pt - y_init > 1 and top_left_pt - x_init > 0:
            image = image[y_init: bottom_right_pt, x_init:top_left_pt]
            print(image)
            image_to_show = np.copy(image)

    if k == ord('s'):
        cv.imwrite('teste.png', image_to_show)

    if cv.waitKey(1) == ord('q'):
        break


cv.destroyAllWindows()


