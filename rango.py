import random


def escalonada(matriz):
    # Funcion que calcula si una matriz esta escalonada es decir que el triangulo de abajo de numeros sean 0
    # Mediante una funcion recursiva que va quitando las filas y columnas comprovadas
    if len(matriz) > len(matriz[0]):
        return False

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j and matriz[i][j] != 0:
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

def uno(matriz, fila, pivote):
    # Primera operacion que busca que haya un 1 en alguna fila de pivote o si hay un 0 cambiarlo por otra fila
    if matriz[fila][pivote] == 1:
        return matriz
    
    # MOVIENDO LINEAS
    for i in range(fila, len(matriz)):
        if matriz[i][pivote] == 1:
            matriz = mover_lineas(matriz, 0, i)
            return matriz
    
    if matriz[fila][pivote] == 0:
        for i in range(fila+1, len(matriz)):
            if matriz[i][pivote] == 1:
                matriz = mover_lineas(matriz, 0, i)
                return matriz

        for i in range(fila+1, len(matriz)):
            if matriz[i][pivote] != 0:
                matriz = mover_lineas(matriz, 0, i)
                
    # GAUSS PURO
    div = matriz[fila][pivote]
    for j in range(len(matriz[fila])):
        matriz[fila][j] = matriz[fila][j] / div  

    return matriz


def ceros(matriz, fila, pivote):
    for i in range(fila+1, len(matriz)):
        resta = matriz[i][pivote]
        for j in range(fila, len(matriz[i])):
                matriz[i][j] -= resta
    return matriz

def conbinacion_lineal(matriz):
    # Borrar filas llenas de 0
    borrar = []
    for i in range(len(matriz)):
        c = True
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                c = False
        if c:
            borrar.append(i)
    
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
    
    if len(borrar) > 1:
        borrar.reverse()
    for x in borrar:
        matriz.pop(x)

    return matriz

def rango(matriz):
    if escalonada(matriz):
        return len(matriz)
    
    for i in range(len(matriz[0])):
        pivote = 0
        for j in range(i, len(matriz[i])):
            if matriz[i][j] != 0:
                pivote = j
                break
        matriz = uno(matriz, i, pivote)
        matriz = ceros(matriz, i, pivote)
        matriz = conbinacion_lineal(matriz)
        if escalonada(matriz):
            return len(matriz)
        if len(matriz) <= len(matriz[0]):
            return len(matriz)
    return len(matriz)




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

matrices = creador_de_matrices(10, 10, 5)

for matriz in matrices:
    for x in matriz:
        print(x)
    print(rango(matriz))
    print('')
