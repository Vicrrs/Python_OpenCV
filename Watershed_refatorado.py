import cv2
import numpy as np
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
import matplotlib.pyplot as plt


class Imagem():
    def __init__(self, path=None):
        self.img = None
        if path is not None:
            self.img = cv2.imread(path)

    def Filtro(self):
        global filtro, gray, thresh
        filtro = cv2.pyrMeanShiftFiltering(self.img, 20, 40)
        gray = cv2.cvtColor(filtro, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        titulos = ['Imagem Original', 'Filtro', 'Tons de Cinza', 'Thresh']
        imagens = [self.img, filtro, gray, thresh]

        fig = plt.gcf()
        fig.set_size_inches(16, 12)
        for i in range(4):
            plt.subplot(2, 2, i + 1)
            plt.imshow(imagens[i])
            plt.title(titulos[i])
            plt.xticks([]), plt.yticks([])
        plt.show()

    def Contornos(self):
        contornos, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        buracos = []
        for con in contornos:
            area = cv2.contourArea(con)
            if area < 1000:
                buracos.append(con)
        cv2.drawContours(thresh, buracos, -1, 255, -1)

        fig = plt.gcf()
        fig.set_size_inches(12, 8)
        plt.imshow(thresh)
        plt.show()

    def Watershed(self):
        dist = ndi.distance_transform_edt(thresh, cv2.DIST_L2)
        dist_visual = dist.copy()
        local_max = peak_local_max(dist, indices=False, min_distance=20, labels=thresh)
        markers = ndi.label(local_max, structure=np.ones((3, 3)))[0]
        labels = watershed(-dist, markers, mask=thresh)
        titulos = ["Imagem Original", "Limiarização (objetos juntos)", 
                "Distance Transform", "Watershed (objetos separados)"]
        imagens = [self.img, thresh, dist_visual, labels]
        fig = plt.gcf()
        fig.set_size_inches(16, 12)
        for i in range(4):
            plt.subplot(2, 2, i + 1)
            if (i == 3):
                cmap = "jet"
            else:
                cmap = "gray"
            
            plt.imshow(imagens[i], cmap)
            plt.title(titulos[i])
            plt.xticks([]), plt.yticks([])
        plt.show()
            

imagem = Imagem("008_tomates.jpeg")
imagem.Filtro()
imagem.Contornos()
imagem.Watershed()
