# Importando as bibliotecas Necessárias

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


class ImgProc():
    def __init__(self, path=None):
        self.image = None
        if path is not None:
            self.img = cv.imread(path)

    def GetMeanColor(self):
        linha_de_cor_media = np.average(self.img, axis=0)
        cor_media = np.average(linha_de_cor_media, axis=0)
        print(cor_media)

        d_img = np.ones((624, 624, 3), dtype=np.uint8)
        d_img[:, :] = cor_media

        # cv.imshow("Imagem_de_origem", img)
        cv.imshow("Cor media", cor_media)
        cv.waitKey(0)

    def GetHist(self):
        cv.imshow("Janela", self.img)
        azul, verde, vermelho = cv.split(self.img)
        fig = plt.figure(figsize=(20, 5))
        # Histograma para cor azul
        ax1 = fig.add_subplot(131)
        ax1.hist(azul.ravel(), 256, [0, 256])
        plt.title("Histograma com canal azul")
        # Histograma para cor verde
        ax2 = fig.add_subplot(132)
        ax2.hist(verde.ravel(), 256, [0, 256])
        plt.title("Histograma com canal verde")
        # Histograma para canal vermelho
        ax3 = fig.add_subplot(133)
        ax3.hist(vermelho.ravel(), 256, [0, 256])
        plt.title("Histograma com canal vermelho")
        plt.show()

    def ApplyBlur(self):
        Gaussian = cv.GaussianBlur(self.img, (7, 7), 100)
        cv.imwrite("011_Gaussian.jpg", Gaussian)
        median = cv.medianBlur(self.img, 101, 21)
        cv.imwrite("011_median.jpg", median)
        bilateral = cv.bilateralFilter(self.img, 9, 100, 750)
        cv.imwrite("011_bilateral.jpg", bilateral)

    def Affine(self):
        rows, cols, ch = self.img.shape

        pts1 = np.float32([[50, 50],
                           [200, 50],
                           [50, 200]])

        pts2 = np.float32([[10, 100],
                           [200, 50],
                           [100, 250]])

        M = cv.getAffineTransform(pts1, pts2)
        dst = cv.warpAffine(self.img, M, (cols, rows))
        plt.subplot(121)
        plt.imshow(self.img)
        plt.title('Input')

        plt.subplot(122)
        plt.imshow(dst)
        plt.title('Output')
        plt.show()

        while (True):
            cv.imshow("Imagem", self.img)
            if cv.waitKey(20) & 0xFF == 27:
                break
        cv.destroyAllWindows()

    # independe do init

    @staticmethod
    def visualizar_cores_dominantes(cluster, C_centroids):
        C_labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
        (C_hist, _) = np.histogram(cluster.labels_, bins=C_labels)
        C_hist = C_hist.astype("float")
        C_hist /= C_hist.sum()

        # zeros()função no código acima é usada para criar uma imagem em branco
        rect_color = np.zeros((50, 300, 3), dtype=np.uint8)
        img_colors = sorted([(percent, color)
                             for (percent, color) in zip(C_hist, C_centroids)])
        start = 0
        for (percent, color) in img_colors:
            print(color, "{:0.2f}%".format(percent * 100))
            end = start + (percent * 300)
            cv.rectangle(rect_color, (int(start), 0), (int(end), 50),
                         color.astype("uint8").tolist(), -1)
            start = end
        return rect_color


teste = ImgProc("001_moeda.PNG")
# teste.GetMeanColor()
teste.GetHist()
teste.ApplyBlur()
teste.Affine()
teste.visualizar_cores_dominantes()