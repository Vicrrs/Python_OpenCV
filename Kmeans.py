"""
Em vez de encontrar uma única cor média, também podemos encontrar as cores mais dominantes em uma imagem usando
o k_mean algoritmo de agrupamento.

Por exemplo, para encontrar cinco cores dominantes em uma imagem, podemos fazer cinco agrupamentos de cores na imagem
dada usando a KMeans() função da sklearnbiblioteca.

Esta função funciona no princípio dos vizinhos mais próximos, no qual o valor mais próximo de um pixel será colocado
no cluster desse pixel e assim por diante.

Por exemplo, se um cluster contiver a cor preta, as outras cores próximas à cor preta também serão colocadas dentro
desse cluster e assim por diante. Então podemos descobrir qual cor é dominante em cada cluster usando o histograma dos
clusters.

Podemos mostrar as cores dominantes usando a rectangle() função do OpenCV. Também exibiremos a porcentagem das cores
dominantes.
"""

import cv2, numpy as np
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

        # rectangle() função para criar retângulos de cores dominantes de acordo com sua porcentagem em cima
        # da imagem em branco.
        # Também podemos definir a tolerância usando o tol argumento definido como 0,0001 por padrão

        """O primeiro argumento da rectangle()função é a imagem na qual queremos desenhar a caixa de cores. O segundo 
        argumento é a posição inicial, que definirá o ponto inicial do retângulo.

        O terceiro argumento é a posição final do retângulo. O quarto argumento define a cor do retângulo no formato 
        triplo BGR e o quinto argumento é a espessura da linha do retângulo."""

        cv2.rectangle(rect_color, (int(start), 0), (int(end), 50), \
                      color.astype("uint8").tolist(), -1)
        start = end
    return rect_color


# Load image
src_image = cv2.imread('003_RGB.jpg')
src_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
reshape_img = src_image.reshape((src_image.shape[0] * src_image.shape[1], 3))

# Display dominant colors Present in the image
# Valor do cluster esta definido como 10

KM_cluster = KMeans(n_clusters=10).fit(reshape_img)
visualize_color = visualizar_cores_dominantes(KM_cluster, KM_cluster.cluster_centers_)

# OpenCV lê imagens no espaço de cores BRG, por isso convertemos a imagem em RGB usando a cvtColor()função do OpenCV.

visualize_color = cv2.cvtColor(visualize_color, cv2.COLOR_RGB2BGR)
cv2.imshow('visualize_Color', visualize_color)
cv2.waitKey()
