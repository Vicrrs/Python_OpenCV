l = int(input("Valores para a linha: "))
c = int(input("Valores para a coluna: "))

matrix = []

for i in range(l):
    a = []
    for j in range(c):
        var = int(input())
        a.append(var)
    matrix.append(a)
for i in range(l):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()