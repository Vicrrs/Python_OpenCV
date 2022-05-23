# INERCIAIS

"""
As caracterísitcas inerciais definem informações sobre os momentos, o centro geométrico e
as formas geométricas de um objeto de interesse. É possível através dessas características
reconhecer objetos mesmo que tenham sofrido alterações na escala, rotação ou translação.

Os momentos de uma imagem, também conhecido como momentos estatícos, é um dos principais
métodos para extração de características. São obtidos por funções matemáticas, com base
em estatística, que fornecem valores que representam um determinado objetivo.
"""
# convert image to grayscale image
import cv2


img = cv2.imread("011_circle.JPG")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,127,255,0)

# calculate moments of binary image
M = cv2.moments(thresh)
print(M)
print(len(M))

# calculate x,y coordinate of center
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

# put text and highlight the center
cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# display the image
cv2.imshow("Image", img)
cv2.waitKey(0)

