# Diferenciação de Frames

"""
• A diferenciação de frames trata de determinar a presença de objetos em movimento, calculando
a diferença de pixels entre duas imagens consecutivas em um video.Embora o cálculo geral seja 
simples e fácil de implementar, a complexidade aumenta por causa do objeto"em movimento", o que
pode comprometer a precisão.

• As técnicas de diferenciação de frames têm alta precisãoetempo computacional relativamente baixo
ou moderado; este método funciona bem para fundos estáticos.

Função: cv2.absdiff(src1, src2)
- Calcula a diferença absoluta por elemento entre duas matrizes ou entre uma matriz e um escalar
- Parâmetros:
    * src1: primeira matriz de entrada ou um escalar
    * src2: segunda matriz de entrada ou um escalar
"""
#Captação de movimento
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
prox_frame = frame

while True:
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    prox_frame_gray = cv2.cvtColor(prox_frame, cv2.COLOR_BGR2GRAY)

    frame_diff = cv2.absdiff(frame_gray, prox_frame_gray)

    cv2.imshow('frame diff', frame_diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    prox_frame = frame.copy()
    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()   
