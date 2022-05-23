"""
Função calcOpticalFlowFarneback()
Computar um fluxo ótico denso usando o algoritmo de Gunnar Ferneback's

cv2.calcOpticalFlowFarneback(prev,next,flow,pyr_scale,levels,winsize,iterations,poly_n,poly_sigma,flags)

•Parâmetros:
1. prev=frame de entrada

2. next=segundo frame do mesmo tamanho queoprev

3. flow=computaofluxo da imagem que temomesmo tamanho do prev

4. pyr_scale=parâmetro,especificandoaescala da imagem(<1)para construir pirâmides para cada imagem; 
pyr_scale=0.5 significa uma pirâmide clássica,onde cada camada seguinte é duas vezes menor que a 
anterior.

5. levels=número de camadas da pirâmide incluindoaimagem inicial;níveis=1significa que nenhuma camada extraécriadaeapenas as imagens
originais são usadas.

6. winsize=tamanho médio da janela;valores maiores aumentamarobustez do algoritmo para ruído de imagemefornecem mais chances de
detecção de movimento rápido,mas geram mais campo de movimento borrado.

7. interations=número de interações do algoritmo de cada level da pirâmede.

8. poly_n=tamanho da vizinhança do pixel usado para encontraraexpansão polinomial em cada pixel;valores 
maiores significam queaimagem será aproximada com superfícies mais suaves,gerando algoritmo mais r
obustoecampo de movimento mais borrado,normalmente poly_n=5ou7.

9. poly_sigma=desvio padrão do Gaussiano queéusado para suavizar as derivadas usadas como base paraaexpansão polinomial;para poly_n=
5,você pode definir poly_sigma=1,1,para poly_n=7,um bom valor seria poly_sigma=1,5.

10. flags=operações de fluxo

▪OPTFLOW_USE_INITIAL_FLOW usaofluxo de entrada como uma aproximação de fluxo inicial.
▪OPTFLOW_FARNEBACK_GAUSSIAN usaofiltro Gaussiano do tamanho da janela em vez de um filtro de caixa do 
mesmo tamanho para estimativa de fluxo ótico;geralmente,esta opção fornece um fluxo mais preciso do que 
com um filtro de caixa,ao custo de uma velocidade menor,normalmente,otamanho da caixa para uma janela 
Gaussiana deve ser definido com um valor maior para atingiromesmo nível de robustez.

Resumo do Algoritmo:

O algoritmo Farneback gera uma pirâmide de imagens,onde cada nível possui uma resolução inferior em 
relação ao nível anterior.Quando você seleciona um nível de pirâmide maior que1, o algoritmo pode  
rastrear os pontos em vários níveis de resolução,começando no nível mais baixo.Aumentaronúmero de 
níveis de pirâmide permite queoalgoritmo trate de maiores deslocamentos de pontos entre quadros. No 
entanto,onúmero de cálculos também aumenta.O diagrama mostra uma pirâmide de imagens com três níveis.

O rastreamento começa no nível de resolução mais baixoecontinua atéaconvergência.Os locais de pontos 
detectados em um nível são propagados como pontos-chave paraonível seguinte.Desta forma,o algoritmo 
refinaorastreamento com cada nível.Adecomposição da pirâmide permite queoalgoritmo lide com grandes 
movimentos de pixel,que podem ser distâncias maiores queotamanho da vizinhança.
"""
#Captação de movimento
from cv2 import magnitude
import numpy as np
import cv2

#Captação da Imagem
cap = cv2.VideoCapture(0)

#Lendo o primeiro frame
ret, first_frame = cap.read()
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

#Mascara no primeiro frame
mask = np.zeros_like(first_frame)

#Imagem com saturação no max
mask[..., 1] = 255

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prev_gray,
                                        gray,
                                        None,
                                        pyr_scale=0.5,
                                        levels=3,
                                        winsize=15,
                                        iterations=3,
                                        poly_n=5,
                                        poly_sigma=1.1,
                                        flags=0)

    #Magnitude e angulo optico  do vetores em 2D
    magnitude, angle = cv2.cartToPolar(flow[...,0], flow[...,1])

    #Setar o hue de acordo com o fluxo optico
    mask[...,0] = angle * 180 / np.pi / 2

    #Setar a imagem de acordo com a magnitude do fluxo optico
    mask[...,2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    #HSV para RGB
    rgb = cv2.cvtColor  (mask, cv2.COLOR_HSV2BGR)

    #Soma ponderada
    dense_flow = cv2.addWeighted(frame, 1, rgb, 2, 0)

    cv2.imshow('Dense Optical Flow', dense_flow)
    prev_gray = gray
    if cv2.waitKey(10) &  0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
