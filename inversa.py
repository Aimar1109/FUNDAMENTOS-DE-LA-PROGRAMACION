import random


def creador_de_matrices(num_matrices, filas, columas):
    # Un generador de matrices con valores de -10 a 10
    matrices = []
    for i in range(num_matrices):
        matriz = []
        for y in range(filas):
            linea = []
            for x in range(columas):
                linea.append(random.randint(-10, 10))
            matriz.append(linea)
        matrices.append(matriz)
    return matrices

def escalonada_a2(matriz):
    # Funcion que calcula si una matriz esta escalonada es decir que el triangulo de abajo de numeros sean 0
    # Mediante una funcion recursiva que va quitando las filas y columnas comprovadas
    if len(matriz) > len(matriz[0]):
        return False
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != j and matriz[i][j] != 0:
                return False
            elif i == j and matriz[i][j] != 1:
                return False
    return True


def mover_lineas(matriz, ln1, ln2):
    # Operacion elemental de mover dos filas lo que conlleva multiplicar por menos uno despues al determinante
    linea1 = matriz[ln1]
    linea2 = matriz[ln2]
    for i in range(len(matriz)):
        if i == ln1:
            matriz[i] = linea2
        elif i == ln2:
            matriz[i] = linea1
    return matriz

def uno(matriz, fila, inversa):
    # Primera operacion que busca que haya un 1 en alguna fila de pivote o si hay un 0 cambiarlo por otra fila
    if matriz[fila][fila] == 1:
        return matriz, inversa, False
    
    # MOVIENDO LINEAS
    for i in range(fila, len(matriz)):
        if matriz[i][fila] == 1:
            matriz = mover_lineas(matriz, fila, i)
            inversa = mover_lineas(inversa, fila, i)
            return matriz, inversa, False
    
    if matriz[fila][fila] == 0:
        for i in range(fila+1, len(matriz)):
            if matriz[i][fila] == 1:
                matriz = mover_lineas(matriz, fila, i)
                inversa = mover_lineas(inversa, fila, i)
                return matriz, inversa, False

        for i in range(fila+1, len(matriz)):
            if matriz[i][fila] != 0:
                matriz = mover_lineas(matriz, fila, i)
                inversa = mover_lineas(inversa, fila, i)
    
    if matriz[fila][fila] == 0:
        matriz.pop()
        return matriz, inversa, True

    # GAUSS PURO
    div = matriz[fila][fila]
    for j in range(len(matriz[fila])):
        matriz[fila][j] = matriz[fila][j] / div
        inversa[fila][j] = inversa[fila][j] /div

    return matriz, inversa, False


def ceros(matriz, col, inversa):
    for i in range(len(matriz)):
        if i != col:
            resta = matriz[i][col]
            for j in range(len(matriz)):
                matriz[i][j] -= resta*matriz[col][j]
                inversa[i][j] -= resta*inversa[col][j]
    return matriz, inversa

def conbinacion_lineal(matriz):
    # Borrar filas llenas de 0
    borrar = []
    for i in range(len(matriz)):
        c = True
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                c = False
                break
        if c:
            borrar.append(i)
    
    borrar.reverse()
    for x in borrar:
        matriz.pop(x)

    borrar = []
    # Borrar convinaciones lineales
    for i in range(len(matriz)):
        for i_a in range(i+1, len(matriz)):
            n = True
            counter = 0
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0 and matriz[i_a][j] != 0:
                    n = False
                    break
                elif matriz[i][j] != 0 and matriz[i_a][j] == 0:
                    n = False
                    break
                if matriz[i][j] == 0 and matriz[i_a][j] == 0:
                    counter += 1
            if not n or counter < (len(matriz[i])-1):
                continue
            else:
                if i_a not in borrar:
                    borrar.append(i_a)

    borrar.sort()
    borrar.reverse()
    for x in borrar:
        matriz.pop(x)

    return matriz

def inversa(matriz):
    if escalonada_a2(matriz):
        return len(matriz)
    
    inversa = crear_identidad(matriz)

    for i in range(len(matriz)):
        matriz, inversa, c = uno(matriz, i, inversa)
        if c:
            return 'columna lleva de 0'
        matriz, inversa = ceros(matriz, i, inversa)
        matriz = conbinacion_lineal(matriz)
        if len(matriz) < len(matriz[0]):
            return 'Esta matriz no es cuadrada'
        if escalonada_a2(matriz):
            return inversa
    return inversa

def crear_identidad(matriz):
    identidad = [[0 for y in range(len(matriz[x]))] for x in range(len(matriz))]
    for x in range(len(identidad)):
        identidad[x][x] = 1
    return identidad 


a = creador_de_matrices(1, 4, 4)[0]


b = [
    [2, 1, 1, 3],
    [1, 2, 3, 1],
    [3, 1, 2, 1],
    [1, 3, 1, 2]
]

i = inversa(a)

for x in i:
    print(x)