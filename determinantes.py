import random

def escalonada(matriz):
    if len(matriz) == 2 and matriz[1][0] == 0:
        return True
    for i in range(1, len(matriz)):
        if matriz[i][0] != 0:
            return False
    matriz.pop(0)
    for i in range(len(matriz)):
        matriz[i].pop(0)
    return escalonada(matriz)

def mover_lineas(matriz, fuera, ln1, ln2):
    linea1 = matriz[ln1]
    linea2 = matriz[ln2]
    for i in range(len(matriz)):
        if i == ln1:
            matriz[i] = linea2
        elif i == ln2:
            matriz[i] = linea1
    fuera = fuera*(-1)
    return matriz, fuera

def primera(matriz, fuera):
    if matriz[0][0] == 1:
        return matriz, fuera
    elif matriz[0][0] == 0:
        for i in range(len(matriz)):
            if matriz[i][0] == 1:
                matriz, fuera = mover_lineas(matriz, fuera, 0, i)
                return matriz, fuera

        for i in range(len(matriz)):
            if matriz[i][0] != 0:
                matriz, fuera = mover_lineas(matriz, fuera, 0, i)
                return matriz, fuera
    
    for i in range(len(matriz)):
        if matriz[i][0] == 1:
            matriz, fuera = mover_lineas(matriz, fuera, 0, i)
            return matriz, fuera
        
    return matriz, fuera

def ceros(matriz, fuera, fila):
    for i in range(fila+1, len(matriz)):
        mul = matriz[i][fila] / matriz[fila][fila]
        for j in range(fila, len(matriz)):
            resta =  matriz[fila][j]*mul
            matriz[i][j] = matriz[i][j] - resta
    return matriz, fuera

def convinacion_lineal(matriz):
    for i in range(len(matriz)):
        counter = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                counter += 1
        if counter == len(matriz[i]):
            return True
    return False



def determinante(matriz, fuera=1):
    if len(matriz) == 1:
        return matriz[0][0]
    if escalonada(matriz):
        deter = 0
        for i in range(len(matriz)):
            deter = deter * matriz[i][i]
        return deter * fuera
    
    matriz, fuera = primera(matriz, fuera)
    for i in range(len(matriz)):
        matriz, fuera = ceros(matriz, fuera, i)
        cl = convinacion_lineal(matriz)
        if cl:
            return 0

    
    deter = 1
    for i in range(len(matriz)):
        deter = deter*matriz[i][i]
    return deter * fuera


# print(determinante([[4, 9, -6, 3],
#                     [1, 2, -2, 2],
#                     [1, 6, 3, 1],
#                     [2, -1, 1, -1]]))


def creador_de_matrices(num_matrices, dimension):
    matrices = []
    for i in range(num_matrices):
        matriz = []
        for y in range(dimension):
            linea = [random.randint(-10, 10) for x in range(dimension)]
            matriz.append(linea)
        matrices.append(matriz)
    return matrices

# matrices = creador_de_matrices(100, 4)
# for matriz in matrices:
#     for linea in matriz:
#         print(linea)
#     print(determinante(matriz))

m1 = [[0, 10, -4, 8],
      [-7, 6, 2, -1],
      [10, 7, 4, -9],
      [-9, -7, 1, -5]]
m2 = [[4, 6, 8, -5],
      [6, -8, 7, 9],
      [6, -7, 10, -3],
      [-8, 4, -4, -10]]
m3 = [[7, 5, -5, -4],
      [-4, -10, -6, 9],
      [2, 2, 2, 2],
      [1, 1, 1, 1]]

m4 = [[8, 8, 8, -3],
      [-1, 1, 0, 4],
      [-4, 4, 0, -1],
      [9, 5, 1, 10]]


print(determinante(m4))