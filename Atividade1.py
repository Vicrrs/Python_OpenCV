"""
you have a class to storage data in a dataset. The data is composed of two different types.
A) Point(x,y,acc)
B) Matrix(numpy.array,acc)
I would like to add new data in the following form:
"""
import numpy as np

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.acc = 0

    def retorne_ponto(self, x, y, acc):
        self.x = x
        self.y = y
        self.acc = acc
        return self.x, self.y, self.acc


class Matrix:
    def __init__(self):
        self.EDO = 0
        self.acc = 0

    def retorne_matriz(self, EDO, acc):
        self.EDO = EDO
        self.acc = acc
        return self.EDO, self.acc


class DB():
    def __init__(self):
        self.__database = []

    def append(self, obj):
        self.__database.append(obj)

    def show(self):
        #print(self.__database[0]["EDO"])
        for i in self.__database:
            print(i)


# Imprimir os valores da matriz e do ponto

new_db = DB()
new_matriz = Matrix()
new_ponto = Point()

new_EDO, new_acc = new_matriz.retorne_matriz(np.array([1, 2, 3]), 'acc')
new_db.append({"EDO": new_EDO,
               "acc": new_acc})

new_x, new_y, new_acc = new_ponto.retorne_ponto(2, 8, 'FISMAT')
new_db.append([new_x, new_y, new_acc])

new_db.show()