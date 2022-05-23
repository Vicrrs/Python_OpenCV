"""Para ler as imagens é usado o método cv2.imread(). Este método carrega uma imagem do arquivo especificado.
Se a imagem não puder ser lida (por causa de arquivo ausente, permissões impróprias, formato não suportado ou inválido),
esse método retornará uma matriz vazia.

Sintaxe: cv2.imread(caminho, sinalizador)

Parâmetros:
path: Uma string representando o caminho da imagem a ser lida.
flag: Especifica a forma como a imagem deve ser lida. Seu valor padrão é cv2.IMREAD_COLOR

Valor de retorno: este método retorna uma imagem que é carregada do arquivo especificado.

Sintaxe: cv2.imread(caminho, sinalizador)

Parâmetros:
path: Uma string representando o caminho da imagem a ser lida.
flag: Especifica a forma como a imagem deve ser lida. Seu valor padrão é cv2.IMREAD_COLOR

Valor de retorno: este método retorna uma imagem que é carregada do arquivo especificado.
A imagem deve estar no diretório de trabalho ou um caminho completo da imagem deve ser fornecido.

cv2.IMREAD_COLOR: Especifica para carregar uma imagem colorida. Qualquer transparência de imagem será negligenciada.
É a bandeira padrão. Alternativamente, podemos passar o valor inteiro 1 para este sinalizador.
cv2.IMREAD_GRAYSCALE: Especifica para carregar uma imagem em modo de escala de cinza. Alternativamente,
podemos passar o valor inteiro 0 para este sinalizador.
cv2.IMREAD_UNCHANGED: Especifica para carregar uma imagem como tal incluindo o canal alfa. Alternativamente,
podemos passar o valor inteiro -1 para este sinalizador."""


import cv2

# Para ler a imagem do disco, usamos
# função cv2.imread, no método abaixo,
img = cv2.imread("getter.jpeg", cv2.IMREAD_COLOR)

# Criando janela GUI para exibir uma imagem na tela
# primeiro parâmetro é o título do Windows (deve estar no formato string)
# Segundo parâmetro é array de imagens
cv2.imshow("GETTER", img)

# Para manter a janela na tela, usamos o método cv2.waitKey
# Uma vez detectado a entrada de fechamento, ele liberará o controle
# Para a próxima linha
# O primeiro parâmetro é para segurar a tela por milissegundos especificados
# Deve ser um número inteiro positivo. Se 0 passar um parâmetro, então ele irá
# segure a tela até o usuário fechá-la.
cv2.waitKey(0)

# É para remover/excluir a janela GUI criada da tela
# e memória
cv2.destroyAllWindows()