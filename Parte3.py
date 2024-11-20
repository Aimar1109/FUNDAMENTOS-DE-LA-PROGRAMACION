#import os
#
#with open(r'a\prueba.txt', 'a') as file:
#    file.write('\nAimar Mardones; 18; 0003')
#
#with open(r'a\prueba.txt', 'r') as file:
#    for line in file:
#        print(line)
#
#f = open(r'a\prueba.txt', 'r')
#
#lineas = f.readlines()
#
#print(lineas)
#for linea in lineas:
#    print(linea)
#
#f.close()

def menor(matriz:list[list], fila:int, columna:int) -> list[list]:
    menor : list[list] = []
    for i in range(len(matriz)):
        if i != fila:
            nueva: list = []
            for j in range(len(matriz[i])):
                if j != columna:
                    nueva.append(matriz[i][j])
            menor.append(nueva)
    return menor

def det(matriz:list[list]) -> int:
    if len(matriz) == 1:
        return matriz[0][0]
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    deter : int = 0
    for i in range(len(matriz[0])):
        signo : int = (-1) ** i
        valor : int = matriz[0][i]
        menorc : list[list] = menor(matriz, 0, i)
        deter += signo * valor * det(menorc)
    return deter

if __name__ == "__main__":
    matriz = [
        [1, 2, 3, 5],
        [0, 4, 5, 0],
        [2, 6, 7, 0],
        [0, 4, 0, 1],

    ]
    print("Determinante de la matriz:", det(matriz))