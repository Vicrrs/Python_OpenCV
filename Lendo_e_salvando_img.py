import cv2

local_img = "getter.jpeg"  # caminho da imagem
img = cv2.imread(local_img)
cv2.imshow("Janela", img)  # cria janela
k = cv2.waitKey(0)  # mostra jamela criada e aguarda evento de uma tecla
if k == ord("s"):  # se s for pressionado salva a imagem
    cv2.imwrite('getter.jpeg', img)
cv2.destroyAllWindows()
