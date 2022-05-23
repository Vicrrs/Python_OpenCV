import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans


def visualizar_cores_dominantes(cluster, C_centroids):
    C_labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (C_hist, _) = np.histogram(cluster.labels_, bins=C_labels)
    C_hist = C_hist.astype("float")
    C_hist /= C_hist.sum()

    # zeros()função no código acima é usada para criar uma imagem em branco
    rect_color = np.zeros((50, 300, 3), dtype=np.uint8)
    img_colors = sorted([(percent, color) for (percent, color) in zip(C_hist, C_centroids)])
    start = 0
    for (percent, color) in img_colors:
        print(color, "{:0.2f}%".format(percent * 100))
        end = start + (percent * 300)
        cv.rectangle(rect_color, (int(start), 0), (int(end), 50), \
                     color.astype("uint8").tolist(), -1)
        start = end
    return rect_color


img = cv.imread("005_fone.jpg")
Z = img.reshape((-1, 3))
Z = np.float32(Z)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
reshape_img = img.reshape((img.shape[0] * img.shape[1], 3))

# define critérios, número de clusters(K) e aplica kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 3, 1.0)
K = 8
ret, label, center = cv.kmeans(Z, K, None, criteria, 3, cv.KMEANS_RANDOM_CENTERS)

KM_cluster = KMeans(n_clusters=3).fit(reshape_img)
visualize_color = visualizar_cores_dominantes(KM_cluster, KM_cluster.cluster_centers_)

# Agora convertendo de volta para uint8 e faça a imagem original
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape(img.shape)

visualize_color = cv.cvtColor(visualize_color, cv.COLOR_RGB2BGR)
cv.imshow('res2', res2)
cv.waitKey()
cv.destroyAllWindows()
