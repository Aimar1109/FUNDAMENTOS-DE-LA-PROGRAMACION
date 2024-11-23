def lista_vuelos():
    try:
        # Cargar los datos de vuelos_limpios
        vuelos = []
        with open('vuelos_limpios.csv', 'r', encoding='utf-8') as f:
            for linea in f:
                vuelos.append([x for x in linea.strip().split(';')])
            f.close()

    except FileNotFoundError:
        # Si no se ha encontrado el archivo crearlo
        lista = []
        with open('BAreviews.csv', 'r', encoding='utf-8') as f:
            p =  True
            for linea in f:
                if p:
                    encabezado = linea.strip().split(',')
                    p = False
                else:
                    linea = linea.strip().split(',')
                    if linea[4] != 'None':
                        lista.append(linea[4])
            f.close()

        vuelos = []
        for i in lista:
            vuelo = i.split(' to ')
    
            if len(vuelo) > 1:
                vuelos.append(vuelo[:2])
            else:
                vuelo = i.split('-')
                if len(vuelo) > 1:
                    vuelos.append(vuelo)


        for v in range(len(vuelos)):
            el = vuelos[v][1].split(' ')
            if len(el) > 1:
                if el[1] == 'via' or el[1] == 'return':
                    vuelos[v][1] = el[0]
                elif len(el) > 2:
                    if el[2] == 'via' or el[2] == 'return':
                        vuelos[v][1] = ''.join(el[:2])

        with open('vuelos_limpios.csv', 'w', encoding='utf-8') as f:
            for vuelo in vuelos:
                a = ';'.join(vuelo)+'\n'
                f.write(a)
    return vuelos


def crear_dict(lista):
    index = 0
    dict_vuelos = {}
    for vuelo in lista:
        if vuelo[0] not in dict_vuelos.keys():
            dict_vuelos[vuelo[0]] = index
            index += 1
    return dict_vuelos

def guardar_dict(diccionario):
    with open('diccionario_indices.csv', 'w', encoding='utf-8') as f:
        for key in diccionario.keys():
            a = key + ';' + str(diccionario[key]) + '\n'
            f.write(a)

        f.close()


def leer_dict():
    dict_v = {}
    with open('diccionario_indices.csv', 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip().split(';')
            dict_v[linea[0]] = linea[1]
        f.close()
    return dict_v

def crear_matriz(lista, diccionario):
    matriz = []
    for l in diccionario:
        linea = []
        for c in diccionario:
            for vuelo in vuelos:
                if l == vuelo[0] and c == vuelo[1]:
                    linea.append(1)
                    break
            linea.append(0)
        matriz.append(linea)
    return matriz


def guardar_matriz(matriz):
    with open('matriz_vuelos.csv', 'w', encoding='utf-8') as f:
        for linea in matriz:
            a = ';'.join([str(x) for x in linea])
            f.write(a+'\n')
        
        f.close()


def leer_matriz():
    with open('matriz_vuelos.csv', 'r', encoding='utf-8') as f:
        matriz = []
        for linea in f:
            linea = linea.strip().split(';')
            matriz.append(linea)

        f.close()
    return matriz


vuelos = lista_vuelos()

try:
    dict_vuelos = leer_dict()
except FileNotFoundError:
    dict_vuelos = crear_dict(vuelos)
    guardar_dict(dict_vuelos)

try:
    matriz_vuelos = leer_matriz()
except FileNotFoundError:
    matriz_vuelos = crear_matriz(vuelos, dict_vuelos)
    guardar_matriz(matriz_vuelos)

